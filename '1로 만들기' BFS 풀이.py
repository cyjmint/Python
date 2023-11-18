#BFS로 탐색한 결과는 항상 최단거리를 보장

from collections import deque
x = int(input())
Q = deque([x]) 
visited = [0]*(x+1) #값이 있으면 방문 했다는 의미, 값은 해당 노드에 방문하는데 걸린 횟수

while Q:
    c = Q.popleft()
    if c == 1: #계산할 숫자가 1, 즉 목표한 숫자이면 반복문 종료
        break
    if c % 3 == 0 and visited[c//3] == 0: #3으로 나누어지고, 3으로 나눈 숫자에 아직 방문하지 않았으면
        Q.append(c//3) #다음에 계산할 숫자 append
        visited[c//3] = visited[c] + 1
    if c % 2 == 0 and visited[c//2] == 0: #2로 나누어지고, 2로 나눈 숫자에 아직 방문하지 않았으면
        Q.append(c//2)
        visited[c//2] = visited[c] + 1
    if visited[c-1] == 0: #1을 뺀 숫자에 아직 방문하지 않았으면
        Q.append(c-1)
        visited[c-1] = visited[c] + 1
    
print(visited[1]) #1에 방문하는데 걸린 횟수 출력