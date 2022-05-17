#  The aim of this exercise is to generate a program that will give an output of either
#  FizzBuzz, Fizz or Buzz depending on if the input is divisible by a combination 3 and 5 or both
value = int(input('Enter an Integer value: '))
if value % 3 == 0 and value % 5 == 0:
    print('FizzBuzz')
elif value % 3 == 0:
    print('Fizz')
elif value % 5 == 0:
    print('Buzz')
else:
    print(value)
#  New FizzBuzz Question

upper_number = int(input('How many values should we process: '))
for ok in range(1, upper_number + 1):
    if ok % 3 == 0 and ok % 5 == 0:
        print('FizzBuzz')
    elif ok % 3 == 0:
        print('Fizz')
    elif ok % 5 == 0:
        print('Buzz')
    else:
        print(ok)
