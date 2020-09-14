import requests

# live_dustbin_status api
res = requests.get('https://qdsnh8xlo9.execute-api.ap-south-1.amazonaws.com/default')

response = res.json()
print(response["dustbin_1"])
