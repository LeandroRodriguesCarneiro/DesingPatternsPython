from typing import Any


class MetaSingleton(type):

    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances: 
            cls.__instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]
    
class Logger(metaclass = MetaSingleton):
    pass

log1 = Logger()
print(f'LOG1: {id(log1)}')

log2 = Logger()
print(f'LOG2: {id(log2)}')