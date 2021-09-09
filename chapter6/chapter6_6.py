# 図形の表示
import tkinter 
  
  # ウィンドウを描く
window = tkinter.Tk()
window.title("図形を描くよ")  # ウィンドウのタイトル
window.geometry("800x450")  # ウィンドウのサイズ

  # キャンバスの表示
canvas = tkinter.Canvas(window, width=700, height=350, bg="lightskyblue")  # キャンバスのサイズ、色の指定
canvas.pack()  # キャンバスの表示
  # キャンバスに文字を表示
canvas.create_text(150, 50, text="毎日楽しい♪", fill="green", font=("Noteworthy", 24))

  # create_lineでキャンバスに線の表示
canvas.create_line(30,30, 400,350, fill="red", width=5)
canvas.create_line(200,120, 50,140, fill="green", width=8)
canvas.create_line(120,20, 80,50, 200,80, 140,120, fill="blue", smooth=True)  # Trueは曲線、Falseは直線になる

  # create_rectangleでキャンバスに全て直角の四角形（矩形）の表示
canvas.create_rectangle(600,30, 680,80, fill="palegreen", outline="salmon", width=2)

  # create_ovalで円の表示
canvas.create_oval(20,200, 160,330, fill="peru", outline="olive", width=4)

  # create_polygonで多角形の表示
canvas.create_polygon(250,250, 150,350, 350,350, fill="magenta", width=0)
canvas.create_polygon(400,150, 400,340, 660,340, 660,250, fill="navy", outline="yellow", width=2)

  # create_arcで円弧の表示
canvas.create_arc(80,200, 450,300, fill="gold", start=40, extent=120, style=tkinter.CHORD)

  # 最後にウィンドウの表示
window.mainloop()
