# 함수

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


def add(a, b): return a+b  # 저장하거나 출력하면 lambda가 def로 변환됨..


result = add(3, 4)
print(result)
