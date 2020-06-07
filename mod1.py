def add(a, b):
    return a+b


def sub(a, b):
    return a-b


if __name__ == "__main__":      # 파일 실행할 경우, 참이되어 문장수행
    # 대화형 인터프리터나 import 통해 부를때는 수행되지 않음
    print(add(1, 4))
    print(sub(4, 2))

"""
 파이썬의 __name__ 변수는 파이썬이 내부적으로 사용하는 특별한 변수 이름이다. 
 만약 C:\doit>python mod1.py처럼 직접 mod1.py 파일을 실행할 경우 mod1.py의 __name__ 변수에는 __main__ 값이 저장된다.
 하지만 파이썬 셸이나 다른 파이썬 모듈에서 mod1을 import 할 경우에는 mod1.py의 __name__ 변수에는 mod1.py의 모듈 이름 값 mod1이 저장된다.
"""

PI = 3.141592


class Math:
    def solv(self, r):
        return PI*(r**2)
