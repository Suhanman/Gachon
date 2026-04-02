import np
import pandas as pd
a= 3
b =4
print(a+b)
print(a-b)
print(a/b)
print(a ** b)
a % b
a //b

s1 = 'Hello python'
s1
s2 = 'Hello python'
s2
s3 = '''Helloy python'''
s3
s4 = """Hello python"""
s4
head = 'python'
tail = 'is fun'
print(head + tail)
print(head * 2)
print("=" * 5)
a = "Now is better than never"
print(a[0])
print(a[4])
print(a[-1])
print(a[-2])
print(a[:])
print(a[7:-11])
b = "Python"
a.count('p')

a.find('y')
a.find('p')
# a.index('y')
# a.index('p')
b = ","
b= b.join('Abcd')

a= "python"
print(a.upper(),
      a.lower())

a = [1,2,3]
b = ['Life','is','too','short']
c=[1,2,'Life','is']
d=[1,2,[3,4],['Life'],'is']
print(d[0],d[2],d[3],d[3][-1],d[0:3],a+b,)
# b[0]+"hi~^^",a[0]+"hi~^^"
print(a*3)
a[2]=99
print(a)
a[1:2]= ['a','b','c']
print(a)
a[-1] = ['d','e','f']
print(a)
del a[-1]
print(a)
a.append(5)
print(a)
b.sort()
print(b)
a=[3,4,1,9]
a.reverse()

t1=(1,)
t2=(1,2,3)
t3=1,2,3
t4=(1,2,(3,4),('Life','is'))
print(t4[0])
print(t4[3][-1])
print(t4[0:3])
print(t1+t2)
print(t2*2)
t2[2]=99

dic = {'name':'pey','phone':'0119993323','birth':'1118'}
dic[1]='a'
print(dic[1])
dic['pet']='dog'
del dic[1]
print(dic['pet'])
print(dic['name'])

s1 = {1,2,'a',5}
s2 = set([1,2,3,4,5,6])
print(s2)
s3 = set([4,5,6,7,8,9])
print(s3)

print(s2&s3)
print(s2.intersection(s3))
print(s2|s3)
print(s2.union(s3))
print(s2-s3)
print(s2.difference(s3))
print(s2, s3)
s2.add(7)
print(s2)
a ='abc'
print(a)



s1 = {1,2,'a',5}
s2 = set([1,2,3,4,5,6])
print(s2)
s3 = set([4,5,6,7,8,9])
print(s3)

print(s2&s3)
print(s2.intersection(s3))
print(s2|s3)
print(s2.union(s3))
print(s2-s3)
print(s2.difference(s3))
print(s2, s3)
s2.add(7)
print(s2)
a ='abc'
print(a)

test_list=['one','two','three']
for i in test_list:
    x = i + '!'
    print(x)

number = 0
for score in [90,25,67,45,93]:
    number +=1
    if score >=60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다." %number)

i = 0
while i<5:
    i +=1
    print('*'*i)

def sum1(a,b):
    x = a + b
    return x
def sum2(*args):
    x=0
    for i in args:
        x+= i
    return x

a = 5
b = 3
sum1(a,b)
sum1(3,5)
sum2(1,2,3,4,5)
sum2(2,3.5,10)

sum = lambda a,b : a+b

print(sum(3,5))

# 내장함수 람다, length , range, input ,numpy, pandas , metaplotlib

ar1 = np.array([1,2,3,4,5])
print(ar1)
array([1,2,3,4,5])
type(ar1)


sr3 = pd.Series([101,102,103,104,105])

