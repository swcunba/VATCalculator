from tkinter import *
import math
#창 생성: win = Tk(). 반드시 변수로 저장해 창 생성할 때마다 호출.
#창 실행: win.mainloop()
#창 크기: win.geometry("가로x세로") 픽셀단위.
#창 제목: win.title("창 제목")
#전체 폰트: win.option_add("*Font"."맑은고딕 25")

def calSumVAT():
    sum = float(ent.get()) #입력된 값 가져와서 저장.
    vos = sum // 1.1
    sumResLabel.configure(text = "부가세: " + str(int(sum-vos)) + "공급가액: " + str(int(vos)))

def entCalSumVAT(event):
    sum = float(ent.get()) #입력된 값 가져와서 저장.
    vos = sum // 1.1
    sumResLabel.configure(text = "부가세: " + str(int(sum-vos)) + "공급가액: " + str(int(vos)))

def calVosVAT():
    vos = float(vosEnt.get()) #입력된 값 가져와서 저장.
    sum = vos * 1.1
    vosResLabel.configure(text = "부가세: " + str(math.ceil(sum-vos)) + "합계금액: " + str(math.ceil(sum)))

def entCalVosVAT(event):
    vos = float(vosEnt.get()) #입력된 값 가져와서 저장.
    sum = vos * 1.1
    math.ceil(sum)
    vosResLabel.configure(text = "부가세: " + str(math.ceil(sum-vos)) + "합계금액: " + str(math.ceil(sum)))

win = Tk() #창 생성, 변수에 저장해서 mainloop으로 실행해줘야함.
win.geometry("500x500") #창 크기 설정.
win.title("부가세 계산기") #창 제목 설정.
win.option_add("*Font", "맑은고딕 25") #전체 폰트 설정.

sumLabel = Label(win) #sum 입력label.
sumLabel.configure(text = "합계 금액")
sumLabel.place(x=10, y=10)

ent = Entry(win) #입력창 생성.
ent.place(x=10, y=50) #입력창 배치. 위에서 아래로. grid나 place 통해 원하는 곳 배치 가능.

btn = Button(win, text = "계산하기") #버튼 생성.
btn.config(command = calSumVAT) #버튼 누르면 함수 실행.
btn.place(x=10, y=90)

ent.bind('<Return>', entCalSumVAT)
sumResLabel = Label(win)
sumResLabel.place(x=10, y=150)

vosLabel = Label(win) #vos 입력label.
vosLabel.configure(text = "공급가액")
vosLabel.place(x=10, y=230)

vosEnt = Entry(win) #입력창 생성.
vosEnt.place(x=10, y=270) #입력창 배치. 위에서 아래로. grid나 place 통해 원하는 곳 배치 가능.

btn2 = Button(win, text = "계산하기") #버튼 생성.
btn2.config(command = calVosVAT) #버튼 누르면 함수 실행.
btn2.place(x=10, y=310)

vosEnt.bind('<Return>', entCalVosVAT)
vosResLabel = Label(win)
vosResLabel.place(x=10, y=370)

win.mainloop() #창 실행.

#pyinstaller로 exe형태로 배포 가능.
#pyinstaller --onefile --noconsole 파일명.py