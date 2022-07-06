# -뒤에 +는 전부다 괄호

strr = input()
# -가 없을 경우 모든 값을 합한다.
if '-' not in strr:
    print(sum(list(map(int, strr.split("+")))))
else:
    # -를 기준으로 나눠서 리스트를만든다
    strr = strr.split("-")
    # 가장 처음의 수는 양수이므로 기본값으로 설정

    base = int(sum(list(map(int, strr[0].split("+")))))

    # -를 기준으로 나눠진 문자열안의 숫자의 합을 기본값에서 뺸다,
    for i in range(1, len(strr)):
        base -= sum(list(map(int, strr[i].split("+"))))
    print(base)
