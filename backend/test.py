import urllib.request
import json

req = urllib.request.Request(
    'http://127.0.0.1:8000/chat',
    data=json.dumps({"message": "merhaba"}).encode('utf-8'),
    headers={'Content-Type': 'application/json'}
)

try:
    with urllib.request.urlopen(req) as response:
        print("SUCCESS:", response.read().decode())
except Exception as e:
    if hasattr(e, 'read'):
        print("ERROR BODY:", e.read().decode())
    else:
        print("ERROR:", e)
