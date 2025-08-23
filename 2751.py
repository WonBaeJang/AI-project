# 수 정렬하기 2
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	256 MB	385598	121214	85045	31.714%
# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 예제 입력 1 
# 5
# 5
# 4
# 3
# 2
# 1
# 예제 출력 1 
# 1
# 2
# 3
# 4
# 5

# 시간초과
# n = int(input())
# nl = []
# for _ in range(n):
#     nl.append(int(input()))
# nl.sort()
# for x in nl:
#     print(x)


# import sys

# input = sys.stdin.readline
# n = int(input())
# nl = [int(input()) for _ in range(n)]
# nl.sort()
# sys.stdout.write('\n'.join(map(str, nl)) + '\n')

import sys

input = sys.stdin.readline
n = int(input())
nl = [int(input()) for _ in range(n)]
nl.sort()
sys.stdout.write('\n'.join(map(str, nl)) + '\n')