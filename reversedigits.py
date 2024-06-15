# 1 Reverse digits of an integer
def reverse_digits(num):
    num_str = str(abs(num))
    reversed_str = ''
    for char in num_str[::-1]:
        reversed_str += char
    reversed_num = int(reversed_str) * (-1 if num < 0 else 1)
    return reversed_num


print(reverse_digits(50))  
print(reverse_digits(-12)) 