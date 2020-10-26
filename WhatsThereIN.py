a = input('Create a sentence - ')
b = input('What letter are we going to count? ')

c=0
for i in (a):
    if i==b:
        c=c+1

if (c) > 0:
    print('This letter appears' ,(c), 'times')
else:
    print('I can not find this letter')




