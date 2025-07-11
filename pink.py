# デスクトップマスコット 伺か みたいなやつ
import tkinter as tk
from tkinter import ttk
import os
import glob
import random
import tkinter.font # フォントの設定
from tkinter import messagebox
#天気予報APIで使う
import requests
from datetime import datetime
# 時報のチャイム音(.mp3)に使う
import pygame
import time

#ランチャーに使う
import subprocess
import configparser

import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass


# ----------
# アプリランチャー

class Luncher:

    # config.iniの読み込み
    config = configparser.ConfigParser()
    config.read("config.ini")

    direction = config.get("Gneneral", "direction")

    #icon0_path = config.get("IconPaths", "icon0_path")
    #icon1_path = config.get("IconPaths", "icon1_path")
    icon2_path = config.get("IconPaths", "icon2_path")
    icon3_path = config.get("IconPaths", "icon3_path")
    icon4_path = config.get("IconPaths", "icon4_path")
    icon5_path = config.get("IconPaths", "icon5_path")
    icon6_path = config.get("IconPaths", "icon6_path")
    #command1 = config.get("Commands", "command1")
    command2 = config.get("Commands", "command2")
    command3 = config.get("Commands", "command3")
    command4 = config.get("Commands", "command4")
    command5 = config.get("Commands", "command5")
    command6 = config.get("Commands", "command6")


    """
     events
    """
    # These events handle dragging the window.
    def mouseDown(self, e):
        if e.num == 1: # 左クリックしたとき
            self.origin = (e.x, e.y)
            self.isMouseDown = True

    def mouseRelease(self, e):
        self.isMouseDown = False

    def mouseMove(self, e):
        if self.isMouseDown:
            buf = self.root.geometry().split("+")
            self.setPos(e.x - self.origin[0] + int(buf[1]),
                        e.y - self.origin[1] + int(buf[2]),
                        )
    """
     set geometry, Position
    """
    def setPos(self, x, y):
        self.root.geometry("+%s+%s" % (x, y))

    # The application is terminated by pressing the "ESC" key.
    def keyRelease(self, e):
        if e.keycode == 27:
            self.root.destroy()

        
    def lunch_icon1(self,event=None):
        subprocess.Popen([r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "-incognito",'--new-window https://mail.google.com/mail/ https://sites.google.com/kaienonline.com/trainingsite2020/home https://sites.google.com/kaienonline.com/area-kk/ https://kaien-t.slack.com/ https://ibmcsr.udemy.com/'])

    def lunch_icon2(self,event=None):
        subprocess.Popen(self.command2)

    def lunch_icon3(self,event=None):
        subprocess.Popen(self.command3)

    def lunch_icon4(self,event=None):
        subprocess.Popen(self.command4)

    def lunch_icon5(self,event=None):
        subprocess.Popen(self.command5)

    def lunch_icon6(self,event=None):
        subprocess.Popen(self.command6)


    def main_luncher(self):

        #self.root = tk.Tk()
        self.top = tk.Toplevel(root) #別クラスの場合はこっち
        self.top.overrideredirect(True)
        #root.wm_attributes("-transparentcolor", "red")
        #style = ttk.Style()
        #style.configure("Transparent.TFrame", background="red")
        frame = ttk.Frame(self.top, style="Transparent.TFrame", width=400, height=300)
        frame.pack()

        self.canvas0 = tk.Canvas(frame, width=28, height=28,bg="red", highlightthickness=0, bd=0)
        if self.direction != "Y":
            self.canvas0.pack(anchor=tk.NW,side=tk.LEFT)
        else:
            self.canvas0.pack()
        img0 = tk.PhotoImage(file="icons/apps.png")
        icon0 = self.canvas0.create_image(20, 20, image=img0)

        self.screenInit(self.top)

        canvas1 = tk.Canvas(frame, width=28, height=28,bg="red", highlightthickness=0, bd=0)
        if self.direction != "Y":
            canvas1.pack(anchor=tk.NW,side=tk.LEFT)
        else:
            canvas1.pack()
        img1 = tk.PhotoImage(file="icons/internet.png")
        icon1 = canvas1.create_image(20, 20, image=img1)

        canvas2 = tk.Canvas(frame, width=28, height=28,bg="red", highlightthickness=0, bd=0)
        if self.direction != "Y":
            canvas2.pack(anchor=tk.NW,side=tk.LEFT)
        else:
            canvas2.pack()
        img2 = tk.PhotoImage(file=self.icon2_path)
        icon2 = canvas2.create_image(20, 20, image=img2)

        canvas3 = tk.Canvas(frame, width=28, height=28,bg="red", highlightthickness=0, bd=0)
        if self.direction != "Y":
            canvas3.pack(anchor=tk.NW,side=tk.LEFT)
        else:
            canvas3.pack()
        img3 = tk.PhotoImage(file=self.icon3_path)
        icon3 = canvas3.create_image(20, 20, image=img3)

        canvas4 = tk.Canvas(frame, width=28, height=28,bg="red", highlightthickness=0, bd=0)
        if self.direction != "Y":
            canvas4.pack(anchor=tk.NW,side=tk.LEFT)
        else:
            canvas4.pack()
        img4 = tk.PhotoImage(file=self.icon4_path)
        icon4 = canvas4.create_image(20, 20, image=img4)

        canvas5 = tk.Canvas(frame, width=28, height=28,bg="red", highlightthickness=0, bd=0)
        if self.direction != "Y":
            canvas5.pack(anchor=tk.NW,side=tk.LEFT)
        else:
            canvas5.pack()
        img5 = tk.PhotoImage(file=self.icon5_path)
        icon5 = canvas5.create_image(20, 20, image=img5)

        canvas6 = tk.Canvas(frame, width=28, height=28,bg="red", highlightthickness=0, bd=0)
        if self.direction != "Y":
            canvas6.pack(anchor=tk.NW,side=tk.LEFT)
        else:
            canvas6.pack()
        img6 = tk.PhotoImage(file=self.icon6_path)
        icon6 = canvas6.create_image(20, 20, image=img6)

        self.top.configure(bg="red")  # 背景を透明にしたい色に設定
        #self.top.wm_attributes("-transparentcolor", canvas1["bg"])
        self.top.wm_attributes("-transparentcolor", "red")
        self.top.attributes("-topmost", True)

        # イベントバインド
        canvas1.tag_bind(icon1, "<Button-1>", self.lunch_icon1)
        canvas2.tag_bind(icon2, "<Button-1>", self.lunch_icon2)
        canvas3.tag_bind(icon3, "<Button-1>", self.lunch_icon3)
        canvas4.tag_bind(icon4, "<Button-1>", self.lunch_icon4)
        canvas5.tag_bind(icon5, "<Button-1>", self.lunch_icon5)
        canvas6.tag_bind(icon6, "<Button-1>", self.lunch_icon6)

        self.top.mainloop()

    def screenInit(self,root):
    
        # Set window size
        offset_x = root.winfo_screenwidth() -250-200
        offset_y = root.winfo_screenheight() -400+200
        self.top.geometry("263x349"+"+"+str(offset_x)+"+"+str(offset_y))
        """
            Bind events
        """
        self.canvas0.bind("<Button>", self.mouseDown)
        self.canvas0.bind("<ButtonRelease>", self.mouseRelease)
        self.canvas0.bind("<Motion>", self.mouseMove)
        self.top.bind_all("<KeyRelease>", self.keyRelease)

    def __init__(self,root):

        self.root = root # わけわからんが

        self.origin = (0, 0)
        self.isMouseDown = False
        self.main_luncher()


