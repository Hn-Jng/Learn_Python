
# 클래스
"""
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result


cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
"""


class FourCal:
    def __init__(self, first, second):  # 생성자(Constructor)
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first+self.second
        return result

    def mul(self):
        result = self.first*self.second
        return result

    def sub(self):
        result = self.first-self.second
        return result

    def div(self):
        result = self.first/self.second
        return result


"""
a = FourCal(4, 2)
b = FourCal(3, 7)

# a.setdata(4, 2)       # 다른형태 : FourCal.setdata(a,4,2)
# b.setdata(3, 7)

print(a.first)

print(id(a.first))    # 같은 클래스로 만들어진 객체들, 다른 객체의 영향 받지 않으며 고유한 주소값 가짐
print(id(b.first))

print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
"""

# 클래스 상속
# 왜 상속?? : 기존 class가 라이브러리 형태로 제공되거나, 수정이 허용되지 않는 상황등에서 상속 사용


class MoreFourCal(FourCal):        # class 상속 받는클래스(상속할 클래스 이름)
    def pow(self):
        result = self.first**self.second
        return result


a = MoreFourCal(4, 2)
print(a.add())
print(a.pow())

# Method Overriding_ 부모클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것


class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first/self.second


b = SafeFourCal(4, 0)
print(b.div())
# 클래스 변수


class Family:
    lastname = '김'


a = Family()
b = Family()

print(Family.lastname)
print(a.lastname)
print(b.lastname)
Family.lastname = '정'
print(a.lastname)  # 정
print(b.lastname)  # 정      + 주소값도 같음
