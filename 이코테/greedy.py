# # 동전개수 구하기
# n = 1260
# count = 0
# array = [500, 100, 50, 10]

# for coin in array:
#     count += n // coin
#     n %= coin
# print(count)

# # 1이 될 때까지
# n, k = map(int, input().split())
# count = 0
# while True:
#     # n이 k로 나누어 떨어지는 수가 될 때까지 빼기
#     new_n = (n//k)*k
#     count += n - new_n
#     n = new_n

#     # n을 k로 더 이상 나눌 수 없을 때 탈출
#     if n < k:
#         break
#     # n이 k보다 크다면, n을 k로 나눈다
#     count += 1
#     n //= k

# # n이 k보다 작아서 탈출한 경우, 마지막으로 1씩 빼준다
# # 1이 될때까지 빼줘야 함으로
# count += (n-1)
# print(count)

# 다른 방법
# n, k = map(int, input().split())

# count = 0

# while n > k:
#     while n % k != 0:
#         n -= 1
#         count += 1
#     n //= k
#     count += 1
# while n > 1:
#     n -= 1
#     count += 1

# print(count)


# # 곱하기 혹은 더하기
# s = list(map(int, input()))
# first = int(s[0])
# for i in range(1, len(s)):
#     if first <= 1 or s[i] <= 1:
#         first += s[i]
#     else:
#         first *= s[i]

# print(first)

# # 모험가 길드
# n = int(input())
# scare = list(map(int, input().split()))
# scare.sort()
# print(scare)

# group = 0  # 총 그룹의 수
# num = 0  # 현재 그룹에 포함된 모험가의 수5

# for i in scare:
#     num += 1  # 현재 그룹에 모험가 포함
#     if num >= i:  # 모험가의 수가 공포도보다 크거나 같으면
#         group += 1  # 그룹을 만듦
#         num = 0  # 그룹을 만들었으므로 현재 그룹에 포함된 모험가의 수 초기화
# print(group)

# # 숫자 카드 게임
# n, m = map(int, input().split())
# result = 0
# for i in range(n):
#     data = list(map(int, input().split()))
#     min_value = min(data)
#     result = max(result, min_value)
# print(result)

# # 큰 수의 법칙
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))

# data.sort(reverse=True)
# first = data[0]
# second = data[1]

# result = 0

# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
#     if m == 0:
#         break
#     result += second
#     m -= 1
# print(result)

# # 문자열 뒤집기
# data = input()
# count0 = 0
# count1 = 0

# if data[0] == '0':
#     count1 += 1
# else:
#     count0 += 1

# for i in range(len(data)-1):
#     if data[i] != data[i+1]:
#         if data[i+1] == '0':
#             count1 += 1
#         else:
#             count0 += 1

# print(min(count0, count1))

# # 만들 수 없는 금액
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()

# target = 1
# for i in data:
#     if target < i:
#         break
#     else:
#         target += i

# print(target)
