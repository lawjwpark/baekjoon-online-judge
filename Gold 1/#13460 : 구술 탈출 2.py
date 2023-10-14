from collections import deque

def solution(N, M, board):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    def bfs():
        

N, M = map(int, input().split())
board = [input() for _ in range(N)]

print(solution(N, M, board))