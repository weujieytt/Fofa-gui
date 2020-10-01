from tkinter import *
import requests
import json
import base64
import tkinter.font as tf
from tkinter.messagebox import  showerror ,showinfo
data_url = []
def main(targetsrting):
    try :
        email="290277493@qq.com" #email
        key="你的apikey" #key
        print(targetsrting)
        target=base64.b64encode(targetsrting.encode('utf-8')).decode("utf-8")
        page="1" #翻页数
        size="100" 
        url="https://fofa.so/api/v1/search/all?email="+email+"&key="+key+"&qbase64="+target+"&size="+size
        # print(url)
        global data_url
        data_url=[]
        resp = requests.get(url)
        data_model = json.loads(resp.text)
        save=open('fofaurl.txt','w+')
        for i in data_model['results']: 
            for j in i[0:1]: 
                data_url.append(j)
        for i in data_url:
            save.write(i+"\n")
        save.close()
    except:
        pass
    #print(data_model)
def read_fofa_url():
        t.delete(1.0, 'end')  
        rule_data = e.get()  
        if rule_data=="":
            showerror("error","语法错误！")
          # text()
        main(rule_data)
        if len(data_url)>1:
            for w in data_url:
                t.insert("end", str(w))
                t.insert(INSERT, '\n')
            showinfo(title = "提取成功！",message="提取成功！")
root=Tk()
root.title("Fofa 提取")
# root.geometry("235x600+600+200")
var =StringVar()
ft = tf.Font(family='微软雅黑', size=12)  
e=Entry(root,textvariable=var,font=ft)
e.grid(row=0,column=0)
b=Button(root,text="提取",command=read_fofa_url,width=5).grid(row=0,column=1)
t=Text(root,font=ft,bg = '#ffffff',width=30,height=14)
t.grid(row=1,column=0)
root.mainloop()
