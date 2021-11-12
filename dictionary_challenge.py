import math


def run():
    dict_challengue = {i:math.sqrt(i) for i in range(1,1001) if i}

    print(dict_challengue)


if __name__ == '__main__':
    run()
