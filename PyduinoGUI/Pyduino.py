from ctypes.wintypes import BOOLEAN
from os import read
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5 import QtCore
#from PyQt5.uic.properties import QtGui
import serial
import serial.tools.list_ports 
import sys
from PyQt5.QtCore import QTime, QTimer


app = QtWidgets.QApplication([])

#add icons
icon = QtGui.QIcon()
icon.addFile('icon/leaf.png', QtCore.QSize(16,16))
ui = uic.loadUi("Pyduino.ui")
ui.setWindowTitle("Pyduino")
ui.setWindowIcon(QtGui.QIcon(icon))

Pyserial = serial.Serial()
ports = serial.tools.list_ports.comports()
portList = []
for port in ports:
    portList.append(port[0])

#initial value before use
Hon = []; Mon = []; Hoff = []; Moff = []
Hon = [0 for i in range(20)]
Mon = [0 for i in range(20)]
Hoff = [0 for i in range(20)]
Moff = [0 for i in range(20)]
Data_buffer = []
Data_buffer = [0 for i in range(5)]

def openPort():
    Pyserial.port = ui.cb_comport.currentText()
    Pyserial.baudrate = 115200
    Pyserial.open()
    ui.btn_Connect.setEnabled(False)
    ui.btn_Disconnect.setEnabled(True)
    Level.start(1000)
    if Pyserial.isOpen():
        print("Open port with : " + str(ui.cb_comport.currentText()))

def closePort():
    Pyserial.close()
    ui.btn_Connect.setEnabled(True)
    ui.btn_Disconnect.setEnabled(False)

#Read data incomming form uart
def rxBuffer():
    if Pyserial.isOpen():
        global Data_buffer
        Data = Pyserial.readline().strip().decode('utf-8')
        Data_buffer = Data.split(",")

#Update Bar
def updateBar():
    ui.Temp_1.setValue(int(Data_buffer[0]))
    ui.Temp_2.setValue(int(Data_buffer[1]))
    ui.SoilTemp1.setValue(int(Data_buffer[2]))
    ui.SoilTemp2.setValue(int(Data_buffer[3]))

#Show current time on lcd display
def clock():
    currentTime = QTime.currentTime()
    currentTimeText = currentTime.toString('hh:mm:ss')
    ui.lcdDatetime.display(currentTimeText)
    global Hours,Mins,Sec
    Hours = currentTime.hour()
    Mins = currentTime.minute()
    Sec = currentTime.second()

#################    Start : Hour time on the value from spinBox     #################
def spinHon_t1(value):  Hon[0] = value  #you can use Hon[0] = ui.spnHon_t1.value()
def spinHon_t2(value):  Hon[1] = value
def spinHon_t3(value):  Hon[2] = value
def spinHon_t4(value):  Hon[3] = value
def spinHon_t5(value):  Hon[4] = value
def spinHon_t6(value):  Hon[5] = value
def spinHon_t7(value):  Hon[6] = value
def spinHon_t8(value):  Hon[7] = value
def spinHon_t9(value):  Hon[8] = value
def spinHon_t10(value): Hon[9] = value
def spinHon_t11(value): Hon[10] = value
def spinHon_t12(value): Hon[11] = value
def spinHon_t13(value): Hon[12] = value
def spinHon_t14(value): Hon[13] = value
def spinHon_t15(value): Hon[14] = value
def spinHon_t16(value): Hon[15] = value
def spinHon_t17(value): Hon[16] = value
def spinHon_t18(value): Hon[17] = value
def spinHon_t19(value): Hon[18] = value
def spinHon_t20(value): Hon[19] = value

