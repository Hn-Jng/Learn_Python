# 모듈
# import는 현재 dir에 있는 파일이나 파이썬 라이브러리가 저장된 dir에 있는 모듈만 불러올 수 있다.
# import mod1  >> print(mod1.add(3,4))
# from 파일명 import * : 파일 안의 모든 함수 불러서 사용가능

#from mod1 import*
import mod1
print(mod1.add(3, 4))
#print(add(3, 4))

print(mod1.PI)

a = mod1.Math()       # 모듈 안의 클래스 사용하는 방법
print(a.solv(2))
print(mod1.add(mod1.PI, 4.4))  # 변수,함수도 마찬가지로, " 모듈명.변수or함수 ""

result = mod1.add(10, 11)
print(result)

# sys.path.append(모듈을 저장한 디렉터리) 사용하기
# PYTHONPATH 환경 변수 사용하기
