import argparse
import json
import os

from ps_monitor.process import ProcessNotification

parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument(
    "pid", type=int, help="Process ID of the process to monitor. os.getpid()"
)
parser.add_argument(
    "delay", type=int, default=1, help="Delay in Minutes"
)

path = os.path.dirname(__file__)

with open(f"{path}/../configs/slack_conf.json", "r") as fr:
    slack_conf = json.loads(fr.read())


def main():
    args = parser.parse_args()
    print(f"selected pid={args.pid}, {type(args.pid)} with delay = {args.delay}")
    ProcessNotification(pid=args.pid).schedule(args.delay)


if __name__ == "__main__":
    main()
