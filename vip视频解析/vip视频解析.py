import tkinter as tk
import requests
import re
import webbrowser

root = tk.Tk()
root.geometry("900x400+200+200")
root.title("在线观看电影")

def show():
    num = num_int_var.get()
    word = input_var.get()
    if num == 1:
        link = 'https://www.wannengjiexi.com/jiexi1/?url=' + word
        html_data = requests.get(url=link).text
        video_url = re.findall('<iframe id="baiyug" scrolling="no" src="(.*?)"', html_data)[0]
        webbrowser.open(video_url)
    elif num == 2:
        link = 'https://www.wannengjiexi.com/jiexi2/?url=' + word
        html_data = requests.get(url=link).text
        video_url = re.findall('<iframe id="baiyug" scrolling="no" src="(.*?)"', html_data)[0]
        webbrowser.open(video_url)
    elif num == 3:
        link = 'https://www.wannengjiexi.com/jiexi3/?url=' + word
        html_data = requests.get(url=link).text
        video_url = re.findall('<iframe id="baiyug" scrolling="no" src="(.*?)"', html_data)[0]
        webbrowser.open(video_url)

img = tk.PhotoImage(file='img/20170317115702426.png')
tk.Label(root, image=img).pack()

choose_frame = tk.LabelFrame(root)
choose_frame.pack(pady=10, fill='both')
tk.Label(choose_frame, text='选择接口:', font=('黑体', 20)).pack(side=tk.LEFT)
num_int_var = tk.IntVar()
tk.Radiobutton(choose_frame, text='①号通用vip引擎系统【稳定通用】', variable=num_int_var, value=1).pack(side=tk.LEFT, padx=5)
tk.Radiobutton(choose_frame, text='②号通用vip引擎系统【稳定通用】', variable=num_int_var, value=2).pack(side=tk.LEFT, padx=5)
tk.Radiobutton(choose_frame, text='③号通用vip引擎系统【稳定通用】', variable=num_int_var, value=3).pack(side=tk.LEFT, padx=5)

input_frame = tk.LabelFrame(root)
input_frame.pack(pady=10, fill='both')
input_var = tk.StringVar()
tk.Label(input_frame, text='输入视频地址：', font=('黑体', 20)).pack(side=tk.LEFT)
tk.Entry(input_frame, width=100, relief='flat', textvariable=input_var).pack(side=tk.LEFT, fill='both')

go_button = tk.Button(root, text='Go在线解析视频', font=('黑体', 15), relief='flat', bg='#449d44', command=show)
go_button.pack(fill='both')

root.mainloop()
