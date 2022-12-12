def to_check_leapyear(leapyear):
    if leapyear % 4 == 0:
        return f"{leapyear} is a leapyear"
    else:
        return f'{leapyear} is not a leapyear'


def validate_input():
    if num.isdigit():
        convert_num = int(num)
        value = to_check_leapyear(convert_num)
        print(value)
    else:
        print("Invalid input, Please enter a valid year")


num = input("Enter a Year to check it is leapyear or not: ")
validate_input()
