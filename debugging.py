def divisors(num):        
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        return divisors


def run():
    try:
        num = int(input("Enter a number: "))
        if num < 0:
            raise NameError
        print(divisors(num))
        print("Finished my program")
    except ValueError:
        print("You must enter a number")
    except NameError:
        print("Enter a positive number")

if __name__ == '__main__':
    run()

