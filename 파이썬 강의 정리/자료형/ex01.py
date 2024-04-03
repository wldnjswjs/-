from math import*
# 자료형을 구하기 위해서는 type()을 사용
print(type(17))

# 반지름이 r인 구의 부피를 계산하는 프로그램
r = 5.0
volume = 4.0/3.0 * pi * r**3
print(volume)
volume = 4.0/3.0 * pi * pow(r, 3)
print(volume)
print("구의 부피: " + str(volume))

# 구의 겉넓이 계싼하는 프로그램
r = 5.0
outer_area = 4 * pi * pow(r, 2)
print(outer_area)
print("구의 겉넓이: " + str(outer_area))