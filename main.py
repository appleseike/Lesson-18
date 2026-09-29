from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Main window
root = Tk()
root.title("Denomination Counter")
root.geometry("650x400")
root.config(bg="light blue")

# Add image
img = Image.open("download.jpg")
img = img.resize((300, 300))
photo = ImageTk.PhotoImage(img)

Label(root, image=photo, bg="light blue").place(x=180, y=20)

# Welcome message
Label(root,
      text="Hey User! Welcome to Denomination Counter Application.",
      bg="light blue").place(x=120, y=340)


# Function to open calculator
def open_calculator():

    answer = messagebox.askyesno(
        "Alert",
        "Do you want to calculate the denomination count?"
    )

    if answer:
        calculator_window()


# Calculator window
def calculator_window():

    top = Toplevel(root)
    top.title("Denominations Calculator")
    top.geometry("500x350")
    top.config(bg="light grey")

    Label(top, text="Enter total amount",
          bg="light grey").pack(pady=10)

    amount = Entry(top)
    amount.pack()

    # Result labels
    Label(top, text="2000 notes:", bg="light grey").place(x=100, y=150)
    Label(top, text="500 notes:", bg="light grey").place(x=100, y=190)
    Label(top, text="100 notes:", bg="light grey").place(x=100, y=230)

    result2000 = Entry(top)
    result2000.place(x=250, y=150)

    result500 = Entry(top)
    result500.place(x=250, y=190)

    result100 = Entry(top)
    result100.place(x=250, y=230)


    # Calculate function
    def calculate():

        try:
            money = int(amount.get())   #5000 

            notes2000 = money // 2000   # 5000//2000 = 2

            money = money % 2000        # 5000%2000 = 1000

            notes500 = money // 500      # 1000//500 = 2
            money = money % 500

            notes100 = money // 100      # 1000%500 = 0

            result2000.delete(0, END)
            result500.delete(0, END)
            result100.delete(0, END)

            result2000.insert(0, notes2000)
            result500.insert(0, notes500)
            result100.insert(0, notes100)

        except:
            messagebox.showerror("Error", "Please enter a valid number.")


    Button(top,
           text="Calculate",
           command=calculate,
           bg="brown",
           fg="white").place(x=220, y=100)


# Start button
Button(root,
       text="Let's get started!",
       command=open_calculator,
       bg="brown",
       fg="white").place(x=260, y=370)

