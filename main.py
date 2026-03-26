import requests
import json
import tkinter as tk


history = []
def send_message():   
    user_input = entry.get()
    history.append({"role": "user", "content": user_input})
    
    response = requests.post(
        "http://localhost:1234/v1/chat/completions",
        headers={
            "Authorization": "Bearer sk-xxxx",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-oss-20b",
            "messages": history,
        }
    )

    if response.status_code != 200:
        ouput.config(text="エラー：" + response.text)
        return

    response_data = response.json()
    answer = response_data["choices"][0]["message"]["content"]
    history.append({"role": "assistant", "content": answer})
    ouput.config(text=answer)


    


#GUI
root=tk.Tk()
root.title("AIチャットツール")
root.geometry("400x200")

title=tk.Label(root, text="質問", font=("Arial", 16))
title.pack()


entry=tk.Entry(root)
entry.insert(0, "")
entry.pack()

btn_add = tk.Button(root, text="送信", command=send_message)
btn_add.pack()

ouput = tk.Label(root, text="")
ouput.pack()

root.mainloop()