#################     Start : Min time on the value from spinBox    #################
def spinMon_t1(value):  Mon[0] = value
def spinMon_t2(value):  Mon[1] = value
def spinMon_t3(value):  Mon[2] = value
def spinMon_t4(value):  Mon[3] = value
def spinMon_t5(value):  Mon[4] = value
def spinMon_t6(value):  Mon[5] = value
def spinMon_t7(value):  Mon[6] = value
def spinMon_t8(value):  Mon[7] = value
def spinMon_t9(value):  Mon[8] = value
def spinMon_t10(value): Mon[9] = value
def spinMon_t11(value): Mon[10] = value
def spinMon_t12(value): Mon[11] = value
def spinMon_t13(value): Mon[12] = value
def spinMon_t14(value): Mon[13] = value
def spinMon_t15(value): Mon[14] = value
def spinMon_t16(value): Mon[15] = value
def spinMon_t17(value): Mon[16] = value
def spinMon_t18(value): Mon[17] = value
def spinMon_t19(value): Mon[18] = value
def spinMon_t20(value): Mon[19] = value

#################    Start : Hour time off the value from spinBox     #################
def spinHoff_t1(value):     Hoff[0] = value  #you can use Hon[0] = ui.spnHon_t1.value()
def spinHoff_t2(value):     Hoff[1] = value
def spinHoff_t3(value):     Hoff[2] = value
def spinHoff_t4(value):     Hoff[3] = value
def spinHoff_t5(value):     Hoff[4] = value
def spinHoff_t6(value):     Hoff[5] = value
def spinHoff_t7(value):     Hoff[6] = value
def spinHoff_t8(value):     Hoff[7] = value
def spinHoff_t9(value):     Hoff[8] = value
def spinHoff_t10(value):    Hoff[9] = value
def spinHoff_t11(value):    Hoff[10] = value 
def spinHoff_t12(value):    Hoff[11] = value
def spinHoff_t13(value):    Hoff[12] = value
def spinHoff_t14(value):    Hoff[13] = value
def spinHoff_t15(value):    Hoff[14] = value
def spinHoff_t16(value):    Hoff[15] = value
def spinHoff_t17(value):    Hoff[16] = value
def spinHoff_t18(value):    Hoff[17] = value
def spinHoff_t19(value):    Hoff[18] = value
def spinHoff_t20(value):    Hoff[19] = value


#################     Start : Min time off the value from spinBox    #################
def spinMoff_t1(value):     Moff[0] = value
def spinMoff_t2(value):     Moff[1] = value
def spinMoff_t3(value):     Moff[2] = value
def spinMoff_t4(value):     Moff[3] = value
def spinMoff_t5(value):     Moff[4] = value
def spinMoff_t6(value):     Moff[5] = value
def spinMoff_t7(value):     Moff[6] = value
def spinMoff_t8(value):     Moff[7] = value
def spinMoff_t9(value):     Moff[8] = value
def spinMoff_t10(value):    Moff[9] = value
def spinMoff_t11(value):    Moff[10] = value
def spinMoff_t12(value):    Moff[11] = value
def spinMoff_t13(value):    Moff[12] = value
def spinMoff_t14(value):    Moff[13] = value
def spinMoff_t15(value):    Moff[14] = value
def spinMoff_t16(value):    Moff[15] = value
def spinMoff_t17(value):    Moff[16] = value
def spinMoff_t18(value):    Moff[17] = value
def spinMoff_t19(value):    Moff[18] = value
def spinMoff_t20(value):    Moff[19] = value

def RelayCH1ON():
    Pyserial.write(b'A')

def RelayCH1OFF():
    Pyserial.write(b'a')

def RelayCH2ON():
    Pyserial.write(b'B')

def RelayCH2OFF():
    Pyserial.write(b'b')

