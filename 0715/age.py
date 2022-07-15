import requests

response = requests.get('https://api.agify.io/?name=michael')

print(response.json())

final_data = response.json()

name = final_data['name']

print(name)
# output => 응답 데이터
# 저장/조건/반복

