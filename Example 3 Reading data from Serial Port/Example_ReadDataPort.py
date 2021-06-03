#นำไลบรารี่ pyserial เข้ามาใช้งาน
#และไลบรารี่คำสั่งของ Qt Designer
import serial
import serial.tools.list_ports 
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QTime, QTimer

app = QtWidgets.QApplication([])            
ui = uic.loadUi("Example 3 Reading serialPort.ui") #ตั้งให้ตรงกับชื่อไฟล์ Qt Designer

Pyserial = serial.Serial()  #ประกาศตัวแปร Pyserial เพื่อรับค่าจากพอร์ตอนุกรม
ports = serial.tools.list_ports.comports()  #ประกาศตัวแปร ports สำหรับเก็บรายการคอมพอร์ต
portList = []   #ประกาศตัวแปร portList สำหรับเก็บค่าพอร์ตที่อ่านได้
for port in ports:              #for loop สำหรับวนรอบการค้นหาพอร์ต
    portList.append(port[0])    #นำตัวแปร port มาแสดงใน portList 

def openPort():         #ฟังก์ชันการปิดพอร์ต
    Pyserial.port = ui.cmb_port.currentText()   #ให้ตัวแปร Pyserial มีค่าเท่ากับค่าที่แสดงบน Combo Box
    Pyserial.baudrate = 9600    #เปิดพอร์ตสื่อสารที่อัตรา 9600
    Pyserial.open()             #เปิดพอร์ต
    ui.btn_connect.setEnabled(False)    #เมื่อมีการกดปุ่ม Connect ให้ปุ่ม Disable
    ui.btn_disconnect.setEnabled(True)  #เมื่อมีการกดปุ่ม Disconnect ให้ปุ่ม Disable
    if Pyserial.isOpen():
        print("Open port with : " + str(ui.cmb_port.currentText())) #แสดงข้อความผ่านดีบัค

def closePort():        #ฟังก์ชันการปิดพอร์ต
    Pyserial.close()
    ui.btn_connect.setEnabled(True)     #เมื่อมีการกดปุ่ม Disconnect ให้ปุ่ม Connect enable
    ui.btn_disconnect.setEnabled(False) #เมื่อมีการกดปุ่ม Disconnect ให้ปุ่ม Disconnect Disable
    print("Disconnect port with : " + str(ui.cmb_port.currentText())) #แสดงข้อความผ่านดีบัค

#Read data incomming form uart
def rxBuffer():
    if Pyserial.isOpen():
        global Data_buffer
        Data = Pyserial.readline().strip().decode('utf-8')  
        Data_buffer = Data.split(",")   #แบ่งข้อมูลด้วย comma
        print("Data incomming : " + str(Data_buffer))

readRx = QTimer()
readRx.timeout.connect(rxBuffer)
readRx.start(1)

ui.cmb_port.addItems(portList)  #นำค่า portList ทีไ่ด้ไปแสดงใน Combo Box
ui.btn_connect.clicked.connect(openPort)        #ปุ่มเปิดพอร์ต
ui.btn_disconnect.clicked.connect(closePort)    #ปุ่มปิดพอร์ต

ui.show()   #แสดง ui
app.exec()  #รันแอป
