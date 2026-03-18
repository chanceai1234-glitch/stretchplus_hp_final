import urllib.request
import json
import base64

data = {
    "filename": "flow_step_3.png",
    "data": base64.b64encode(b"dummy data").decode("utf-8")
}

req = urllib.request.Request(
    'http://localhost:8080/upload',
    data=json.dumps(data).encode('utf-8'),
    headers={'Content-Type': 'application/json'}
)

try:
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
except Exception as e:
    print(f"Fetch failed: {e}")
