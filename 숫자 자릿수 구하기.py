def digit_length(n):
    ans = 0
    while n:
        n //= 10 #n //= 10 -> n = n // 10
        ans += 1
    return ans

print(digit_length(0)) #while문에서 조건문이 숫자일 때, n=0이면 False이기 때문에 0이 출력됨.
print(digit_length(10))
print(digit_length(100))
print(digit_length(12345))

#digit_length(100) -> n = 100//10 = 10 -> ans = 1 -> n = 10//10 = 1 -> ans = 2 
#-> n = 1//10 = 0 -> ans = 3