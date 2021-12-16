from tkinter import *

def show_table():
    num = int(entry.get())
    if num > 100:
        str1 = 'ป้อนคะแนนใหม่อีกครั้ง'+ '\n'
    elif num >= 80:
        str1 = 'คุณได้เกรด A'+ '\n'
    elif num >= 70:
        str1 = 'คุณได้เกรด B'+ '\n'
    elif num >= 60:
        str1 = 'คุณได้เกรด C'+ '\n'
    elif num >= 50:
        str1 = 'คุณได้เกรด D'+ '\n'
    elif num < 50:
        str1 = 'คุณได้เกรด F'+ '\n'
    output_label.configure(text = str1, justify=LEFT)

main_window = Tk()
main_window.title("ตัดเกรด")
message_label = Label(text= ' ป้อนคะแนน ' ,font=( ' Verdana ' , 12))
output_label = Label(font=( ' Verdana ' , 12))
entry = Entry(font=( ' Verdana ' , 12), width=6)
cal_button = Button(text= ' คำนวณ ' , font=( ' Verdana ', 12) , command=show_table)
message_label.grid(row=0, column=0,padx=10, pady=10)
entry.grid(row=0, column=1,padx=10, pady=10, ipady=10)
cal_button.grid(row=0, column=2,padx=10, pady=10)
output_label.grid(row=1, column=0, columnspan=3,padx=10, pady=10)
mainloop()

