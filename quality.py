def arabic_to_roman(number):
    num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    str_list = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X",
                "IX", "V", "IV", "I"]
    temp = ''
    if not isinstance(number, int):
        return "ERROR: It's not an int"
    if number > 4000 or number < 1:
        return "ERROR: It's not in the range(1,4000)"
    for i in range(len(num_list)):
        while(number >= num_list[i]):
            number -= num_list[i]
            temp += str_list[i]
    return temp


if __name__ == '__main__':
    number_list = [740, 320, 450, 500, 55, 68, 35]
    for num in number_list:
        print(arabic_to_roman(num))
