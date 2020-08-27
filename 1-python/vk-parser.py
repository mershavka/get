import requests
import pathlib
import shutil
import os

def taken_n_posts():
    token = 'a4c4b52ca4c4b52ca4c4b52c37a4b71199aa4c4a4c4b52cfb823157be21d1d148d028c6'
    version = '5.122'
    domain = 'miptru'
    count = 100
    offset = 0
    all_posts = []
    #https://api.vk.com/method/wall.get?access_token=a4c4b52ca4c4b52ca4c4b52c37a4b71199aa4c4a4c4b52cfb823157be21d1d148d028c6&v=5.122&domain=miptru

    while offset < 200 :
        response = requests.get('https://api.vk.com/method/wall.get', params={
                                                                    'access_token': token,
                                                                    'v': version,
                                                                    'domain': domain,
                                                                    'count': count,
                                                                    'offset': offset
                                                                    })
        data = response.json()['response']['items']
        all_posts.extend(data)
        offset += count

    return all_posts

def file_writer(all_posts):
    path = str(pathlib.Path().absolute()) + '\\' + 'mipt_wall_imgs'
    try:
        shutil.rmtree(path)
    except OSError:
        print ("Deletion of the directory %s failed" % path)
    else:
        print ("Successfully deleted the directory %s" % path)

    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)

    for post in all_posts:
        try:
            img_url = post['attachments'][0]['photo']['sizes'][-1]['url']
        except:
            continue
        img_name = img_url.split("/")[-1]
        print(img_name)
        r = requests.get(img_url)
        open(path + '/' + img_name, 'wb').write(r.content)

all_posts = taken_n_posts()
file_writer(all_posts)