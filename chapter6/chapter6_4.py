# キャンバスを使って画像表示
import tkinter
from PIL import Image, ImageTk  # ImageTkを指定することで下でImagaTkが使える

  # windowを書く
window = tkinter.Tk()

  # タイトルの指定
window.title("ドリフト画像")

  # キャンバスの作成
canvas = tkinter.Canvas(window, width=800, height=450, bg="red")  # キャンバス自体のサイズや色を決める
canvas.pack()                # winsdowの中央上部に配置
#canvas.place(x=400, y=200)  # windowから見てキャンバスがどの位置にくるか決まる

  # 画像の準備
supra = Image.open("image/supra_320x180.png")
supra = ImageTk.PhotoImage(supra)

  # キャンバスに画像を配置
canvas.create_image(400, 200, image=supra)  # キャンバスから見て画像がどの位置にくるか決まる

window.mainloop()