from tkinter import *
from tkinter import messagebox


def reset_entry():
    age_tf.delete(0, 'end')
    height_tf.delete(0, 'end')
    weight_tf.delete(0, 'end')


def calculate_bmi():
    kg = int(weight_tf.get())
    m = int(height_tf.get()) / 100
    bmi = kg / (m * m)
    bmi = round(bmi, 1)
    bmi_index(bmi)


def bmi_index(bmi):
    if bmi < 18.5:
        messagebox.showinfo('BMI Calculator', f'Your BMI = {bmi} is Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('BMI Calculator', f'Your BMI = {bmi} is Normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('BMI Calculator', f'Your BMI = {bmi} is Overweight')
    elif (bmi > 29.9):
        messagebox.showinfo('BMI Calculator', f'Your BMI = {bmi} is Obesity')
    else:
        messagebox.showerror('BMI Calculator', 'something went wrong!')


ws = Tk()
ws.title('BMI Calculator')
ws.geometry('335x450')
ws.config(bg='#2E4053')

img = PhotoImage(file="image.png")
label = Label(
    ws,
    image=img)
label.place(x=0, y=0)

var = IntVar()

frame = Frame(
    ws,
    padx=50,
    pady=40
)
frame.pack(expand=True)

age_lb = Label(
    frame,
    text="Your Age (2 - 100)"
)
age_lb.grid(row=1, column=1)

age_tf = Entry(
    frame,
)
age_tf.grid(row=1, column=2, pady=5)

gen_lb = Label(
    frame,
    text='Gender'
)
gen_lb.grid(row=2, column=1)

frame2 = Frame(
    frame
)
frame2.grid(row=2, column=2, pady=5)

male_rb = Radiobutton(
    frame2,
    text='Male',
    variable=var,
    value=1
)
male_rb.pack(side=LEFT)

female_rb = Radiobutton(
    frame2,
    text='Female',
    variable=var,
    value=2
)
female_rb.pack(side=RIGHT)

height_lb = Label(
    frame,
    text="Height (cm)  "
)
height_lb.grid(row=3, column=1)

weight_lb = Label(
    frame,
    text="Weight (kg)  ",

)
weight_lb.grid(row=4, column=1)

height_tf = Entry(
    frame,
)
height_tf.grid(row=3, column=2, pady=5)

weight_tf = Entry(
    frame,
)
weight_tf.grid(row=4, column=2, pady=5)

frame3 = Frame(
    frame
)
frame3.grid(row=5, columnspan=3, pady=35)

cal_btn = Button(
    frame3,
    text='CALCULATE',
    command=calculate_bmi
)
cal_btn.pack(side=RIGHT)

reset_btn = Button(
    frame3,
    text='RESET',
    command=reset_entry
)
reset_btn.pack(side=RIGHT)

exit_btn = Button(
    frame3,
    text='Exit',
    command=lambda: ws.destroy()
)
exit_btn.pack(side=RIGHT)

ws.mainloop()