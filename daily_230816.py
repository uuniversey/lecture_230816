

# 1223. 계산기2

# import sys
# sys.stdin = open('input_1223.txt', 'r')
#
# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     formula = input()
#     stack = []
#     top = -1
#     box = []
#     icp = {'+': 1, '*': 2}
#     isp = {'+': 1, '*': 2}
#
#     for i in formula:
#         if i not in '+*':
#             box.append(i)
#         else:
#             if len(stack) == 0:
#                 top += 1
#                 stack.append(i)
#             else:
#                 if icp[i] > isp[stack[top]]:
#                     top += 1
#                     stack.append(i)
#                 else:
#                     top -= 1
#                     box.append(stack.pop())
#                     top += 1
#                     stack.append(i)
#
#     while len(stack) != 0:
#         box.append(stack.pop())
#     # 후위 표기식 완성
#
#     for j in box:
#         if j not in '+*':
#             stack.append(j)
#         else:
#             if j == '+':
#                 cal_B = int(stack.pop())
#                 cal_A = int(stack.pop())
#                 stack.append(cal_A + cal_B)
#             else:
#                 cal_B = int(stack.pop())
#                 cal_A = int(stack.pop())
#                 stack.append(cal_A * cal_B)
#
#     result = stack.pop()
#     print(f'#{tc} {result}')


# # 4408. 자기 방으로 돌아가기

# import sys
# sys.stdin = open('input_4408.txt', 'r')
#


# 18385. 토너먼트 카드게임

# import sys
# sys.stdin = open('input_4880.txt', 'r')
#
#
# def rsp(arr, idx, long):
#
#     if long == 2:
#         if arr[0] == 2 and arr[1] != 3:
#             arr.clear()
#             arr.append(idx[0])
#
#         elif arr[0] == 3 and arr[1] != 1:
#             arr.clear()
#             arr.append(idx[0])
#
#         elif arr[0] == 1 and arr[1] != 2:
#             arr.clear()
#             arr.append(idx[0])
#
#         else:
#             arr.clear()
#             arr.append(idx[1])
#
#     if long == 1:
#         pass
#
#     half = len(arr) // 2
#
#     idx = idx[0:half]
#     long = len(idx)
#     rsp(arr[0:half], idx, long)
#
#     idx = idx[half:len(arr)]
#     long = len(idx)
#     rsp(arr[half:len(arr)], idx, long)
#
#
#
#
# T = int((input()))
# for tc in range(1, T+1):
#     N = int(input())
#     card = list(map(int, input().split()))
#
#     rsp(card, card[0:len(card)], len(card))
#
#     print(f'#{tc} {card}')



# 18388. 배열 최소 합

import sys
sys.stdin = open('input_4881.txt', 'r')

def permutation(idx, result):
    global min_v

    if idx == N:
        if result < min_v:
            min_v = result
        return
    elif min_v <= result:
        return

    else:
        for swap_idx in range(idx, N):      # 바꿀 위치를 반복
            col[idx], col[swap_idx] = col[swap_idx], col[idx]
            permutation(idx + 1, result + arr[idx][col[idx]])    # 다음 자리 확인
            col[idx], col[swap_idx] = col[swap_idx], col[idx]
            # 원상 복구 (처음 모양에서 자리를 바꾸는게 아니라 바뀌어진 모양에서
            # 또 자리를 바꾸기 떄문에 예측하기 어려워 지고 잘못된 동작을 수행하게 된다.)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    col = [i for i in range(N)]
    min_v = 1000000
    permutation(0, 0)

    print(f'#{tc} {min_v}')

# 18404. 부분집합

# import sys
# sys.stdin = open('input_18404.txt', 'r', encoding='UTF8')
#
# arr = list(map(int, input().split()))
# selected = [False] * len(arr)
# my_list = []
# my_sum = 0
# result = 0
#
#
# def powerset(idx):
#     global my_list
#     global my_sum
#     global result
#     if idx == len(arr):
#         for i in range(len(arr)):
#             if selected[i] == True:
#                 my_list.append(arr[i])
#         for j in my_list:
#             my_sum += j
#         if my_sum == 10:
#             result += 1
#         my_list = []
#         my_sum = 0
#         return
#
#     selected[idx] = True
#     powerset(idx + 1)
#
#     selected[idx] = False
#     powerset(idx + 1)
#
# powerset(0)
#
# print(f'#{1} {result}')