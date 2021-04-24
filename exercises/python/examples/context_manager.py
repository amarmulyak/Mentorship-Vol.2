# with open("text.txt") as f:
#     data = f.read()


# Example 1
class ContextManager:
    def __init__(self):
        print('init method called')

    def __enter__(self):
        print('enter method called')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')


# with ContextManager() as manager:
#     print('with statement block')

# Output:
#
# init method called
# enter method called
# with statement block
# exit method called


# Example 2
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


# loading a file
# with FileManager('test.txt', 'w') as f:
#     f.write('Test')

# print(f.closed)


# Example 3
# from pymongo import MongoClient


class MongoDBConnectionManager():
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(self.hostname, self.port)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()


# connecting with a localhost
# with MongoDBConnectionManager('localhost', '27017') as mongo:
#     collection = mongo.connection.SampleDb.test
#     data = collection.find({'_id': 1})
#     print(data.get('name'))


from contextlib import contextmanager


@contextmanager
def my_context_manager():
    # Before yield as the enter method
    print("Enter method called")
    yield

    # After yield as the exit method
    print("Exit method called")


with my_context_manager() as manager:
    print('with statement block')
