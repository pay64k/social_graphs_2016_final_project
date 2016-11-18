import time


def write_to_file(data, filename, path):
    with open(path + filename, "w") as text_file:
        text_file.write(data)
    text_file.close()

def timestamp():
    return str(time.strftime("%Y%m%d-%H%M%S"))