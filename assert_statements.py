def divisors(num):
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        return divisors


def run():
    num = input("Enter a number: ")
    assert num.isnumeric(), "You must enter a positive number"
    print(divisors(int(num)))
    print("Finished my program")
    

if __name__ == '__main__':
    run()