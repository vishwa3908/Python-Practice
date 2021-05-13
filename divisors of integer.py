# Python program to generate all divisor of  integer
def generate_divisor(num):
    for i in range(1, num+1):
        if num % i == 0:
            print(i, end=" ")

number = int(input("Enter A number => "))
generate_divisor(number)
