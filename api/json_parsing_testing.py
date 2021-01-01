import requests

# live_dustbin_status api
# 'https://qdsnh8xlo9.execute-api.ap-south-1.amazonaws.com/default'
# "http://localhost/cgi-bin/live_dustbin_status.py"
res = requests.get('http://localhost/cgi-bin/temp.py')

response = res.json()
print(type(response))
