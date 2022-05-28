import json
import requests
import datetime



# print(x)

headers = {"Authorization": "Bearer ya29.a0ARrdaM9_UF1f60c_bg-Ua5HkNRofe9tn1svcW-UKtwqV-P-KQIg8hsdL9WXCq0-vkT7xSGqLHLLjMkxvJ9l7cp1n3ZIepNjT7V2mMXGc_AeAmVlAt3Aayv7IY6mldlO8T-5PcgHRj8IVeTVNMdQiTNoPZjcq"}
# x = datetime.datetime.now()
para = {
    "name": "duq940.sql",
    # "x" : datetime.datetime.now()
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open("./duq.sql", "rb"),
    
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files 
)
print(r.text)

# import datetime

# x = datetime.datetime.now()

# print(x)
