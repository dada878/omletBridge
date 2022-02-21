from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge

import json
from bs4 import BeautifulSoup

import logging
from websocket_server import WebsocketServer
import time

import lib
    
class ombBuff:
    def __init__(self,sender,message,omb):
        self.json = json.dumps({
            "type":"buff",
            "sender":sender,
            "message":message,
            "ombCount":omb
        },ensure_ascii=False)

class subscribe:
    def __init__(self,sender):
        self.json = json.dumps({
            "type":"subscribe",
            "sender":sender
        },ensure_ascii=False)

def new_client(client, server):
    while 1:
        time.sleep(2)
        soup = BeautifulSoup(edge.page_source, 'html.parser')

        msg = lib.getLatestMessage(soup)
        try:
            buff = ombBuff(lib.getLatestBuffMessage(soup),lib.getLatestBuffSender(soup),lib.getLatestBuffOmbCount(soup))
            #確認是否有新buff
            if buff.json != lib.getBuffCache():
                server.send_message_to_all(buff.json)
                print(buff.json)

                lib.setBuffCache(buff.json)
        except:
            1 + 1 
        
        try:
            sub = subscribe(lib.getLatestSubscribe(soup))
            #確認是否有新sub
            if sub.json != lib.getSubCache():
                server.send_message_to_all(sub.json)
                print(sub.json)

                lib.setSubCache(sub.json)
        except:
            1 + 1 

        #確認是否有新留言
        if msg.json != lib.getMessageCache():
            server.send_message_to_all(msg.json)
            print(msg.json)

            lib.setMessageCache(msg.json)

edge_options = EdgeOptions()
edge_options.use_chromium = True
edge_options.add_argument('headless')
edge_options.add_argument('disable-gpu')                    

edge = Edge(options=edge_options)
edge.get("https://omlet.gg/streamchat/dada878?transparent=false")

time.sleep(6)

server = WebsocketServer(host='127.0.0.1', port=13254, loglevel=logging.INFO)
server.set_fn_new_client(new_client)
server.run_forever()