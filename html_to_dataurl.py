import base64

with open("index.html", "r", encoding="utf-8") as file:
    html_content = file.read()

base64_content = base64.b64encode(html_content.encode("utf-8")).decode("utf-8")

data_url = f"data:text/html;base64,{base64_content}"
print(data_url)