def TimerProcess():
    if Pyserial.isOpen():
        if ui.ckb_t1.isChecked():       #Timer1 CH1
            if Hours == Hon[0] and Mins == Mon[0]:      RelayCH1ON()
            elif Hours == Hoff[0] and Mins == Moff[0]:  RelayCH1OFF()
        if ui.ckb_t2.isChecked():       #Timer2 CH1
            if Hours == Hon[1] and Mins == Mon[1]:      RelayCH1ON()
            elif Hours == Hoff[1] and Mins == Moff[1]:  RelayCH1OFF()
        if ui.ckb_t3.isChecked():       #Timer3 CH1
            if Hours == Hon[2] and Mins == Mon[2]:      RelayCH1ON()
            elif Hours == Hoff[2] and Mins == Moff[2]:  RelayCH1OFF()
        if ui.ckb_t4.isChecked():       #Timer4 CH1
            if Hours == Hon[3] and Mins == Mon[3]:      RelayCH1ON()
            elif Hours == Hoff[3] and Mins == Moff[3]:  RelayCH1OFF()
        if ui.ckb_t5.isChecked():       #Timer5 CH1
            if Hours == Hon[4] and Mins == Mon[4]:      RelayCH1ON()
            elif Hours == Hoff[4] and Mins == Moff[4]:  RelayCH1OFF()
        if ui.ckb_t6.isChecked():       #Timer6 CH1
            if Hours == Hon[5] and Mins == Mon[5]:      RelayCH1ON()
            elif Hours == Hoff[5] and Mins == Moff[5]:  RelayCH1OFF()
        if ui.ckb_t7.isChecked():       #Timer7 CH1
            if Hours == Hon[6] and Mins == Mon[6]:      RelayCH1ON()
            elif Hours == Hoff[6] and Mins == Moff[6]:  RelayCH1OFF()
        if ui.ckb_t8.isChecked():       #Timer8 CH1
            if Hours == Hon[7] and Mins == Mon[7]:      RelayCH1ON()
            elif Hours == Hoff[7] and Mins == Moff[7]:  RelayCH1OFF()
        if ui.ckb_t9.isChecked():       #Time9 CH1
            if Hours == Hon[8] and Mins == Mon[8]:      RelayCH1ON()
            elif Hours == Hoff[8] and Mins == Moff[8]:  RelayCH1OFF()
        if ui.ckb_t10.isChecked():      #Timer10 CH1
            if Hours == Hon[9] and Mins == Mon[9]:      RelayCH1ON()
            elif Hours == Hoff[9] and Mins == Moff[9]:  RelayCH1OFF()
        
        if ui.ckb_t11.isChecked():      #Timer1 CH2
            if Hours == Hon[10] and Mins == Mon[10]:      RelayCH2ON()
            elif Hours == Hoff[10] and Mins == Moff[10]:  RelayCH2OFF()
        if ui.ckb_t12.isChecked():      #Timer2 CH2
            if Hours == Hon[11] and Mins == Mon[11]:      RelayCH2ON()
            elif Hours == Hoff[11] and Mins == Moff[11]:  RelayCH2OFF()
        if ui.ckb_t13.isChecked():      #Timer3 CH2
            if Hours == Hon[12] and Mins == Mon[12]:      RelayCH2ON()
            elif Hours == Hoff[12] and Mins == Moff[12]:  RelayCH2OFF()
        if ui.ckb_t14.isChecked():      #Timer4 CH2
            if Hours == Hon[13] and Mins == Mon[13]:      RelayCH2ON()
            elif Hours == Hoff[13] and Mins == Moff[13]:  RelayCH2OFF()
        if ui.ckb_t15.isChecked():      #Timer5 CH2
            if Hours == Hon[14] and Mins == Mon[14]:      RelayCH2ON()
            elif Hours == Hoff[14] and Mins == Moff[14]:  RelayCH2OFF()
        if ui.ckb_t16.isChecked():      #Timer6 CH1
            if Hours == Hon[15] and Mins == Mon[15]:      RelayCH2ON()
            elif Hours == Hoff[15] and Mins == Moff[15]:  RelayCH2OFF()
        if ui.ckb_t17.isChecked():      #Timer7 CH2
            if Hours == Hon[16] and Mins == Mon[16]:      RelayCH2ON()
            elif Hours == Hoff[16] and Mins == Moff[16]:  RelayCH2OFF()
        if ui.ckb_t18.isChecked():      #Timer8 CH2
            if Hours == Hon[17] and Mins == Mon[17]:      RelayCH2ON()
            elif Hours == Hoff[17] and Mins == Moff[17]:  RelayCH2OFF()
        if ui.ckb_t19.isChecked():      #Timer9 CH2
            if Hours == Hon[18] and Mins == Mon[18]:      RelayCH2ON()
            elif Hours == Hoff[18] and Mins == Moff[18]:  RelayCH2OFF()
        if ui.ckb_t20.isChecked():      #Timer10 CH2
            if Hours == Hon[19] and Mins == Mon[19]:      RelayCH2ON()
            elif Hours == Hoff[19] and Mins == Moff[19]:  RelayCH2OFF()


