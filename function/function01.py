# def(define) = 함수를 정의한다.

# 오버로딩 (같은 변수명에 매개변수 다르게) 파이썬에서 오버로딩안됨
def add(x, y):
    result = x + y
    return result

# 여러개의 매개변수, 여러개의 리턴은 튜플자료형으로 정의되어진다.
def add(*a):
    print(type(a))
    return list(a), 10

r = list(add(20, 10, 5, 30, 40))

print(r)

#######################################################################################

# **이면 딕셔너리 자료형으로 매개변수를 변환해준다.
def sub(**data):
    print(type(data))
    print(data)

sub(a=1, b=2)

def sub(data):
    print(type(data))
    print(data)

sub({"a":1, "b":2})

def connection(servername, password, ip="127.0.0.1", port="8080", username="root"):
    print(f"ip: {ip}")
    print(f"port: {port}")
    print(f"servername: {servername}")
    print(f"username: {username}")
    print(f"password: {password}")

# 초기값을 설정해도 밑에서 변경하고자 하는 값으로 변경 가능함
connection(servername="test_server", password="1q2w3e4r", port="3306")

#######################################################################################

a = 2   # 전역변수
def multi(a):
    return a ** 2

a = multi(a)
print(a)

def div():
    global a    # 전역변수를 global 사용해야지 return을 사용안할 수 있음
    a = a * 10

div()
print(a)

######################################################################################

def add(a, b):
    return a + b

print(add(10, 20))

# 파이썬에서 람다는 하나의 명령만 수행할 수 있다.(여러줄 불가능)
add = lambda a, b: print(a + b)

add (30, 30)