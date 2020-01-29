from gabriel_client.server_comm import WebsocketClient
from openrtist_timing import TimingClient
#from timing_client import TimingClient
from adapter import Adapter
import config
import cv2
import argparse
import sys
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "server_ip", action="store", help="IP address for Openrtist Server"
    )
    parser.add_argument(
        "-i", "--folder", action='store', dest='input_dir', help="input file with frame-%06d.png"
    )
    parser.add_argument(
        "--display", action="store_true", help="Show frames received from server"
    )
    parser.add_argument(
        "--timing", action="store_true", help="Print timing information"
    )
    parser.add_argument(
        "--fps", action="store", dest='fps', type=int, default=30, help="Camera fps"
    )
    parser.add_argument(
        "--resolution", action="store", dest='resolution', type=int, default=360, help="Image resolution"
    )

    args = parser.parse_args()


    def preprocess(frame):
        frame = cv2.resize(frame, dimension)
        return frame

    def fetch_w_h(res):
        switcher = {
            240: (352, 240),
            360: (480, 360),
            480: (858, 480),
            720: (1280, 720),
        }
        return switcher.get(res, (352, 240))

    if args.display:

        def consume_frame_style(frame, style):
            cv2.imshow("Result from server", frame)
            cv2.waitKey(1)

    else:

        def consume_frame_style(frame, style, style_image):
            pass

    if not os.path.exists(args.input_dir):
        print("Wrong Input Path")
        sys.exit()

    dimension = fetch_w_h(args.resolution)
    video_capture = cv2.VideoCapture(os.path.join(args.input_dir, "frame-%06d.png"))
    video_capture.set(cv2.CAP_PROP_FPS, args.fps)

    adapter = Adapter(preprocess, consume_frame_style, video_capture, framerate=args.fps)

    if args.timing:
        timing_client = TimingClient(
            args.server_ip, config.PORT, adapter.producer, adapter.consumer, args.resolution
        )
        try:
            timing_client.launch()
        except KeyboardInterrupt:
            timing_client.print_rtt() #compute_avg_rtt()
    else:
        client = WebsocketClient(
            args.server_ip, config.PORT, adapter.producer, adapter.consumer
        )
        client.launch()


if __name__ == "__main__":
    main()
