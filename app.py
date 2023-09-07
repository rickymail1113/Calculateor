import tkinter as tk

root = tk.Tk()
root.title("My Python Calculateor")
root.geometry("600x400")

tmp = 0
num = tk.StringVar()
num.set(tmp)

# 計算函式
def cal_process(e):
    global tmp
    # 如果按下等於
    if e == "equal":
        tmp = eval(tmp)   # 使用 eval() 計算
        num.set(tmp)    # 設定顯示的文字變數
        tmp = 0         # 歸零
    # 如果按下AC
    elif e == "empty":
        tmp = 0         # 歸零
        num.set(tmp)
    else:
        # 如果目前的數字不是 0
        if tmp != 0:
            tmp = f'{tmp}{e}'   # 字串相加
        else:
            tmp = f'{e}'      # 顯示輸入的字串
        num.set(tmp)


label = tk.Label(root, textvariable=num,
                borderwidth=1, relief='solid',
                background='#fff', width=20,
                font=('Arial',20), justify='left',
                anchor='e')

#設定文字標籤 輸入內容&輸出結果
label.place(x=20, y=10)

#數字按鈕
btn_7 = tk.Button(root, text='7', font=('Arial',20), width=3, command=lambda: cal_process(7))
btn_7.place(x=105, y=47)
btn_8 = tk.Button(root, text='8', font=('Arial',20), width=3, command=lambda: cal_process(8))
btn_8.place(x=165, y=47)
btn_9 = tk.Button(root, text='9', font=('Arial',20), width=3, command=lambda: cal_process(9))
btn_9.place(x=225, y=47)

#數字按鈕
btn_4 = tk.Button(root, text='4', font=('Arial',20), width=3, command=lambda: cal_process(4))
btn_4.place(x=105, y=107)
btn_5 = tk.Button(root, text='5', font=('Arial',20), width=3, command=lambda: cal_process(5))
btn_5.place(x=165, y=107)
btn_6 = tk.Button(root, text='6', font=('Arial',20), width=3, command=lambda: cal_process(6))
btn_6.place(x=225, y=107)

#數字按鈕
btn_1 = tk.Button(root, text='1', font=('Arial',20), width=3, command=lambda: cal_process(1))
btn_1.place(x=105, y=167)
btn_2 = tk.Button(root, text='2', font=('Arial',20), width=3, command=lambda: cal_process(2))
btn_2.place(x=165, y=167)
btn_3 = tk.Button(root, text='3', font=('Arial',20), width=3, command=lambda: cal_process(3))
btn_3.place(x=225, y=167)

#數字按鈕
btn_0 = tk.Button(root, text='0', font=('Arial',20), width=3, command=lambda: cal_process(0))
btn_0.place(x=105, y=227)

#計算按鈕
btn_add = tk.Button(root, text='+', font=('Arial',20), width=3, command=lambda: cal_process("+"))
btn_add.place(x=285, y=47)

btn_sub = tk.Button(root, text='-', font=('Arial',20), width=3, command=lambda: cal_process("-"))
btn_sub.place(x=285, y=107)

btn_multi = tk.Button(root, text='*', font=('Arial',20), width=3, command=lambda: cal_process("*"))
btn_multi.place(x=285, y=167)

btn_div = tk.Button(root, text='/', font=('Arial',20), width=3, command=lambda: cal_process("/"))
btn_div.place(x=285, y=227)

#結果按鈕
btn_result = tk.Button(root, text='=', font=('Arial',20), width=3, command=lambda: cal_process("equal"))
btn_result.place(x=225, y=227)

#清除按鈕
btn_ac= tk.Button(root, text='ac', font=('Arial',20), width=3, command=lambda: cal_process("empty"))
btn_ac.place(x=165, y=227)



root.mainloop()