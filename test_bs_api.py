import urllib.request, json, time, base64

USER = "chance.ai1234@gmail.com"
KEY = "b3FH73CfMgAazQnPrT14"
auth = base64.b64encode(f"{USER}:{KEY}".encode("utf-8")).decode("utf-8")
headers = {
    "Authorization": f"Basic {auth}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

data = {
    "url": "https://stretch-plus.co.jp/v2/?nocache=" + str(time.time()),
    "browsers": [
        {"os": "ios", "os_version": "6.0", "browser": "Mobile Safari", "device": "iPhone 5"}
    ]
}

req = urllib.request.Request("https://api.browserstack.com/screenshots", data=json.dumps(data).encode("utf-8"), headers=headers)
try:
    response = urllib.request.urlopen(req)
    job = json.loads(response.read().decode("utf-8"))
    print("SUCCESS! Job ID:", job.get("job_id"))
except urllib.error.HTTPError as e:
    print("FAILED:", e.code, e.reason)
    print("Response:", e.read().decode("utf-8"))
