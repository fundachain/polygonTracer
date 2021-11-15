import telebot , web3,requests
from bs4 import BeautifulSoup

#api polygonscan (replace public address{ADDRESS} & apikey{KEY}
url = "https://api.polygonscan.com/api?module=account&action=txlist&address=ADDRESS&startblock=1&endblock=99999999&sort=asc&apikey=KEY"

# telegram bot connection  - enter BOT key
bot = telebot.TeleBot("TOKEN", parse_mode=None)


r = requests.get(url)
r = r.json()
h = ""
while (True) :
    
    if r["status"] == "1" :
        r1  = r["result"]
        r1= r1[-1]
        if  r1["hash"] == h :
            pass
        else :
            h = r1["hash"]
            # print("ALERT", "new hash is : ",h)
            # t = "ALERT"
            func = requests.get("https://polygonscan.com/tx/"+h)
            soup = BeautifulSoup(func.text , 'html.parser')
            func_value = soup.find(id='inputdata')
            func_value = func_value.getText("Function")
            
            t="🚨 Alert 🚨 \n"+func_value+"\n"+"tx id : \n"+ "https://polygonscan.com/tx/"+h
            # replace your userid {USERID} you can use this bot for get userid : https://t.me/@userinfobot
            bot.send_message(USERID,t)

    else :
        r = requests.get(url)
        r = r.json()
    r = requests.get(url)
    r = r.json()

bot.infinity_polling()
