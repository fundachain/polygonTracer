import telebot , web3,mariadb,requests

#api polygonscan
url = "https://api.polygonscan.com/api?module=account&action=txlist&address=0x32d295Cfedc58A638d1CaeF98BE9A895E15d5f6C&startblock=1&endblock=99999999&sort=asc&apikey=V7QT1U7ARJZZ52U5T3WBBPKWW5A6KIWURT"

# telegram bot connection  - enter BOT key
bot = telebot.TeleBot("2053507571:AAGLh6I9PbRJeKFG8TW3fYA4EGgUtpKAV04", parse_mode=None)

#database connection 

try:
    conn = mariadb.connect(
        user="root",
        password="toor",
        host="localhost",
        port=3306,
        database="poly"

    )
    
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()


@bot.message_handler(commands=['add'])
def account_add(message):
    pub_key = message.text.replace("/add ","")
    command_sql = "INSERT INTO accounts(publickey) Values("+pub_key+")"
    cur.execute(command_sql)
    conn.commit()

    bot.reply_to(message,"DOne "+pub_key)
r = requests.get(url)
r = r.json()
h = ""
while True :
    
    if r["status"] == "1" :
        r1  = r["result"]
        r1= r1[-1]
        if  r1["hash"] == h :
            pass
        else :
            h = r1["hash"]
            # print("ALERT", "new hash is : ",h)
            t = "ALERT"
            bot.send_message(536667805,t)
    else :
        r = requests.get(url)
        r = r.json()
    r = requests.get(url)
    r = r.json()

bot.infinity_polling()