# ----------
# 天気予報API
# get_weather() で戻り値は文字列
# 2025年06月24日の京都府 京都 の天気は曇時々雨です。
# 最高気温は28度、最低気温は25度です。

KYOTO = 260010
def get_weather():
    try:
        url = f"https://weather.tsukumijima.net/api/forecast?city={KYOTO}"
        response  = requests.get(url)
        response.raise_for_status()

        data_json = response.json()
    
        date_str = data_json["forecasts"][1]["date"]
        date = datetime.strptime(date_str,"%Y-%m-%d").strftime("%Y年%m月%d日")
        title = data_json["title"]
        weather = data_json["forecasts"][1]["telop"]
        max_temp = data_json["forecasts"][1]["temperature"]["max"]["celsius"]
        min_temp = data_json["forecasts"][1]["temperature"]["min"]["celsius"]
        
        results = f"{date}の{title}は{weather}です。\n最高気温は{max_temp}℃、最低気温は{min_temp}℃です。"
        return results
    
    except requests.exceptions.RequestException as e:
        return f"天気情報の取得に失敗しました: {e}"
        
    except KeyError as e:
        return f"予期しないデータ形式です: {e}"
    
# ----------

class Mascot:

    # 時報の音
    pygame.mixer.init()
    pygame.mixer.music.load("assets/chime_nhk.mp3")

    """
     events
    """
    # These events handle dragging the window.
    def mouseDown(self, e):
        if e.num == 1: # 左クリックしたとき
            self.origin = (e.x, e.y)
            self.isMouseDown = True

    def mouseRelease(self, e):
        self.isMouseDown = False

    def mouseMove(self, e):
        if self.isMouseDown:
            buf = self.root.geometry().split("+")
            self.setPos(e.x - self.origin[0] + int(buf[1]),
                        e.y - self.origin[1] + int(buf[2]),
                        )
            buf_oppai = self.oppai.geometry().split("+") # oppaiも同時に動かす
            self.setPosOppai(e.x - self.origin[0] + int(buf_oppai[1]),
                        e.y - self.origin[1] + int(buf_oppai[2]),
                        )
            buf_bubble = self.bubble.geometry().split("+") # 吹き出しも同時に動かす
            self.setPosBubble(e.x - self.origin[0] + int(buf_bubble[1]),
                        e.y - self.origin[1] + int(buf_bubble[2]),
                        )
    
    def mouseMoveBubble(self, e): # 吹き出し用
        if self.isMouseDown:
            buf = self.bubble.geometry().split("+")
            self.setPosBubble(e.x - self.origin[0] + int(buf[1]),
                        e.y - self.origin[1] + int(buf[2]),
                        )

    def mouseClickOppai(self,e): # oppaiをクリックしたとき
        messagebox.showwarning("おさわり禁止", "ちょっと、どこ触ってるんですか！")

    # The application is terminated by pressing the "ESC" key.
    def keyReleease(self, e):
        if e.keycode == 27:
            self.root.destroy()

    """
     set geometry, Position
    """
    def setPos(self, x, y):
        self.root.geometry("+%s+%s" % (x, y))

    def setPosOppai(self, x, y): # oppai用
        self.oppai.geometry("+%s+%s" % (x, y))

    def setPosBubble(self, x, y): # 吹き出し用
        self.bubble.geometry("+%s+%s" % (x, y))

    """
     load image, and drawing to canvas
    """
    # 体本体を表示する。
    def dispImageBody(self, path):
        self.canvas.delete("all")
        self.image = tk.PhotoImage(file=path)
        self.canvas.create_image(0, 0, image=self.image, anchor="nw")
    
    # oppai穴(※ウィンドウの穴)をつくる
    def dispOppaiHole(self, has_oppai):
        self.canvas.delete("oppai_hole")
        if(has_oppai): # has_oppai=Falseの場合はOppai穴を消しただけで終わり
            self.canvas.create_rectangle(105,170,105+45,170+35, fill = "#FC0204",tag="oppai_hole",width=0)

    # oppaiを表示する。
    def dispImageOppai(self, path): 
        self.oppai_canvas.delete("all")
        self.oppai_image = tk.PhotoImage(file=path)
        self.oppai_canvas.create_image(-105, -170, image=self.oppai_image, anchor="nw") ###############

    # 顔の差分を上から表示する
    def dispImageFace(self, path):
        self.canvas.delete("face") # faceタグで、顔差分を一旦、削除する。
        if(path!=""): # path==""の場合は顔面差分を消しただけで終わり
            self.image_face = tk.PhotoImage(file=path)
            self.canvas.create_image(0, 0, image=self.image_face, anchor="nw", tag="face") # タグ付け

    def dispImageBubble(self, path,lines):
        self.bubble_canvas.delete("all") # 吹き出しを一旦消す
        self.text_widget.delete('1.0', 'end') # セリフを一旦消す（枠は残る）
        self.text_widget.place_forget() # セリフを一旦消す（枠ごと消す）←効果ない？？？
        if lines != "":
            self.bubble_image = tk.PhotoImage(file=path)
            self.bubble_canvas.create_image(0, 0, image=self.bubble_image, anchor="nw")
            self.bubble_canvas.dchars("lines", 0) # 吹き出しのセリフ文字列を一旦、削除
            self.bubble_canvas.create_text(190,110, text="Esc：閉じる", anchor="nw",tag="lines") # タグ付け
            
            self.text_widget.place(x=40,y=40)
            self.text_widget.insert(tk.END,lines)

    """
     create main window
    """

    def screenOppaiInit(self):
        self.oppai = tk.Toplevel(self.root)     # 別ウィンドウを作成
        offset_x = self.oppai.winfo_screenwidth() -250 +105
        offset_y = self.oppai.winfo_screenheight() -400 +170
        self.oppai.geometry("45x35"+"+"+str(offset_x)+"+"+str(offset_y))
        self.oppai.overrideredirect(True) # ウィンドウのデコレーションを消す
        self.oppai_canvas = tk.Canvas(self.oppai, bd=0, highlightthickness=0, bg="#55AA55", cursor='hand2')
        self.oppai_canvas.pack(expand=True, fill=tk.BOTH)
        self.oppai.attributes("-topmost", True)# このウィンドウは体の直ぐ後ろに表示する．

    def screenInit(self):
        # Set window size
        offset_x = self.root.winfo_screenwidth() -250
        offset_y = self.root.winfo_screenheight() -400
        self.root.geometry("263x349"+"+"+str(offset_x)+"+"+str(offset_y))

        # Create canvas and drawing image
        self.canvas = tk.Canvas(self.root, bd=0, highlightthickness=0, bg="#FC0204")
        #self.canvas.pack(fill="both") # これだと下側が切れて表示される．
        self.canvas.pack(expand=True, fill=tk.BOTH)
        self.dispImageBody("images/000_000.png")

        """
         Various settings
        """
        # Transparency setting ウィンドウを透過設定
        self.root.wm_attributes("-transparentcolor", self.canvas["bg"])
        # Disable window decoration ウィンドウのデコレーションを消す
        self.root.overrideredirect(True)
        # Fix the screen to the front ウィンドウを最前面に表示
        self.root.attributes("-topmost", True)

        """
         Bind events
        """
        self.canvas.bind("<Button>", self.mouseDown)
        self.canvas.bind("<ButtonRelease>", self.mouseRelease)
        self.canvas.bind("<Motion>", self.mouseMove)
        self.oppai_canvas.bind("<Button-1>", self.mouseClickOppai)
        self.root.bind_all("<KeyRelease>", self.keyReleease)

    # 吹き出しのウィンドウ
    def bubbleInit(self):
        self.bubble = tk.Toplevel(self.root)     # 別ウィンドウを作成
        offset_x = self.bubble.winfo_screenwidth() - 500
        offset_y = self.bubble.winfo_screenheight() -350
        self.bubble.geometry("320x200"+"+"+str(offset_x)+"+"+str(offset_y))
        self.bubble_canvas = tk.Canvas(self.bubble, bd=0, highlightthickness=0, bg="#FF0000")
        self.bubble_canvas.pack(expand=True, fill=tk.BOTH)
        #self.dispImageBubble("images/bubble.png","Hello World !")

        self.bubble.wm_attributes("-transparentcolor", self.bubble_canvas["bg"])
        self.bubble.overrideredirect(True)
        self.bubble.attributes("-topmost", True)
        
        self.f = tk.font.Font(family="UD Digi Kyokasho NK",size=9) # 游ゴシック体 "Yu Gothic"
        self.text_widget = tk.Text(self.bubble, height=4, width=24, bd=0,wrap=tk.WORD,font=self.f)
        #self.text_widget.insert(tk.END,"Hello World Good Morning")
        self.text_widget.place(x=40,y=40)

        self.bubble_canvas.bind("<Button>", self.mouseDown)
        self.bubble_canvas.bind("<ButtonRelease>", self.mouseRelease)
        self.bubble_canvas.bind("<Motion>", self.mouseMoveBubble)
        self.bubble.bind_all("<KeyRelease>", self.keyReleease)

    # 体を右クリックした際にポップアップメニューを表示する
    def showMenu(self,e):
        self.pmenu.post(e.x_root, e.y_root)

    def popupMenu(self):
        self.pmenu = tkinter.Menu(self.root, tearoff=0)
        self.pmenu.add_command(label="Exit", command=self.root.quit)

        self.root.bind("<Button-3>", self.showMenu) # 右クリック
        pass

    # imageフォルダ内のpngファイルをリストアップする。
    def pngFileList(self):
        # 体のPathをリスト化する
        self.body_path_list = glob.glob("images/*_000.png") # 003だけ素材pngのファイル名を変更
  
        # 顔のPathを3次元リストにする
        self.face_path_list = [[[]]]

        self.face_path_list[0][0][0:0]=glob.glob("images/000_000?.png")
 
        for i in range(0,9+1+1): #000_000x～#000_009x,000_039,000_xxx
            self.face_path_list[0].append([])
        for i in range(1,9+1+1):
            self.face_path_list[0][i][0:0]=glob.glob("images/000_00"+str(i)+"*.png")
        self.face_path_list[0][10][0:0]=glob.glob("images/000_039.png") # ←飛び番？
        self.face_path_list[0][11][0:0]=glob.glob("images/000_xxx.png") # ←飛び番？

        self.face_path_list.append([]) #001_000x～001_009
        for i in range(0,8):
            self.face_path_list[1].append([])
        self.face_path_list[1][0][0:0]=glob.glob("images/001_000?.png")
        self.face_path_list[1][1][0:0]=glob.glob("images/001_001.png") # ←飛び番？
        for i in range(3,7+1):
            self.face_path_list[1][i-1][0:0]=glob.glob("images/001_00"+str(i)+"*.png") # ←飛び番？
        self.face_path_list[1][7][0:0]=glob.glob("images/001_009.png") # ←飛び番？

        self.face_path_list.append([]) #002_000x～002_009x
        for i in range(0,6):
            self.face_path_list[2].append([])
        self.face_path_list[2][0][0:0]=glob.glob("images/002_000?.png")
        self.face_path_list[2][1][0:0]=glob.glob("images/002_001.png")
        self.face_path_list[2][2][0:0]=glob.glob("images/002_003.png") # ←飛び番？
        for i in range(7,9+1):
            self.face_path_list[2][i-4][0:0]=glob.glob("images/002_00"+str(i)+"*.png")
        
        self.face_path_list.append([]) #003_001x～003_009x ここで003_000xは無い
        for i in range(0,5):
            self.face_path_list[3].append([])
        self.face_path_list[3][0][0:0]=glob.glob("images/003_001*.png")
        for i in range(6,9+1):
            self.face_path_list[3][i-5][0:0]=glob.glob("images/003_00"+str(i)+"*.png")
        
        self.face_path_list.append([]) #004_001～004_002x
        for i in range(0,2):
            self.face_path_list[4].append([])
        for i in range(0,1+1):
            self.face_path_list[4][i][0:0]=glob.glob("images/004_00"+str(i)+"*.png")
        
        self.face_path_list.append([]) #005_000x～005_008x
        for i in range(0,4):
            self.face_path_list[5].append([])
        self.face_path_list[5][0][0:0]=glob.glob("images/005_000?.png")
        self.face_path_list[5][1][0:0]=glob.glob("images/005_004*.png") # ←飛び番？
        self.face_path_list[5][2][0:0]=glob.glob("images/005_007.png") # ←飛び番？
        self.face_path_list[5][3][0:0]=glob.glob("images/005_008*.png")

        self.face_path_list.append([]) #007_000x～007_008x
        for i in range(0,7):
            self.face_path_list[6].append([])
        self.face_path_list[6][0][0:0]=glob.glob("images/007_000?.png")
        self.face_path_list[6][1][0:0]=glob.glob("images/007_001*.png")
        for i in range(3,7+1):
            self.face_path_list[6][i-1][0:0]=glob.glob("images/007_00"+str(i)+"*.png")#

        self.face_path_list.append([]) #008_000x～008_008
        for i in range(0,6):
            self.face_path_list[7].append([])
        self.face_path_list[7][0][0:0]=glob.glob("images/008_000?.png")
        self.face_path_list[7][1][0:0]=glob.glob("images/008_003*.png")
        self.face_path_list[7][2][0:0]=glob.glob("images/008_004.png")
        for i in range(6,8+1):
            self.face_path_list[7][i-3][0:0]=glob.glob("images/008_00"+str(i)+"*.png")

        #print(self.face_path_list)

    # imageフォルダ内のlines.txtの中のセリフをリストにする。
    def linesList(self):
        path = "assets/lines.txt"
        with open(path,encoding='utf_8') as f: # UTF-8を指定しないと上手くいかない？
            self.lines_list = [s.rstrip() for s in f.readlines()]
        #print(self.lines_list)
        

    # 顔の差分画像を2秒ごとに切り替える
    def repeatChange(self):
        
        # 体を選択・表示（顔はデフォルト）
        body_total = len(self.body_path_list)
        rand_body = random.randint(0, body_total-1) # a <= n <= b のランダム整数
        self.dispImageBody(self.body_path_list[rand_body])
        if(rand_body!=3): # rand_body==3のときはoppaiガードの体勢
            self.dispOppaiHole(True)
            self.dispImageOppai(self.body_path_list[rand_body]) # Oppaiを表示 #######
        else:
            self.dispOppaiHole(False)
        self.dispImageFace("") # 顔はデフォルト

        # セリフを表示する
        lines_total = len(self.lines_list)
        rand_lines = random.randint(0, lines_total-1)
        rand_empty = random.randint(0, 20) # 数回に一回だけセリフが無くなる

        is_1030done = False # 時報フラグ（1度だけ時報を鳴らす）
        is_1230done = False
        is_1330done = False

        if datetime.now().hour == 10 and datetime.now().minute == 30: # 時報10:30
            self.dispImageBubble("assets/bubble_angular.png",
                                 datetime.now().strftime("午前の部の始まりですよー。\n%H:%M をお知らせします"))
            if not is_1030done :
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    time.sleep(0.1)
                is_1030done = True
        elif datetime.now().hour == 12 and datetime.now().minute == 30: # 時報12:30
            self.dispImageBubble("assets/bubble_angular.png",
                                 datetime.now().strftime("昼休みですよー。\n%H:%M をお知らせします"))
            if not is_1230done :
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    time.sleep(0.1)
                is_1230done = True
        elif datetime.now().hour == 13 and datetime.now().minute == 30: # 時報13:30
            self.dispImageBubble("assets/bubble_angular.png",
                                 datetime.now().strftime("午後の部の始まりですよー。\n%H:%M をお知らせします"))
            if not is_1330done :
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    time.sleep(0.1)
                is_1330done = True
        elif datetime.now().hour == 15 and datetime.now().minute == 20: # 時報15:20
            self.dispImageBubble("assets/bubble_angular.png",
                                 datetime.now().strftime("終了10分前ですよー。\n%H:%M をお知らせします"))      
        elif(datetime.now().minute==0): # 時報
            self.dispImageBubble("assets/bubble_angular.png",
                                 datetime.now().strftime("世界の針がひとつ刻みを進めた。\n%H:%M をお知らせします"))
        elif(rand_empty==0):
            self.dispImageBubble("","") # セリフ無し（吹き出しを消す）
        elif(rand_empty==1): # 吹き出しがギザギザになる。
            self.dispImageBubble("assets/bubble_jagged.png",self.lines_list[rand_lines])
        elif(rand_empty==2): # 天気予報を話す
            self.dispImageBubble("assets/bubble_angular.png",get_weather())
        else:
            self.dispImageBubble("assets/bubble.png",self.lines_list[rand_lines])
            #self.text_widget.insert(tk.END,"おはようございます")

        k=0
        for j in range(3): # 体はそのままで頭を3回変える
            # 頭を選択
            head_total = len(self.face_path_list[rand_body])
            rand_head = random.randint(0, head_total-1)
            # 顔(表情)を選択・表示
            face_total = len(self.face_path_list[rand_body][rand_head])
            for i in range(0,face_total):
                k+=1
                if i==0:
                    k+=4 # 頭が変わるタイミングで時間をおく
                self.root.after(500*k,self.dispImageFace,self.face_path_list[rand_body][rand_head][i])
                #print(rand_body,rand_head,i)

        self.root.after(500*(k+4), self.repeatChange) # ループ．関数を渡すために()は付けない．
        

    def __init__(self,root):

        self.root = root # よくわからんが

        self.origin = (0, 0)
        self.isMouseDown = False

        self.pngFileList()
        self.linesList()

        #self.root = tk.Tk()
        self.screenOppaiInit()
        self.screenInit()
        self.bubbleInit()
        self.popupMenu()
        self.repeatChange()
        #self.root.mainloop()

 

if __name__ == "__main__":
    root = tk.Tk()
    m = Mascot(root)
    l= Luncher(root)
    root.mainloop()
