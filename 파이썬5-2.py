#반복문으로 팩토리얼 구하기
def factorial(n):
    output = 1
    for i in range(1, n + 1):
        output *= i
    return output

print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))

#재귀함수로 팩토리얼 구하기
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))

#재귀함수로 피보나치 수열 구하기(1)
def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print("fibonacci(1):", fibonacci(1))
print("fibonacci(2):", fibonacci(2))
print("fibonacci(3):", fibonacci(3))

#재귀함수로 피보나치 수열 구하기(2)
counter = 0

def fibonacci(n):
    print("fibonacci({})를 구합니다.".format(n))
    global counter
    counter += 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
fibonacci(10)
print("--")
#print("fibonacci(10) 계산에 활용된 덧셈 횟수는 {}번입니다." .format(counter))

#메모화
dictionary = {1: 1, 2: 1}
def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci(n - 1) + fibonacci(n - 2)
        dictionary[n] = output
        return output
    
print("fibonacci(10):", fibonacci(10))

#리스트 평탄화하기(!)
def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += item
        else:
            output.append(item)
    return output

example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본: ", example)
print("변환: ", flatten(example))

#리스트 평탄화하기(2)
def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += flatten(item)
        else:
            output.append(item)
    return output

example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본: ", example)
print("변환: ", flatten(example))

#확인문제
min = 2
max = 10
sum = 100
memo = {}

def qeustion(rest, done):
    key = str([rest, done])
    #종료 조건
    if key in memo:
        return memo[key]
    if rest < 0:
        return 0
    if rest == 0:
        return 1   
    
    count = 0
    for i in range(done, max + 1):
        count += qeustion(rest - i, i)
    
    memo[key] = count
    return count

print(qeustion(sum, min))