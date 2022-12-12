def to_check_leapyear(leapyear):
    if leapyear % 4 == 0:
        return f"{leapyear} is a leapyear"
    else:
        return f'{leapyear} is not a leapyear'


num = int(input("Enter a Year to check it is leapyear or not: "))
value = to_check_leapyear(num)
print(value)