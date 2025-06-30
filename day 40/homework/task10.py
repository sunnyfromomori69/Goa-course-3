text = "OMORIII, hooray"

print(text.split())

print(text.split(','))


print(text.split(' ', 2))

# split

words = ['OMORI', 'is', 'deppresing']


print(' '.join(words))



print('-'.join(words))


print(''.join(words))

# join

text = "I wish I was OMORI"


print(text.replace('OMORI', 'KEL'))


print(text.replace('i', '*'))



print(text.replace('i', '*', 1))

# replace

text = "   go to hell!   "


print(text.strip())



print(text.rstrip())


special_text = "***Go***"
print(special_text.strip('*'))
