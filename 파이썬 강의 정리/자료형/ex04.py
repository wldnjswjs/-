#문자열에 대한 실습

#큰따옴표(double quotation marks)로 묶으면 문자열이 된다. (권장)
welcome = "Happy New year 2023"
print(welcome)

#작은따옴표(single quotation)로 묶어도 문자열이 된다.
welcome = 'Happy New year 2023'
print(welcome)

# 아래와 같이 ""안에 또 다른 ""이 들어있다면 컴파일러가 혼돈을 일으켜 
# 틀린 문법이다라고 에러를 발생시킨다. 
message = "은혁이가 '안녕하세요'라고 인사했습니다."
print(message)

# 파이썬에서는 따옴표를 출력하고자 할 때, \를 이용한다.
message= 'doesn\'t'
print(message)

message = "\"Yes, \" I can do it"
print(message)

# 특수문자 형탱인 \n은 개행(Enter)을 하는 문자이다.
message = "First\nSecond\nThird"
print(message)

# 특수문자 \t는 탭만큼 띄우는 문자이다.
message = "c:\temp\name"
print(message)

# 위에서 살펴봤던 \t, \n 이런 이스케이프 문자들의 기능을 제거를 
# 시키기 위해서는 문자열 앞에 r을 붙여준다.(중요함)
message = r"c:\temp\name"
print(message)

# 문자열(영어나 한글 상관없음)의 길이를 알고자 한다면 len()함수를 이용한다.
message = "world"
print("문자열의 길이: ", len(message))