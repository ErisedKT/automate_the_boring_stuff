# MIT 6.00.1x Problem 1
s = 'azcbobobegghakl'
count = 0
vowels = 'aeiou'
for c in s:
    if c in vowels:
        count += 1
print('Number of vowels: ' + str(count))