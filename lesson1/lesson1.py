import time


def my_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{end - start}")
        return result

    return wrapper


# @my_decorator
# def my_function():
#     time.sleep(0)


cacheDict = {}


def cache(dict):
    def decorator(func):
        def wrapper(*args, **kwargs):
            key = f"{func.__name__}{args}{kwargs}"
            if key in dict:
                result = dict[key]
            else:
                result = func(*args, **kwargs)
                dict[key] = result
            return result

        return wrapper

    return decorator


@cache(cacheDict)
@my_decorator
def fibonacci(n):
    a, b = 0, 1
    time.sleep(2)
    for _ in range(n):
        a, b = b, a + b
    return b


print(fibonacci(1000))
print(fibonacci(1000))
print(fibonacci(1000))
print(fibonacci(30))
print(fibonacci(30))

print(cacheDict)
