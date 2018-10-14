from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters


#/start Handling
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="SOBAKI ETO PROSTO BLYAD OHUENNAYA TEMA")

#/stop react
def stop(num):
    subprocess.call(["rm","-v","description/"+num])                
           
#MessageHandler
def messagesave(bot, update):
    if ((update.effective_user.username != "goglike") & (update.effective_user.username != "Leenza") & (update.effective_user.username != "kireenkov")):
        bot.send_message(chat_id=update.message.chat_id, text="NAHUI POSHEL, ti ne goglike")
        return
    current_number_file=open("current_number","r")
    current_number=current_number_file.read()
    current_number_file.close()

    if (update.message.text != None ):
        comarr = update.message.text.split(' ')
        if ((comarr[0] == '/stop') & (len(comarr) > 1) ):
            stop(comarr[1])
            bot.send_message(chat_id=update.message.chat_id, text="Task number "+comarr[1] +" stopped")
            return
    
    bot.send_message(chat_id=update.message.chat_id, text="Your task number = "+ current_number+". Use it if you want to stop bot from posting it in form: /stop "+current_number)

    if (len(update.message.photo) != 0):
        desc=open("description/"+current_number,"w")
        desc.write("photo\n")
        incomephotos=update.message.photo
        incomefile=incomephotos[len(incomephotos)-1].get_file();
        incomefile.download(custom_path="pictures/"+current_number+".jpg")
        bot.send_message(chat_id=update.message.chat_id, text="Photo saved")
        if (update.message.caption != None):
            #bot.send_message(chat_id=update.message.chat_id, text="caption "+update.message.caption)
            desc.write("cap")
            cap=open("text/"+current_number,"w")
            cap.write(update.message.caption)
            cap.close()
            bot.send_message(chat_id=update.message.chat_id, text="Caption saved")
    if (update.message.text != None):
        desc=open("description/"+current_number,"w")
        desc.write("text\n")
        desc.close()
        cap=open("text/"+current_number,"w")
        cap.write(update.message.text)
        cap.close()
        bot.send_message(chat_id=update.message.chat_id, text="Text saved")
    if (update.message.document != None):
        print("document")
        desc=open("description/"+current_number,"w")
        desc.write("doc\n")
        incomefile=update.message.document.get_file();
        incomefile.download(custom_path="docs/"+current_number+mimetypes.guess_extension(update.message.document.mime_type))
        bot.send_message(chat_id=update.message.chat_id, text=mimetypes.guess_extension(update.message.document.mime_type)+" saved")
        desc.write(mimetypes.guess_extension(update.message.document.mime_type)+'\n')
        if (update.message.caption != None):
            #bot.send_message(chat_id=update.message.chat_id, text="caption "+update.message.caption)
            desc.write("cap")
            cap=open("text/"+current_number,"w")
            cap.write(update.message.caption)
            cap.close()
            bot.send_message(chat_id=update.message.chat_id, text="Caption saved")
        desc.close()
    if (update.message.video != None):
        print("video")
        desc=open("description/"+current_number,"w")
        desc.write("video\n")
        incomefile=update.message.video.get_file();
        incomefile.download(custom_path="videos/"+current_number)
        bot.send_message(chat_id=update.message.chat_id, text="video saved")
        #desc.write(mimetypes.guess_extension(update.message.document.mime_type)+'\n')
        if (update.message.caption != None):
            #bot.send_message(chat_id=update.message.chat_id, text="caption "+update.message.caption)
            desc.write("cap")
            cap=open("text/"+current_number,"w")
            cap.write(update.message.caption)
            cap.close()
            bot.send_message(chat_id=update.message.chat_id, text="Caption saved")
        desc.close()

    current_number_file=open("current_number","w")
    current_number_file.write(str(int(current_number)+1))
    
    print(update.effective_user.username)


