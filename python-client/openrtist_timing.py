from gabriel_client.server_comm import WebsocketClient
from openrtist_protocol import openrtist_pb2
import time
import logging
import os 
import sys

logger = logging.getLogger(__name__)


class TimingClient(WebsocketClient):
    def __init__(self, host, port, producer, consumer, res=240, output_freq=10):
        super().__init__(host, port, self.producer, self.consumer)
        self.adater_producer = producer
        self.adapter_consumer = consumer
        self.logname = os.path.join("logs",time.strftime("%Y%m%d-%H%M%S")+"-{}-{}.txt")
        self._output_freq = output_freq
        self._send_timestamps = {}
        self._recv_timestamps = {}
        self._server_timestamps = {}
        self._s2c_timestamps = {}
        self._c2s_timestamps = {}
        self._unprocessed_frames = []
        self._count = 0
        self.res = res
        self._interval_count = 0
        self._start_time = time.time()
        self._interval_start_time = time.time()
        self._start = True
        self.log_fps = None

    def producer(self):
        timestamp = time.time()
        from_client = self.adater_producer()

        if self.get_frame_id() >50: #3000
            if self.log_fps:
                self.log_fps.close()
                self.log_rtt.close()
            sys.exit()

        if from_client is not None:
            self._send_timestamps[self.get_frame_id()] = time.time()

        return from_client

    def consumer(self, result_wrapper):
        timestamp = time.time()
        self._recv_timestamps[result_wrapper.frame_id] = timestamp
        self.adapter_consumer(result_wrapper)
        engine_fields = openrtist_pb2.EngineFields()
        result_wrapper.engine_fields.Unpack(engine_fields)
        self._server_timestamps[result_wrapper.frame_id] = engine_fields.timestamps
        self._s2c_timestamps[result_wrapper.frame_id] = result_wrapper.s2c_timestamps
        self._c2s_timestamps[result_wrapper.frame_id] = result_wrapper.c2s_timestamps
        self._count += 1
        self._interval_count += 1
        self._unprocessed_frames.append(result_wrapper.frame_id)

        if self._count % self._output_freq == 0:
            if not self._start:
                overall_fps = self._count / (timestamp - self._start_time)
                print('Overall FPS:', overall_fps)
                interval_fps = (self._interval_count /
                                (timestamp - self._interval_start_time))
                print('FPS: {}'.format(interval_fps), file=self.log_fps)
                self.compute_rtt()
            else:
                self.log_fps = open(self.logname.format("fps", self.res), "w")
                self.log_rtt = open(self.logname.format("rtt", self.res), "w")

            self._start = False
            self._interval_count = 0
            self._interval_start_time = time.time()

    def compute_rtt(self):
        count = 0
        total_rtt = 0
        
        for frame_id in list(self._unprocessed_frames):
            self._unprocessed_frames.remove(frame_id)
            c2s_time = self._c2s_timestamps[frame_id]
            s2c_time = self._s2c_timestamps[frame_id]
            print("Client {} -> Server {} : Transmit {}".format(c2s_time.sent, c2s_time.received,
                                                                 c2s_time.received - c2s_time.sent))
            print("Server {} -> Client {} : Transmit {}".format(s2c_time.sent, s2c_time.received,
                                                                (s2c_time.received - s2c_time.sent)))
            count += 1
            total_rtt += (s2c_time.received - c2s_time.sent)

        #print('Average RTT: {}'.format(total_rtt / count))
        print('Average RTT: {}'.format(total_rtt / count), file=self.log_rtt)

    def compute_avg_rtt(self):
        count = 0
        total_rtt = 0

        for frame_id, sent in self._send_timestamps.items():
            received = self._recv_timestamps.get(frame_id)
            if received is None:
                logger.error('Frame with ID %d never received', frame_id)
            else:
                count += 1
                server_times = self._server_timestamps.get(frame_id)
                print("Old Client {} -> Server {} : Transmit {}".format(sent, server_times.received, server_times.received - sent))
                print("Old Server {} -> Client {} : Transmit {}".format(server_times.sent, received, (received - server_times.sent)))
                total_rtt += (received - sent)

        print('Old Average RTT: {}'.format(total_rtt / count))
        #print('Old Average RTT: {}'.format(total_rtt / count), file=self.log_rtt)

    def clear_timestamps(self):
        self._send_timestamps.clear()
        self._recv_timestamps.clear()
        self._c2s_timestamps.clear()
        self._s2c_timestamps.clear()
        self._server_timestamps.clear()
