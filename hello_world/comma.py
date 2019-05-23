spam = ['apples', 'bananas', 'tofu', 'cats']
def comma(l_value):
    res = ''
    for i in range(len(spam) - 1):
            res += spam[i] + ', '
    return res + 'and ' + spam[-1]
print(comma(spam))