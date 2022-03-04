import sys
import math

import pyqtgraph
from PySide6.QtWidgets import *
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from Car_Motor4 import Ui_MainWindow
from qt_material import apply_stylesheet


class CarWindow(QMainWindow, Ui_MainWindow):
    Addr_Offset = int(128)

    Theta_Addr        = [Addr_Offset * 0 + 0,  Addr_Offset * 1 + 0,  Addr_Offset * 2 + 0,  Addr_Offset * 3 + 0]
    ThetaE_Addr       = [Addr_Offset * 0 + 1,  Addr_Offset * 1 + 1,  Addr_Offset * 2 + 1,  Addr_Offset * 3 + 1]
    SinTheta_Addr     = [Addr_Offset * 0 + 2,  Addr_Offset * 1 + 2,  Addr_Offset * 2 + 2,  Addr_Offset * 3 + 2]
    CosTheta_Addr     = [Addr_Offset * 0 + 3,  Addr_Offset * 1 + 3,  Addr_Offset * 2 + 3,  Addr_Offset * 3 + 3]
    Ia_Addr           = [Addr_Offset * 0 + 4,  Addr_Offset * 1 + 4,  Addr_Offset * 2 + 4,  Addr_Offset * 3 + 4]
    Ic_Addr           = [Addr_Offset * 0 + 5,  Addr_Offset * 1 + 5,  Addr_Offset * 2 + 5,  Addr_Offset * 3 + 5]
    Ix_Addr           = [Addr_Offset * 0 + 6,  Addr_Offset * 1 + 6,  Addr_Offset * 2 + 6,  Addr_Offset * 3 + 6]
    Iy_Addr           = [Addr_Offset * 0 + 7,  Addr_Offset * 1 + 7,  Addr_Offset * 2 + 7,  Addr_Offset * 3 + 7]
    Ux_Addr           = [Addr_Offset * 0 + 8,  Addr_Offset * 1 + 8,  Addr_Offset * 2 + 8,  Addr_Offset * 3 + 8]
    Uy_Addr           = [Addr_Offset * 0 + 9,  Addr_Offset * 1 + 9,  Addr_Offset * 2 + 9,  Addr_Offset * 3 + 9]
    U1_Addr           = [Addr_Offset * 0 + 10, Addr_Offset * 1 + 10, Addr_Offset * 2 + 10, Addr_Offset * 3 + 10]
    U2_Addr           = [Addr_Offset * 0 + 11, Addr_Offset * 1 + 11, Addr_Offset * 2 + 11, Addr_Offset * 3 + 11]
    U3_Addr           = [Addr_Offset * 0 + 12, Addr_Offset * 1 + 12, Addr_Offset * 2 + 12, Addr_Offset * 3 + 12]
    Ua_Addr           = [Addr_Offset * 0 + 13, Addr_Offset * 1 + 13, Addr_Offset * 2 + 13, Addr_Offset * 3 + 13]
    Ub_Addr           = [Addr_Offset * 0 + 14, Addr_Offset * 1 + 14, Addr_Offset * 2 + 14, Addr_Offset * 3 + 14]
    Uc_Addr           = [Addr_Offset * 0 + 15, Addr_Offset * 1 + 15, Addr_Offset * 2 + 15, Addr_Offset * 3 + 15]
    Mode_Addr         = [Addr_Offset * 0 + 16, Addr_Offset * 1 + 16, Addr_Offset * 2 + 16, Addr_Offset * 3 + 16]
    Np_Addr           = [Addr_Offset * 0 + 17, Addr_Offset * 1 + 17, Addr_Offset * 2 + 17, Addr_Offset * 3 + 17]
    TargetUd_Addr     = [Addr_Offset * 0 + 18, Addr_Offset * 1 + 18, Addr_Offset * 2 + 18, Addr_Offset * 3 + 18]
    TargetUdExt_Addr  = [Addr_Offset * 0 + 19, Addr_Offset * 1 + 19, Addr_Offset * 2 + 19, Addr_Offset * 3 + 19]
    TargetUq_Addr     = [Addr_Offset * 0 + 20, Addr_Offset * 1 + 20, Addr_Offset * 2 + 20, Addr_Offset * 3 + 20]
    TargetUqExt_Addr  = [Addr_Offset * 0 + 21, Addr_Offset * 1 + 21, Addr_Offset * 2 + 21, Addr_Offset * 3 + 21]
    PresentId_Addr    = [Addr_Offset * 0 + 22, Addr_Offset * 1 + 22, Addr_Offset * 2 + 22, Addr_Offset * 3 + 22]
    TargetId_Addr     = [Addr_Offset * 0 + 23, Addr_Offset * 1 + 23, Addr_Offset * 2 + 23, Addr_Offset * 3 + 23]
    TargetIdExt_Addr  = [Addr_Offset * 0 + 24, Addr_Offset * 1 + 24, Addr_Offset * 2 + 24, Addr_Offset * 3 + 24]
    Id_Kp_Addr        = [Addr_Offset * 0 + 25, Addr_Offset * 1 + 25, Addr_Offset * 2 + 25, Addr_Offset * 3 + 25]
    Id_Ki_Addr        = [Addr_Offset * 0 + 26, Addr_Offset * 1 + 26, Addr_Offset * 2 + 26, Addr_Offset * 3 + 26]
    Ud_Max_Addr       = [Addr_Offset * 0 + 27, Addr_Offset * 1 + 27, Addr_Offset * 2 + 27, Addr_Offset * 3 + 27]
    PresentIq_Addr    = [Addr_Offset * 0 + 28, Addr_Offset * 1 + 28, Addr_Offset * 2 + 28, Addr_Offset * 3 + 28]
    TargetIq_Addr     = [Addr_Offset * 0 + 29, Addr_Offset * 1 + 29, Addr_Offset * 2 + 29, Addr_Offset * 3 + 29]
    TargetIqExt_Addr  = [Addr_Offset * 0 + 30, Addr_Offset * 1 + 30, Addr_Offset * 2 + 30, Addr_Offset * 3 + 30]
    Iq_Kp_Addr        = [Addr_Offset * 0 + 31, Addr_Offset * 1 + 31, Addr_Offset * 2 + 31, Addr_Offset * 3 + 31]
    Iq_Ki_Addr        = [Addr_Offset * 0 + 32, Addr_Offset * 1 + 32, Addr_Offset * 2 + 32, Addr_Offset * 3 + 32]
    Uq_Max_Addr       = [Addr_Offset * 0 + 33, Addr_Offset * 1 + 33, Addr_Offset * 2 + 33, Addr_Offset * 3 + 33]
    PresentSpd_Addr   = [Addr_Offset * 0 + 34, Addr_Offset * 1 + 34, Addr_Offset * 2 + 34, Addr_Offset * 3 + 34]
    TargetSpd_Addr    = [Addr_Offset * 0 + 35, Addr_Offset * 1 + 35, Addr_Offset * 2 + 35, Addr_Offset * 3 + 35]
    TargetSpdExt_Addr = [Addr_Offset * 0 + 36, Addr_Offset * 1 + 36, Addr_Offset * 2 + 36, Addr_Offset * 3 + 36]
    Spd_Kp_Addr       = [Addr_Offset * 0 + 37, Addr_Offset * 1 + 37, Addr_Offset * 2 + 37, Addr_Offset * 3 + 37]
    Spd_Ki_Addr       = [Addr_Offset * 0 + 38, Addr_Offset * 1 + 38, Addr_Offset * 2 + 38, Addr_Offset * 3 + 38]
    Iq_Max_Addr       = [Addr_Offset * 0 + 39, Addr_Offset * 1 + 39, Addr_Offset * 2 + 39, Addr_Offset * 3 + 39]
    PresentPos_Addr_H = [Addr_Offset * 0 + 40, Addr_Offset * 1 + 40, Addr_Offset * 2 + 40, Addr_Offset * 3 + 40]
    PresentPos_Addr_L = [Addr_Offset * 0 + 41, Addr_Offset * 1 + 41, Addr_Offset * 2 + 41, Addr_Offset * 3 + 41]
    TargetPos_Addr_H  = [Addr_Offset * 0 + 42, Addr_Offset * 1 + 42, Addr_Offset * 2 + 42, Addr_Offset * 3 + 42]
    TargetPos_Addr_L  = [Addr_Offset * 0 + 43, Addr_Offset * 1 + 43, Addr_Offset * 2 + 43, Addr_Offset * 3 + 43]
    Pos_Kp_Addr       = [Addr_Offset * 0 + 44, Addr_Offset * 1 + 44, Addr_Offset * 2 + 44, Addr_Offset * 3 + 44]
    Pos_Ki_Addr       = [Addr_Offset * 0 + 45, Addr_Offset * 1 + 45, Addr_Offset * 2 + 45, Addr_Offset * 3 + 45]
    Spd_Max_Addr      = [Addr_Offset * 0 + 46, Addr_Offset * 1 + 46, Addr_Offset * 2 + 46, Addr_Offset * 3 + 46]
    Error_Addr        = [Addr_Offset * 0 + 47, Addr_Offset * 1 + 47, Addr_Offset * 2 + 47, Addr_Offset * 3 + 47]
    Enable_Addr       = [Addr_Offset * 0 + 48, Addr_Offset * 1 + 48, Addr_Offset * 2 + 48, Addr_Offset * 3 + 48]

    None_Control_Mode = 0
    Voltage_Control_Mode = 1
    Current_Control_Mode = 2
    Speed_Control_Mode = 3
    Position_Control_Mode = 4
    Enable = 1
    Disable = 0

    def __init__(self):
        super(CarWindow, self).__init__()
        self.Uart = None
        self.setupUi(self)
        self.addItems()
        self.addSlot()

    def addItems(self):
        # Qt 串口类
        self.Uart = QSerialPort()

    def addSlot(self):
        # 通信页面

        # Uart通信方式选择按钮
        self.UartConnect_pushButton.clicked.connect(self.UartConnectSelect)
        # Uart端口查找按钮
        self.UartCheck_pushButton.clicked.connect(self.UartCheck)
        # Uart端口开关按钮
        self.UartEnable_pushButton.clicked.connect(self.UartEnable)

        # 电机使能选择

        # 电机1使能
        self.MotorEnable_pushButton_1.clicked.connect(self.MotorEnable1)
        # 电机2使能
        self.MotorEnable_pushButton_2.clicked.connect(self.MotorEnable2)
        # 电机3使能
        self.MotorEnable_pushButton_3.clicked.connect(self.MotorEnable3)
        # 电机4使能
        self.MotorEnable_pushButton_4.clicked.connect(self.MotorEnable4)

        # 电机1页面

        # 电机1参数读取
        self.ParametersRead_pushButton_1.clicked.connect(self.ParametersRead)
        # 电机1参数写入
        self.ParametersWrite_pushButton_1.clicked.connect(self.ParametersWrite)
        # 实际极对数参数显示
        self.Poles_spinBox_1.editingFinished.connect(self.Poles_Update)
        # 实际IdKp参数显示
        self.IdKp_lineEdit_1.editingFinished.connect(self.IdKp_Update)
        # 实际IdKi参数显示
        self.IdKi_lineEdit_1.editingFinished.connect(self.IdKi_Update)
        # 实际IqKp参数显示
        self.IqKp_lineEdit_1.editingFinished.connect(self.IqKp_Update)
        # 实际IqKi参数显示
        self.IqKi_lineEdit_1.editingFinished.connect(self.IqKi_Update)
        # 实际UdMax参数显示
        self.UdMax_lineEdit_1.editingFinished.connect(self.UdMax_Update)
        # 实际UqMax参数显示
        self.UqMax_lineEdit_1.editingFinished.connect(self.UqMax_Update)
        # 实际SpdKp参数显示
        self.SpdKp_lineEdit_1.editingFinished.connect(self.SpdKp_Update)
        # 实际SpdKi参数显示
        self.SpdKi_lineEdit_1.editingFinished.connect(self.SpdKi_Update)
        # 实际IqMax参数显示
        self.IqMax_lineEdit_1.editingFinished.connect(self.IqMax_Update)
        # 实际PosKp参数显示
        self.PosKp_lineEdit_1.editingFinished.connect(self.PosKp_Update)
        # 实际PosKi参数显示
        self.PosKi_lineEdit_1.editingFinished.connect(self.PosKi_Update)
        # 实际SpdMax参数显示
        self.SpdMax_lineEdit_1.editingFinished.connect(self.SpdMax_Update)
        # 实际Ud参数显示
        self.UdExt_lineEdit_1.editingFinished.connect(self.UdExt_Update)
        # 实际Uq参数显示
        self.UqExt_lineEdit_1.editingFinished.connect(self.UqExt_Update)
        # 实际Id参数显示
        self.IdExt_lineEdit_1.editingFinished.connect(self.IdExt_Update)
        # 实际Iq参数显示
        self.IqExt_lineEdit_1.editingFinished.connect(self.IqExt_Update)
        # 实际Spd参数显示
        self.SpdExt_lineEdit_1.editingFinished.connect(self.SpdExt_Update)
        # 实际Pos参数显示
        self.Pos_lineEdit_1.editingFinished.connect(self.Pos_Update)
        # 参数计算按钮
        self.Calculate_pushButton_1.clicked.connect(self.Calculate)
        # 电压控制模式按钮
        self.VolCtrlMode_pushButton_1.clicked.connect(self.VolCtrlMode)
        # 电流控制模式按钮
        self.CurCtrlMode_pushButton_1.clicked.connect(self.CurCtrlMode)
        # 速度控制模式按钮
        self.SpdCtrlMode_pushButton_1.clicked.connect(self.SpdCtrlMode)
        # 位置控制模式按钮
        self.PosCtrlMode_pushButton_1.clicked.connect(self.PosCtrlMode)

    # 选择使用Uart通信
    def UartConnectSelect(self):
        if self.UartConnect_pushButton.isChecked():
            self.Uart_widget.setEnabled(True)
            self.UartCheck_pushButton.setEnabled(True)
            self.UartEnable_pushButton.setEnabled(True)
        else:
            self.Uart_widget.setEnabled(False)
            self.UartCheck_pushButton.setEnabled(False)
            self.UartEnable_pushButton.setEnabled(False)

    def UartCheck(self):
        self.UartSelect_comboBox.clear()
        Uart = QSerialPort()
        UartList = QSerialPortInfo.availablePorts()
        for UartInfo in UartList:
            Uart.setPort(UartInfo)
            if Uart.open(QSerialPort.ReadWrite):
                self.UartSelect_comboBox.addItem(Uart.portName())
                Uart.close()

    def UartEnable(self):
        if self.UartEnable_pushButton.isChecked():
            UartName = self.UartSelect_comboBox.currentText()
            UartBaud = int(self.UartBaudSelect_comboBox.currentText())
            self.Uart.setPortName(UartName)
            try:
                if not self.Uart.open(QSerialPort.ReadWrite):
                    QMessageBox.critical(self, '严重错误', '串口打开失败')
                    self.UartEnable_pushButton.setChecked(False)
                    return
            except:
                QMessageBox.critical(self, '严重错误', '串口打开失败')
                self.UartEnable_pushButton.setChecked(False)
                return

            self.Uart.setBaudRate(UartBaud)
            self.Uart_widget.setEnabled(False)
            self.UartCheck_pushButton.setEnabled(False)
            self.UartConnect_pushButton.setEnabled(False)

            self.ParametersRead_pushButton_1.setEnabled(True)
            self.ParametersWrite_pushButton_1.setEnabled(True)

            self.VolCtrlMode_pushButton_1.setEnabled(True)
            self.CurCtrlMode_pushButton_1.setEnabled(True)
            self.SpdCtrlMode_pushButton_1.setEnabled(True)
            self.PosCtrlMode_pushButton_1.setEnabled(True)

            self.MotorEnable_pushButton_1.setEnabled(True)
            self.MotorEnable_pushButton_2.setEnabled(True)
            self.MotorEnable_pushButton_3.setEnabled(True)
            self.MotorEnable_pushButton_4.setEnabled(True)

            # 电机1 使能读取
            Data = self.UartRead(self.Enable_Addr[0])
            if Data == self.Enable:
                self.MotorEnable_pushButton_1.setChecked(True)
            elif Data == self.Disable:
                self.MotorEnable_pushButton_1.setChecked(False)

            # 电机2 使能读取
            Data = self.UartRead(self.Enable_Addr[1])
            if Data == self.Enable:
                self.MotorEnable_pushButton_2.setChecked(True)
            elif Data == self.Disable:
                self.MotorEnable_pushButton_2.setChecked(False)

            # 电机3 使能读取
            Data = self.UartRead(self.Enable_Addr[2])
            if Data == self.Enable:
                self.MotorEnable_pushButton_3.setChecked(True)
            elif Data == self.Disable:
                self.MotorEnable_pushButton_3.setChecked(False)

            # 电机4 使能读取
            Data = self.UartRead(self.Enable_Addr[3])
            if Data == self.Enable:
                self.MotorEnable_pushButton_4.setChecked(True)
            elif Data == self.Disable:
                self.MotorEnable_pushButton_4.setChecked(False)
        else:
            self.Uart.close()
            self.Uart_widget.setEnabled(True)
            self.UartCheck_pushButton.setEnabled(True)
            self.UartConnect_pushButton.setEnabled(True)

            self.ParametersRead_pushButton_1.setEnabled(False)
            self.ParametersWrite_pushButton_1.setEnabled(False)

            self.VolCtrlMode_pushButton_1.setEnabled(False)
            self.CurCtrlMode_pushButton_1.setEnabled(False)
            self.SpdCtrlMode_pushButton_1.setEnabled(False)
            self.PosCtrlMode_pushButton_1.setEnabled(False)

            self.MotorEnable_pushButton_1.setEnabled(False)
            self.MotorEnable_pushButton_2.setEnabled(False)
            self.MotorEnable_pushButton_3.setEnabled(False)
            self.MotorEnable_pushButton_4.setEnabled(False)

    def UartRead(self, Addr):
        self.Uart.write(bytes([int('0xAA', 16), int(int(Addr) / 256), int(int(Addr) % 256), int('0xAB', 16), 0]))
        while self.Uart.waitForReadyRead(10):
            pass
        rxData = bytes(self.Uart.read(2))
        return rxData[0] << 8 | rxData[1]

    def UartWrite(self, Addr, Data):
        self.Uart.write(bytes([int('0xAA', 16), int(int(Addr) / 256), int(int(Addr) % 256), int('0xAB', 16), 1,
                               int('0xAC', 16), int(int(Data) / 256), int(int(Data) % 256)]))

    def MotorEnable1(self):
        if self.MotorEnable_pushButton_1.isChecked():
            Data = self.Enable
        else:
            Data = self.Disable
        self.UartWrite(self.Enable_Addr[0], Data)

    def MotorEnable2(self):
        if self.MotorEnable_pushButton_2.isChecked():
            Data = self.Enable
        else:
            Data = self.Disable
        self.UartWrite(self.Enable_Addr[1], Data)

    def MotorEnable3(self):
        if self.MotorEnable_pushButton_3.isChecked():
            Data = self.Enable
        else:
            Data = self.Disable
        self.UartWrite(self.Enable_Addr[2], Data)

    def MotorEnable4(self):
        if self.MotorEnable_pushButton_4.isChecked():
            Data = self.Enable
        else:
            Data = self.Disable
        self.UartWrite(self.Enable_Addr[3], Data)

    def ParametersRead(self):
        if self.Motor_tabWidget.currentIndex() == 0:
            # 电机1 模式读取
            Data = self.UartRead(self.Mode_Addr[0])
            if Data == self.Voltage_Control_Mode:
                self.VolCtrlMode_Enable_1()
            elif Data == self.Current_Control_Mode:
                self.CurCtrlMode_Enable_1()
            elif Data == self.Speed_Control_Mode:
                self.SpdCtrlMode_Enable_1()
            elif Data == self.Position_Control_Mode:
                self.PosCtrlMode_Enable_1()
            else:
                self.CtrlMode_Disable_1()

            # 电机1 极对数读取
            Data = self.UartRead(self.Np_Addr[0])
            self.Poles_spinBox_1.setValue(Data)

            # 电机1 电流环d轴Kp读取
            Data = self.UartRead(self.Id_Kp_Addr[0])
            self.IdKp_lineEdit_1.setText(str(Data))

            # 电机1 电流环d轴Ki读取
            Data = self.UartRead(self.Id_Ki_Addr[0])
            self.IdKi_lineEdit_1.setText(str(Data))

            # 电机1 电流环q轴Kp读取
            Data = self.UartRead(self.Iq_Kp_Addr[0])
            self.IqKp_lineEdit_1.setText(str(Data))

            # 电机1 电流环q轴Ki读取
            Data = self.UartRead(self.Iq_Ki_Addr[0])
            self.IqKi_lineEdit_1.setText(str(Data))

            # 电机1 d轴电压最大值读取
            Data = self.UartRead(self.Ud_Max_Addr[0])
            self.UdMax_lineEdit_1.setText(str(Data))

            # 电机1 q轴电压最大值读取
            Data = self.UartRead(self.Uq_Max_Addr[0])
            self.UqMax_lineEdit_1.setText(str(Data))

            # 电机1 速度环Kp读取
            Data = self.UartRead(self.Spd_Kp_Addr[0])
            self.SpdKp_lineEdit_1.setText(str(Data))

            # 电机1 速度环Ki读取
            Data = self.UartRead(self.Spd_Ki_Addr[0])
            self.SpdKi_lineEdit_1.setText(str(Data))

            # 电机1 q轴电流最大值读取
            Data = self.UartRead(self.Iq_Max_Addr[0])
            self.IqMax_lineEdit_1.setText(str(Data))

            # 电机1 位置环Kp读取
            Data = self.UartRead(self.Pos_Kp_Addr[0])
            self.PosKp_lineEdit_1.setText(str(Data))

            # 电机1 位置环Ki读取
            Data = self.UartRead(self.Pos_Ki_Addr[0])
            self.PosKi_lineEdit_1.setText(str(Data))

            # 电机1 速度最大值读取
            Data = self.UartRead(self.Spd_Max_Addr[0])
            self.SpdMax_lineEdit_1.setText(str(Data))

            # 电机1 d轴目标电压读取
            Data = self.UartRead(self.TargetUdExt_Addr[0])
            self.UdExt_lineEdit_1.setText(str(Data))

            # 电机1 q轴目标电压读取
            Data = self.UartRead(self.TargetUqExt_Addr[0])
            self.UqExt_lineEdit_1.setText(str(Data))

            # 电机1 d轴目标电流读取
            Data = self.UartRead(self.TargetIdExt_Addr[0])
            self.IdExt_lineEdit_1.setText(str(Data))

            # 电机1 q轴目标电流读取
            Data = self.UartRead(self.TargetIqExt_Addr[0])
            self.IqExt_lineEdit_1.setText(str(Data))

            # 电机1 目标速度读取
            Data = self.UartRead(self.TargetSpdExt_Addr[0])
            self.SpdExt_lineEdit_1.setText(str(Data))

            # 电机1 目标位置读取
            Data = self.UartRead(self.TargetPos_Addr_H[0]) << 16 | self.UartRead(self.TargetPos_Addr_L[0])
            self.Pos_lineEdit_1.setText(str(Data))
        else:
            return

        self.DataUpdate()

    def ParametersWrite(self):
        if self.Motor_tabWidget.currentIndex() == 0:
            # 电机1 模式写入
            if self.VolCtrlMode_pushButton_1.isChecked():
                Data = self.Voltage_Control_Mode
            elif self.CurCtrlMode_pushButton_1.isChecked():
                Data = self.Current_Control_Mode
            elif self.SpdCtrlMode_pushButton_1.isChecked():
                Data = self.Speed_Control_Mode
            elif self.PosCtrlMode_pushButton_1.isChecked():
                Data = self.Position_Control_Mode
            else:
                Data = self.None_Control_Mode
            self.UartWrite(self.Mode_Addr[0], Data)

            # 电机1 极对数写入
            Data = self.Poles_spinBox_1.text()
            self.UartWrite(self.Np_Addr[0], Data)

            # 电机1 电流环d轴Kp写入
            Data = self.IdKp_lineEdit_1.text()
            self.UartWrite(self.Id_Kp_Addr[0], Data)

            # 电机1 电流环d轴Ki写入
            Data = self.IdKi_lineEdit_1.text()
            self.UartWrite(self.Id_Ki_Addr[0], Data)

            # 电机1 电流环q轴Kp写入
            Data = self.IqKp_lineEdit_1.text()
            self.UartWrite(self.Iq_Kp_Addr[0], Data)

            # 电机1 电流环q轴Ki写入
            Data = self.IqKi_lineEdit_1.text()
            self.UartWrite(self.Iq_Ki_Addr[0], Data)

            # 电机1 d轴电压最大值写入
            Data = self.UdMax_lineEdit_1.text()
            self.UartWrite(self.Ud_Max_Addr[0], Data)

            # 电机1 q轴电压最大值写入
            Data = self.UqMax_lineEdit_1.text()
            self.UartWrite(self.Uq_Max_Addr[0], Data)

            # 电机1 速度环Kp写入
            Data = self.SpdKp_lineEdit_1.text()
            self.UartWrite(self.Spd_Kp_Addr[0], Data)

            # 电机1 速度环Ki写入
            Data = self.SpdKi_lineEdit_1.text()
            self.UartWrite(self.Spd_Ki_Addr[0], Data)

            # 电机1 q轴电流最大值写入
            Data = self.IqMax_lineEdit_1.text()
            self.UartWrite(self.Iq_Max_Addr[0], Data)

            # 电机1 位置环Kp写入
            Data = self.PosKp_lineEdit_1.text()
            self.UartWrite(self.Pos_Kp_Addr[0], Data)

            # 电机1 位置环Ki写入
            Data = self.PosKi_lineEdit_1.text()
            self.UartWrite(self.Pos_Ki_Addr[0], Data)

            # 电机1 速度最大值写入
            Data = self.SpdMax_lineEdit_1.text()
            self.UartWrite(self.Spd_Max_Addr[0], Data)

            # 电机1 d轴目标电压写入
            Data = self.UdExt_lineEdit_1.text()
            self.UartWrite(self.TargetUdExt_Addr[0], Data)

            # 电机1 q轴目标电压写入
            Data = self.UqExt_lineEdit_1.text()
            self.UartWrite(self.TargetUqExt_Addr[0], Data)

            # 电机1 d轴目标电流写入
            Data = self.IdExt_lineEdit_1.text()
            self.UartWrite(self.TargetIdExt_Addr[0], Data)

            # 电机1 q轴目标电流写入
            Data = self.IqExt_lineEdit_1.text()
            self.UartWrite(self.TargetIqExt_Addr[0], Data)

            # 电机1 目标速度写入
            Data = self.SpdExt_lineEdit_1.text()
            self.UartWrite(self.TargetSpdExt_Addr[0], Data)

            # 电机1 目标位置写入
            Data = int(self.Pos_lineEdit_1.text())
            self.UartWrite(self.TargetPos_Addr_H[0], Data / 65536)
            self.UartWrite(self.TargetPos_Addr_L[0], Data % 65536)
        else:
            return

    def DataUpdate(self):
        self.Poles_Update()
        self.IdKp_Update()
        self.IdKi_Update()
        self.IqKp_Update()
        self.IqKi_Update()
        self.UdMax_Update()
        self.UqMax_Update()
        self.SpdKp_Update()
        self.SpdKi_Update()
        self.IqMax_Update()
        self.PosKp_Update()
        self.PosKi_Update()
        self.SpdMax_Update()
        self.UdExt_Update()
        self.UqExt_Update()
        self.IdExt_Update()
        self.IqExt_Update()
        self.SpdExt_Update()
        self.Pos_Update()

    def Poles_Update(self):
        if self.Motor_tabWidget.currentIndex() == 0:
            Data = int(self.Poles_spinBox_1.text()) * 2
            self.Poles_Calculate_lineEdit_1.setText(str(Data))
        else:
            return

    def IdKp_Update(self):
        if self.Motor_tabWidget.currentIndex() == 0:
            Data = int(self.IdKp_lineEdit_1.text())
            self.IdKp_Calculate_lineEdit_1.setText(str(Data))
        else:
            return

    def IdKi_Update(self):
        if self.Motor_tabWidget.currentIndex() == 0:
            Data = int(self.IdKi_lineEdit_1.text())
            self.IdKi_Calculate_lineEdit_1.setText(str(Data))
        else:
            return

    def IqKp_Update(self):
        if self.Motor_tabWidget.currentIndex() == 0:
            Data = int(self.IqKp_lineEdit_1.text())
            self.IqKp_Calculate_lineEdit_1.setText(str(Data))
        else:
            return

    def IqKi_Update(self):
        if self.Motor_tabWidget.currentIndex() == 0:
            Data = int(self.IqKi_lineEdit_1.text())
            self.IqKi_Calculate_lineEdit_1.setText(str(Data))
        else:
            return

    def UdMax_Update(self):
        if self.Motor_tabWidget.currentIndex() == 0:
            Data = int(self.UdMax_lineEdit_1.text())
            self.UdMax_Calculate_lineEdit_1.setText(str(Data) + 'V')
        else:
            return

    def UqMax_Update(self):
        if self.Motor_tabWidget.currentIndex() == 0:
            Data = int(self.UqMax_lineEdit_1.text())
            self.UqMax_Calculate_lineEdit_1.setText(str(Data) + 'V')
        else:
            return

    def SpdKp_Update(self):
        if self.Motor_tabWidget.currentIndex() == 0:
            Data = int(self.SpdKp_lineEdit_1.text())
            self.SpdKp_Calculate_lineEdit_1.setText(str(Data))
        else:
            return

    def SpdKi_Update(self):
        if self.Motor_tabWidget.currentIndex() == 0:
            Data = int(self.SpdKi_lineEdit_1.text())
            self.SpdKi_Calculate_lineEdit_1.setText(str(Data))
        else:
            return

    def IqMax_Update(self):
        if self.Motor_tabWidget.currentIndex() == 0:
            Data = int(self.IqMax_lineEdit_1.text())
            self.IqMax_Calculate_lineEdit_1.setText(str(Data) + 'A')
        else:
            return

    def PosKp_Update(self):
        if self.Motor_tabWidget.currentIndex() == 0:
            Data = int(self.PosKp_lineEdit_1.text())
            self.PosKp_Calculate_lineEdit_1.setText(str(Data))
        else:
            return

    def PosKi_Update(self):
        if self.Motor_tabWidget.currentIndex() == 0:
            Data = int(self.PosKi_lineEdit_1.text())
            self.PosKi_Calculate_lineEdit_1.setText(str(Data))
        else:
            return

    def SpdMax_Update(self):
        if self.Motor_tabWidget.currentIndex() == 0:
            Data = int(self.SpdMax_lineEdit_1.text())
            self.SpdMax_Calculate_lineEdit_1.setText(str(Data) + 'rpm')
        else:
            return

    def UdExt_Update(self):
        if self.Motor_tabWidget.currentIndex() == 0:
            Data = int(self.UdExt_lineEdit_1.text())
            self.UdExt_Calculate_lineEdit_1.setText(str(Data) + 'V')
        else:
            return

    def UqExt_Update(self):
        if self.Motor_tabWidget.currentIndex() == 0:
            Data = int(self.UqExt_lineEdit_1.text())
            self.UqExt_Calculate_lineEdit_1.setText(str(Data) + 'V')
        else:
            return

    def IdExt_Update(self):
        if self.Motor_tabWidget.currentIndex() == 0:
            Data = int(self.IdExt_lineEdit_1.text())
            self.IdExt_Calculate_lineEdit_1.setText(str(Data) + 'A')
        else:
            return

    def IqExt_Update(self):
        if self.Motor_tabWidget.currentIndex() == 0:
            Data = int(self.IqExt_lineEdit_1.text())
            self.IqExt_Calculate_lineEdit_1.setText(str(Data) + 'A')
        else:
            return

    def SpdExt_Update(self):
        if self.Motor_tabWidget.currentIndex() == 0:
            Data = int(self.SpdExt_lineEdit_1.text())
            self.SpdExt_Calculate_lineEdit_1.setText(str(Data) + 'rpm')
        else:
            return

    def Pos_Update(self):
        if self.Motor_tabWidget.currentIndex() == 0:
            Data = int(self.Pos_lineEdit_1.text())
            self.Pos_Calculate_lineEdit_1.setText(str(Data))
        else:
            return

    def Calculate(self):
        if self.Motor_tabWidget.currentIndex() == 0:
            Udc = float(self.Udc_lineEdit_1.text())
            Ll = float(self.Ll_lineEdit_1.text()) / 1000
            Rl = float(self.Rl_lineEdit_1.text())
            Kt = float(self.Kt_lineEdit_1.text())
            Jm = float(self.Jm_lineEdit_1.text()) / 10000
            UdcMax = float(self.UdcMax_lineEdit_1.text())
            ADCUdcMax = float(self.ADCUdcMax_lineEdit_1.text())
            CurMax = float(self.CurMax_lineEdit_1.text())
            ADCCurMax = float(self.ADCCurMax_lineEdit_1.text())
            AbsSpdMax = float(self.AbsSpdMax_lineEdit_1.text())
            SingleTurnMax = float(self.SingleTurnMax_lineEdit_1.text())
            CurFs = float(self.CurFs_lineEdit_1.text())
            CurFc = float(self.CurFc_lineEdit_1.text())
            SpdFs = float(self.SpdFs_lineEdit_1.text())
            SpdFc = float(self.SpdFc_lineEdit_1.text())
            SpdH = float(self.SpdH_lineEdit_1.text())
            PosFs = float(self.PosFs_lineEdit_1.text())
            PosFc = float(self.PosFc_lineEdit_1.text())
            PosH = float(self.PosH_lineEdit_1.text())

            # 电流环参数计算
            Ls = Ll / 2
            Rs = Rl / 2
            CurWc = CurFc * 2 * math.pi

            IdKp = CurWc * Ls
            IdKi = CurWc * Rs / CurFs
            IqKp = CurWc * Ls
            IqKi = CurWc * Rs / CurFs

            CurGain = ((Udc / math.sqrt(3)) / 32768) / (CurMax / (ADCCurMax / 2048 * 32768))

            IdKp_Q9 = int(round(IdKp / CurGain * 512))
            IdKi_Q9 = int(round(IdKi / CurGain * 512))
            IqKp_Q9 = int(round(IqKp / CurGain * 512))
            IqKi_Q9 = int(round(IqKi / CurGain * 512))

            self.IdKp_Calculate_lineEdit_1.setText(str(IdKp))
            self.IdKi_Calculate_lineEdit_1.setText(str(IdKi))
            self.IqKp_Calculate_lineEdit_1.setText(str(IqKp))
            self.IqKi_Calculate_lineEdit_1.setText(str(IqKi))

            self.IdKp_lineEdit_1.setText(str(IdKp_Q9))
            self.IdKi_lineEdit_1.setText(str(IdKi_Q9))
            self.IqKp_lineEdit_1.setText(str(IqKp_Q9))
            self.IqKi_lineEdit_1.setText(str(IqKi_Q9))

            # 速度环参数计算
            SpdWc = SpdFc * 2 * math.pi

            SpdKp = Jm / Kt * SpdWc
            SpdKi = SpdKp * (SpdWc / SpdH) / SpdFs

            SpdGain = (CurMax / (ADCCurMax / 2048 * 32768)) / ((AbsSpdMax / 60 * 2 * math.pi) / (SingleTurnMax * AbsSpdMax / 60 / SpdFs))

            SpdKp_Q11 = int(round(SpdKp / SpdGain * 2048))
            SpdKi_Q11 = int(round(SpdKi / SpdGain * 2048))

            self.SpdKp_Calculate_lineEdit_1.setText(str(SpdKp))
            self.SpdKi_Calculate_lineEdit_1.setText(str(SpdKi))

            self.SpdKp_lineEdit_1.setText(str(SpdKp_Q11))
            self.SpdKi_lineEdit_1.setText(str(SpdKi_Q11))
        else:
            return

    def CtrlMode_Disable_1(self):
        self.VolCtrlMode_pushButton_1.setChecked(False)
        self.UdExt_lineEdit_1.setEnabled(False)
        self.UdExt_Calculate_lineEdit_1.setEnabled(False)
        self.UqExt_lineEdit_1.setEnabled(False)
        self.UqExt_Calculate_lineEdit_1.setEnabled(False)

        self.CurCtrlMode_pushButton_1.setChecked(False)
        self.IdExt_lineEdit_1.setEnabled(False)
        self.IdExt_Calculate_lineEdit_1.setEnabled(False)
        self.IqExt_lineEdit_1.setEnabled(False)
        self.IqExt_Calculate_lineEdit_1.setEnabled(False)

        self.SpdCtrlMode_pushButton_1.setChecked(False)
        self.SpdExt_lineEdit_1.setEnabled(False)
        self.SpdExt_Calculate_lineEdit_1.setEnabled(False)

        self.PosCtrlMode_pushButton_1.setChecked(False)
        self.Pos_lineEdit_1.setEnabled(False)
        self.Pos_Calculate_lineEdit_1.setEnabled(False)

    def VolCtrlMode_Enable_1(self):
        self.VolCtrlMode_pushButton_1.setChecked(True)
        self.UdExt_lineEdit_1.setEnabled(True)
        self.UdExt_Calculate_lineEdit_1.setEnabled(True)
        self.UqExt_lineEdit_1.setEnabled(True)
        self.UqExt_Calculate_lineEdit_1.setEnabled(True)

        self.CurCtrlMode_pushButton_1.setChecked(False)
        self.IdExt_lineEdit_1.setEnabled(False)
        self.IdExt_Calculate_lineEdit_1.setEnabled(False)
        self.IqExt_lineEdit_1.setEnabled(False)
        self.IqExt_Calculate_lineEdit_1.setEnabled(False)

        self.SpdCtrlMode_pushButton_1.setChecked(False)
        self.SpdExt_lineEdit_1.setEnabled(False)
        self.SpdExt_Calculate_lineEdit_1.setEnabled(False)

        self.PosCtrlMode_pushButton_1.setChecked(False)
        self.Pos_lineEdit_1.setEnabled(False)
        self.Pos_Calculate_lineEdit_1.setEnabled(False)

    def CurCtrlMode_Enable_1(self):
        self.VolCtrlMode_pushButton_1.setChecked(False)
        self.UdExt_lineEdit_1.setEnabled(False)
        self.UdExt_Calculate_lineEdit_1.setEnabled(False)
        self.UqExt_lineEdit_1.setEnabled(False)
        self.UqExt_Calculate_lineEdit_1.setEnabled(False)

        self.CurCtrlMode_pushButton_1.setChecked(True)
        self.IdExt_lineEdit_1.setEnabled(True)
        self.IdExt_Calculate_lineEdit_1.setEnabled(True)
        self.IqExt_lineEdit_1.setEnabled(True)
        self.IqExt_Calculate_lineEdit_1.setEnabled(True)

        self.SpdCtrlMode_pushButton_1.setChecked(False)
        self.SpdExt_lineEdit_1.setEnabled(False)
        self.SpdExt_Calculate_lineEdit_1.setEnabled(False)

        self.PosCtrlMode_pushButton_1.setChecked(False)
        self.Pos_lineEdit_1.setEnabled(False)
        self.Pos_Calculate_lineEdit_1.setEnabled(False)

    def SpdCtrlMode_Enable_1(self):
        self.VolCtrlMode_pushButton_1.setChecked(False)
        self.UdExt_lineEdit_1.setEnabled(False)
        self.UdExt_Calculate_lineEdit_1.setEnabled(False)
        self.UqExt_lineEdit_1.setEnabled(False)
        self.UqExt_Calculate_lineEdit_1.setEnabled(False)

        self.CurCtrlMode_pushButton_1.setChecked(False)
        self.IdExt_lineEdit_1.setEnabled(False)
        self.IdExt_Calculate_lineEdit_1.setEnabled(False)
        self.IqExt_lineEdit_1.setEnabled(False)
        self.IqExt_Calculate_lineEdit_1.setEnabled(False)

        self.SpdCtrlMode_pushButton_1.setChecked(True)
        self.SpdExt_lineEdit_1.setEnabled(True)
        self.SpdExt_Calculate_lineEdit_1.setEnabled(True)

        self.PosCtrlMode_pushButton_1.setChecked(False)
        self.Pos_lineEdit_1.setEnabled(False)
        self.Pos_Calculate_lineEdit_1.setEnabled(False)

    def PosCtrlMode_Enable_1(self):
        self.VolCtrlMode_pushButton_1.setChecked(False)
        self.UdExt_lineEdit_1.setEnabled(False)
        self.UdExt_Calculate_lineEdit_1.setEnabled(False)
        self.UqExt_lineEdit_1.setEnabled(False)
        self.UqExt_Calculate_lineEdit_1.setEnabled(False)

        self.CurCtrlMode_pushButton_1.setChecked(False)
        self.IdExt_lineEdit_1.setEnabled(False)
        self.IdExt_Calculate_lineEdit_1.setEnabled(False)
        self.IqExt_lineEdit_1.setEnabled(False)
        self.IqExt_Calculate_lineEdit_1.setEnabled(False)

        self.SpdCtrlMode_pushButton_1.setChecked(False)
        self.SpdExt_lineEdit_1.setEnabled(False)
        self.SpdExt_Calculate_lineEdit_1.setEnabled(False)

        self.PosCtrlMode_pushButton_1.setChecked(True)
        self.Pos_lineEdit_1.setEnabled(True)
        self.Pos_Calculate_lineEdit_1.setEnabled(True)

    def VolCtrlMode(self):
        if self.Motor_tabWidget.currentIndex() == 0:
            if self.VolCtrlMode_pushButton_1.isChecked():
                self.VolCtrlMode_Enable_1()
            else:
                self.CtrlMode_Disable_1()
        else:
            return

    def CurCtrlMode(self):
        if self.Motor_tabWidget.currentIndex() == 0:
            if self.CurCtrlMode_pushButton_1.isChecked():
                self.CurCtrlMode_Enable_1()
            else:
                self.CtrlMode_Disable_1()
        else:
            return

    def SpdCtrlMode(self):
        if self.Motor_tabWidget.currentIndex() == 0:
            if self.SpdCtrlMode_pushButton_1.isChecked():
                self.SpdCtrlMode_Enable_1()
            else:
                self.CtrlMode_Disable_1()
        else:
            return

    def PosCtrlMode(self):
        if self.Motor_tabWidget.currentIndex() == 0:
            if self.PosCtrlMode_pushButton_1.isChecked():
                self.PosCtrlMode_Enable_1()
            else:
                self.CtrlMode_Disable_1()
        else:
            return


if __name__ == "__main__":
    app = QApplication()
    window = CarWindow()

    apply_stylesheet(app, theme='light_red.xml')

    window.show()
    sys.exit(app.exec())
