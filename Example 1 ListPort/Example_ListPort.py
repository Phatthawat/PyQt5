#นำไลบรารี่ pyserial เข้ามาใช้งาน
#และไลบรารี่คำสั่งของ Qt Designer
import serial
import serial.tools.list_ports 
from PyQt5 import QtWidgets, uic


app = QtWidgets.QApplication([])            
ui = uic.loadUi("Example 1 List serialPort.ui") #ตั้งให้ตรงกับชื่อไฟล์ Qt Designer

Pyserial = serial.Serial()  #ประกาศตัวแปร Pyserial เพื่อรับค่าจากพอร์ตอนุกรม
ports = serial.tools.list_ports.comports()  #ประกาศตัวแปร ports สำหรับเก็บรายการคอมพอร์ต
portList = []   #ประกาศตัวแปร portList สำหรับเก็บค่าพอร์ตที่อ่านได้
for port in ports:              #for loop สำหรับวนรอบการค้นหาพอร์ต
    portList.append(port[0])    #นำตัวแปร port มาแสดงใน portList 

ui.cmb_port.addItems(portList)  #นำค่า portList ทีไ่ด้ไปแสดงใน Combo Box

ui.show()   #แสดง ui
app.exec()  #รันแอป
