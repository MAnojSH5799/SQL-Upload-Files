import json
import requests
import datetime



# print(x)

headers = {"Authorization": "Bearer ya29.a0ARrdaM_Arm1uw0fC9uzUe6CZOBtsHvcloBZiRb9oMDPsbSM31ymcEp77U6eF4QtAO3IrqOb_6b9EdV62KzhMgYBcwZH3UHRo0Hmg46A0lQejFpqS7isnQgXxlNCNbSpzGLY6BRxdlUJifwtVDUkXoVI2S06e"}
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
