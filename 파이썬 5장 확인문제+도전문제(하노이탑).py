#확인문제(1)
numbers = [1, 2, 3, 4, 5, 6]
print('::'.join(str(i) for i in numbers)) #리스트안의 값들을 for문을 통해 하나씩 불러내어 문자열로 변경 후 join 함수로 합침

#확인문제(2)
numbers = list(range(1, 11))
print("홀수만 출력")
print(list(filter(lambda x: x % 2 != 0, numbers)))
print()

print("# 3이상, 7 미만 출력하기")
print(list(filter(lambda x: x >= 3 and x < 7, numbers)))
print()

print("# 제곱해서 50미만 출력하기")
print(list(filter(lambda x: x ** 2 < 50, numbers )))

#도전문제 하노이탑
def top(n, start, final, support):
    if n == 1:
        print(start, '->', final)
        return
    elif n >= 2:
        top(n - 1, start, support, final)
        print(start, '->', final)
        top(n - 1, support, final, start)
        return
n = int(input("원판의 개수를 입력하세요: "))
top(n, start='A', final = 'B', support = 'C')

#하노이탑 이동 횟수
count = 0
def top(n, start, final, support):
    global count
    if n == 1:
        count += 1
        return
    elif n >= 2:
        top(n - 1, start, support, final)
        count += 1
        top(n - 1, support, final, start)
        return
    print(count)
n = int(input("원판의 개수를 입력하세요: "))
top(n, start='A', final = 'B', support = 'C')
print("이동 횟수는 {}회입니다.".format(count))

