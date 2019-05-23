# MIT 6.00.1x Problem 3

s = 'azcbobobegghakl'
longest = ''
sub = ''
i = 0
while i < len(s)-1:
    sub = s[i]
    for j in range(i+1, len(s)):
        if s[j] >= s[j-1]:
            sub += s[j]
        else:
            if len(sub) > len(longest):
                longest = sub
            break
    i += len(sub)
print('Longest substring in alphabetical order is: ' + longest)