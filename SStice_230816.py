

# 2304. 창고 다각형

import sys
sys.stdin = open('SStice.txt', 'r')

arr = [0] * 1001    # 인덱스를 따기 위한 배열
max_high = 0
left = 10000
right = 0
area = 0
idx = 0
N = int(input())
for i in range(N):
    position, high = map(int, input().split())
    arr[position] = high    # arr에 인덱스를 맞춰서 높이를 인덱스의 밸류값으로 넣는다.

    if max_high < high:     # 제일 높은 곳 찾기
        max_high = high
        idx = position      # 제일 높은 곳의 인덱스 따놓기
    if left > position:     # 제일 왼쪽 찾기
        left = position
    if right < position:    # 제일 오른쪽 찾기
        right = position

stick_L = 0     # 제일 높은 곳 왼쪽의 기둥
stick_R = 0     # 제일 높은 곳 오른쪽의 기둥
for j in range(left, idx):          # 왼쪽인 경우
    if stick_L < arr[j]:            # 높은곳을 만나기 전까지
        stick_L = arr[j]
    area += stick_L                 # 계속 기둥값을 더해준다.

for k in range(right, idx-1, -1):   # 오른쪽인 경우 거꾸로 돈다 왼쪽과 같은 법칙을 사용하기 위해서
    if stick_R < arr[k]:            # 높은곳을 만나기 전까지
        stick_R = arr[k]
    area += stick_R                 # 계속 기둥값을 더해준다.

print(area)

# # 재귀 호출?
#
# def f(i, N):
#     if i == N:
#         print(B)
#         return
#     else:
#         B[i] = A[i]
#         f(i+1, N)
#         return
#
#
# N = 3
# A = [1, 2, 3]
# B = [0] * N
# f(0, N)


# 재귀 호출2?

# def f(i, N):
#     if i == N:
#         print(bit, end=' ')
#         for j in range(N):
#             if bit[j]:
#                 print(A[j], end=' ')
#         print()
#         return
#     else:
#         bit[i] = 1
#         f(i+1, N)
#         bit[i] = 0
#         f(i + 1, N)
#         return
#
#
# A = [1, 2, 3]
# bit = [0] * 3
# f(0, 3)
#
#
# # 부분집합 합 구하기
#
# def f(i, N):
#     if i == N:
#         print(bit, end=' ')
#         s = 0
#         for j in range(N):
#             if bit[j]:
#                 s += A[j]
#                 print(A[j], end=' ')
#         print(f': {s}')
#         return
#     else:
#         bit[i] = 1
#         f(i+1, N)
#         bit[i] = 0
#         f(i + 1, N)
#         return
#
#
# A = [1, 2, 3]
# bit = [0] * 3
# f(0, 3)


# 부분집합 합 구하기

# def f(i, N, s):  # s: i-1 원소까지 부분집합의 합(포함된 원소의 합)
#     if i == N:
#         print(bit, end=' ')
#         print(f': {s}')
#         return
#     else:
#         bit[i] = 1      # 부분집합에 A[i] 포함
#         f(i+1, N, s+A[i])
#         bit[i] = 0      # 부분집합에 A[i] 빠짐
#         f(i + 1, N, s)
#         return
#
#
# A = [1, 2, 3]
# bit = [0] * 3
# f(0, 3, 0)


# 부분집합의 합(백트래킹) - 연습문제

# def f(i, N, s, t):  # s: i-1 원소까지 부분집합의 합(포함된 원소의 합), t: 찾으려는 합
#     global cnt
#     cnt += 1
#     if s == t:
#         print(bit)
#         return
#     elif i == N:    # 남은 원소가 없는 경우
#         return
#     elif s > t:
#         return
#     else:
#         bit[i] = 1      # 부분집합에 A[i] 포함
#         f(i+1, N, s+A[i], t)
#         bit[i] = 0      # 부분집합에 A[i] 빠짐
#         f(i + 1, N, s, t)
#         return
#
# # 1부터 10까지 원소인 집합, 부분집합의 합이 10인 경우는?
# N = 10
# A = [i for i in range(1, N+1)]
# bit = [0] * N
# cnt = 0
# f(0, N, 0, 1)
# print(cnt)


