#try, except문 사용해서 리스트 내 중복값 출력
#key = 중복값, value = 중복 수
count = {}
l = [3,3,6]
for i in l:
    try: count[i] += 1
    except: count[i] = 1
for key, value in count.items():
    if value >= 2:
        print(key)
        
#count() 함수 사용해서 중복값 개수 출력
l = [3,3,6]
cnt = l.count(3)
print('%s은 %d개 있습니다.' %(3, cnt))

#리스트 내 중복값 제거
#set 자료형은 중복값을 허용하지 않으므로 리스트를 set으로 바꿔주면 자동으로 중복값이 삭제됨
s = set(l)
print(s)
l2 = list(s)
print(l2)
