url = "https://api.divar.ir/v8/web-search/1/real-estate"
last_post_date = 1691648551038929
token_list=[]
count = 0
while True:
    count+=1
    data ={"json_schema": {"category": {"value": "real-estate"}}, "last-post-date": last_post_date}
    headers = {"Content-Type":"application/json"}
    res = requests.post(url,headers=headers,json=data)
    last_post_date = res.json()['last_post_date']
    for i in res.json()['web_widgets']['post_list']:
        token=i['data']['token']
        token_list.append(token)
    if count>=100:
        break
print('success!')

phone_number = []
TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiMDkzNzY5OTA1ODciLCJpc3MiOiJhdXRoIiwidmVyaWZpZWRfdGltZSI6MTY5MTU2NzI0NywiaWF0IjoxNjkxNTY3MjQ3LCJleHAiOjE2OTI4NjMyNDcsInVzZXItdHlwZSI6InBlcnNvbmFsIiwidXNlci10eXBlLWZhIjoiXHUwNjdlXHUwNjQ2XHUwNjQ0IFx1MDYzNFx1MDYyZVx1MDYzNVx1MDZjYyIsInNpZCI6ImI4YWYxNzYwLTM3NTItNDAwZi05ZWZlLWUyYTZkZjAxNmY2ZSJ9.KSnDwBjD1VgxnaiMQv_MPVtaITqPTRyM7ZvPXHWF06g'
HEADERS = {'Authorization': 'token {}'.format(TOKEN)}
for i in token_list:
    with requests.Session() as s:
        s.headers.update(HEADERS)
        resp = s.get(f'https://api.divar.ir/v8/postcontact/web/contact_info/{i}')
    ppp=resp.json()
    ddd=ppp.get('widget_list')[0].get('data')
    print(ddd['value'])
    
    phone_number.append(ddd['value'])