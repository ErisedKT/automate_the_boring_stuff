# MIT 6.00.1x Week 2
# Exercise Guess My Number

print('Please think of a number between 0 and 100!')
low = 0
high = 100
ans = ''
while low <= high:
    mid = (low + high) // 2
    print('Is your secret number ' + str(mid) + '?')
    print('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly.')
    ans = input()
    if ans == 'c':
        print('Game over. Your secret number was: ' + str(mid))
        break
    elif ans == 'h':
        high = mid - 1
    elif ans == 'l':
        low = mid + 1
    else:
        print('Sorry, I did not understand your input.')
    