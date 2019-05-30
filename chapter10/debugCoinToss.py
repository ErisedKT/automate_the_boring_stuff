import random, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Starting program execution.')

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.debug('The guess is %s!' % (guess))
toss = random.choice(('heads', 'tails')) # 0 is tails, 1 is heads
logging.debug('Toss is ' + str(toss) + ' and guess is ' + guess)
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    logging.debug('Guess is %s' % (guess))
    if toss == guess:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
logging.debug('Program terminated.')