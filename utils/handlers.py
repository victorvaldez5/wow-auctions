from requests import HTTPError

def error_handler(func):
    def inner(*args, **kwargs):
        code = int(func(*args, **kwargs).get('code', 200))
        if code and code != 200:
            raise HTTPError
        return func(*args, **kwargs)
    return inner