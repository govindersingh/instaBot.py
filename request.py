import requests
import urllib
import textblob


ACCESS_TOKEN= '2107825401.8e9fcea.494a7a948b6f4182b4564cb74ee4c9ad'
BASE_URL= 'https://api.instagram.com/v1/'

#print self profile photo.........................................
#https://api.instagram.com/v1/users/self/?access_token=ACCESS-TOKEN
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
#https://api.instagram.com/v1/users/self/?access_token=ACCESS-TOKEN
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
#https://api.instagram.com/v1/users/search?q=jack&access_token=ACCESS-TOKEN
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
## https://api.instagram.com/v1/users/{user-id}/?access_token=ACCESS-TOKEN
def get_user_info(insta_username):
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

#get the recent post of a user by username....................................
#https://api.instagram.com/v1/users/{user-id}/media/recent/?access_token=ACCESS-TOKEN
def get_user_post(insta_username):
    user_post=get_user_id(insta_username)
    if user_post==None:
        print "user does not exist"
        exit()
    url=BASE_URL+"users/%s/media/recent/?access_token=%s"%(user_post,ACCESS_TOKEN)
    print "get request url :%s" %(url)
    r=requests.get(url).json()

    if r['meta']['code']==200:
        if len(r['data']):
            image_name = r['data'][0]['id'] + '.jpeg'
            image_url = r['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
        else:
            print "post does not exist"
    else:
        print "status code other than 200 received"

#ID of recent post of user using username.....................
#https://api.instagram.com/v1/users/{user-id}/media/recent/?access_token=ACCESS-TOKEN
def get_post_id(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
        else:
            print 'There is no recent post of the user!'
            exit()
    else:
        print 'Status code other than 200 received!'

#ID of our own post..................................................
#https://api.instagram.com/v1/users/self/media/recent/?access_token=ACCESS-TOKEN
def get_own_post():
    url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (ACCESS_TOKEN)
    print 'GET request url : %s' % (url)
    r = requests.get(url).json()

    if r['meta']['code'] == 200:
        if len(r['data']):
            return r['data'][0]['id']
            image_url = r['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
        else:
            print 'There is no recent post of the user!'
            exit()
    else:
        print 'Status code other than 200 received!'


#liking own post....................................................
#curl -F 'access_token=ACCESS-TOKEN' \
    #https://api.instagram.com/v1/media/{media-id}/likes
def like_own_post():
    media_id = get_own_post()
    url = (BASE_URL + 'media/%s/likes') % (media_id)
    payload = {"access_token": ACCESS_TOKEN}
    print 'POST request url : %s' % (url)
    r= requests.post(url, payload).json()
    if r['meta']['code'] == 200:
        print 'Like was successful!'
    else:
        print 'Your like was unsuccessful. Try again!'


#like recent postof user..............................
#curl -F 'access_token=ACCESS-TOKEN' \
    #https://api.instagram.com/v1/media/{media-id}/likes
def like_user_post(insta_username):
    get_post_id(insta_username)
    media_id = get_post_id(insta_username)
    url = (BASE_URL + 'media/%s/likes') % (media_id)
    payload = {"access_token": ACCESS_TOKEN}
    print 'POST request url : %s' % (url)
    r = requests.post(url, payload).json()
    if r['meta']['code'] == 200:
        print 'Like was successful!'
    else:
        print 'Your like was unsuccessful. Try again!'

#post comment on own post...............................................
#curl -F 'access_token=ACCESS-TOKEN' \
     #-F 'text=This+is+my+comment' \
     #https://api.instagram.com/v1/media/{media-id}/comments
def post_own_comment():
    media_id = get_own_post()
    comment = raw_input("")
    payload = {"access_token": ACCESS_TOKEN, "text": comment}
    url = (BASE_URL + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (url)

    make_comment = requests.post(url, payload).json()
    print make_comment
    if make_comment['meta']['code'] == 200:
        print "Successfully added a new comment!"
    else:
        print "Unable to add comment. Try again!"

post_own_comment()
#post comment on user post.............................................
#curl -F 'access_token=ACCESS-TOKEN' \
     #-F 'text=This+is+my+comment' \
     #https://api.instagram.com/v1/media/{media-id}/comments



