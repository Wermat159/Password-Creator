from random import randint

# BY WERMAT159
# SIMPLE PASSWORD CREATOR

print("********************************")
print("WELCOME TO THE PASSWORD CREATOR")
print("********************************")

lowercase = 5
uppercase = 3
numbers = 2
symbols = 2
list_names = ["lowercase", "uppercase", "numbers", "symbols"]
defaults_list = [5, 3, 2, 2]
chosen_number_list = ["", "", "", ""]


def get_input():
    i = 0
    while i < 4:
        temp = input(f"Enter number of {list_names[i]} letters: (default is {defaults_list[i]})")
        if temp.isnumeric() and int(temp) > 0:
            chosen_number_list[i] = temp
            i += 1
            continue
        else:
            print("Input must be a positive number.")
            continue


def generate_lowercase():
    lowercase_list = []
    for i in range(int(chosen_number_list[0])):
        rint = randint(0, 26)
        char = chr(97 + rint)
        lowercase_list.append(char)
    return lowercase_list


def generate_uppercase():
    uppercase_list = []
    for i in range(int(chosen_number_list[1])):
        rint = randint(0, 26)
        char = chr(65 + rint)
        uppercase_list.append(char)
    return uppercase_list


def generate_numbers():
    numbers_list = []
    for i in range(int(chosen_number_list[2])):
        numbers_list.append(randint(0, 10))
    return numbers_list


def generate_symbols():
    symbols_list = []
    choose_list = ['!', '^', '+', '%', '&', '/', '(', ')', '=', '_', '-', '>', '£', '#', '$', '{', '}', '[', ']', '*']
    for i in range(int(chosen_number_list[3])):
        rint = randint(0, 19)
        symbols_list.append(choose_list[rint])
    return symbols_list


def main():
    get_input()
    lowercases = generate_lowercase()
    uppercases = generate_uppercase()
    numberss = generate_numbers()
    symbolss = generate_symbols()

    all_list = [lowercases, uppercases, numberss, symbolss]
    to_shuffle = []
    password = ""

    def shuffle():
        for i in range(4):
            for j in range(len(all_list[i])):
                to_shuffle.append(all_list[i].__getitem__(j))

    shuffle()
    for x in range(len(to_shuffle)):
        rint = randint(0, len(to_shuffle) - 1)
        password += (str(to_shuffle[rint]))
        to_shuffle.remove(to_shuffle[rint])
    print(password)


main()
