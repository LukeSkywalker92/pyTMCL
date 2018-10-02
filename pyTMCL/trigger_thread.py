from threading import Thread, Event


class TriggerThread(Thread):
    """
    Thread that checks every 0.01 seconds if a condition is reached.
    When the condition is reached, a callback function will be called.
    """

    def __init__(self, condition, callback):
        """
        :condition:
                Condition that needs to be reached
        :callback:
                Callback function that should be called, when condition is
                reached.
        """
        Thread.__init__(self)
        self.condition = condition
        self.callback = callback
        self.position_reached = Event()

    def run(self):
        while not self.position_reached.wait(0.01):
            if self.condition():
                self.position_reached.set()
        self.callback()
