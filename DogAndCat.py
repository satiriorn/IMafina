import  datetime, requests

now = datetime.datetime.now()

def get_url_cat():
    contents = requests.get('http://aws.random.cat/meow').json()
    url = contents['file']
    return url

def get_url_dog():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def is_image(url):
    allowed_extension = ['jpg', 'jpeg', 'png']
    flag = False
    for allowed_ext in allowed_extension:
        if url.lower().endswith(allowed_ext):
            flag = True
            return flag
    return flag

def is_animation(url):
    allowed_extension = ['mp4', 'gif']
    flag = False
    for allowed_ext in allowed_extension:
        if url.lower().endswith(allowed_ext):
            flag = True
            return flag
    return flag

def Photo(url, update):
    if is_image(url):
        update.message.reply_photo(url)
    elif is_animation(url):
        update.message.reply_animation(url)

def Cat_photo(bot, update):
    try:
        url = get_url_cat()
        Photo(url, update)
    except Exception:
        bot.send_message(update.message.chat_id, "Пока без котиков, только не плачь, умоляю")


def Dog_photo(bot, update):
    try:
        url = get_url_dog()
        Photo(url, update)
    except Exception:
        bot.send_message(update.message.chat_id, "Пока без собакеном, только не плачь, умоляю")