N = int(input())

def queen(answer_list):
    if len(answer_list)==N:
        return 1

    answer = 0
    now_r = len(answer_list)
    for i in range(N):
        a_available = True
        for j,a in enumerate(answer_list):
            if i==a or abs(j-now_r) == abs(a-i):
                a_available = False
                break
        if a_available:
            answer_list.append(i)
            answer += queen(answer_list)
            answer_list.pop()
    return answer

print(queen([]))