from random import *
from termcolor import colored


mandarin_int = ["líng", "yī", "èr", "sān", "sì", "wǔ", "liù", "qī", "bā", "jiǔ"]
mandarin_measures = {
    3: "bǎi",
    4: "qīan",
    5: "wàn"
}

measure_colours = {
    3: "green",
    4: "yellow",
    5: "red"
}


def print_num_measure(num_str):
    if int(num_str) == 0:
        return
    if int(num_str[0]) != 0 or int(num_str[1]) != 0:
        if int(num_str[0]) == 2:
            print("liǎng", end=" ")
        else:
            print(mandarin_int[int(num_str[0])], end=" ")
    if int(num_str[0]) != 0:
        print(colored(mandarin_measures[len(num_str)], measure_colours[len(num_str)]), end=" ")
    if len(num_str) > 3:
        print_num_measure(num_str[1-len(num_str):])
    else:
        print_2_digit(num_str[-2:], False)


def generate_number():
    size = randint(1, 8)
    return round(random() * pow(10, size))


def print_2_digit(num_str, is_only_2):
    if int(num_str) == 0:
        return
    if int(num_str[0]) != 1 or not is_only_2:
        print(mandarin_int[int(num_str[0])], end=" ")
    if int(num_str[0]) != 0:
        print(colored("shí", "blue"), end=" ")
    if int(num_str[1]) != 0:
        print(mandarin_int[int(num_str[1])], end=" ")


def get_mandarin(num):
    num_str = str(num)

    if len(num_str) == 1:
        print(mandarin_int[int(num_str)], end="")
    elif len(num_str) == 2:
        print_2_digit(num_str, True)
    elif len(num_str) <= 5:
        print_num_measure(num_str)
    else:
        get_mandarin(num_str[:-4])
        if int(num_str[0]) != 0:
            print(colored("wàn", "red"), end=" ")
        print_num_measure(num_str[-4:])


if __name__ == '__main__':
    while 1:
        num = generate_number()
        if len(str(num)) > 6:
            print(str(num)[:-6], end=",")
            print(str(num)[-6:-3], end=",")
            print(str(num)[-3:], end="")
        elif len(str(num)) > 4:
            print(str(num)[:-3], end=",")
            print(str(num)[-3:], end="")
        else:
            print(num, end="")
        input()
        get_mandarin(num)
        print("")
        input()
