"""
python 으로 telegram message보내기

"""

import requests



#(1) getUpdates 을 통해 chat_id를 가져옴
id_url = 'https://api.telegram.org/bot872675185:AAHqLJuLIRJc6QGs-W85MDHONNKMClJkC5w/getUpdates'
response =  requests.get(id_url)
res_dict = response.json()
chat_id = res_dict['result'][0]['message']['chat']['id']

print(chat_id)
# (2) url를 조합하여 requests로 요청 보내기

token = '872675185:AAHqLJuLIRJc6QGs-W85MDHONNKMClJkC5w/'
base_url = 'https://api.telegram.org/'
msg = '555'
method = 'sendMessage?'

url = base_url +'bot'+ token + method + 'chat_id=' +str(chat_id) +'&text='+ msg

requests.get(url)




"""

base_url = 'https://api.telegram.org'

url = f'{base_url}/bot{token}/getUpdates'
res = requests.get(url)
res_dict = res.json()


chat_id 가져오는 스텍
chat_id = str(res_dict['result'][0]['message']['chat']['id'])


url 조합
text='와 자동화햇다'
url = f'{base_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
"""