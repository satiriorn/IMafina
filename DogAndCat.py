import DB, badge, Url, telegram.ext, datetime

def Cat_photo(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.chat_id)
    try:
        Url.Photo(Url.get_url('https://api.thecatapi.com/v1/images/search'), update, context)
    except Exception:
        context.bot.send_message(context.bot_data[update.poll_answer.poll_id], answer["6"])

def Dog_photo(update, context):
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, update.message.from_user.first_name)
    try:
        Url.Photo(Url.get_url('https://random.dog/woof.json'), update, context)
    except Exception:
        context.bot.send_message(context.bot_data[update.poll_answer.poll_id], answer["7"])

def StartSysAnimal():
    cursor = DB.DataBase.UsersSysAnimal(badge.DB)
    target_tzinfo = datetime.timezone(datetime.timedelta(hours=2))
    target_time = None
    for x in cursor:
        for y in range(len(x)):
            if y + 1 < len(x) and x[y + 1] == True:
                for i in range(2):
                    if i==0:
                        target_time = datetime.time(hour=9, minute=00, second=25).replace(tzinfo=target_tzinfo)
                    else:
                        target_time = datetime.time(hour=22, minute=00, second=25).replace(tzinfo=target_tzinfo)
                    badge.jobchat[str(x[y])] = badge.job.run_daily(AnimalJob, target_time, context=x[y])

def SysAnimal(update,context):
    chat_id = update.callback_query.message.chat_id
    answer = DB.DataBase.GetJsonLanguageBot(badge.DB, chat_id)
    cursor = DB.DataBase.UsersSysAnimal(badge.DB)
    target_tzinfo = datetime.timezone(datetime.timedelta(hours=2))
    target_time = datetime.time(hour=9, minute=00, second=25).replace(tzinfo=target_tzinfo)
    NewUser = True
    for x in cursor:
        for y in range(len(x)):
            if str(x[y]) == str(chat_id):
                state = (lambda x, y: True if x[y+1] == False else False) (x,y)
                DB.DataBase.UpdateSysAnimal(badge.DB, chat_id, state)
                if str(chat_id) in badge.jobchat.keys() and state==False:
                    badge.jobchat[str(chat_id)].schedule_removal()
                    badge.jobchat.pop(str(chat_id))
                    context.bot.edit_message_text(chat_id=chat_id, text=answer["37"],
                                                  message_id=update.callback_query.message.message_id)
                    NewUser = False
                    break
                else:
                    badge.jobchat[str(chat_id)] = badge.job.run_daily(AnimalJob, target_time, context=chat_id)
                    context.bot.edit_message_text(chat_id=chat_id, text=answer["37"],
                                                  message_id=update.callback_query.message.message_id)
                    NewUser = False
                break
    if NewUser:
        DB.DataBase.InsertSysAnimal(badge.DB, update.callback_query.message.chat_id, True)
        badge.jobchat[str(chat_id)] = badge.job.run_daily(AnimalJob, target_time, context=chat_id)
        context.bot.edit_message_text(chat_id=chat_id, text=answer["37"],
                                      message_id=update.callback_query.message.message_id)


def AnimalJob(context: telegram.ext.CallbackContext):
    fileID = DB.DataBase.GetFileId(badge.DB, context.job.context)
    file = context.bot.getFile(fileID)
    title = ("{0}.gif").format(context.job.context)
    file.download(title)
    try:
        context.bot.send_video(context.job.context, open(title, 'rb'))
    except Exception:
        context.bot.send_animation(context.job.context, open(title, 'rb'))
    DB.DataBase.UpCountAnimal(badge.DB, context.job.context)