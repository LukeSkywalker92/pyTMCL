from threading import Thread, Event


class TriggerThread(Thread):
    """
    Thread that checks every 0.01 seconds if a condition is reached.
    When the condition is reached, a callback function will be called.
    """

    def __init__(self, condition, callback=None, args=(), kwargs={}):
        """
        :condition:
                Condition that needs to be reached
        :callback:
                Callback function that should be called, when condition is
                reached.
        :args:
                is the argument tuple for the target invocation. Defaults to ().
        :kwargs:
                is a dictionary of keyword arguments for the target
                invocation. Defaults to {}.
        """
        Thread.__init__(self)
        if kwargs is None:
            kwargs = {}
        self._condition = condition
        self._callback = callback
        self._args = args
        self._kwargs = kwargs
        self._condition_reached = Event()

    def run(self):
        while not self._condition_reached.wait(0.01):
            if self._condition():
                self._condition_reached.set()
        try:
            if self._callback:
                self._callback(*self._args, **self._kwargs)
        finally:
            # Avoid a refcycle if the thread is running a function with
            # an argument that has a member that points to the thread.
            del self._callback, self._args, self._kwargs

if __name__ == "__main__":
    import time

    class TestCondition(object):
        def __init__(self):
            self.bool = False

        def get_condition(self):
            return self.bool

    def callback(arg1, arg2):
        print(arg1)
        print(arg2)

    def test(callback=None, args=(), kwargs=None):
        condition = TestCondition()
        args = args
        kwargs = kwargs
        if callback is not None:
            TriggerThread(condition=condition.get_condition,
                          callback=callback, args=args, kwargs=kwargs).start()
            time.sleep(3)
            condition.bool = True

    test(callback=callback, args=("test1", "test2"))
