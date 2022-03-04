import sys
import math

import pyqtgraph as pg
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from UI_Sub import UISub
from Tcp_Sub import Tcp_Module
from qt_material import apply_stylesheet


class CarWindow(UISub, Tcp_Module):
    def __init__(self):
        UISub.__init__(self)
        Tcp_Module.__init__(self)

        self.pw1 = None
        self.setupUi(self)
        self.addSlot()
        self.addGraph()

    def addGraph(self):
        self.pw1 = pg.PlotWidget()
        self.pw1.plot([0],)
        layout1 = QGridLayout()
        self.WaveDisplay_widget_1.setLayout(layout1)
        layout1.addWidget(self.pw1)

    def addSlot(self):
        # 通信页面

        # Uart通信方式选择按钮
        self.UartConnect_pushButton.clicked.connect(self.UartConnectSelect)
        # Uart端口查找按钮
        self.UartCheck_pushButton.clicked.connect(self.UartCheck)
        # Uart端口开关按钮
        self.UartEnable_pushButton.clicked.connect(self.UartEnable)

        # ETH通信方式选择按钮
        self.ETH_Connect_pushButton.clicked.connect(self.ETH_ConnectSelect)
        # Uart端口开关按钮
        self.ETH_Enable_pushButton.clicked.connect(self.ETH_Enable)

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
        self.Poles_spinBox_1.editingFinished.connect(lambda: self.Poles_Update(Page=1))
        # 实际IdKp参数显示
        self.IdKp_lineEdit_1.editingFinished.connect(lambda: self.IdKp_Update(Page=1))
        # 实际IdKi参数显示
        self.IdKi_lineEdit_1.editingFinished.connect(lambda: self.IdKi_Update(Page=1))
        # 实际IqKp参数显示
        self.IqKp_lineEdit_1.editingFinished.connect(lambda: self.IqKp_Update(Page=1))
        # 实际IqKi参数显示
        self.IqKi_lineEdit_1.editingFinished.connect(lambda: self.IqKi_Update(Page=1))
        # 实际UdMax参数显示
        self.UdMax_lineEdit_1.editingFinished.connect(lambda: self.UdMax_Update(Page=1))
        # 实际UqMax参数显示
        self.UqMax_lineEdit_1.editingFinished.connect(lambda: self.UqMax_Update(Page=1))
        # 实际SpdKp参数显示
        self.SpdKp_lineEdit_1.editingFinished.connect(lambda: self.SpdKp_Update(Page=1))
        # 实际SpdKi参数显示
        self.SpdKi_lineEdit_1.editingFinished.connect(lambda: self.SpdKi_Update(Page=1))
        # 实际IqMax参数显示
        self.IqMax_lineEdit_1.editingFinished.connect(lambda: self.IqMax_Update(Page=1))
        # 实际PosKp参数显示
        self.PosKp_lineEdit_1.editingFinished.connect(lambda: self.PosKp_Update(Page=1))
        # 实际PosKi参数显示
        self.PosKi_lineEdit_1.editingFinished.connect(lambda: self.PosKi_Update(Page=1))
        # 实际SpdMax参数显示
        self.SpdMax_lineEdit_1.editingFinished.connect(lambda: self.SpdMax_Update(Page=1))
        # 实际Ud参数显示
        self.UdExt_lineEdit_1.editingFinished.connect(lambda: self.UdExt_Update(Page=1))
        # 实际Uq参数显示
        self.UqExt_lineEdit_1.editingFinished.connect(lambda: self.UqExt_Update(Page=1))
        # 实际Id参数显示
        self.IdExt_lineEdit_1.editingFinished.connect(lambda: self.IdExt_Update(Page=1))
        # 实际Iq参数显示
        self.IqExt_lineEdit_1.editingFinished.connect(lambda: self.IqExt_Update(Page=1))
        # 实际Spd参数显示
        self.SpdExt_lineEdit_1.editingFinished.connect(lambda: self.SpdExt_Update(Page=1))
        # 实际Pos参数显示
        self.Pos_lineEdit_1.editingFinished.connect(lambda: self.Pos_Update(Page=1))
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

    def MotorEnable1(self):
        if self.MotorEnable_pushButton_1.isChecked():
            self.ParametersRead()
            Data = self.Enable
        else:
            Data = self.Disable
        self.UartWrite_int16(self.Enable_Addr[0], Data)

        if self.MotorEnable_pushButton_1.isChecked():
            self.MotorEnable_Enable_1()
        else:
            self.MotorEnable_Disable_1()

    def MotorEnable2(self):
        if self.MotorEnable_pushButton_2.isChecked():
            Data = self.Enable
        else:
            Data = self.Disable
        self.UartWrite_int16(self.Enable_Addr[1], Data)

    def MotorEnable3(self):
        if self.MotorEnable_pushButton_3.isChecked():
            Data = self.Enable
        else:
            Data = self.Disable
        self.UartWrite_int16(self.Enable_Addr[2], Data)

    def MotorEnable4(self):
        if self.MotorEnable_pushButton_4.isChecked():
            Data = self.Enable
        else:
            Data = self.Disable
        self.UartWrite_int16(self.Enable_Addr[3], Data)

    # 选择使用Uart通信
    def UartConnectSelect(self):
        if self.UartConnect_pushButton.isChecked():
            self.UartConnectSelect_Enable()
        else:
            self.UartConnectSelect_Disable()

    # 选择使用ETH通信
    def ETH_ConnectSelect(self):
        if self.ETH_Connect_pushButton.isChecked():
            self.ETH_ConnectSelect_Enable()
        else:
            self.ETH_ConnectSelect_Disable()

    # 选择使用ETH通信
    def ETH_Enable(self):
        if self.ETH_Enable_pushButton.isChecked():
            ipAddr = self.ETH_IPAddr_lineEdit.text()
            Port = int(self.ETH_Port_lineEdit.text())

            self.Tcp_Enable(ipAddr, Port)
        else:
            self.Tcp_Disable()

    def ParametersRead(self):
        if self.Motor_tabWidget.currentIndex() == 0:
            self.ParametersRead_Page1()
        else:
            return

    def ParametersWrite(self):
        if self.Motor_tabWidget.currentIndex() == 0:
            self.ParametersWrite_Page1()
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
    app = QApplication(sys.argv)
    window = CarWindow()

    apply_stylesheet(app, theme='light_red.xml')

    window.show()
    sys.exit(app.exec())
