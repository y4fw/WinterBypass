import os
import sys
import subprocess
import urllib.request
import tempfile

url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSu9QBmZWUaoXYs1umKum-eILZHoq-ODFIJHw&s"
img_path = os.path.join(tempfile.gettempdir(), "bypasslindo.jpg")

def ensure_pillow():
    try:
        from PIL import Image, ImageTk
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])

ensure_pillow()
from PIL import Image, ImageTk

def download_image():
    try:
        if not os.path.exists(img_path):
            urllib.request.urlretrieve(url, img_path)
    except Exception as e:
        print("erro ao baixar imagem:", e)
        sys.exit()

download_image()

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

img = Image.open(img_path)
img_ratio = img.width / img.height
screen_ratio = screen_w / screen_h

if img_ratio > screen_ratio:
    new_w = screen_w
    new_h = int(screen_w / img_ratio)
else:
    new_h = screen_h
    new_w = int(screen_h * img_ratio)

img = img.resize((new_w, new_h), Image.LANCZOS)
photo = ImageTk.PhotoImage(img, master=root)  # master=root resolve o pyimage1

root.attributes("-fullscreen", True)
root.configure(bg="black")
root.config(cursor="none")

def fechar(event=None):
    root.attributes("-fullscreen", False)
    root.configure(bg="#1a1a1a")
    root.config(cursor="")
    for w in root.winfo_children():
        if isinstance(w, tk.Canvas) and w.winfo_width() == screen_w:
            w.destroy()

root.bind("<Escape>", fechar)
root.bind("<Return>", fechar)
root.bind("<Button-1>", fechar)

canvas = tk.Canvas(root, width=screen_w, height=screen_h,
                   highlightthickness=0, bg="black")
canvas.pack(fill="both", expand=True)

x = (screen_w - new_w) // 2
y = (screen_h - new_h) // 2
canvas.create_image(x, y, anchor="nw", image=photo)
canvas.photo = photo  # evita garbage collection
