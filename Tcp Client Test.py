import socket
import time

if __name__ == "__main__":
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.settimeout(1)
    server_addr = ('192.168.1.30', 8088)
    try:
        tcp_socket.connect(server_addr)
    except:
        print('链接超时')

    while True:
        try:
            recv_data = tcp_socket.recv(1024)  # 接收1024个字节
            num = len(recv_data)
            for i in range(num):
                print(recv_data[i])
        except socket.timeout:
            print('连接超时')
        except socket.error:
            print('error')
        except:
            print('其他错误')

        time.sleep(0.02)
