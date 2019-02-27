import requests

# # Get request
# url = 'https://httpbin.org/get'  # get url
# payload = {'posts': 2, 'count': 25}
# r = requests.get(url, params=payload) # Get request

# # Post request
# url = 'https://httpbin.org/post'  # post url
# payload = {'username': 'swadhi', 'password': 'swadhi'}
# r = requests.post(url, params=payload)  # Post request

# # Basic authentication
# url = 'https://httpbin.org/basic-auth/swadhi/swadhi'
# r = requests.get(url, auth=('swadhi', 'swadhi'))
# r = requests.get(url, auth=('swadhi', 'gibberish'))  # Wrong credentials

# # Timeout example
url = 'https://httpbin.org/delay/10'
r = requests.get(url, timeout=3)  # Wrong credentials

# print(r.url)
print(r)  # <Response [401]>
print(r.text)
# print(r.json())
