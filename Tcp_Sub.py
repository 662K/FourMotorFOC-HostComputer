import socket
import _thread
import time


def Bytetoint16(DataL, DataH):
    Data = DataH << 8 | DataL
    if Data >= 32768:
        Data = Data - 65536
    else:
        Data = Data
    return Data


def Bytetouint16(DataL, DataH):
    Data = DataH << 8 | DataL
    return Data


def Bytetoint32(DataHL, DataHH, DataLL, DataLH):
    Data = DataHH << 24 | DataHL << 16 | DataLH << 8 | DataLL
    if Data >= 2147483648:
        Data = Data - 4294967296
    else:
        Data = Data
    return Data


class Tcp_Module:
    None_Display_Flag = 0
    UdExt_Display_Flag = 1
    UqExt_Display_Flag = 2
    IdExt_Display_Flag = 3
    IqExt_Display_Flag = 4
    SpdExt_Display_Flag = 5
    Pos_Display_Flag = 6
    Theta_Display_Flag = 7
    SinCosTheta_Display_Flag = 8
    Iabc_Display_Flag = 9
    Uabc_Display_Flag = 10
    Ixy_Display_Flag = 11
    Uxy_Display_Flag = 12

    Save_Num = 1000

    def __init__(self):
        super(Tcp_Module, self).__init__()
        self.tcp_socket = None
        self.Tcp_recv_Enable = False
        self.recv_data = None

        self.Tcp_Signal1 = []
        self.Tcp_Signal2 = []
        self.Tcp_Signal3 = []
        self.Tcp_Signal4 = []

        self.Display_Flag = self.None_Display_Flag

        try:
            _thread.start_new_thread(self.Tcp_recv, ())
        except:
            print("Error: 无法启动线程")

    def Tcp_Enable(self, ipAddr, Port):
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_addr = (ipAddr, Port)
        self.tcp_socket.connect(server_addr)
        self.Tcp_recv_Enable = True

    def Tcp_Disable(self):
        self.tcp_socket.close()
        self.Tcp_recv_Enable = False

    def Tcp_Signal_Clear(self):
        self.Tcp_Signal1.clear()
        self.Tcp_Signal2.clear()
        self.Tcp_Signal3.clear()
        self.Tcp_Signal4.clear()

    def Tcp_recv(self):
        while True:
            if self.Tcp_recv_Enable:
                try:
                    self.recv_data = self.tcp_socket.recv(160)

                    if self.Display_Flag == self.UdExt_Display_Flag:
                        for cnt in range(20):
                            self.Tcp_Signal1.append(
                                Bytetoint16(self.recv_data[cnt * 8 + 0], self.recv_data[cnt * 8 + 1]))
                            self.Tcp_Signal2.append(
                                Bytetoint16(self.recv_data[cnt * 8 + 2], self.recv_data[cnt * 8 + 3]))
                            if len(self.Tcp_Signal1) > self.Save_Num:
                                del self.Tcp_Signal1[0]
                            if len(self.Tcp_Signal2) > self.Save_Num:
                                del self.Tcp_Signal2[0]
                    elif self.Display_Flag == self.UqExt_Display_Flag:
                        for cnt in range(20):
                            self.Tcp_Signal1.append(
                                Bytetoint16(self.recv_data[cnt * 8 + 0], self.recv_data[cnt * 8 + 1]))
                            self.Tcp_Signal2.append(
                                Bytetoint16(self.recv_data[cnt * 8 + 2], self.recv_data[cnt * 8 + 3]))
                            if len(self.Tcp_Signal1) > self.Save_Num:
                                del self.Tcp_Signal1[0]
                            if len(self.Tcp_Signal2) > self.Save_Num:
                                del self.Tcp_Signal2[0]
                    elif self.Display_Flag == self.IdExt_Display_Flag:
                        for cnt in range(20):
                            self.Tcp_Signal1.append(
                                Bytetoint16(self.recv_data[cnt * 8 + 0], self.recv_data[cnt * 8 + 1]))
                            self.Tcp_Signal2.append(
                                Bytetoint16(self.recv_data[cnt * 8 + 2], self.recv_data[cnt * 8 + 3]))
                            self.Tcp_Signal3.append(
                                Bytetoint16(self.recv_data[cnt * 8 + 4], self.recv_data[cnt * 8 + 5]))
                            if len(self.Tcp_Signal1) > self.Save_Num:
                                del self.Tcp_Signal1[0]
                            if len(self.Tcp_Signal2) > self.Save_Num:
                                del self.Tcp_Signal2[0]
                            if len(self.Tcp_Signal3) > self.Save_Num:
                                del self.Tcp_Signal3[0]
                    elif self.Display_Flag == self.IqExt_Display_Flag:
                        for cnt in range(20):
                            self.Tcp_Signal1.append(
                                Bytetoint16(self.recv_data[cnt * 8 + 0], self.recv_data[cnt * 8 + 1]))
                            self.Tcp_Signal2.append(
                                Bytetoint16(self.recv_data[cnt * 8 + 2], self.recv_data[cnt * 8 + 3]))
                            self.Tcp_Signal3.append(
                                Bytetoint16(self.recv_data[cnt * 8 + 4], self.recv_data[cnt * 8 + 5]))
                            if len(self.Tcp_Signal1) > self.Save_Num:
                                del self.Tcp_Signal1[0]
                            if len(self.Tcp_Signal2) > self.Save_Num:
                                del self.Tcp_Signal2[0]
                            if len(self.Tcp_Signal3) > self.Save_Num:
                                del self.Tcp_Signal3[0]
                    elif self.Display_Flag == self.SpdExt_Display_Flag:
                        for cnt in range(20):
                            self.Tcp_Signal1.append(
                                Bytetoint16(self.recv_data[cnt * 8 + 0], self.recv_data[cnt * 8 + 1]))
                            self.Tcp_Signal2.append(
                                Bytetoint16(self.recv_data[cnt * 8 + 2], self.recv_data[cnt * 8 + 3]))
                            self.Tcp_Signal3.append(
                                Bytetoint16(self.recv_data[cnt * 8 + 4], self.recv_data[cnt * 8 + 5]))
                            self.Tcp_Signal4.append(
                                Bytetoint16(self.recv_data[cnt * 8 + 6], self.recv_data[cnt * 8 + 7]))
                            if len(self.Tcp_Signal1) > self.Save_Num:
                                del self.Tcp_Signal1[0]
                            if len(self.Tcp_Signal2) > self.Save_Num:
                                del self.Tcp_Signal2[0]
                            if len(self.Tcp_Signal3) > self.Save_Num:
                                del self.Tcp_Signal3[0]
                            if len(self.Tcp_Signal4) > self.Save_Num:
                                del self.Tcp_Signal4[0]
                    elif self.Display_Flag == self.Pos_Display_Flag:
                        for cnt in range(20):
                            self.Tcp_Signal1.append(
                                Bytetoint32(self.recv_data[cnt * 8 + 0], self.recv_data[cnt * 8 + 1],
                                            self.recv_data[cnt * 8 + 2], self.recv_data[cnt * 8 + 3]))
                            self.Tcp_Signal2.append(
                                Bytetoint32(self.recv_data[cnt * 8 + 4], self.recv_data[cnt * 8 + 5],
                                            self.recv_data[cnt * 8 + 6], self.recv_data[cnt * 8 + 7]))
                            if len(self.Tcp_Signal1) > self.Save_Num:
                                del self.Tcp_Signal1[0]
                            if len(self.Tcp_Signal2) > self.Save_Num:
                                del self.Tcp_Signal2[0]
                    elif self.Display_Flag == self.Theta_Display_Flag:
                        for cnt in range(20):
                            self.Tcp_Signal1.append(Bytetouint16(self.recv_data[cnt * 8 + 0], self.recv_data[cnt * 8 + 1]))
                            self.Tcp_Signal2.append(Bytetouint16(self.recv_data[cnt * 8 + 2], self.recv_data[cnt * 8 + 3]))
                            if len(self.Tcp_Signal1) > self.Save_Num:
                                del self.Tcp_Signal1[0]
                            if len(self.Tcp_Signal2) > self.Save_Num:
                                del self.Tcp_Signal2[0]
                    elif self.Display_Flag == self.SinCosTheta_Display_Flag:
                        for cnt in range(20):
                            self.Tcp_Signal1.append(
                                Bytetoint16(self.recv_data[cnt * 8 + 0], self.recv_data[cnt * 8 + 1]))
                            self.Tcp_Signal2.append(
                                Bytetoint16(self.recv_data[cnt * 8 + 2], self.recv_data[cnt * 8 + 3]))
                            if len(self.Tcp_Signal1) > self.Save_Num:
                                del self.Tcp_Signal1[0]
                            if len(self.Tcp_Signal2) > self.Save_Num:
                                del self.Tcp_Signal2[0]
                    elif self.Display_Flag == self.Iabc_Display_Flag:
                        for cnt in range(20):
                            self.Tcp_Signal1.append(
                                Bytetoint16(self.recv_data[cnt * 8 + 0], self.recv_data[cnt * 8 + 1]))
                            self.Tcp_Signal2.append(
                                Bytetoint16(self.recv_data[cnt * 8 + 2], self.recv_data[cnt * 8 + 3]))
                            if len(self.Tcp_Signal1) > self.Save_Num:
                                del self.Tcp_Signal1[0]
                            if len(self.Tcp_Signal2) > self.Save_Num:
                                del self.Tcp_Signal2[0]
                    elif self.Display_Flag == self.Uabc_Display_Flag:
                        for cnt in range(20):
                            self.Tcp_Signal1.append(
                                Bytetoint16(self.recv_data[cnt * 8 + 0], self.recv_data[cnt * 8 + 1]))
                            self.Tcp_Signal2.append(
                                Bytetoint16(self.recv_data[cnt * 8 + 2], self.recv_data[cnt * 8 + 3]))
                            self.Tcp_Signal3.append(
                                Bytetoint16(self.recv_data[cnt * 8 + 4], self.recv_data[cnt * 8 + 5]))
                            if len(self.Tcp_Signal1) > self.Save_Num:
                                del self.Tcp_Signal1[0]
                            if len(self.Tcp_Signal2) > self.Save_Num:
                                del self.Tcp_Signal2[0]
                            if len(self.Tcp_Signal3) > self.Save_Num:
                                del self.Tcp_Signal3[0]
                    elif self.Display_Flag == self.Ixy_Display_Flag:
                        for cnt in range(20):
                            self.Tcp_Signal1.append(
                                Bytetoint16(self.recv_data[cnt * 8 + 0], self.recv_data[cnt * 8 + 1]))
                            self.Tcp_Signal2.append(
                                Bytetoint16(self.recv_data[cnt * 8 + 2], self.recv_data[cnt * 8 + 3]))
                            if len(self.Tcp_Signal1) > self.Save_Num:
                                del self.Tcp_Signal1[0]
                            if len(self.Tcp_Signal2) > self.Save_Num:
                                del self.Tcp_Signal2[0]
                    elif self.Display_Flag == self.Uxy_Display_Flag:
                        for cnt in range(20):
                            self.Tcp_Signal1.append(
                                Bytetoint16(self.recv_data[cnt * 8 + 0], self.recv_data[cnt * 8 + 1]))
                            self.Tcp_Signal2.append(
                                Bytetoint16(self.recv_data[cnt * 8 + 2], self.recv_data[cnt * 8 + 3]))
                            if len(self.Tcp_Signal1) > self.Save_Num:
                                del self.Tcp_Signal1[0]
                            if len(self.Tcp_Signal2) > self.Save_Num:
                                del self.Tcp_Signal2[0]

                except socket.error:
                    print('Tcp连接断开')
            else:
                pass

            time.sleep(0.005)
