#순차 탐색 알고리즘: 맨 앞에서부터 순서대로 탐색을 실시하는 알고리즘
def LSearch(l,target):
    n = len(l)
    for i in range(n):
        if target == l[i]:
            return i
    return -1

l = [1,2,3,4,5]
n = int(input())
if LSearch(l, n) != -1:
    print(f'타겟 저장 인덱스: {LSearch(l,n)}')
else:
    print('탐색 실패')