# ウィンドウの表示
import tkinter
wind = tkinter.Tk()
wind.title("ベテランのウィンウィンドウ")
wind.geometry("800x600")

label = tkinter.Label(wind, text="お腹空いた", font=("Libian TC", 50))
label.place(x=200, y=100)

wind.mainloop() 