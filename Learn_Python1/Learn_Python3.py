# 함수
"""
# 예제1-여러 개의 입력값 받는 함수 만들기
def add(*args):
    result = 0
    for i in args:
        result = result+i
    return result


a = add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(a)

# 예제2


def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result = result+i
    elif choice == 'mul':
        result = 1
        for i in args:
            result = result*i
    return result


q = add_mul('mul', 3, 4, 5)
print(q)

# 예제3- 키워드 파라미터


def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(name='KHJ')  # {'name':'KHJ'}_딕셔너리 형태로 출력

# 예제4- 결과값 2개


def add_and_mul(a, b):
    return a+b, a*b  # 하나의 튜플값 (a+b,a*b)로 인식


z = add_and_mul(5, 6)
print(z)  # (11,30)

# 결과값 두개 만들고 싶을 때
result1, result2 = add_and_mul(3, 4)
print(result1)
print(result2)

# 예제5- 함수에서 return사용


def write_nick(nick):
    if nick == '등신':
        return  # 함수 빠져나갈 때 사용
    print('당신의 별명은 %s입니다.' % nick)


write_nick('바보')
write_nick('등신')

# 예제6- 초기값 설정한 함수


def say_myself(name, old, man=True):  # man=True처럼 초기값 설정한 매개변수는 맨 뒤로 와야함
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


say_myself('김현중', 27)

# 예제7-global 명령어
a = 1


def vartest():
    global a
    a = a+1


vartest()
print(a)

# 예제8-lambda
# lambda 예약어로 만든 함수는 return 명령어가 없어도 결과값을 돌려줌


def add(a, b): return a+b  # 저장하거나 출력하면 lambda가 def로 변환됨..

result = add(3, 4)
print(result)
"""
# Input/Output
"""
# Input
a = input()
print(a)

number = input("숫자를 입력하세요 :")
print(number)

# Output
print("Jump" "to" "python")
print("Jump", "to", "python")  # ,로 띄어쓰기

for i in range(10):
    print(i, end=' ')  # 한줄에 결과값 이어서 출력하고 싶으면 'end' 사용
"""
# File open
"""
f = open("test.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다\n" % i
    f.write(data)    # 파일내용 작성
f.close()
#
f = open("D:/새파일.txt", 'w')   # 'w' : 아무것도 작성안하고 열고닫기만 해도 기존내용 초기화됨
for i in range(1, 11):
    data = "%d번째 줄입니다\n" % i
    print(data)   # 파일 내부에 입력되는건 아님
f.close()

# redline()으로 읽기
f = open("test.txt", 'r')
line = f.readline()  # 파일의 가장 첫번째 줄 읽음
print(line)
f.close()

f = open("test.txt", 'r')
while True:
    line = f.readline()
    if not line:
        break            # readline()은 더 이상 읽을 줄이 없으면 빈 문자열을 리턴한다.
    print(line)
f.close()

# redlines() : 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려줌
f = open("test.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

# read() : 파일의 내용 전체를 문자열로 돌려준다
f = open("test.txt", 'r')
lines = f.read()
print(lines)
f.close()

# 'a' 기존파일에 추가 작성
f = open("test.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다\n" % i
    f.write(data)
f.close()

# with문과 함께 사용_with 블록을 벗어나는 순간 열린 객체가 자동으로 close 됨
with open("fofo.txt", 'w') as f:
    f.write("you need python")
"""

# sys 명령어___(나중에)
