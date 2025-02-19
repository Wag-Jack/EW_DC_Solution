import base64

with open('hint.txt', 'r', newline='') as hint:
    print(base64.b64encode(hint.read().encode("utf-8")).decode("utf-8"))