import requests
import urllib
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
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
def get_own_id():
    url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (ACCESS_TOKEN)
    print 'GET request url : %s' % (url)
    r = requests.get(url).json()

    if r['meta']['code'] == 200:
        if len(r['data']):
            print r['data'][0]['id']
            return r['data'][0]['id']
            # image_url = r['data'][0]['images']['standard_resolution']['url']
            # urllib.urlretrieve(image_url, image_name)
            # print 'Your image has been downloaded!'
        else:
            print 'There is no recent post of the user!'
            exit()
    else:
        print 'Status code other than 200 received!'
print get_own_id()

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

#To comment on own post...............................................
#curl -F 'access_token=ACCESS-TOKEN' \
     #-F 'text=This+is+my+comment' \
     #https://api.instagram.com/v1/media/{media-id}/comments
def post_own_comment():
    media_id = get_own_post()
    comment = raw_input("enter your comment : ")
    payload = {"access_token": ACCESS_TOKEN, "text": comment}
    url = (BASE_URL + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (url)

    make_comment = requests.post(url, payload).json()
    print make_comment
    if make_comment['meta']['code'] == 200:
        print "Successfully added a new comment!"
    else:
        print "Unable to add comment. Try again!"

#To comment on user post.............................................
#curl -F 'access_token=ACCESS-TOKEN' \
     #-F 'text=This+is+my+comment' \
     #https://api.instagram.com/v1/media/{media-id}/comments
def post_a_comment(insta_username):
    media_id = get_post_id(insta_username)
    comment = raw_input("Your comment: ")
    payload = {"access_token": ACCESS_TOKEN, "text": comment}
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (request_url)

    make_comment = requests.post(request_url, payload).json()

    if make_comment['meta']['code'] == 200:
        print "Successfully added a new comment!"
    else:
        print "Unable to add comment. Try again!"

#delete negative comments from recent post user of user

def delete_negative_comment(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()

    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                    print 'Negative comment : %s' % (comment_text)
                    delete_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') % (media_id, comment_id, ACCESS_TOKEN)
                    print 'DELETE request url : %s' % (delete_url)
                    delete_info = requests.delete(delete_url).json()

                    if delete_info['meta']['code'] == 200:
                        print 'Comment successfully deleted!\n'
                    else:
                        print 'Unable to delete comment!'
                else:
                    print 'Positive comment : %s\n' % (comment_text)
        else:
            print 'There are no existing comments on the post!'
    else:
        print 'Status code other than 200 received!'

#get listof comments on your own recent post

def get_own_comment_list():
    media_id=get_own_post()
    request_url= (BASE_URL+ 'media/%s/comments?access_token=%s') %(media_id , ACCESS_TOKEN)
    print'GET request url=%s' %(request_url)
    comment_list=requests.get(request_url).json()
    print comment_list
    if comment_list['meta']['code'] == 200:
        if len(comment_list['data']):
            print'list of comments'
            number=1
            for text in comment_list['data']:
                print'%s from %s\n comment=%s' %(number,text['from']['username'],text['text'])
                number=number+1
        else:
            print'no comments found'
            return None
    else:
        print'status code other than 200 recieved'
        exit()

#Get list of comment of a users recent post

def user_comment_list(insta_username):
    media_id=get_user_post(insta_username)
    request_url = (BASE_URL + 'media/%s/comments?access_token=%s') % (media_id, ACCESS_TOKEN)
    print'GET request url=%s' % (request_url)
    comment_list = requests.get(request_url).json()
    print comment_list
    if comment_list['meta']['code'] == 200:
        if len(comment_list['data']):
            print'list of comments'
            number = 1
            for text in comment_list['data']:
                print'%s from %s\n comment=%s' % (number, text['from']['username'], text['text'])
                number = number + 1
        else:
            print'no comments found'
            return None
    else:
        print'status code other than 200 recieved'
        exit()


def start_bot():
    while True:
        try:
            username_selection = int(raw_input("do you want to continue with the username already provided=rajan.rana.05\n if yes type 1\n else press 2"))
            if username_selection == 1:  # starting with the already provided username
                while True:
                    try:
                        print 'welcome to instabot'
                        print'here are you menu options'
                        print'1.Get your own details\n'
                        print'2.Get your own recent post\n'
                        print'3.Get ID of your recent post\n'
                        print'4.like your recent post\n'
                        print'5.comment on your recent post\n'
                        print'6.Get comment list on your recent post\n'
                        print'0.To exit'
                        selection = int(raw_input('enter your choice'))
                        if selection == 1:
                            get_self_info()
                        elif selection == 2:
                            get_own_post()
                        elif selection == 3:
                            get_own_id()
                        elif selection == 4:
                            like_own_post()
                        elif selection == 5:
                            post_own_comment()
                        elif selection == 6:
                            get_own_comment_list()
                        elif selection == 0:
                            exit()
                        else:
                            print "INVALID ENTRY,ENTER AGAIN"
                    except ValueError:
                        print'ENTER CORRECT INPUT PLEASE'

            else:

                while True:
                    try:
                        print '\n'
                        print 'Hey! Welcome to instaBot!'
                        print 'Here are your menu options:'
                        print "1.Get details of a user by username\n"
                        print "2.Get the recent post and ID of post of a user by username\n"
                        print "3.Like the recent post of a user\n"
                        print "4.Get a list of comments on the recent post of a user\n"
                        print "5.Make a comment on the recent post of a user\n"
                        print "6.Delete negative comments from the recent post of a user\n"
                        print "0.For exit"

                        choice = int(raw_input("Enter you choice: "))
                        if choice == 1:
                            insta_username = raw_input("Enter the username of the user: ")
                            get_user_info(insta_username)
                        elif choice == 2:
                            insta_username = raw_input("Enter the username of the user: ")
                            get_user_post(insta_username)
                            get_post_id(insta_username)
                        elif choice == 3:
                            insta_username = raw_input("Enter the username of the user: ")
                            like_user_post(insta_username)
                        elif choice == 4:
                            insta_username = raw_input("Enter the username of the user: ")
                            user_comment_list(insta_username)
                        elif choice == 5:
                            insta_username = raw_input("Enter the username of the user: ")
                            post_a_comment(insta_username)
                        elif choice == 6:
                            insta_username = raw_input("Enter the username of the user: ")
                            delete_negative_comment(insta_username)
                        elif choice == 0:
                            exit()
                        else:
                            print "PLEASE ENTER A CORRECT INPUT"
                    except ValueError:
                        print'ENTER A VALID INPUT PLEASE'
        except ValueError:
            print'enter a valid input please'


print start_bot()