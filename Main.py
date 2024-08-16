number = int(input('Введи чотирьохзначне число:'))
number1 = number//1000
number2 = number//100%10
number3 = number//10%10
number4 = number%10
print(number1)
print(number2)
print(number3)
print(number4)
number = int(input('А тепер введи п\'ятизначне число:'))
number1 = number//10000
number2 = number//1000%10
number3 = number//100%10
number4 = number//10%10
number5 = number%10
print(f'{number5}{number4}{number3}{number2}{number1}')