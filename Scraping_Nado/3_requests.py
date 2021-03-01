import requests
res = requests.get("http://naver.com")
print("응답코드 : ", res.status_code) # 200 이면 정상, 403은 페이지 접근 권한이 없음

if res.status_code == requests.codes.ok: # requests.codes.ok 이건 200이랑 같은거
    print('정상임')
else:
    print('문제가 생김')