import requests
import urllib

ACCESS_TOKEN= '2107825401.8e9fcea.494a7a948b6f4182b4564cb74ee4c9ad'
BASE_URL= 'https://api.instagram.com/v1/'

#print self profile photo.........................................

def self_profile():
    url =(BASE_URL+ 'users/self/?access_token=%s') %(ACCESS_TOKEN)
    r=requests.get(url).json()
    if r['meta']['code'] == 200:
        if len(r['data']):
            print "your profile pic is %s :" %(r['data']['profile_picture'])
        else:
            print '..'
    else:
        return "you have entered wrong value"

#get self information...........................................

def get_self_info():
    url =(BASE_URL+ 'users/self/?access_token=%s') %(ACCESS_TOKEN)
    print "request url is : %s" %(url)
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

#Id of user using username...................................

def get_user_id(insta_username):
    url= BASE_URL+"users/search?q=%s&access_token=%s" %(insta_username , ACCESS_TOKEN)
    print 'GET request url is : %s' %(url)
    r=requests.get(url).json()

    if r['meta']['code']==200:
        return r['data'][0]['id']
        # if len(r['data']):
        #     return r['data'][0]['id']
        # else:
        #     return None
    else:
        print 'status code other then 200 received'

# getting info of user by using username.......................................

def get_user_info(insta_username):
    # https://api.instagram.com/v1/users/{user-id}/?access_token=ACCESS-TOKEN
    user_id=get_user_id(insta_username)
    if user_id==None:
        print 'user does not exist'
        exit()
    url=(BASE_URL+ "users/%s/?access_token=%s") % (user_id , ACCESS_TOKEN)
    print 'request url is: %s' %(url)
    r=requests.get(url).json()

    if r['meta']['code']==200:
        if len(r['data']):
            print 'Username is: %s' %(r['data']['username'])
            print 'No. of followers: %s' % (r['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (r['data']['counts']['follows'])
            print 'No. of posts: %s' % (r['data']['counts']['media'])
        else:
            print 'there is no data for this user'
    else:
        print 'status code other than 200 received'

#getting our own post...................................
#https://api.instagram.com/v1/users/self/media/recent/?access_token=ACCESS-TOKEN
def get_own_post():
    url=BASE_URL+ "users/self/media/recent/?access_token=%s" %(ACCESS_TOKEN)
    print "GET request url :%s" %(url)
    r=requests.get(url).json()

    if r['meta']['code']==200:
        if len(r['data']):
            img_name=r['data'][0]['id']+'.jpeg'
            img_url=r['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(img_url,img_name)
            print "your image has been downloaded"
        else:
            print "post does not exist"
    else:
        print "status code other than 200 received"

#getting user poet.....................................................

def get_user_post(insta_username)
    url=BASE_URL+""%(get_user_id,ACCESS_TOKEN)

