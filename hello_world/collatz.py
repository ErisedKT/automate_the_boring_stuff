def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

print('Enter an integer: ', end = '')
try:
    i = int(input())
except ValueError:
    print('Error: Invalid argument')
while i != 1:
    i = collatz(i)