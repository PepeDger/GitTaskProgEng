# task5/timing_decorator.py
import time
from typing import Callable, Any


def timing_decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функция {func.__name__} выполнилась за {execution_time:.6f} секунд")
        return result

    return wrapper


# Тестовые функции
@timing_decorator
def add_numbers(a: int, b: int) -> int:
    result = a + b
    print(f"Результат сложения: {a} + {b} = {result}")
    return result


@timing_decorator
def process_file(input_file: str = "input.txt", output_file: str = "output.txt") -> None:
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            numbers = f.read().strip().split()
            if len(numbers) < 2:
                raise ValueError("Должно быть хотя бы 2 значения")
            a, b = map(int, numbers[:2])

        result = a + b

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"{a} + {b} = {result}")

        print(f"Результат записан в файл {output_file}")

    except FileNotFoundError:
        print(f"Файл {input_file} не найден")
    except ValueError as e:
        print(f"Ошибка обработки чисел: {e}")


if __name__ == '__main__':
    add_numbers(2, 3)
