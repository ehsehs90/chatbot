"""

requests를 통해 동행복권 API 요청을 보내어,
1등 번호를 가져와 python list로 만듬
"""

import requests

# 1. requests 를 통해 요청 보내기

#가져와라... 브라우저 통해서 직접 게챠하는게 아니라 니가 가져와서 보내라..
url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=873'

#갖고왔으면 응답으로 받아라
response = requests.get(url)
response.text
res_dict = response.json()
print(res_dict)
print(res_dict['drwtNo1'])



#1등 번호 6개가 담긴 result 라는 list를 출력.
temp = []
temp.append(res_dict['drwtNo1'])
temp.append(res_dict['drwtNo2'])
temp.append(res_dict['drwtNo3'])
temp.append(res_dict['drwtNo4'])
temp.append(res_dict['drwtNo5'])
temp.append(res_dict['drwtNo6'])

print(temp)