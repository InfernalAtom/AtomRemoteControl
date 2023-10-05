import socket
from PIL import Image
import tkinter as tk
from tkinter import scrolledtext
import cv2
import numpy as np

s = socket.socket()

def listen(ip, port, listenCount):
    s.bind((ip, port))
    s.listen(listenCount)
    c,addr = s.accept()

    def send_message():
        info = entry.get()
        c.send(info.encode())
        if info == 'screen':
            viewScreenWindow(c)
        else:
            data = c.recv(524288).decode()  
            text.insert(tk.END, data + '\n')
    def viewScreenWindow(c):
        while True:
            length = recvall(c,16)
            stringData = recvall(c, int(length))
            data = np.fromstring(stringData, dtype='uint8')
            decimg=cv2.imdecode(data,1)
            cv2.imshow('Shunbird ScreenViewer ++',decimg)
            if cv2.waitKey(10) == 27:
                break
        cv2.destroyAllWindows()
    def recvall(sock, count):
        buf = b''
        while count:
            newbuf = sock.recv(count)
            if not newbuf: return None
            buf += newbuf
            count -= len(newbuf)
        return buf
    
    root = tk.Tk()
    root.title("AtomConsole")
    root.geometry("1000x500")
    entry = tk.Entry(root)
    entry.pack()
    send_button = tk.Button(root, text="Send", command=send_message)
    send_button.pack()
    text = scrolledtext.ScrolledText(root,bg="black", fg="white",font=("consolas", 12))
    text.pack()
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    root.mainloop()