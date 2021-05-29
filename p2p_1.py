#check whether a number is in between 1 and 10 using membership operator

list1=[2,3,4,5,6,7,8,9]
n=int(input('enter number: '))

if n in list1:
    print('the number is between 1 and 10')
else:
    print('not in between')
