import tkinter as tk

MSG_HEIGHT = 2
PAD = 2

def init_frames(root):
    frame_main = tk.Frame(root)
    frame_main.pack(fill=tk.BOTH, expand=True)
    input_frame = tk.Frame(frame_main)
    input_frame.pack(fill=tk.X, side = tk.BOTTOM)
    msgs_frame = tk.Frame(frame_main)
    msgs_frame.pack(side=tk.RIGHT)
    nickname_frame = tk.Frame(frame_main)
    nickname_frame.pack(fill=tk.X, side = tk.BOTTOM)
    lbl = tk.Label(frame_main,height=MSG_HEIGHT,text="helloworld")
    lbl.pack(side=tk.TOP)
    return frame_main, input_frame, msgs_frame,nickname_frame

def init_input_frame(frame, nickname_frame):
    txt_entry = tk.Entry(frame)
    txt_entry.pack(fill=tk.X, side = tk.LEFT, expand = True)
    nick_label = tk.Label(nickname_frame,text="Nickname")
    nick_entry = tk.Entry(nickname_frame)
    nick_entry.insert(0, "Anon")
    def click(txt_entry):
        text = txt_entry.get()
        add_label(msgs_frame, text)

    btn = tk.Button(frame,text= "send",command = lambda:click(txt_entry))
    
    btn.pack(side=tk.LEFT)
    nick_label.pack(side=tk.LEFT)
    nick_entry.pack(side=tk.LEFT)

def add_label(frame,text):
    lbl = tk.Label(frame, height=MSG_HEIGHT, background='#92c2f2',text=text)
    lbl.pack(side=tk.TOP,padx=PAD,pady=PAD, anchor = tk.NE)
def init_gui():
    root = tk.Tk()
    frames = init_frames(root)
    input_frame = frames[1]
    nickname_frame = frames[3]
    init_frames(root)
    return root
if __name__ == '__main__':
    root = init_gui()
    root.mainloop()