def CH01ON():
    Pyserial.write(b'A')
    print("RY01 is ON")
def CH01OFF():
    Pyserial.write(b'a')
    print("RY01 is OFF")
def CH02ON():
    Pyserial.write(b'B')
    print("RY02 is ON")
def CH02OFF():
    Pyserial.write(b'b')
    print("RY02 is OFF")

timer = QTimer();   
timer.timeout.connect(clock)
timer.timeout.connect(TimerProcess)
timer.start()

#   update current data from uart to progress bar
Level = QTimer()
Level.timeout.connect(updateBar)

readRx = QTimer()
readRx.timeout.connect(rxBuffer)
readRx.start(1)



def closeApp():
    sys.exit()
#################################### spinBox Hours on ####################################
ui.spnHon_t1.valueChanged.connect(spinHon_t1)
ui.spnHon_t2.valueChanged.connect(spinHon_t2)
ui.spnHon_t3.valueChanged.connect(spinHon_t3)
ui.spnHon_t4.valueChanged.connect(spinHon_t4)
ui.spnHon_t5.valueChanged.connect(spinHon_t5)
ui.spnHon_t6.valueChanged.connect(spinHon_t6)
ui.spnHon_t7.valueChanged.connect(spinHon_t7)
ui.spnHon_t8.valueChanged.connect(spinHon_t8)
ui.spnHon_t9.valueChanged.connect(spinHon_t9)
ui.spnHon_t10.valueChanged.connect(spinHon_t10)
ui.spnHon_t11.valueChanged.connect(spinHon_t11)
ui.spnHon_t12.valueChanged.connect(spinHon_t12)
ui.spnHon_t13.valueChanged.connect(spinHon_t13)
ui.spnHon_t14.valueChanged.connect(spinHon_t14)
ui.spnHon_t15.valueChanged.connect(spinHon_t15)
ui.spnHon_t16.valueChanged.connect(spinHon_t16)
ui.spnHon_t17.valueChanged.connect(spinHon_t17)
ui.spnHon_t18.valueChanged.connect(spinHon_t18)
ui.spnHon_t19.valueChanged.connect(spinHon_t19)
ui.spnHon_t20.valueChanged.connect(spinHon_t20)
#################################### spinBox Min on ####################################
ui.spnMon_t1.valueChanged.connect(spinMon_t1)
ui.spnMon_t2.valueChanged.connect(spinMon_t2)
ui.spnMon_t3.valueChanged.connect(spinMon_t3)
ui.spnMon_t4.valueChanged.connect(spinMon_t4)
ui.spnMon_t5.valueChanged.connect(spinMon_t5)
ui.spnMon_t6.valueChanged.connect(spinMon_t6)
ui.spnMon_t7.valueChanged.connect(spinMon_t7)
ui.spnMon_t8.valueChanged.connect(spinMon_t8)
ui.spnMon_t9.valueChanged.connect(spinMon_t9)
ui.spnMon_t10.valueChanged.connect(spinMon_t10)
ui.spnMon_t11.valueChanged.connect(spinMon_t11)
ui.spnMon_t12.valueChanged.connect(spinMon_t12)
ui.spnMon_t13.valueChanged.connect(spinMon_t13)
ui.spnMon_t14.valueChanged.connect(spinMon_t14)
ui.spnMon_t15.valueChanged.connect(spinMon_t15)
ui.spnMon_t16.valueChanged.connect(spinMon_t16)
ui.spnMon_t17.valueChanged.connect(spinMon_t17)
ui.spnMon_t18.valueChanged.connect(spinMon_t18)
ui.spnMon_t19.valueChanged.connect(spinMon_t19)
ui.spnMon_t20.valueChanged.connect(spinMon_t20)

