import tinder_api.session
import itertools
from datetime import datetime
sess = tinder_api.session.Session() # inits the session

from PIL import Image
import requests
import subprocess
import os

#sess.update_profile(bio="VIM is the best")
img_name = 'WuPro'

import os.path
import psutil
path = './like'
like_files = len([f for f in os.listdir(path)
                if os.path.isfile(os.path.join(path, f))])
path = './dislike'
dislike_files = len([f for f in os.listdir(path)
                if os.path.isfile(os.path.join(path, f))])

like_num = like_files + 1
dislike_num = dislike_files + 1

for user in itertools.islice(sess.yield_usersv2(), 10):
    print(user.name) # prints the name of the user see __init__
    for photo in user.photos:
        im = Image.open(requests.get(photo, stream=True).raw)
        process_list = []
        for proc in psutil.process_iter():
            process_list.append(proc)
        im.show()
        choice = input('1 to like 2 to dislike ')
        if choice == '1':
            im.save('./like/'+ img_name + str(like_num) + '.jpg')
            like_num += 1
        else:
            im.save('./dislike/'+ img_name + str(dislike_num) + '.jpg')
            dislike_num += 1
        for proc in psutil.process_iter():
            if not proc in process_list:
                proc.kill()
    #print(user.photos) 
    # How to check if it exists, if it doesnt, it returns <MisssingValue>
    '''if user.bio is not "<MissingValue>":
        print(user.bio)'''
    print(user.like()) # returns false if not a match



