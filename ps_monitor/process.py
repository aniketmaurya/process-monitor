import sched
import time
from datetime import datetime
from typing import Callable

import psutil

from .slack import post_msg


class ProcessNotification:
    def __init__(self, pid, action: Callable = post_msg):
        """delay in mins"""
        self.action = action
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.pid = pid
        self.process = None

        if not self.exist_process():
            raise UserWarning(f"No process with pid={pid}")

        self.running = True
        print(f"Process selected={self.process}")

    def exist_process(self):
        pid = self.pid
        for process in psutil.process_iter():
            if process.pid == pid:
                self.process = process
                return True
        self.running = False
        return False

    def on_terminate(self):
        if not self.exist_process():
            self.action(f"{self.process} terminated at {datetime.now()}")

    def __repr__(self):
        return str(self.process)

    def __call__(self):
        if self.exist_process():
            return True
        else:
            self.on_terminate()

    def schedule(self, delay):
        if not self.running:
            print(f"Process not in running stage! {self.process}")
            return
        delay, priority = 60 * delay, 1
        self.scheduler.enter(delay, priority, self)
        self.scheduler.run()

        return self.schedule(delay)
