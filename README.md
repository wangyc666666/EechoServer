# 1、安装依赖包
# pip3.4 install requirement.text
# 2、创建配置文件目录
# mkdir /etc/EchoServer/
# 3、自动生成配置文件 自动生成后可根据需要手动对配置文件进行修改
# /usr/local/python34/bin/oslo-config-generator --namespace EchoServerCfg >/etc/EchoServer/EchoServer.conf
# 4、部署程序
# cd /home/EchoServer/
# python3 setup.py install
# 5、启动服务端(python3.4 安装目录/usr/local/python34/)
# （1）服务端入口
# /usr/local/python34/bin/EchoServer
# 服务端日志文件cat /var/log/EchoServer/EchoServer.log
# （2）客户端命令行入口
# /usr/local/python34/bin/server
# （3）客户端入口
# /usr/local/python34/bin/client -u


环境机器 192.168.231.140 账号root 密码json@123 可登入查看


# 参考文献:https://python3-cookbook.readthedocs.io/zh_CN/latest/c11/p02_creating_tcp_server.html