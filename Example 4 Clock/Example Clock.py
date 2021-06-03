from PyQt5.QtCore import QTime, QTimer
from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])
ui = uic.loadUi("Example 4 Clock.ui")

def clock():
    currentTime = QTime.currentTime()           #ให้ตัวแปร currentTime รับค่าจากฟังก์ชัน QTime.currentTime()
    currentTimeText = currentTime.toString('hh:mm:ss')  #ให้ตัวแปร currentTimeText รับค่าเวลาปัจจุบัน
    ui.lcdClock.display(currentTimeText)        #แสดงค่าบนจอ LCD

timer = QTimer();               #สร้างคัวแปร timer สำหรับฟังก์ชัน QTimer()
timer.timeout.connect(clock)    #ให้ timer เรียกใช้ method clock
timer.start()                   #เริ่มต้นการทำงานแสดงเวลา

ui.show()   #แสดงผล UI
app.exec()  #รันแอป
