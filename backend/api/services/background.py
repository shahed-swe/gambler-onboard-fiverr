import sched
import time
import threading
import traceback


class BackgroundProcessor:
    scheduler = None
    queue = list()

    def init_on_new_thread(self):
        threading.Thread(target=self.init).start()

    def init(self):
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.__periodic_run__(1, self.process_queue)
        self.scheduler.run()

    def __periodic_run__(self, interval, function, function_args=()):
        self.scheduler.enter(interval, 1, self.__periodic_run__, (interval, function, function_args))
        try:
            function(*function_args)
        except Exception:
            print('Caught exception while running background task')
            print(traceback.format_exc())

    def process_queue(self):
        if len(self.queue) > 0:
            for task in self.queue:
                self.queue.remove(task)
                self.__periodic_run__(*task)

    def schedule_repeating_task(self, interval, function, function_args=()):
        self.queue.append((interval, function, function_args))
