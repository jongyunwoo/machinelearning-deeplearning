#매개변수의 기본
def print_n_times(value, n):
    for i in range(n):
        print(value)

print_n_times("안녕하세요", 5)

#가변 매개변수 함수
def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")

#기본 매개변수
def print_n_times(value, n=2):
    for i in range(n):
        print(value)

print_n_times("안녕하세요")

#카워드 매개변수
def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍", n = 3)

#여러 함수 호출 형태
def test(a, b = 10, c = 100):
    print(a + b + c)

test(10, 20 ,30)
test(a = 10, b = 100, c = 200)
test(c = 10, a = 100, b = 200)
test(10, c = 200)

#자료없이 리턴하기
def return_test():
    print("A 위치입니다.")
    return
    print("B 위치입니다.")

return_test()

#자료와 함께 리턴하기
def return_test():
    return 100

value = return_test()
print(value)

#아무것도 리턴하지 않았을 때의 리턴값
def return_test():
    return

value = return_test()
print(value)

#범위 내부의 정수를 모두 더하는 함수
def sum_all(start, end):
    output = 0
    for i in range(start, end+1):
        output += i
    return output

print("0 to 100:", sum_all(0, 100))
print("0 to 1000:", sum_all(0 , 1000))
print("50 to 100:", sum_all(50, 100))
print("500 to 1000:", sum_all(500, 1000))

#기본 매개변수와 키워드 매개변수를 활용해 범위의 정수를 더하는 함수
def sum_all(start = 0, end = 100, step = 1):
    output = 0
    for i in range(start, end + 1, step):
        output += i
    return output

print("A.", sum_all(0, 100, 10))
print("B.", sum_all(end=100))
print("C.", sum_all(end = 100, step = 2))

#모든 값 곱하기
def mul(*values):
    output = 1
    for value in values:
        output *= value
    return output
print(mul(5, 7, 9, 10))

