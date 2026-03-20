import urllib.request, json, time, base64, sys, os

ART_DIR = "/Users/ai_stretch/.gemini/antigravity/brain/5b227e4a-2e93-4b73-b436-af64a60dd58c"
USER = "chance.ai1234@gmail.com"
KEY = "b3FH73CfMgAazQnPrT14"
auth = base64.b64encode(f"{USER}:{KEY}".encode("utf-8")).decode("utf-8")
headers = {
    "Authorization": f"Basic {auth}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}
target_url = "https://stretch-plus.co.jp/v2/?nocache=" + str(time.time())

data = {
    "url": target_url,
    "browsers": [
        {"os": "ios", "os_version": "8.3", "browser": "Mobile Safari", "device": "iPhone 6 Plus", "browser_version": None, "real_mobile": False}
    ],
    "quality": "original",
    "orientation": "portrait"
}

req = urllib.request.Request("https://www.browserstack.com/screenshots", data=json.dumps(data).encode("utf-8"), headers=headers)
try:
    response = urllib.request.urlopen(req)
    job = json.loads(response.read().decode("utf-8"))
    job_id = job.get("job_id")
    print("✅ BrowserStack Job Started (iPhone):", job_id)
except Exception as e:
    print("❌ Failed to start job:", e)
    sys.exit(1)

while True:
    time.sleep(5)
    r2 = urllib.request.Request(f"https://www.browserstack.com/screenshots/{job_id}.json", headers=headers)
    try:
        res2 = urllib.request.urlopen(r2)
        status = json.loads(res2.read().decode("utf-8"))
        state = status.get("state")
        if state == "done":
            images = status.get("screenshots", [])
            if images:
                img_url = images[0].get("image_url")
                print("Downloading:", img_url)
                save_path = os.path.join(ART_DIR, "bs_iphone.png")
                urllib.request.urlretrieve(img_url, save_path)
                print("✅ Successfully saved screenshot to:", save_path)
                break
            else:
                print("❌ No images returned.")
                break
        elif state == "error":
            print("❌ Job failed.")
            break
        else:
            print("Waiting... state:", state)
    except Exception as e:
        print("❌ Error polling job:", e)
        break
