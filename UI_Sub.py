from Car_Motor4 import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo


class UISub(QMainWindow, Ui_MainWindow):
    Addr_Offset = int(128)

    Theta_Addr = [Addr_Offset * 0 + 0, Addr_Offset * 1 + 0, Addr_Offset * 2 + 0, Addr_Offset * 3 + 0]
    ThetaE_Addr = [Addr_Offset * 0 + 1, Addr_Offset * 1 + 1, Addr_Offset * 2 + 1, Addr_Offset * 3 + 1]
    SinTheta_Addr = [Addr_Offset * 0 + 2, Addr_Offset * 1 + 2, Addr_Offset * 2 + 2, Addr_Offset * 3 + 2]
    CosTheta_Addr = [Addr_Offset * 0 + 3, Addr_Offset * 1 + 3, Addr_Offset * 2 + 3, Addr_Offset * 3 + 3]
    Ia_Addr = [Addr_Offset * 0 + 4, Addr_Offset * 1 + 4, Addr_Offset * 2 + 4, Addr_Offset * 3 + 4]
    Ic_Addr = [Addr_Offset * 0 + 5, Addr_Offset * 1 + 5, Addr_Offset * 2 + 5, Addr_Offset * 3 + 5]
    Ix_Addr = [Addr_Offset * 0 + 6, Addr_Offset * 1 + 6, Addr_Offset * 2 + 6, Addr_Offset * 3 + 6]
    Iy_Addr = [Addr_Offset * 0 + 7, Addr_Offset * 1 + 7, Addr_Offset * 2 + 7, Addr_Offset * 3 + 7]
    Ux_Addr = [Addr_Offset * 0 + 8, Addr_Offset * 1 + 8, Addr_Offset * 2 + 8, Addr_Offset * 3 + 8]
    Uy_Addr = [Addr_Offset * 0 + 9, Addr_Offset * 1 + 9, Addr_Offset * 2 + 9, Addr_Offset * 3 + 9]
    U1_Addr = [Addr_Offset * 0 + 10, Addr_Offset * 1 + 10, Addr_Offset * 2 + 10, Addr_Offset * 3 + 10]
    U2_Addr = [Addr_Offset * 0 + 11, Addr_Offset * 1 + 11, Addr_Offset * 2 + 11, Addr_Offset * 3 + 11]
    U3_Addr = [Addr_Offset * 0 + 12, Addr_Offset * 1 + 12, Addr_Offset * 2 + 12, Addr_Offset * 3 + 12]
    Ua_Addr = [Addr_Offset * 0 + 13, Addr_Offset * 1 + 13, Addr_Offset * 2 + 13, Addr_Offset * 3 + 13]
    Ub_Addr = [Addr_Offset * 0 + 14, Addr_Offset * 1 + 14, Addr_Offset * 2 + 14, Addr_Offset * 3 + 14]
    Uc_Addr = [Addr_Offset * 0 + 15, Addr_Offset * 1 + 15, Addr_Offset * 2 + 15, Addr_Offset * 3 + 15]
    Mode_Addr = [Addr_Offset * 0 + 16, Addr_Offset * 1 + 16, Addr_Offset * 2 + 16, Addr_Offset * 3 + 16]
    Np_Addr = [Addr_Offset * 0 + 17, Addr_Offset * 1 + 17, Addr_Offset * 2 + 17, Addr_Offset * 3 + 17]
    TargetUd_Addr = [Addr_Offset * 0 + 18, Addr_Offset * 1 + 18, Addr_Offset * 2 + 18, Addr_Offset * 3 + 18]
    TargetUdExt_Addr = [Addr_Offset * 0 + 19, Addr_Offset * 1 + 19, Addr_Offset * 2 + 19, Addr_Offset * 3 + 19]
    TargetUq_Addr = [Addr_Offset * 0 + 20, Addr_Offset * 1 + 20, Addr_Offset * 2 + 20, Addr_Offset * 3 + 20]
    TargetUqExt_Addr = [Addr_Offset * 0 + 21, Addr_Offset * 1 + 21, Addr_Offset * 2 + 21, Addr_Offset * 3 + 21]
    PresentId_Addr = [Addr_Offset * 0 + 22, Addr_Offset * 1 + 22, Addr_Offset * 2 + 22, Addr_Offset * 3 + 22]
    TargetId_Addr = [Addr_Offset * 0 + 23, Addr_Offset * 1 + 23, Addr_Offset * 2 + 23, Addr_Offset * 3 + 23]
    TargetIdExt_Addr = [Addr_Offset * 0 + 24, Addr_Offset * 1 + 24, Addr_Offset * 2 + 24, Addr_Offset * 3 + 24]
    Id_Kp_Addr = [Addr_Offset * 0 + 25, Addr_Offset * 1 + 25, Addr_Offset * 2 + 25, Addr_Offset * 3 + 25]
    Id_Ki_Addr = [Addr_Offset * 0 + 26, Addr_Offset * 1 + 26, Addr_Offset * 2 + 26, Addr_Offset * 3 + 26]
    Ud_Max_Addr = [Addr_Offset * 0 + 27, Addr_Offset * 1 + 27, Addr_Offset * 2 + 27, Addr_Offset * 3 + 27]
    PresentIq_Addr = [Addr_Offset * 0 + 28, Addr_Offset * 1 + 28, Addr_Offset * 2 + 28, Addr_Offset * 3 + 28]
    TargetIq_Addr = [Addr_Offset * 0 + 29, Addr_Offset * 1 + 29, Addr_Offset * 2 + 29, Addr_Offset * 3 + 29]
    TargetIqExt_Addr = [Addr_Offset * 0 + 30, Addr_Offset * 1 + 30, Addr_Offset * 2 + 30, Addr_Offset * 3 + 30]
    Iq_Kp_Addr = [Addr_Offset * 0 + 31, Addr_Offset * 1 + 31, Addr_Offset * 2 + 31, Addr_Offset * 3 + 31]
    Iq_Ki_Addr = [Addr_Offset * 0 + 32, Addr_Offset * 1 + 32, Addr_Offset * 2 + 32, Addr_Offset * 3 + 32]
    Uq_Max_Addr = [Addr_Offset * 0 + 33, Addr_Offset * 1 + 33, Addr_Offset * 2 + 33, Addr_Offset * 3 + 33]
    PresentSpd_Addr = [Addr_Offset * 0 + 34, Addr_Offset * 1 + 34, Addr_Offset * 2 + 34, Addr_Offset * 3 + 34]
    TargetSpd_Addr = [Addr_Offset * 0 + 35, Addr_Offset * 1 + 35, Addr_Offset * 2 + 35, Addr_Offset * 3 + 35]
    TargetSpdExt_Addr = [Addr_Offset * 0 + 36, Addr_Offset * 1 + 36, Addr_Offset * 2 + 36, Addr_Offset * 3 + 36]
    Spd_Kp_Addr = [Addr_Offset * 0 + 37, Addr_Offset * 1 + 37, Addr_Offset * 2 + 37, Addr_Offset * 3 + 37]
    Spd_Ki_Addr = [Addr_Offset * 0 + 38, Addr_Offset * 1 + 38, Addr_Offset * 2 + 38, Addr_Offset * 3 + 38]
    Iq_Max_Addr = [Addr_Offset * 0 + 39, Addr_Offset * 1 + 39, Addr_Offset * 2 + 39, Addr_Offset * 3 + 39]
    PresentPos_Addr_H = [Addr_Offset * 0 + 40, Addr_Offset * 1 + 40, Addr_Offset * 2 + 40, Addr_Offset * 3 + 40]
    PresentPos_Addr_L = [Addr_Offset * 0 + 41, Addr_Offset * 1 + 41, Addr_Offset * 2 + 41, Addr_Offset * 3 + 41]
    TargetPos_Addr_H = [Addr_Offset * 0 + 42, Addr_Offset * 1 + 42, Addr_Offset * 2 + 42, Addr_Offset * 3 + 42]
    TargetPos_Addr_L = [Addr_Offset * 0 + 43, Addr_Offset * 1 + 43, Addr_Offset * 2 + 43, Addr_Offset * 3 + 43]
    Pos_Kp_Addr = [Addr_Offset * 0 + 44, Addr_Offset * 1 + 44, Addr_Offset * 2 + 44, Addr_Offset * 3 + 44]
    Pos_Ki_Addr = [Addr_Offset * 0 + 45, Addr_Offset * 1 + 45, Addr_Offset * 2 + 45, Addr_Offset * 3 + 45]
    Spd_Max_Addr = [Addr_Offset * 0 + 46, Addr_Offset * 1 + 46, Addr_Offset * 2 + 46, Addr_Offset * 3 + 46]
    Error_Addr = [Addr_Offset * 0 + 47, Addr_Offset * 1 + 47, Addr_Offset * 2 + 47, Addr_Offset * 3 + 47]
    Enable_Addr = [Addr_Offset * 0 + 48, Addr_Offset * 1 + 48, Addr_Offset * 2 + 48, Addr_Offset * 3 + 48]
    Display_Addr = [Addr_Offset * 0 + 49, Addr_Offset * 1 + 49, Addr_Offset * 2 + 49, Addr_Offset * 3 + 49]

    None_Control_Mode = 0
    Voltage_Control_Mode = 1
    Current_Control_Mode = 2
    Speed_Control_Mode = 3
    Position_Control_Mode = 4
    Enable = 1
    Disable = 0

    def __init__(self):
        super(UISub, self).__init__()
        self.pw1 = None
        self.Uart = None
        self.setupUi(self)
        self.addItems()

    def addItems(self):
        # Qt 串口类
        self.Uart = QSerialPort()

    def UartConnectSelect_Enable(self):
        self.UartCheck_pushButton.setEnabled(True)
        self.UartEnable_pushButton.setEnabled(True)
        self.UartSelect_comboBox.setEnabled(True)
        self.UartBaudSelect_comboBox.setEnabled(True)

    def UartConnectSelect_Disable(self):
        self.UartCheck_pushButton.setEnabled(False)
        self.UartEnable_pushButton.setEnabled(False)
        self.UartSelect_comboBox.setEnabled(False)
        self.UartBaudSelect_comboBox.setEnabled(False)

    def ETH_ConnectSelect_Enable(self):
        self.ETH_Enable_pushButton.setEnabled(True)
        self.ETH_IPAddr_lineEdit.setEnabled(True)
        self.ETH_Port_lineEdit.setEnabled(True)

    def ETH_ConnectSelect_Disable(self):
        self.ETH_Enable_pushButton.setEnabled(False)
        self.ETH_IPAddr_lineEdit.setEnabled(False)
        self.ETH_Port_lineEdit.setEnabled(False)

    def UartCheck(self):
        self.UartSelect_comboBox.clear()
        Uart = QSerialPort()
        UartList = QSerialPortInfo.availablePorts()
        for UartInfo in UartList:
            Uart.setPort(UartInfo)
            if Uart.open(QSerialPort.ReadWrite):
                self.UartSelect_comboBox.addItem(Uart.portName())
                Uart.close()

    def UartRead_int16(self, Addr):
        self.Uart.write(bytes([int('0xAA', 16), int(int(Addr) / 256), int(int(Addr) % 256), int('0xAB', 16), 0]))
        while self.Uart.waitForReadyRead(10):
            pass
        rxData = bytes(self.Uart.read(2))
        Data = rxData[0] << 8 | rxData[1]
        if Data >= 32768:
            Data = Data - 65536
        else:
            Data = Data
        return Data

    def UartWrite_int16(self, Addr, Data):
        Byte_Addr_H = int(int(Addr) / 256)
        Byte_Addr_L = int(int(Addr) % 256)

        Data = int(Data)
        if Data < 0:
            Data = 65536 + Data
            Byte_Data_H = int(Data / 256)
            Byte_Data_L = int(Data % 256)
        else:
            Byte_Data_H = int(Data / 256)
            Byte_Data_L = int(Data % 256)

        self.Uart.write(bytes([int('0xAA', 16), Byte_Addr_H, Byte_Addr_L, int('0xAB', 16), 1,
                               int('0xAC', 16), Byte_Data_H, Byte_Data_L]))

    def UartRead_int32(self, AddrH, AddrL):
        self.Uart.write(bytes([int('0xAA', 16), int(int(AddrH) / 256), int(int(AddrH) % 256), int('0xAB', 16), 0]))
        while self.Uart.waitForReadyRead(10):
            pass
        rxData = bytes(self.Uart.read(2))
        Data = rxData[0] << 8 | rxData[1]

        self.Uart.write(bytes([int('0xAA', 16), int(int(AddrL) / 256), int(int(AddrL) % 256), int('0xAB', 16), 0]))
        while self.Uart.waitForReadyRead(10):
            pass
        rxData = bytes(self.Uart.read(2))
        Data = Data << 16 | rxData[0] << 8 | rxData[1]

        if Data >= 2147483648:
            Data = Data - 4294967296
        else:
            Data = Data

        return Data

    def UartWrite_int32(self, AddrH, AddrL, Data):
        Byte_AddrH_H = int(int(AddrH) / 256)
        Byte_AddrH_L = int(int(AddrH) % 256)

        Byte_AddrL_H = int(int(AddrL) / 256)
        Byte_AddrL_L = int(int(AddrL) % 256)

        Data = int(Data)
        if Data < 0:
            Data = 4294967296 + Data
            DataH = int(Data / 65536)
            DataL = int(Data % 65536)
            Byte_DataH_H = int(DataH / 256)
            Byte_DataH_L = int(DataH % 256)
            Byte_DataL_H = int(DataL / 256)
            Byte_DataL_L = int(DataL % 256)
        else:
            DataH = int(Data / 65536)
            DataL = int(Data % 65536)
            Byte_DataH_H = int(DataH / 256)
            Byte_DataH_L = int(DataH % 256)
            Byte_DataL_H = int(DataL / 256)
            Byte_DataL_L = int(DataL % 256)

        self.Uart.write(bytes([int('0xAA', 16), Byte_AddrH_H, Byte_AddrH_L, int('0xAB', 16), 1,
                               int('0xAC', 16), Byte_DataH_H, Byte_DataH_L]))

        self.Uart.write(bytes([int('0xAA', 16), Byte_AddrL_H, Byte_AddrL_L, int('0xAB', 16), 1,
                               int('0xAC', 16), Byte_DataL_H, Byte_DataL_L]))

    def MotorEnable_Enable_1(self):
        self.Poles_spinBox_1.setEnabled(False)
        self.Poles_Calculate_lineEdit_1.setEnabled(False)

        self.VolCtrlMode_pushButton_1.setEnabled(False)
        self.CurCtrlMode_pushButton_1.setEnabled(False)
        self.SpdCtrlMode_pushButton_1.setEnabled(False)
        self.PosCtrlMode_pushButton_1.setEnabled(False)

    def MotorEnable_Disable_1(self):
        self.Poles_spinBox_1.setEnabled(True)
        self.Poles_Calculate_lineEdit_1.setEnabled(True)

        self.VolCtrlMode_pushButton_1.setEnabled(True)
        self.CurCtrlMode_pushButton_1.setEnabled(True)
        self.SpdCtrlMode_pushButton_1.setEnabled(True)
        self.PosCtrlMode_pushButton_1.setEnabled(True)

    def ParametersRead_Page1(self):
        # 电机1 模式读取
        Data = self.UartRead_int16(self.Mode_Addr[0])
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
        Data = self.UartRead_int16(self.Np_Addr[0])
        self.Poles_spinBox_1.setValue(Data)

        # 电机1 电流环d轴Kp读取
        Data = self.UartRead_int16(self.Id_Kp_Addr[0])
        self.IdKp_lineEdit_1.setText(str(Data))

        # 电机1 电流环d轴Ki读取
        Data = self.UartRead_int16(self.Id_Ki_Addr[0])
        self.IdKi_lineEdit_1.setText(str(Data))

        # 电机1 电流环q轴Kp读取
        Data = self.UartRead_int16(self.Iq_Kp_Addr[0])
        self.IqKp_lineEdit_1.setText(str(Data))

        # 电机1 电流环q轴Ki读取
        Data = self.UartRead_int16(self.Iq_Ki_Addr[0])
        self.IqKi_lineEdit_1.setText(str(Data))

        # 电机1 d轴电压最大值读取
        Data = self.UartRead_int16(self.Ud_Max_Addr[0])
        self.UdMax_lineEdit_1.setText(str(Data))

        # 电机1 q轴电压最大值读取
        Data = self.UartRead_int16(self.Uq_Max_Addr[0])
        self.UqMax_lineEdit_1.setText(str(Data))

        # 电机1 速度环Kp读取
        Data = self.UartRead_int16(self.Spd_Kp_Addr[0])
        self.SpdKp_lineEdit_1.setText(str(Data))

        # 电机1 速度环Ki读取
        Data = self.UartRead_int16(self.Spd_Ki_Addr[0])
        self.SpdKi_lineEdit_1.setText(str(Data))

        # 电机1 q轴电流最大值读取
        Data = self.UartRead_int16(self.Iq_Max_Addr[0])
        self.IqMax_lineEdit_1.setText(str(Data))

        # 电机1 位置环Kp读取
        Data = self.UartRead_int16(self.Pos_Kp_Addr[0])
        self.PosKp_lineEdit_1.setText(str(Data))

        # 电机1 位置环Ki读取
        Data = self.UartRead_int16(self.Pos_Ki_Addr[0])
        self.PosKi_lineEdit_1.setText(str(Data))

        # 电机1 速度最大值读取
        Data = self.UartRead_int16(self.Spd_Max_Addr[0])
        self.SpdMax_lineEdit_1.setText(str(Data))

        # 电机1 d轴目标电压读取
        Data = self.UartRead_int16(self.TargetUdExt_Addr[0])
        self.UdExt_lineEdit_1.setText(str(Data))

        # 电机1 q轴目标电压读取
        Data = self.UartRead_int16(self.TargetUqExt_Addr[0])
        self.UqExt_lineEdit_1.setText(str(Data))

        # 电机1 d轴目标电流读取
        Data = self.UartRead_int16(self.TargetIdExt_Addr[0])
        self.IdExt_lineEdit_1.setText(str(Data))

        # 电机1 q轴目标电流读取
        Data = self.UartRead_int16(self.TargetIqExt_Addr[0])
        self.IqExt_lineEdit_1.setText(str(Data))

        # 电机1 目标速度读取
        Data = self.UartRead_int16(self.TargetSpdExt_Addr[0])
        self.SpdExt_lineEdit_1.setText(str(Data))

        # 电机1 目标位置读取
        Data = self.UartRead_int32(self.TargetPos_Addr_H[0], self.TargetPos_Addr_L[0])
        self.Pos_lineEdit_1.setText(str(Data))

        self.DataUpdate(Page=1)

    def ParametersWrite_Page1(self):
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
        self.UartWrite_int16(self.Mode_Addr[0], Data)

        # 电机1 极对数写入
        Data = self.Poles_spinBox_1.text()
        self.UartWrite_int16(self.Np_Addr[0], Data)

        # 电机1 电流环d轴Kp写入
        Data = self.IdKp_lineEdit_1.text()
        self.UartWrite_int16(self.Id_Kp_Addr[0], Data)

        # 电机1 电流环d轴Ki写入
        Data = self.IdKi_lineEdit_1.text()
        self.UartWrite_int16(self.Id_Ki_Addr[0], Data)

        # 电机1 电流环q轴Kp写入
        Data = self.IqKp_lineEdit_1.text()
        self.UartWrite_int16(self.Iq_Kp_Addr[0], Data)

        # 电机1 电流环q轴Ki写入
        Data = self.IqKi_lineEdit_1.text()
        self.UartWrite_int16(self.Iq_Ki_Addr[0], Data)

        # 电机1 d轴电压最大值写入
        Data = self.UdMax_lineEdit_1.text()
        self.UartWrite_int16(self.Ud_Max_Addr[0], Data)

        # 电机1 q轴电压最大值写入
        Data = self.UqMax_lineEdit_1.text()
        self.UartWrite_int16(self.Uq_Max_Addr[0], Data)

        # 电机1 速度环Kp写入
        Data = self.SpdKp_lineEdit_1.text()
        self.UartWrite_int16(self.Spd_Kp_Addr[0], Data)

        # 电机1 速度环Ki写入
        Data = self.SpdKi_lineEdit_1.text()
        self.UartWrite_int16(self.Spd_Ki_Addr[0], Data)

        # 电机1 q轴电流最大值写入
        Data = self.IqMax_lineEdit_1.text()
        self.UartWrite_int16(self.Iq_Max_Addr[0], Data)

        # 电机1 位置环Kp写入
        Data = self.PosKp_lineEdit_1.text()
        self.UartWrite_int16(self.Pos_Kp_Addr[0], Data)

        # 电机1 位置环Ki写入
        Data = self.PosKi_lineEdit_1.text()
        self.UartWrite_int16(self.Pos_Ki_Addr[0], Data)

        # 电机1 速度最大值写入
        Data = self.SpdMax_lineEdit_1.text()
        self.UartWrite_int16(self.Spd_Max_Addr[0], Data)

        # 电机1 d轴目标电压写入
        Data = self.UdExt_lineEdit_1.text()
        self.UartWrite_int16(self.TargetUdExt_Addr[0], Data)

        # 电机1 q轴目标电压写入
        Data = self.UqExt_lineEdit_1.text()
        self.UartWrite_int16(self.TargetUqExt_Addr[0], Data)

        # 电机1 d轴目标电流写入
        Data = self.IdExt_lineEdit_1.text()
        self.UartWrite_int16(self.TargetIdExt_Addr[0], Data)

        # 电机1 q轴目标电流写入
        Data = self.IqExt_lineEdit_1.text()
        self.UartWrite_int16(self.TargetIqExt_Addr[0], Data)

        # 电机1 目标速度写入
        Data = self.SpdExt_lineEdit_1.text()
        self.UartWrite_int16(self.TargetSpdExt_Addr[0], Data)

        # 电机1 目标位置写入
        Data = int(self.Pos_lineEdit_1.text())
        self.UartWrite_int32(self.TargetPos_Addr_H[0], self.TargetPos_Addr_L[0], Data)

    def DataUpdate(self, Page):
        self.Poles_Update(Page=Page)
        self.IdKp_Update(Page=Page)
        self.IdKi_Update(Page=Page)
        self.IqKp_Update(Page=Page)
        self.IqKi_Update(Page=Page)
        self.UdMax_Update(Page=Page)
        self.UqMax_Update(Page=Page)
        self.SpdKp_Update(Page=Page)
        self.SpdKi_Update(Page=Page)
        self.IqMax_Update(Page=Page)
        self.PosKp_Update(Page=Page)
        self.PosKi_Update(Page=Page)
        self.SpdMax_Update(Page=Page)
        self.UdExt_Update(Page=Page)
        self.UqExt_Update(Page=Page)
        self.IdExt_Update(Page=Page)
        self.IqExt_Update(Page=Page)
        self.SpdExt_Update(Page=Page)
        self.Pos_Update(Page=Page)

    def Poles_Update(self, Page):
        if Page == 1:
            Data = int(self.Poles_spinBox_1.text()) * 2
            self.Poles_Calculate_lineEdit_1.setText(str(Data))
        else:
            return

    def IdKp_Update(self, Page):
        if Page == 1:
            Data = int(self.IdKp_lineEdit_1.text())
            self.IdKp_Calculate_lineEdit_1.setText(str(Data))
        else:
            return

    def IdKi_Update(self, Page):
        if Page == 1:
            Data = int(self.IdKi_lineEdit_1.text())
            self.IdKi_Calculate_lineEdit_1.setText(str(Data))
        else:
            return

    def IqKp_Update(self, Page):
        if Page == 1:
            Data = int(self.IqKp_lineEdit_1.text())
            self.IqKp_Calculate_lineEdit_1.setText(str(Data))
        else:
            return

    def IqKi_Update(self, Page):
        if Page == 1:
            Data = int(self.IqKi_lineEdit_1.text())
            self.IqKi_Calculate_lineEdit_1.setText(str(Data))
        else:
            return

    def UdMax_Update(self, Page):
        if Page == 1:
            Data = int(self.UdMax_lineEdit_1.text())
            self.UdMax_Calculate_lineEdit_1.setText(str(Data) + 'V')
        else:
            return

    def UqMax_Update(self, Page):
        if Page == 1:
            Data = int(self.UqMax_lineEdit_1.text())
            self.UqMax_Calculate_lineEdit_1.setText(str(Data) + 'V')
        else:
            return

    def SpdKp_Update(self, Page):
        if Page == 1:
            Data = int(self.SpdKp_lineEdit_1.text())
            self.SpdKp_Calculate_lineEdit_1.setText(str(Data))
        else:
            return

    def SpdKi_Update(self, Page):
        if Page == 1:
            Data = int(self.SpdKi_lineEdit_1.text())
            self.SpdKi_Calculate_lineEdit_1.setText(str(Data))
        else:
            return

    def IqMax_Update(self, Page):
        if Page == 1:
            Data = int(self.IqMax_lineEdit_1.text())
            self.IqMax_Calculate_lineEdit_1.setText(str(Data) + 'A')
        else:
            return

    def PosKp_Update(self, Page):
        if Page == 1:
            Data = int(self.PosKp_lineEdit_1.text())
            self.PosKp_Calculate_lineEdit_1.setText(str(Data))
        else:
            return

    def PosKi_Update(self, Page):
        if Page == 1:
            Data = int(self.PosKi_lineEdit_1.text())
            self.PosKi_Calculate_lineEdit_1.setText(str(Data))
        else:
            return

    def SpdMax_Update(self, Page):
        if Page == 1:
            Data = int(self.SpdMax_lineEdit_1.text())
            self.SpdMax_Calculate_lineEdit_1.setText(str(Data) + 'rpm')
        else:
            return

    def UdExt_Update(self, Page):
        if Page == 1:
            Data = int(self.UdExt_lineEdit_1.text())
            self.UdExt_Calculate_lineEdit_1.setText(str(Data) + 'V')
        else:
            return

    def UqExt_Update(self, Page):
        if Page == 1:
            Data = int(self.UqExt_lineEdit_1.text())
            self.UqExt_Calculate_lineEdit_1.setText(str(Data) + 'V')
        else:
            return

    def IdExt_Update(self, Page):
        if Page == 1:
            Data = int(self.IdExt_lineEdit_1.text())
            self.IdExt_Calculate_lineEdit_1.setText(str(Data) + 'A')
        else:
            return

    def IqExt_Update(self, Page):
        if Page == 1:
            Data = int(self.IqExt_lineEdit_1.text())
            self.IqExt_Calculate_lineEdit_1.setText(str(Data) + 'A')
        else:
            return

    def SpdExt_Update(self, Page):
        if Page == 1:
            Data = int(self.SpdExt_lineEdit_1.text())
            self.SpdExt_Calculate_lineEdit_1.setText(str(Data) + 'rpm')
        else:
            return

    def Pos_Update(self, Page):
        if Page == 1:
            Data = int(self.Pos_lineEdit_1.text())
            self.Pos_Calculate_lineEdit_1.setText(str(Data))
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

    def Display_Close_Sub(self):
        self.UdExt_checkBox_1.setChecked(False)
        self.UqExt_checkBox_1.setChecked(False)
        self.IdExt_checkBox_1.setChecked(False)
        self.IqExt_checkBox_1.setChecked(False)
        self.SpdExt_checkBox_1.setChecked(False)
        self.Pos_checkBox_1.setChecked(False)
        self.Theta_checkBox_1.setChecked(False)
        self.SinCosTheta_checkBox_1.setChecked(False)
        self.Iabc_checkBox_1.setChecked(False)
        self.Uabc_checkBox_1.setChecked(False)
        self.Ixy_checkBox_1.setChecked(False)
        self.Uxy_checkBox_1.setChecked(False)
