from google.analytics.admin import AnalyticsAdminServiceClient
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/ai_stretch/Desktop/stretchplus HPremake final/service-account.json"
property_id = "527652667"

try:
    client = AnalyticsAdminServiceClient()
    parent = f"properties/{property_id}"
    request = client.list_data_streams(parent=parent)
    found = False
    for stream in request:
        if stream.web_stream_data:
            print(f"SUCCESS: {stream.web_stream_data.measurement_id}")
            found = True
            break
    if not found:
        print("Error: No Web Data Stream found.")
except Exception as e:
    print(f"Error: {e}")