#  순열 1

# def f(i, N):
#     global cnt
#     cnt += 1
#     if i == N:
#         print(A)
#     else:
#         for j in range(i, N):   # 자신부터 오른쪽 끝까지
#             A[i], A[j] = A[j], A[i]
#             f(i+1, N)
#             A[i], A[j] = A[j], A[i]
#
# cnt = 0
# A = [1, 2, 3, 4]
# f(0, 4)
# print(cnt)


# 거듭제곱

# def f1(b, e):
#     global cnt1
#     if b == 0:
#         return 1
#     r = 1
#     for i in range(e):
#         r *= b
#         cnt1 += 1
#     return r
#
#
# def f2(b, e):
#     global cnt2
#     if b == 0 or e == 0:
#         return 1
#     if e % 2:   # 홀수라면
#         r = f2(b, (e-1) // 2)
#         cnt2 += 1
#         return r*r*b
#     else:
#         r = f2(b, e // 2)
#         cnt2 += 1
#         return r * r
#
#
# cnt1 = 0
# cnt2 = 0
# print(f1(2, 28), cnt1)
# print(f2(2, 28), cnt2)


# 부분집합 연습

# arr = [3, 5, 6]     # 부분 집합
# selected = [False] * len(arr)     # 해당 숫자가 선택 됐는지 안됐는지 확인 용도
#
# def powerset(idx):      # idx는 현재 숫자, 위치
#
#     if idx == len(arr):       # +1을 붙인이유 -> selected 크기가 len(arr) + 1 이기 때문
#         # 종료 전에 현재 선택된 부분집합을 출력
#         for i in range(len(arr)):
#             if selected[i] == True:
#                 print(arr[i], end=' ')
#         print()     # 줄바꿈 용도
#
#         return      # 함수 종료 (break를 사용하듯이 함수를 종료하기 위한 목적)
#
#     # 현 위치를 선택했을 경우
#     selected[idx] = True
#     powerset(idx+1)     # 다음 자리 선택
#
#     # 현 위치를 선택하지 않았을 경우
#     selected[idx] = False
#     powerset(idx+1)     # 다음 자리 선택


# powerset(0)     # 0 을 뺀 이유 : 0번 index를 selected에서 사용하지 않기 때문


# 순열 연습

# arr = [0, 1, 2]
# N = len(arr)
#
# def permutation(idx):
#     # 종료 조건
#     if idx == N:
#         print(arr)
#         return
#     else:
#         for swap_idx in range(idx, N):      # 바꿀 위치를 반복
#             arr[idx], arr[swap_idx] = arr[swap_idx], arr[idx]
#             permutation(idx + 1)    # 다음 자리 확인
#             arr[idx], arr[swap_idx] = arr[swap_idx], arr[idx]
#             # 원상 복구 (처음 모양에서 자리를 바꾸는게 아니라 바뀌어진 모양에서
#             # 또 자리를 바꾸기 떄문에 예측하기 어려워 지고 잘못된 동작을 수행하게 된다.)
#
#
# permutation(0)


# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     col = [i for i in range(N)]
#     min_v = 1000000
#
#
#     def permutation(idx):
#         global min_v
#         result = 0
#         if idx == N:
#             for i in range(N):
#                 result += arr[i][col[i]]
#             if min_v > result:
#                 min_v = result
#             result = 0
#             return
#
#         else:
#             for swap_idx in range(idx, len(col)):  # 바꿀 위치를 반복
#                 col[idx], col[swap_idx] = col[swap_idx], col[idx]
#                 permutation(idx + 1)  # 다음 자리 확인
#                 col[idx], col[swap_idx] = col[swap_idx], col[idx]
#                 # 원상 복구 (처음 모양에서 자리를 바꾸는게 아니라 바뀌어진 모양에서
#                 # 또 자리를 바꾸기 떄문에 예측하기 어려워 지고 잘못된 동작을 수행하게 된다.)
#
#
#     permutation(0)
#
#     print(f'#{tc} {min_v}')


