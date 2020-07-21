number=23
guess=int(input('input a number: '))

if guess == number:
    print('you are succeed')
elif guess < number:
    print('too small')
else:
    print('too big')
print('done')
