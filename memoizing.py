from functools import wraps


def memoizing(limit):
    """
    Make decorator that will remember recent results of function (up to limit).

    Arguments:
        limit, maximum number of results to remember

    Returns:
        memoizing decorator

    """
    def wrapper(function):
        """
        Memoize function.

        Arguments:
            function, it will be memoized

        Returns:
            memoized version of function

        """
        memory = {}
        order = []
        @wraps(function)
        def inner(argument):
            memoized_result = memory.get(argument)
            if memoized_result is None:
                memoized_result = function(argument)
                memory[argument] = memoized_result
                order.append(argument)
                if len(order) > limit:
                    oldest_argument = order.pop(0)
                    memory.pop(oldest_argument)
            return memoized_result
        return inner
    return wrapper
