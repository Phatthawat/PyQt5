import sys
import serial
import serial.tools.list_ports

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class SerialDlg(QDialog):
    def __init__(self,parent=None):
        super(SerialDlg,self).__init__(parent)
        SerialCOMLabel = QLabel(u'串口号')
        self.SerialCOMComboBox = QComboBox()
        self.SerialCOMComboBox.addItems(self.Port_List())


        SerialBaudRateLabel = QLabel(u'波特率')
        self.SerialBaudRateComboBox = QComboBox()
        self.SerialBaudRateComboBox.addItems(['100','300','600','1200','2400','4800','9600','14400','19200','38400','56000','57600','115200','128000','256000'])
        self.SerialBaudRateComboBox.setCurrentIndex(6)

        SerialDataLabel = QLabel(u'数据位')
        self.SerialDataComboBox = QComboBox()
        self.SerialDataComboBox.addItems(['5','6','7','8'])
        self.SerialDataComboBox.setCurrentIndex(3)

        SerialSTOPBitsLabel = QLabel(u'停止位')
        self.SerialStopBitsComboBox = QComboBox()
        self.SerialStopBitsComboBox.addItems(['1','1.5','2'])
        self.SerialStopBitsComboBox.setCurrentIndex(0)

        SerialParityLabel = QLabel(u'奇偶校验位')
        self.SerialParityComboBox = QComboBox()
        self.SerialParityComboBox.addItems(['NONE','EVEN','ODD','MARK','SPACE'])
        self.SerialParityComboBox.setCurrentIndex(0)

        self.OpenButton = QPushButton(u'打开串口')
        self.CloseButton = QPushButton(u'关闭串口')
        self.CloseButton.setDisabled(True)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.OpenButton)
        buttonLayout.addWidget(self.CloseButton)
        buttonLayout.addStretch()

        layout = QGridLayout()
        layout.addWidget(SerialCOMLabel,0,0)
        layout.addWidget(self.SerialCOMComboBox,0,1)
        layout.addWidget(SerialBaudRateLabel,1,0)
        layout.addWidget(self.SerialBaudRateComboBox,1,1)
        layout.addWidget(SerialDataLabel,2,0)
        layout.addWidget(self.SerialDataComboBox,2,1)
        layout.addWidget(SerialSTOPBitsLabel,3,0)
        layout.addWidget(self.SerialStopBitsComboBox,3,1)
        layout.addWidget(SerialParityLabel,4,0)
        layout.addWidget(self.SerialParityComboBox,4,1)

        mainlayout = QVBoxLayout()
        mainlayout.addLayout(layout)
        mainlayout.addLayout(buttonLayout)

        self.setLayout(mainlayout)
        self.setWindowTitle(u'串口调试工具')

        self.connect(self.OpenButton,SIGNAL("clicked()"),self.OpenSerial)
     #获取COM号列表  
    def Port_List(self):    
        Com_List=[]
        port_list = list(serial.tools.list_ports.comports())
        for port in port_list:
            Com_List.append(port[0])
        return Com_List
    #打开串口
    def OpenSerial(self):
        ser = serial.Serial()
        ser.port = self.SerialCOMComboBox.currentText()
        ser.baudrate = self.SerialBaudRateComboBox.currentText()
        ser.bytesize = int(self.SerialDataComboBox.currentText())

        ParityValue = self.SerialParityComboBox.currentText()
        ser.parity = ParityValue[0]
        ser.stopbits = int(self.SerialStopBitsComboBox.currentText())
        ser.open()
        print(ser.isOpen())
        ser.close()
        print(ser.isOpen())


app = QApplication(sys.argv)
SerialDialog = SerialDlg()
SerialDialog.show()
app.exec()
————————————————
版权声明：本文为CSDN博主「子瓜云鬼」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/u010307522/article/details/50043803