a = input()
print(a)
print(a, end="")
print(type(a))
print(a, type(a), sep=",")

# 점수 변환
a = input()
a = int(a)
print(a, type(a))

b = float(input())
print(b, type(b))

# 정수 2개 입력
# 100
# 200
c = int(input())
b = int(input())
print(c,b)

a = input().split()
print(a, type(a))

a, b, c = map(int, input().split())
print(a, b, c)

# list() 형태로 변환
a = list(map(int, input().split()))
print(a, type(a))


