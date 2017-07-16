import requests

ACCESS_TOKEN= '2107825401.8e9fcea.494a7a948b6f4182b4564cb74ee4c9ad'
BASE_URL= 'https://api.instagram.com/v1/'

def self_info():
    url =(BASE_URL+ 'users/self/?access_token=%s') %(ACCESS_TOKEN)
    r=requests.get(url).json()
    return r['data']

print self_info()
