import json
from bs4 import BeautifulSoup

with open('./awesome-prompts.html', 'r') as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')
headers = soup.find_all('h2')
blockquotes = soup.find_all('blockquote')


data = []

for i in range(len(headers)):
    header = headers[i].text.replace("\n", "")
    text = blockquotes[i].text.replace("\n", "")
    data.append({
        'category':"Category",
        'title': header,
        'text': text
    })

json_data = json.dumps(data, indent=2)
print(json_data)
