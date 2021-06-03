from PyQt5 import QtWidgets, uic
import serial
import serial.tools.list_ports 
from PyQt5.QtCore import QTime, QTimer

app = QtWidgets.QApplication([])
ui = uic.loadUi("Example 5 ONOFF_Relay.ui")

Hon = []; Mon = []; Hoff = []; Moff = []    #ประกาศตัวแปรสำหรับจองค่าเวลา
Hon = [0 for i in range(20)]    #ให้ตัวแปร Hon มีค่าเริ่มต้นเป็น 0 ทั้งหมด
Mon = [0 for i in range(20)]    #ให้ตัวแปร Mon มีค่าเริ่มต้นเป็น 0 ทั้งหมด
Hoff = [0 for i in range(20)]   #ให้ตัวแปร Hoff มีค่าเริ่มต้นเป็น 0 ทั้งหมด
Moff = [0 for i in range(20)]   #ให้ตัวแปร Hoff มีค่าเริ่มต้นเป็น 0 ทั้งหมด

Pyserial = serial.Serial("COM5", 9600)  #เปิดพอร์ตการสื่อสารอนุกรม


#Method แสดงค่าเวลาปัจจุบัน
def clock():
    currentTime = QTime.currentTime()
    currentTimeText = currentTime.toString('hh:mm:ss')
    ui.lcdDatetime.display(currentTimeText)
    global Hours,Mins,Sec
    Hours = currentTime.hour()  #นำค่าเวลาที่เป็นชัวโมงเก็บไว้ในตัวแปร Hours
    Mins = currentTime.minute() #นำค่าเวลาที่เป็นนาทีไว้ในตัวแปร Mins
    Sec = currentTime.second()  #นำค่าเวลาที่เป็นวินาทีเก็บไว้ในตัวแปร Sec

def spnHon_click(value):
    Hon[0] = value
    print("Hour on set : " + str(Hon[0]))

def spnMon_click(value):
    Mon[0] = value
    print("Min on set : " + str(Mon[0]))

def spnHoff_click(value):
    Hoff[0] = value
    print("Hour off set : " + str(Hoff[0]))

def spnMoff_click(value):
    Moff[0] = value
    print("Min off set : " + str(Moff[0]))

def TimerProcess():         #Method การเช็คเวลา
    if Pyserial.isOpen():   #ตรวจสอบการเปิดพอร์ตอนุกรม
        if Hours == Hon[0] and Mins == Mon[0]:      RelayCH1ON()    #เงื่อนไขการสั่งเปิด
        elif Hours == Hoff[0] and Mins == Moff[0]:  RelayCH1OFF()   #เงื่อนไขการสั่งปิด

def RelayCH1ON():           #Medthod การเปิดการทำงานรีเลย์ช่องที่ 1
    Pyserial.write(b'A')    #หากมีการเรียกใช้งาน Method จะให้มีการส่ง 'A' ผ่านพอร์ตอนุกรม
    print("Relay 1 is on")

def RelayCH1OFF():          #Medthod การปิดการทำงานรีเลย์ช่องที่ 1
    Pyserial.write(b'a')    #หากมีการเรียกใช้งาน Method จะให้มีการส่ง 'a' ผ่านพอร์ตอนุกรม
    print("Relay 1 is off")

timer = QTimer();                       #ฟังก์ชันการทำงานของเวลา
timer.timeout.connect(clock)            #เรียกใช้งานฟังก์ชันเวลาโดยเรียกใข้งาน Method clcok
timer.timeout.connect(TimerProcess)     #เรียกใช้งานฟังก์ชันเวลาโดยเรียกใข้งาน Method TimerProcess
timer.start()                           #เริ่มการทำงาน timer

ui.spn_Hon.valueChanged.connect(spnHon_click)   #เช็คการเกิด Event บน QT Design โดยหากเกิด Event ให้เรียกใช้งาน spn_Hon Click
ui.spn_Mon.valueChanged.connect(spnMon_click)   #เช็คการเกิด Event บน QT Design โดยหากเกิด Event ให้เรียกใช้งาน spn_Mon Click
ui.spn_Hoff.valueChanged.connect(spnHoff_click) #เช็คการเกิด Event บน QT Design โดยหากเกิด Event ให้เรียกใช้งาน spn_Hoff Click
ui.spn_Moff.valueChanged.connect(spnMoff_click) #เช็คการเกิด Event บน QT Design โดยหากเกิด Event ให้เรียกใช้งาน spn_Moff Click

ui.show()
app.exec()
