"""
a=10
b=3.14
c=True

print("a의 값은?:", a  )
print("a의 데이터 변수 형태는?: ",  type(a))
print("b의 값은?:",b)
print("b의 데이터 변수 형태는? :",type(b))
print("c의 값은?:",c)
print("c의 데이터 변수 형태는?:",type(c))
"""
"""
print(10==10)
print(10!=10)

sentence = '안녕하세요.'+"반갑습니다."
sentence.split()
print(sentence)
"""
"""
languages = ['python', 'perl', 'c', 'java']

for lang in languages:
    if lang in ['python', 'perl']:
        print("%6s need interpreter" %lang)
    elif lang in ['c', 'java']:
        print("%6s need compiler" % lang)
    else:
        print("should not reach here")
"""

"""
head = "Python"
tail = " is fun!"
head+tail
print(head+tail)
print(head*2)

a="Life is too short"
print(a[16])
b="20200530Windy"

year=b[:4]
day=b[4:8]
weather=b[8:]

print("year :", year)
print("day :" , day)
print("weather :%s\n" % weather)

number =10
day = "three"
print("I ate %d apples. so I was sick for %s days" %(number,day))

print("I eat {0} apples".format(3))
print("I eat {0} apples".format('five'))


print("I ate {number} apples. so I was sick for {day} days.".format(number =10, day='three'))
# 인덱스 항목과 name=value 형태 혼용도 가능

format함수
print("{0:>10}".format('hi'))
print("{0:^10}".format('hi'))
print("{0:=^10}\n".format('hi'))

y = 3.42134234
print("{0:10.4f}".format(y))

name='김현중'
age=23
while(age<27):
    age=age+1
    print(f"나의 이름은 {name}입니다. 나이는 {age}입니다.")
print("\n")

d = {'name':'홍길동', 'age':30}
print(f"나의 이름은 {d['name']}입니다. 나이는 {d['age']}입니다.\n")
"""

"""
######문자열 내장함수#####
a="easydew"
print(a.count ('e'))    #.count 문자 개수 세기

a="Python is the best choice"   
print(a.find('b'))      #.find위치 알려주기/찾는 문자 없으면 -1위치반환
# print(a.index('k'))   #.index : find와 기능 동일하나, 찾는 문자없으면 Error

print("+".join('abcd'))             #문자열 삽입
print("똥".join(['a','b','c','d']))  # ???

a="hi"
b="hello"
print(a,b.upper())  #대문자로 바꾸기
a="Hi"
print(a.lower())    #소문자로 바꾸기

a ="          glass            "
print(a.strip())      #공백지우기 // 왼쪽공배지우기:lstrip(), 오른쪽공백지우기 : rstrip()

c="Life is too short"
print(c.replace("Life","Youth")) #문자열바꾸기

print(c.split())   #문자열나누기_나눈 값은 리스트에 하나씩 들어간다
d="a:b:c:d"
print(d.split(':'))
"""

## list자료형
# list index
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[-1])
print(a[-1][0])  # 리스트 안의 리스트 요소 끌어내기

# list slice
a=[1,2,3,4,5]
print(a[0:2])
a=[1,2,3,['a','b','c'],4,5]
print(a[2:5])
print(a[3][:2])

# list 연산
a=[1,2,3]
b=[4,5,6]

print(a+b)
print(a*3)
print(len(a))

# list 수정,삭제
a=[1,2,3,5]

a[2]=4
print(a)

del a[2:]
print(a)

# list 관련 함수
a=[1,2,3]
a.append(4)
print(a)
a.append([5,6])   #append
print(a)

i=[4,1,2,3]
i.sort()
print(i)          #sort
b=['b','c','a']   #한글도 가능
b.sort()
print(b)
b.reverse()       #reverse
print(b)

a=[1,2,3]

print(a.index(3)) #index : 변수의 위치값

a.insert(0,4)     #insert
print(a)
a.remove(3)       #remove 
print(a)       

a=[1,2,3]
print(a.pop())   # pop{x} x번째 요소 return하고 삭제
print(a)

a=[1,2,3,1]
print(a.count(1))   # count

a=[1,2,3,4]
a.extend([5,6])    # extend = a+=[4,5]
print(a)
