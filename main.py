from requests.api import get
from vidstream import *
import tkinter as tk
import socket as sok
import threading as thr
import requests

local_ip_adress = sok.gethostbyname(sok.gethostname())

server = StreamingServer(local_ip_adress, 9999)
receiver = AudioReceiver(local_ip_adress, 8888)

def start_listening():
    t1 = thr.Thread(target=server.start_server)
    t2 = thr.Thread(target=receiver.start_server)
    t1.start()
    t2.start()

def start_camera_stream():
    camera_client = CameraClient(text_target_ip.get(1.0, 'end-1c'), 7777)
    t3 = thr.Thread(target=camera_client.start_stream)
    t3.start()

def start_screen_sharing():
    screen_client = ScreenShareClient(text_target_ip.get(1.0, 'end-1c'), 7777)
    t4 = thr.Thread(target=screen_client.start_stream)
    t4.start()

def start_audio_stream():
    audio_sender = AudioReceiver(text_target_ip.get(1.0, 'end-1c'), 6666)
    t5 = thr.Thread(target=audio_sender.start_stream)
    t5.start()


window = tk.Tk()
window.title("Python Zoom Clone")
window.geometry('300x200')

text_target_ip = tk.Text(window, height=1)
text_target_ip.pack()

label_target_ip = tk.Label(window, text="Target Ip:")
label_target_ip.pack()

btn_listen = tk.Button(window, text="Eshitishni boshlash", width=50, command=start_listening)
btn_listen.pack(anchor=tk.CENTER, expand=True)

btn_camera = tk.Button(window, text="Camerani yoqish", width=50, command=start_camera_stream)
btn_camera.pack(anchor=tk.CENTER, expand=True)

btn_screen = tk.Button(window, text="Screen qilish", width=50, command=start_screen_sharing)
btn_screen.pack(anchor=tk.CENTER, expand=True)

btn_audio = tk.Button(window, text="Audio yozish", width=50, command=start_audio_stream)
btn_audio.pack(anchor=tk.CENTER, expand=True)

window.mainloop()