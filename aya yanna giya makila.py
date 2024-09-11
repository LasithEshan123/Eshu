num1 = int(input('Write a number?'))
num2 = int(input('Write an another number?'))
product = num1*num2
if product <= 1000:
    result = product
else:
    result = num1+num2
print(result)