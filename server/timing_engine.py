from openrtist_engine import OpenrtistEngine
import time
import os
import signal
import numpy as np

class TimingEngine(OpenrtistEngine):
    def __init__(self, compression_params, adapter):
        super().__init__(compression_params, adapter)
        self.count = 0
        self.lasttime = time.time()
        self.lastcount = 0
        self.lastprint = self.lasttime
        self.LOG_PATH = "logs"
        if not os.path.exists(self.LOG_PATH):
            os.makedirs(self.LOG_PATH)
        self.log_avg = None
        self.is_first = True
        #self.LOG_FILENAME = os.path.join(LOG_PATH, time.strftime("%Y%m%d-%H%M%S")+"-{}-{}.txt")
        #self.log_frame = open(LOG_FILENAME.format("frame"), "w")
        #self.log_avg = open(LOG_FILENAME.format("avg"), "w")
        self.totals = []
        self.res = 0

    def handle(self, from_client):
        self.t0 = time.time()
        result = super().handle(from_client)
        self.t3 = time.time()

        if from_client.frame_id == 0:
            print("Logging ...")
            if self.log_avg:
                self.log_avg.close()
            self.is_first = True
            LOG_FILENAME = os.path.join(self.LOG_PATH, time.strftime("%Y%m%d-%H%M%S")+"-{}-{}.txt")
            #self.log_frame = open(LOG_FILENAME.format("frame", self.res), "w")
            self.log_avg = open(LOG_FILENAME.format("avg", self.res), "w")

        #log_frame = "Send:Rcv {}:{} Latency".format(from_client.time_send_client,)

        log_msg = ("frameid: {0}, pre: {1:.1f}, infer: {2:.1f}, "
                "post: {3:.1f}, total: {4:.1f}, wait: {5:.1f}, "
                "fps: {6:.2f}, ".format(from_client.frame_id, (self.t1-self.t0)*1000,
                (self.t2-self.t1)*1000, (self.t3-self.t2)*1000, (self.t3-self.t0)*1000,
                (self.t0-self.lasttime)*1000, 1.0/(self.t3-self.lasttime)))

        #self.log_frame.write(log_msg+"\n")
        self.count += 1
        if self.t3 - self.lastprint > 5:
            log_msg += "avg fps: {0:.2f}".format((self.count-self.lastcount)/(self.t3-self.lastprint))
            if not self.is_first:
                print(log_msg, file=self.log_avg)
                self.totals.append((self.t3-self.t0)*1000)
                if len(self.totals) > 10:
                    t = np.array(self.totals)
                    print(log_msg)
                    print("Mean {} Std {} Variance{}".format(np.mean(t), np.std(t), np.var(t)))
                    self.totals = []

            self.is_first = False
            self.lastcount = self.count
            self.lastprint = self.t3

        self.lasttime = self.t3

        return result

    def inference(self, preprocessed, res=240):
        self.t1 = time.time()
        result = super().inference(preprocessed)
        self.t2 = time.time()
        if res != self.res:
            self.res = res
            self.is_first = True
            self.totals = []
        return result
