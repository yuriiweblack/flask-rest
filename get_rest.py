import time
import requests

result_post = requests.post("http://127.0.0.1:5000/companies/Cola")
time.sleep(2)
result = requests.get("http://127.0.0.1:5000/companies")

print(result.status_code)
print(result.json())
