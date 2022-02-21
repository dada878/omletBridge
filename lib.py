import json

def getLatestSubscribe(soup):
    message = soup.find_all('div', {'class': 'sender__subscribe-by-fan-msg__-2qlU'})
    return message[len(message)-1].getText()

def getLatestCommemt(soup):
    message = soup.find_all('div', {'class': 'msgBody__message__3oBKx'})
    return message[len(message)-1].getText()

def getLatestCommemtSender(soup):
    sender = soup.find_all('span', {'class': 'sender-name'})
    return sender[len(sender)-1].getText()
    
def getLatestBuffMessage(soup):
    message = soup.find_all('div', {'class': 'sender__buff-msg__3u7oJ'})
    return message[len(message)-1].getText()

def getLatestBuffSender(soup):
    sender = soup.find_all('div', {'class': 'message__buff-msg__xbIJQ'})
    return sender[len(sender)-1].getText()

def getLatestBuffOmbCount(soup):
    sender = soup.find_all('div', {'class': 'amount__buff-msg__3411O'})
    return sender[len(sender)-1].getText()

def setMessageCache(txt):
    with open("Cache/msgCache",'w',encoding='utf-8') as f:
        f.write(txt)

def getMessageCache():
    with open("Cache/msgCache",'r',encoding='utf-8') as f:
        return f.read()

def setBuffCache(txt):
    with open("Cache/buffCache",'w',encoding='utf-8') as f:
        f.write(txt)

def getBuffCache():
    with open("Cache/buffCache",'r',encoding='utf-8') as f:
        return f.read()

def setBuffCache(txt):
    with open("Cache/buffCache",'w',encoding='utf-8') as f:
        f.write(txt)

def getBuffCache():
    with open("Cache/buffCache",'r',encoding='utf-8') as f:
        return f.read()

def setSubCache(txt):
    with open("Cache/subscribeCache",'w',encoding='utf-8') as f:
        f.write(txt)

def getSubCache():
    with open("Cache/subscribeCache",'r',encoding='utf-8') as f:
        return f.read()

class comment:
    def __init__(self,sender,message,isSubscribe):
        self.json = json.dumps({
            "type":"comment",
            "sender":sender,
            "message":message,
            "subscriber":isSubscribe
        },ensure_ascii=False)

def getLatestMessage(soup):
    message = soup.find_all('div',{'class':'msg-content__message__3pgTv msg-align-left__message__1KrzQ'})

    msg = message[len(message)-1]

    #get sent message
    message_return =  msg.find('div',{'class':'msgBody__message__3oBKx'}).getText()

    #get sender name
    sender_return = msg.find('span',{'class':'sender-name'}).getText()

    #check Subscribe
    isSubscribe = False
    if msg.find('div',{'class':'msg-sender-badge'}):
        isSubscribe = True

    return comment(sender_return,message_return,isSubscribe)

def login(account,password,edge,By):
    edge.maximize_window()
    edge.get("https://omlet.gg")
    edge.implicitly_wait(10)

    edge.find_element(By.XPATH,'//*[@id="omlet-bar"]/div[2]/div[2]').click()
    edge.implicitly_wait(10)

    edge.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/a/button').click()
    edge.implicitly_wait(10)

    edge.find_element(By.XPATH,'//*[@id="omid"]').send_keys(account)
    edge.find_element(By.XPATH,'//*[@id="pass"]').send_keys(password)
    edge.find_element(By.XPATH,'/html/body/div[2]/div[3]/form/button').click()
    edge.implicitly_wait(10)

    edge.find_element(By.XPATH,'//*[@id="omlet-bar"]/div[2]/div[8]').click()
    edge.find_element(By.XPATH,'//*[@id="my_profile"]').click()

def sendMessage(msg,edge,By):
    edge.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/div/div[2]/div/div/div[2]/div[2]/div[2]').send_keys(msg)
    edge.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/div/div[2]/div/div/div[2]/div[3]/div').click()
    