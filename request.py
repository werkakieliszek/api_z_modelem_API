import requests

response = requests.get("http://127.0.0.1:5000/Abc?length_s=4.6&length_p=3.2")
print(response.content)
