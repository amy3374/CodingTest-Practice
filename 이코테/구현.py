# # 상하좌우
# n = int(input())
# plans = input().split()
# x, y = 1, 1

# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']

# for i in plans:
#     for j in range(len(move_types)):
#         if i == move_types[j]:
#             nx = x + dx[j]
#             ny = y + dy[j]

#     if nx < 1 or nx > n or ny < 1 or ny > n:
#         continue

#     x, y = nx, ny

# print(x, y)

# # 시각
# h = int(input())
# count = 0

# for i in range(h+1):
#     for j in range(60):
#         for s in range(60):
#             if '3' in str(i)+str(j)+str(s):
#                 count += 1
# print(count)

# # 왕실의 나이트
# data = input()
# row = int(data[1])
# column = int(ord(data[0])) - int(ord('a')) + 1

# steps = [(1, -2), (-1, -2), (1, 2), (-1, 2),
#          (2, -1), (2, 1), (-2, -1), (-2, 1)]
# count = 0

# for step in steps:
#     new_row = row + step[0]
#     new_column = column + step[1]

#     if new_row >= 1 and new_row <= 8 and new_column >= 1 and new_column <= 8:
#         count += 1

# print(count)

# # 문자열 재정렬
# data = input()
# num = 0
# result = []

# for i in data:
#     if i.isalpha():
#         result.append(i)
#     else:
#         num += int(i)
# result.sort()

# if num != 0:
#     result.append(str(num))

# print(''.join(result))

# # 럭키 스트레이트
# n = input()
# length = len(n)  #문제 풀 때 이 부분을 생각 못해서 막힘
# left = 0
# right = 0
# for i in range(length//2):
#     left += int(n[i])
# for i in range(length//2, length):
#     right += int(n[i])

# if left == right:
#     print("LUCKY")
# else:
#     print("READY")
