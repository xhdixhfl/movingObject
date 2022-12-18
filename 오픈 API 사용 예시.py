import requests

url = 'http://apis.data.go.kr/6410000/GOA/GOA001'   # 제공 url 주소 입력

# 서비스 키 자리에 발급받은 키, 타입은 맞게,  , 읽을 페이지 넘버
params = {'serviceKey' : '서비스키', 'type' : 'json', 'numOfRows' : '10', 'pageNo' : '1'} 

response = requests.get(url, params = params)
print(response.content) # 출력

# 결과데이터 형태를 보고 str형태로 뜨면 jason형태로 변형을 해주기
import jason
jason.loads(response.text) 
# jason형태의 결과 데이터 출력
