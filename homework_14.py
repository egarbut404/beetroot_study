# Task 1

def logger(func):
    def wrapper(*args, **kwargs):
        args_list = [str(arg) for arg in args]
        kwargs_list = [f"{key}={value}" for key, value in kwargs.items()]
        full_list = args_list + kwargs_list
        print(f"{func.__name__} called with {', '.join(full_list)}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

add(4, 5)
add(x = 2, y = 3)
square_all(6, 7, 8)

# Task 2

def stop_words(words: list):
    def decor(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for word in words:
                result = result.replace(word, '*')
            return result
        return wrapper
    return decor

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

# Task 3

def arg_rules(type_: type, max_length: int, contains: list):
    def decor(func):
        def wrapper(*args, **kwargs):
            if args:
                arg = args[0]

                if not isinstance(arg, type_):
                    print(f"Error: Argument must be of type {type_.__name__}, but passed {type(arg).__name__}")
                    return False

                if len(str(arg)) > max_length:
                    print(f"Error: Argument length exceeds {max_length} characters")
                    return False

                for symbol in contains:
                    if symbol not in str(arg):
                        print(f"Error: Argument does not contain '{symbol}'")
                        return False
            return func(*args, **kwargs)
        return wrapper
    return decor


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'