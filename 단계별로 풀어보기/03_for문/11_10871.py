# end함수는 print 끝의 개행문자를 무엇으로 바꿀지 정해준다

n,x = map(int,input().split())
numlist = list(map(int,input().split()))
solist = []

for i in numlist:
    if i < x:
        solist.append(i)

for item in solist:
    print(item, end = ' ')

'''
n,x = map(int,input().split())
a = input().split()
lst = []
nums = ''

for integer in a :
    if int(integer) < x :
        lst.append(integer)
for i in lst :
    nums = nums + i + ' '
print(nums)
'''
