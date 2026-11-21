import requests

sheet_id = "1LroFAlr9R1Xk_8-P5FehBQqDCi3QXnc5guK6qQO_3WQ"
gid = "544765590"

url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"
resp = requests.get(url)
print("Aba GID 544765590 - Status:", resp.status_code)
print("Length:", len(resp.text))