#################################### spinBox Hours off ####################################
ui.spnHoff_t1.valueChanged.connect(spinHoff_t1)
ui.spnHoff_t5.valueChanged.connect(spinHoff_t5)
ui.spnHoff_t4.valueChanged.connect(spinHoff_t4)
ui.spnHoff_t2.valueChanged.connect(spinHoff_t2)
ui.spnHoff_t6.valueChanged.connect(spinHoff_t6)
ui.spnHoff_t3.valueChanged.connect(spinHoff_t3)
ui.spnHoff_t7.valueChanged.connect(spinHoff_t7)
ui.spnHoff_t8.valueChanged.connect(spinHoff_t8)
ui.spnHoff_t9.valueChanged.connect(spinHoff_t9)
ui.spnHoff_t11.valueChanged.connect(spinHoff_t11)
ui.spnHoff_t10.valueChanged.connect(spinHoff_t10)
ui.spnHoff_t12.valueChanged.connect(spinHoff_t12)
ui.spnHoff_t13.valueChanged.connect(spinHoff_t13)
ui.spnHoff_t14.valueChanged.connect(spinHoff_t14)
ui.spnHoff_t15.valueChanged.connect(spinHoff_t15)
ui.spnHoff_t16.valueChanged.connect(spinHoff_t16)
ui.spnHoff_t17.valueChanged.connect(spinHoff_t17)
ui.spnHoff_t18.valueChanged.connect(spinHoff_t18)
ui.spnHoff_t19.valueChanged.connect(spinHoff_t19)
ui.spnHoff_t20.valueChanged.connect(spinHoff_t20)
#################################### spinBox Min off ####################################
ui.spnMoff_t1.valueChanged.connect(spinMoff_t1)
ui.spnMoff_t2.valueChanged.connect(spinMoff_t2)
ui.spnMoff_t3.valueChanged.connect(spinMoff_t3)
ui.spnMoff_t4.valueChanged.connect(spinMoff_t4)
ui.spnMoff_t5.valueChanged.connect(spinMoff_t5)
ui.spnMoff_t6.valueChanged.connect(spinMoff_t6)
ui.spnMoff_t7.valueChanged.connect(spinMoff_t7)
ui.spnMoff_t8.valueChanged.connect(spinMoff_t8)
ui.spnMoff_t9.valueChanged.connect(spinMoff_t9)
ui.spnMoff_t10.valueChanged.connect(spinMoff_t10)
ui.spnMoff_t11.valueChanged.connect(spinMoff_t11)
ui.spnMoff_t12.valueChanged.connect(spinMoff_t12)
ui.spnMoff_t13.valueChanged.connect(spinMoff_t13)
ui.spnMoff_t14.valueChanged.connect(spinMoff_t14)
ui.spnMoff_t15.valueChanged.connect(spinMoff_t15)
ui.spnMoff_t16.valueChanged.connect(spinMoff_t16)
ui.spnMoff_t17.valueChanged.connect(spinMoff_t17)
ui.spnMoff_t18.valueChanged.connect(spinMoff_t18)
ui.spnMoff_t19.valueChanged.connect(spinMoff_t19)
ui.spnMoff_t20.valueChanged.connect(spinMoff_t20)


ui.RY01ON.clicked.connect(CH01ON)
ui.RY01OFF.clicked.connect(CH01OFF)
ui.RY02ON.clicked.connect(CH02ON)
ui.RY02OFF.clicked.connect(CH02OFF)

ui.cb_comport.addItems(portList)
ui.btn_close.clicked.connect(closeApp)
ui.btn_Connect.clicked.connect(openPort)
ui.btn_Disconnect.clicked.connect(closePort)

ui.show()
app.exec()


