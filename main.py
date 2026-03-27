import requests
import json
import tkinter as tk

Key=""
history = []
Getkey=False
  


def send_message():   
    user_input = entry.get()
    history.append({"role": "user", "content": user_input})
    
    response = requests.post(
        "http://localhost:1234/v1/chat/completions",
        headers={
            "Authorization": "Bearer " + Key,
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-oss-20b",
            "messages": history,
        }
    )

    if response.status_code != 200:
        output.config(text="エラー：" + response.text)
        return

    response_data = response.json()
    answer = response_data["choices"][0]["message"]["content"]
    history.append({"role": "assistant", "content": answer})
    output.config(text=answer)

def save_key(key):

    global Key, Getkey
    Key = key
    Getkey = True
    Key_label.destroy()
    Key_entry.destroy()
    btn_key.destroy()
    show_chat_ui()

#GUI
root=tk.Tk()
root.title("AIチャットツール")
root.geometry("400x300")


def show_key_ui():  
    global Key_label, Key_entry, btn_key  

    if Getkey:
       btn_return.destroy()
       btn_add.destroy()
       entry.destroy()
       output.destroy()
       show_key.destroy()
       title.destroy()


    Key_label=tk.Label(root, text="APIキー", font=("Arial", 12))
    Key_label.pack()



    Key_entry=tk.Entry(root)
    Key_entry.insert(0, "")
    Key_entry.pack()

    btn_key = tk.Button(root, text="保存", command=lambda: save_key(Key_entry.get()))
    btn_key.pack()

# チャットUIを表示する関数
def show_chat_ui():
    global entry,output,btn_add, btn_return, show_key, title
    
    title=tk.Label(root, text="質問", font=("Arial", 16))
    title.pack()

    btn_return = tk.Button(root, text="APIキーを変更", command=show_key_ui)
    btn_return.pack()


    entry=tk.Entry(root)
    entry.insert(0, "")
    entry.pack()

    btn_add = tk.Button(root, text="送信", command=send_message)
    btn_add.pack()

    output = tk.Label(root, text="")
    output.pack()

    show_key=tk.Label(root, text="APIキー: " + Key, font=("Arial", 10))
    show_key.pack(side=tk.BOTTOM)

    
show_key_ui()
root.mainloop()