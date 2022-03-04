import sys
import math
import _thread
import time

import pyqtgraph as pg
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from UI_Sub import UISub
from Tcp_Sub import Tcp_Module
from qt_material import apply_stylesheet
from PyQt5.QtSerialPort import QSerialPort


class CarWindow(UISub, Tcp_Module):
    def __init__(self):
        UISub.__init__(self)
        Tcp_Module.__init__(self)

        self.pw1 = None
        self.Signal1_Print = None
        self.Signal2_Print = None
        self.Signal3_Print = None
        self.setupUi(self)
        self.addSlot()
        self.addGraph()
        self.timer1 = QTimer()  # 实例化一个计时器
        self.timer1.timeout.connect(self.graphPrint)  # 计时器信号连接到update()函数
        self.timer1.start(33)  # 计时器间隔200毫秒

    def graphPrint(self):
        if self.Display_Flag == self.UdExt_Display_Flag:
            self.Signal1_Print.setData(self.Tcp_Signal1)
            self.Signal2_Print.setData(self.Tcp_Signal2)
        elif self.Display_Flag == self.UqExt_Display_Flag:
            self.Signal1_Print.setData(self.Tcp_Signal1)
            self.Signal2_Print.setData(self.Tcp_Signal2)
        elif self.Display_Flag == self.IdExt_Display_Flag:
            self.Signal1_Print.setData(self.Tcp_Signal1)
            self.Signal2_Print.setData(self.Tcp_Signal2)
            self.Signal3_Print.setData(self.Tcp_Signal3)
        elif self.Display_Flag == self.IqExt_Display_Flag:
            self.Signal1_Print.setData(self.Tcp_Signal1)
            self.Signal2_Print.setData(self.Tcp_Signal2)
            self.Signal3_Print.setData(self.Tcp_Signal3)
        elif self.Display_Flag == self.SpdExt_Display_Flag:
            self.Signal1_Print.setData(self.Tcp_Signal1)
            self.Signal2_Print.setData(self.Tcp_Signal2)
            self.Signal3_Print.setData(self.Tcp_Signal3)
        elif self.Display_Flag == self.Pos_Display_Flag:
            self.Signal1_Print.setData(self.Tcp_Signal1)
            self.Signal2_Print.setData(self.Tcp_Signal2)
        elif self.Display_Flag == self.Theta_Display_Flag:
            self.Signal1_Print.setData(self.Tcp_Signal1)
            self.Signal2_Print.setData(self.Tcp_Signal2)
        elif self.Display_Flag == self.SinCosTheta_Display_Flag:
            self.Signal1_Print.setData(self.Tcp_Signal1)
            self.Signal2_Print.setData(self.Tcp_Signal2)
        elif self.Display_Flag == self.Iabc_Display_Flag:
            self.Signal1_Print.setData(self.Tcp_Signal1)
            self.Signal2_Print.setData(self.Tcp_Signal2)
        elif self.Display_Flag == self.Uabc_Display_Flag:
            self.Signal1_Print.setData(self.Tcp_Signal1)
            self.Signal2_Print.setData(self.Tcp_Signal2)
            self.Signal3_Print.setData(self.Tcp_Signal3)
        elif self.Display_Flag == self.Ixy_Display_Flag:
            self.Signal1_Print.setData(self.Tcp_Signal1)
            self.Signal2_Print.setData(self.Tcp_Signal2)
        elif self.Display_Flag == self.Uxy_Display_Flag:
            self.Signal1_Print.setData(self.Tcp_Signal1)
            self.Signal2_Print.setData(self.Tcp_Signal2)

    def addGraph(self):
        self.pw1 = pg.PlotWidget()
        self.pw1.setBackground('w')
        self.pw1.showGrid(x=True, y=True)
        self.pw1.addLegend()
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

        # 通信显示
        self.UdExt_checkBox_1.clicked.connect(self.UdExt_Display)
        self.UqExt_checkBox_1.clicked.connect(self.UqExt_Display)
        self.IdExt_checkBox_1.clicked.connect(self.IdExt_Display)
        self.IqExt_checkBox_1.clicked.connect(self.IqExt_Display)
        self.SpdExt_checkBox_1.clicked.connect(self.SpdExt_Display)
        self.Pos_checkBox_1.clicked.connect(self.Pos_Display)

        self.Theta_checkBox_1.clicked.connect(self.Theta_Display)
        self.SinCosTheta_checkBox_1.clicked.connect(self.SinCosTheta_Display)
        self.Iabc_checkBox_1.clicked.connect(self.Iabc_Display)
        self.Uabc_checkBox_1.clicked.connect(self.Uabc_Display)
        self.Ixy_checkBox_1.clicked.connect(self.Ixy_Display)
        self.Uxy_checkBox_1.clicked.connect(self.Uxy_Display)

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
            self.UartCheck_pushButton.setEnabled(False)
            self.UartSelect_comboBox.setEnabled(False)
            self.UartBaudSelect_comboBox.setEnabled(False)
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

            self.UdExt_checkBox_1.setEnabled(True)
            self.UqExt_checkBox_1.setEnabled(True)
            self.IdExt_checkBox_1.setEnabled(True)
            self.IqExt_checkBox_1.setEnabled(True)
            self.SpdExt_checkBox_1.setEnabled(True)
            self.Pos_checkBox_1.setEnabled(True)

            self.Theta_checkBox_1.setEnabled(True)
            self.SinCosTheta_checkBox_1.setEnabled(True)
            self.Iabc_checkBox_1.setEnabled(True)
            self.Uabc_checkBox_1.setEnabled(True)
            self.Ixy_checkBox_1.setEnabled(True)
            self.Uxy_checkBox_1.setEnabled(True)

            self.Display_Flag = self.UartRead_int16(self.Display_Addr[0])
            if self.Display_Flag == self.UdExt_Display_Flag:
                self.Display_Close_Sub()
                self.UdExt_checkBox_1.setChecked(True)
            elif self.Display_Flag == self.UqExt_Display_Flag:
                self.Display_Close_Sub()
                self.UqExt_checkBox_1.setChecked(True)
            elif self.Display_Flag == self.IdExt_Display_Flag:
                self.Display_Close_Sub()
                self.IdExt_checkBox_1.setChecked(True)
            elif self.Display_Flag == self.IqExt_Display_Flag:
                self.Display_Close_Sub()
                self.IqExt_checkBox_1.setChecked(True)
            elif self.Display_Flag == self.SpdExt_Display_Flag:
                self.Display_Close_Sub()
                self.SpdExt_checkBox_1.setChecked(True)
            elif self.Display_Flag == self.Pos_Display_Flag:
                self.Display_Close_Sub()
                self.Pos_checkBox_1.setChecked(True)
            elif self.Display_Flag == self.Theta_Display_Flag:
                self.Display_Close_Sub()
                self.Theta_checkBox_1.setChecked(True)
            elif self.Display_Flag == self.SinCosTheta_Display_Flag:
                self.Display_Close_Sub()
                self.SinCosTheta_checkBox_1.setChecked(True)
            elif self.Display_Flag == self.Iabc_Display_Flag:
                self.Display_Close_Sub()
                self.Iabc_checkBox_1.setChecked(True)
            elif self.Display_Flag == self.Uabc_Display_Flag:
                self.Display_Close_Sub()
                self.Uabc_checkBox_1.setChecked(True)
            elif self.Display_Flag == self.Ixy_Display_Flag:
                self.Display_Close_Sub()
                self.Ixy_checkBox_1.setChecked(True)
            elif self.Display_Flag == self.Uxy_Display_Flag:
                self.Display_Close_Sub()
                self.Uxy_checkBox_1.setChecked(True)

            # 电机1 使能读取
            self.ParametersRead_Page1()
            Data = self.UartRead_int16(self.Enable_Addr[0])
            if Data == self.Enable:
                self.MotorEnable_pushButton_1.setChecked(True)
                self.MotorEnable_Enable_1()
            elif Data == self.Disable:
                self.MotorEnable_pushButton_1.setChecked(False)
                self.MotorEnable_Disable_1()

            # 电机2 使能读取
            Data = self.UartRead_int16(self.Enable_Addr[1])
            if Data == self.Enable:
                self.MotorEnable_pushButton_2.setChecked(True)
            elif Data == self.Disable:
                self.MotorEnable_pushButton_2.setChecked(False)

            # 电机3 使能读取
            Data = self.UartRead_int16(self.Enable_Addr[2])
            if Data == self.Enable:
                self.MotorEnable_pushButton_3.setChecked(True)
            elif Data == self.Disable:
                self.MotorEnable_pushButton_3.setChecked(False)

            # 电机4 使能读取
            Data = self.UartRead_int16(self.Enable_Addr[3])
            if Data == self.Enable:
                self.MotorEnable_pushButton_4.setChecked(True)
            elif Data == self.Disable:
                self.MotorEnable_pushButton_4.setChecked(False)
        else:
            self.Uart.close()
            self.UartCheck_pushButton.setEnabled(True)
            self.UartSelect_comboBox.setEnabled(True)
            self.UartBaudSelect_comboBox.setEnabled(True)
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

            self.UdExt_checkBox_1.setEnabled(False)
            self.UqExt_checkBox_1.setEnabled(False)
            self.IdExt_checkBox_1.setEnabled(False)
            self.IqExt_checkBox_1.setEnabled(False)
            self.SpdExt_checkBox_1.setEnabled(False)
            self.Pos_checkBox_1.setEnabled(False)

            self.Theta_checkBox_1.setEnabled(False)
            self.SinCosTheta_checkBox_1.setEnabled(False)
            self.Iabc_checkBox_1.setEnabled(False)
            self.Uabc_checkBox_1.setEnabled(False)
            self.Ixy_checkBox_1.setEnabled(False)
            self.Uxy_checkBox_1.setEnabled(False)

    def UdExt_Display(self):
        if self.UdExt_checkBox_1.isChecked():
            self.Display_Close_Sub()
            self.UartWrite_int16(self.Display_Addr[0], self.UdExt_Display_Flag)
            self.UdExt_checkBox_1.setChecked(True)
            self.Display_Flag = self.UdExt_Display_Flag

            self.Signal1_Print = self.pw1.plot([0], pen=pg.mkPen('r'), name='TargetUd', clear=True)
            self.Signal2_Print = self.pw1.plot([0], pen=pg.mkPen('g'), name='Ud_Ext')
        else:
            self.Display_Close_Sub()
            self.UartWrite_int16(self.Display_Addr[0], self.None_Display_Flag)
            self.Display_Flag = self.None_Display_Flag
            self.pw1.plot(clear=True)

        self.Tcp_Signal1.clear()
        self.Tcp_Signal2.clear()
        self.Tcp_Signal3.clear()

    def UqExt_Display(self):
        if self.UqExt_checkBox_1.isChecked():
            self.Display_Close_Sub()
            self.UartWrite_int16(self.Display_Addr[0], self.UqExt_Display_Flag)
            self.UqExt_checkBox_1.setChecked(True)
            self.Display_Flag = self.UqExt_Display_Flag

            self.Signal1_Print = self.pw1.plot([0], pen=pg.mkPen('r'), name='TargetUq', clear=True)
            self.Signal2_Print = self.pw1.plot([0], pen=pg.mkPen('g'), name='Uq_Ext')
        else:
            self.Display_Close_Sub()
            self.UartWrite_int16(self.Display_Addr[0], self.None_Display_Flag)
            self.Display_Flag = self.None_Display_Flag
            self.pw1.plot(clear=True)

        self.Tcp_Signal1.clear()
        self.Tcp_Signal2.clear()
        self.Tcp_Signal3.clear()

    def IdExt_Display(self):
        if self.IdExt_checkBox_1.isChecked():
            self.Display_Close_Sub()
            self.UartWrite_int16(self.Display_Addr[0], self.IdExt_Display_Flag)
            self.IdExt_checkBox_1.setChecked(True)
            self.Display_Flag = self.IdExt_Display_Flag

            self.Signal1_Print = self.pw1.plot([0], pen=pg.mkPen('r'), name='PresentId', clear=True)
            self.Signal2_Print = self.pw1.plot([0], pen=pg.mkPen('g'), name='TargetId')
            self.Signal3_Print = self.pw1.plot([0], pen=pg.mkPen('b'), name='Id_Ext')
        else:
            self.Display_Close_Sub()
            self.UartWrite_int16(self.Display_Addr[0], self.None_Display_Flag)
            self.Display_Flag = self.None_Display_Flag
            self.pw1.plot(clear=True)

        self.Tcp_Signal1.clear()
        self.Tcp_Signal2.clear()
        self.Tcp_Signal3.clear()

    def IqExt_Display(self):
        if self.IqExt_checkBox_1.isChecked():
            self.Display_Close_Sub()
            self.UartWrite_int16(self.Display_Addr[0], self.IqExt_Display_Flag)
            self.IqExt_checkBox_1.setChecked(True)
            self.Display_Flag = self.IqExt_Display_Flag

            self.Signal1_Print = self.pw1.plot([0], pen=pg.mkPen('r'), name='PresentIq', clear=True)
            self.Signal2_Print = self.pw1.plot([0], pen=pg.mkPen('g'), name='TargetIq')
            self.Signal3_Print = self.pw1.plot([0], pen=pg.mkPen('b'), name='Iq_Ext')
        else:
            self.Display_Close_Sub()
            self.UartWrite_int16(self.Display_Addr[0], self.None_Display_Flag)
            self.Display_Flag = self.None_Display_Flag
            self.pw1.plot(clear=True)

        self.Tcp_Signal1.clear()
        self.Tcp_Signal2.clear()
        self.Tcp_Signal3.clear()

    def SpdExt_Display(self):
        if self.SpdExt_checkBox_1.isChecked():
            self.Display_Close_Sub()
            self.UartWrite_int16(self.Display_Addr[0], self.SpdExt_Display_Flag)
            self.SpdExt_checkBox_1.setChecked(True)
            self.Display_Flag = self.SpdExt_Display_Flag

            self.Signal1_Print = self.pw1.plot([0], pen=pg.mkPen('r'), name='PresentSpd', clear=True)
            self.Signal2_Print = self.pw1.plot([0], pen=pg.mkPen('g'), name='TargetSpd')
            self.Signal3_Print = self.pw1.plot([0], pen=pg.mkPen('b'), name='Spd_Ext')
        else:
            self.Display_Close_Sub()
            self.UartWrite_int16(self.Display_Addr[0], self.None_Display_Flag)
            self.Display_Flag = self.None_Display_Flag
            self.pw1.plot(clear=True)

        self.Tcp_Signal1.clear()
        self.Tcp_Signal2.clear()
        self.Tcp_Signal3.clear()

    def Pos_Display(self):
        if self.Pos_checkBox_1.isChecked():
            self.Display_Close_Sub()
            self.UartWrite_int16(self.Display_Addr[0], self.Pos_Display_Flag)
            self.Pos_checkBox_1.setChecked(True)
            self.Display_Flag = self.Pos_Display_Flag

            self.Signal1_Print = self.pw1.plot([0], pen=pg.mkPen('r'), name='PresentPos', clear=True)
            self.Signal2_Print = self.pw1.plot([0], pen=pg.mkPen('g'), name='TargetPos')
        else:
            self.Display_Close_Sub()
            self.UartWrite_int16(self.Display_Addr[0], self.None_Display_Flag)
            self.Display_Flag = self.None_Display_Flag
            self.pw1.plot(clear=True)

        self.Tcp_Signal1.clear()
        self.Tcp_Signal2.clear()
        self.Tcp_Signal3.clear()

    def Theta_Display(self):
        if self.Theta_checkBox_1.isChecked():
            self.Display_Close_Sub()
            self.UartWrite_int16(self.Display_Addr[0], self.Theta_Display_Flag)
            self.Theta_checkBox_1.setChecked(True)
            self.Display_Flag = self.Theta_Display_Flag

            self.Signal1_Print = self.pw1.plot([0], pen=pg.mkPen('r'), name='Theta', clear=True)
            self.Signal2_Print = self.pw1.plot([0], pen=pg.mkPen('g'), name='ThetaE')
        else:
            self.Display_Close_Sub()
            self.UartWrite_int16(self.Display_Addr[0], self.None_Display_Flag)
            self.Display_Flag = self.None_Display_Flag
            self.pw1.plot(clear=True)

        self.Tcp_Signal1.clear()
        self.Tcp_Signal2.clear()
        self.Tcp_Signal3.clear()

    def SinCosTheta_Display(self):
        if self.SinCosTheta_checkBox_1.isChecked():
            self.Display_Close_Sub()
            self.UartWrite_int16(self.Display_Addr[0], self.SinCosTheta_Display_Flag)
            self.SinCosTheta_checkBox_1.setChecked(True)
            self.Display_Flag = self.SinCosTheta_Display_Flag

            self.Signal1_Print = self.pw1.plot([0], pen=pg.mkPen('r'), name='Sinθ', clear=True)
            self.Signal2_Print = self.pw1.plot([0], pen=pg.mkPen('g'), name='Cosθ')
        else:
            self.Display_Close_Sub()
            self.UartWrite_int16(self.Display_Addr[0], self.None_Display_Flag)
            self.Display_Flag = self.None_Display_Flag
            self.pw1.plot(clear=True)

        self.Tcp_Signal1.clear()
        self.Tcp_Signal2.clear()
        self.Tcp_Signal3.clear()

    def Iabc_Display(self):
        if self.Iabc_checkBox_1.isChecked():
            self.Display_Close_Sub()
            self.UartWrite_int16(self.Display_Addr[0], self.Iabc_Display_Flag)
            self.Iabc_checkBox_1.setChecked(True)
            self.Display_Flag = self.Iabc_Display_Flag

            self.Signal1_Print = self.pw1.plot([0], pen=pg.mkPen('r'), name='Ia', clear=True)
            self.Signal2_Print = self.pw1.plot([0], pen=pg.mkPen('g'), name='Ic')
        else:
            self.Display_Close_Sub()
            self.UartWrite_int16(self.Display_Addr[0], self.None_Display_Flag)
            self.Display_Flag = self.None_Display_Flag
            self.pw1.plot(clear=True)

        self.Tcp_Signal1.clear()
        self.Tcp_Signal2.clear()
        self.Tcp_Signal3.clear()

    def Uabc_Display(self):
        if self.Uabc_checkBox_1.isChecked():
            self.Display_Close_Sub()
            self.UartWrite_int16(self.Display_Addr[0], self.Uabc_Display_Flag)
            self.Uabc_checkBox_1.setChecked(True)
            self.Display_Flag = self.Uabc_Display_Flag

            self.Signal1_Print = self.pw1.plot([0], pen=pg.mkPen('r'), name='Ua', clear=True)
            self.Signal2_Print = self.pw1.plot([0], pen=pg.mkPen('g'), name='Ub')
            self.Signal3_Print = self.pw1.plot([0], pen=pg.mkPen('b'), name='Uc')
        else:
            self.Display_Close_Sub()
            self.UartWrite_int16(self.Display_Addr[0], self.None_Display_Flag)
            self.Display_Flag = self.None_Display_Flag
            self.pw1.plot(clear=True)

        self.Tcp_Signal1.clear()
        self.Tcp_Signal2.clear()
        self.Tcp_Signal3.clear()

    def Ixy_Display(self):
        if self.Ixy_checkBox_1.isChecked():
            self.Display_Close_Sub()
            self.UartWrite_int16(self.Display_Addr[0], self.Ixy_Display_Flag)
            self.Ixy_checkBox_1.setChecked(True)
            self.Display_Flag = self.Ixy_Display_Flag

            self.Signal1_Print = self.pw1.plot([0], pen=pg.mkPen('r'), name='Iα', clear=True)
            self.Signal2_Print = self.pw1.plot([0], pen=pg.mkPen('g'), name='Iβ')
        else:
            self.Display_Close_Sub()
            self.UartWrite_int16(self.Display_Addr[0], self.None_Display_Flag)
            self.Display_Flag = self.None_Display_Flag
            self.pw1.plot(clear=True)

        self.Tcp_Signal1.clear()
        self.Tcp_Signal2.clear()
        self.Tcp_Signal3.clear()

    def Uxy_Display(self):
        if self.Uxy_checkBox_1.isChecked():
            self.Display_Close_Sub()
            self.UartWrite_int16(self.Display_Addr[0], self.Uxy_Display_Flag)
            self.Uxy_checkBox_1.setChecked(True)
            self.Display_Flag = self.Uxy_Display_Flag

            self.Signal1_Print = self.pw1.plot([0], pen=pg.mkPen('r'), name='Uα', clear=True)
            self.Signal2_Print = self.pw1.plot([0], pen=pg.mkPen('g'), name='Uβ')
        else:
            self.Display_Close_Sub()
            self.UartWrite_int16(self.Display_Addr[0], self.None_Display_Flag)
            self.Display_Flag = self.None_Display_Flag
            self.pw1.plot(clear=True)

        self.Tcp_Signal1.clear()
        self.Tcp_Signal2.clear()
        self.Tcp_Signal3.clear()

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
