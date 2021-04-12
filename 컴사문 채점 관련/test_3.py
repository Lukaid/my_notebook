a = int(input("하트면 1, 별이면 2를 누르세요 :"))

if a == 1:
    num1 = input("숫자를 입력하세요 :")
    print("")
    j = 0
    for j in range(0, len(num1)):
        p = num1[j]
        heart1 = int(p)
        heart2 = ""

        for k in range(0, heart1):
            heart2 += "\u2665"

        print(heart2*2)


elif a == 2:
    num2 = input("숫자를 입력하세요 :")
    print("")
    n = 0
    for n in range(0, len(num2)):
        m = num2[n]
        star1 = int(m)
        star2 = ""
        for o in range(0, star1):
            star2 += "\u2605"
        print(star2*2)

        n += 1

else:

    print("틀렸습니다.")
