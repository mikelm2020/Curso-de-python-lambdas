def run():
    my_list = [1, "Hello", 4.5]
    my_dict = {"firstnmae" : "Miguel Angel", "lastname" : "López"}

    super_list = [
        {"firstnmae" : "Facundo", "lastname" : "García"},
        {"firstnmae" : "Miguel Angel", "lastname" : "López"},
        {"firstnmae" : "Mónica", "lastname" : "Nepomuceno"},
        {"firstnmae" : "Santa Yamileth", "lastname" : "López"},
        {"firstnmae" : "Daniel", "lastname" : "Vasquez"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-2, -1, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)




if __name__ == '__main__':
    run()
