`var1 = int(input("*** 시작 숫자를 입력하세요(2이상) : "))

var2 = int(input("*** 끝 숫자를 입력하세요 : "))

hap = 0

for i in range(var1, var2+1):

    for j in range(2, i):

        if i % j == 0:

            break

    else:

        hap = hap + i


print("%d부터 %d까지 소수의 합은 %d 입니다." % (var1, var2, hap))
`
