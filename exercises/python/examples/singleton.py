class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


class Singleton2:
    obj = None  # attribute for storing a single copy

    def __new__(cls, *args, **kwargs):  # class Singleton
        if cls.obj is None:
            # If it does not yet exist, then
            # call __new__ of the parent class
            cls.obj = object.__new__(cls, *args, **kwargs)

        return cls.obj  # will return Singleton


obj = Singleton2()
obj.Attr = 12
new_obj = Singleton2()
print(new_obj.Attr)
print(obj is new_obj)


def decorator_singleton(class_):
    instances = dict()

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance
