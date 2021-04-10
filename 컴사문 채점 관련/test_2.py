a, b, result = 0, 0, 0

a = int(input("첫 번째 숫자를 입력하시오:"))

b = int(input("두 번째 숫자를 입력하시오:"))


for i in range(a, b+1):

    count = 0

    for j in range(1, i+1):

        if i % j == 0:

            count += 1

    if count == 2:

        result += i

print(a, "부터", b, "까지의  소수들의 합은", result, "이다.")
