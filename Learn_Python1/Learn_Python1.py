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

sentence = '안녕하세요.' + " 반갑습니다."
print(sentence.split())
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
"""
"""
## tuple :  ()으로 둘러싸며, 값의 생성,삭제,수정 안됨. 초기화 가능
t1=(1,2,3)
t2=(4,5)
t2= 4,
t3 = (1,2,'a','b')
print(t1+t2)
print(t3[3])     #indexing
print(t3[:2])    #slicing
print(len(t3))   #length
"""

"""
# Dictionary
dic={'name':'Hn-Jng','phone':'01049498989','birth':'0407'}
print(dic)
print(dic['name'])
a={1:'hi'}      #key(정수):value(문자열) 가능
a={'a':[1,2,3]} #key(문자) : value(리스트) 가능
print(a)
a['name']='jng'
print(a)
a[3]=[5,6,7]
print(a)
del a['a']      #delete 
print(a)       

grade = {'hj':80,'jh':90}
print(grade['hj'])  # 80 ,  dictionary value[key] -> value

q={(1,2):'p'}
print(q[(1,2)])     # tuple은 key 가능. list는 key 불가.

dic={'name':'Hn-Jng','phone':'01049498989','birth':'0407'}
print(dic.keys())     # key들의 객체반환
print(dic.values())   # value들의 객체반환
print(dic.items())    # key,value 쌍을 tuple로 묶은 객체 반환
print(dic.get('name'))  # dic.get('name') = dic['name']
                        # 존재하지 않는 키: get -> None, x['y'] -> Error의 차이있음
print(dic.get('foo','bar'))  # dictionary에 해당값 없음. default값인 'bar' 돌려줌
print('name'in dic)
print('email'in dic)     #해당 key 값 있는지 조사. True or False 출력
for k in dic.keys():
    print(k)
print(list(dic.keys()))   #dict_keys 객체를 list로 변환/ values, items 동일

dic.clear()       # dict 쌍 모두 지우기
print(dic)
"""
"""
# 집합 자료형

s1=set([1,2,3])
s2=set("Hello")
print(s1)
print(s2)     # 중복삭제, 순서없음(Unordered) - indexing으로 값 얻을 수 없다

l1=list(s2)   # indexing 하려면 list나 tuple로 변환 후 해야함
print(l1)
print(l1[2])

s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])

print(s1&s2)              # 교집합
print(s1|s2)              # 합집합
print(s1-s2)              # 차집합

s1.add(10)
print(s1)                 # add (값 1개 추가)
s2.update([10,11,12])
print(s2)                 # update(값 여러 개 추가)
s1.remove(10)
print(s1)                 # remove _ 1개 값만 가능..?
"""
"""
# Bool 자료형
a=[1,2,3,4]
while a:
    print(a.pop())

if []:
    print("True")
else:
    print("False\n")

print(bool('python'))
print(bool(''))
print(bool([1,2,3]))
print(bool([]))
print(bool(0))
print(bool(3))
"""

#실험
a=[1,2,3]
#b=a[:]
b=a[:]
#b=a

a[0]
a[1]
a[2]
print(id(a))
print(id(b))
print(id(a[0]))
print(id(a[1]))
print(id(a[2]))
a=b=c='d'
print(a)
print(b)
print(c)
a,b=('c','python')
print(a,b)
[a,b]=['c','python']
print([a,b].pop())
print(a,b)

