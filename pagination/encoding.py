import base64

data = "admin"

print(base64.b64encode(data.encode("utf-8")).decode("utf-8"))
print(base64.b64encode(b"admin:admin").decode("utf-8"))
