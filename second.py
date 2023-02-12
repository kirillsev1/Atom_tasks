from typing import Callable


def create_handlers(callback: Callable[[int], int]) -> Callable:
    """Function which is generating answers of function: func.

    Ars:
        callback: Callable - square function .

    Returns:
        callback: Callable - square function instance.
    """
    for step in range(5):
        yield lambda: callback(step)


def execute_handlers(handlers) -> Callable:
    """Function returns results of square function running.

    Args:
        handlers - object of generator.

    Returns:
        handler() - generated square function.
    """
    # запускаем добавленные обработчики (шаги от 0 до 4)
    for handler in handlers:
        return handler()


def square(num):
    return num**2


execute_handlers(create_handlers(square))
