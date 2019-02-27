import requests

# url = 'https://xkcd.com/353/'

url = 'https://imgs.xkcd.com/comics/python.png'

r = requests.get(url)

with open('comic.png', 'wb') as f_obj:
    f_obj.write(r.content)

print(r.status_code)
print(r.ok)
print(r.headers)
