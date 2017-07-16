import requests

ACCESS_TOKEN= '2107825401.8e9fcea.494a7a948b6f4182b4564cb74ee4c9ad'
BASE_URL= 'https://api.instagram.com/v1/'

def self_info():
    url =(BASE_URL+ 'users/self/?access_token=%s') %(ACCESS_TOKEN)
    r=requests.get(url).json()
    if r['meta']['code'] == 200:
        if len(r['data']):
            print "your profile pic is %s :" %(r['data']['profile_picture'])
        else:
            print '..'
    else:
        return "you have entered wrong value"
print self_info()

def user_info():
    url =(BASE_URL+ 'users/self/?access_token=%s') %(ACCESS_TOKEN)
    r=requests.get(url).json()
    if r['meta']['code'] == 200:
        if len(r['data']):
            print 'Username: %s' % (r['data']['username'])
            print 'No. of followers: %s' % (r['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (r['data']['counts']['follows'])
            print 'No. of posts: %s' % (r['data']['counts']['media'])
        else:
            print 'User does not exist!'
    else:
        print 'Status code other than 200 received!'

print user_info()