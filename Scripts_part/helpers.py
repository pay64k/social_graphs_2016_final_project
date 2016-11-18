import time


def write_to_file(data, filename, path):
    with open(path + filename, "a", 0) as text_file:
        text_file.write(data)
    text_file.close()


def open_file(filename, path):
    _file = open(path + filename,'r')
    return _file.read()


def timestamp():
    return str(time.strftime("%Y%m%d-%H%M%S"))