# if문
"""
money = 2000
card = True
if money >= 3000:
    print("택시 타고 가!")
elif card:
    print("지하철 타고 가")
else:
    print("그냥 걸어가")
print(1 not in [1, 2, 3])

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:     # :(콜론) 뒤에 pass 붙여도 됨
    pass                  # 조건문에 따라 실행할 행동을 정의할 때, 아무런 일도 하지 않도록 설정하고 싶을 때
else:
    print("카드를 꺼내")  # 위처럼 수행문장이 한 문장일 경우 :(콜론) 옆에 작성 가능
print()

score = 50
if score >= 60:
    message = "success"
    print(message)
else:
    message = "failure"
    print(message)

# 조건부표현식(conditional expression)
message = "success" if score >= 60 else "failure"
print(message)
"""
# while문
"""
# 예제1-기본문
treeHit = 0
while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍었습니다" % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다")

# 예제2-break
coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee-1
    elif money > 300:
        print("거스름돈 %d원을 주고 커피를 줍니다." % (money-300))
        coffee = coffee-1
    else:
        print("잔액을 돌려주고 커피를 주지 않습니다.")
        print("남은 커피는 %d개 입니다" % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

# 예제3-continue
a = 0
while a < 10:
    a = a+1
    if a % 2 == 0:
        continue
    print(a)
"""
# for문
"""
# 예제1-기본구조
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first+last)
# 예제2
marks = [90, 25, 67, 45, 80]
number = 0

for mark in marks:
    number += 1
    if mark >= 60:
        print("%d번 학생은 합격입니다" % number)
    else:
        print("%d번 학생은 불합격입니다" % number)

# 예제3-continue문
number = 0
for mark in marks:
    number += 1
    if mark < 60:
        continue
    print("%d번 학생은 합격입니다. 축하합니다" % number)

# 예제4-range문
a = range(10)  # 0부터 10미만의 숫자를 포함하는 range객체를 만들어 준다.
print(a)       # (0,10)
a = range(1, 11)  # 이런 형식으로도 작성 가능_rage(시작숫자, 끝 숫자). 끝숫자는 포함안됨
print(a)       # (1,11)

add = 0
for i in range(1, 11):
    add = add+i
    #print(add)_여기 위치할 경우_1,3,6,10... 55 연산과정 출력됨
print(add)

# 예제 5
#number = 0
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):  # len 함수는 리스트 안의 요소 개수를 돌려주는 함수
    if marks[number] < 60:
        continue
    print("%d번 학생. 합격을 축하합니다" % (number+1))

# 예제6- 구구단 만들기
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=' ')   # 매개변수'end'_ 결과값 출력시 다음줄로 넘기지 않고 그 줄에 출력 하기위해
    print()                   # 2단,3단 등 줄바꿈으로 구분 위해서
"""
# 예제7 - 리스트 내포(List comprehension)
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)
print(result)
# 예제7 코드와 결과값 같음
result = [num*3 for num in a]
print(result)
# 예제7_변형_짝수값만 출력
result = [num*3 for num in a if num % 2 == 0]
print(result)
# 예제8_ 2개 이상 for문
result = [x*y for x in range(2, 10)
          for y in range(1, 10)]
print(result)
