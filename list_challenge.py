def run():
    list_challengue = [i for i in range(1,99999) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(list_challengue)


if __name__ == '__main__':
    run()
