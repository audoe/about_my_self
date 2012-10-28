#linux 基于ssh的证书登录(无需密码)


这两天本来想在宿舍做一下公司的事的，但是，配了半天的服务器，搞了一下ssh 证书登录的，看一下视频，时间就这样过去了，一行代码也没有写过。当然啦，在这两天里，因为在宿舍有了两台电脑，(一台公司的，一台自己的)，所以搞了一下ssh server的东西，实现了双向的证书登录。

###准备工作

- 在每一台计算机上装一个openssh-server

如果你是使用ubuntu,你可以使用一下的命令安装一个openssh-server

    sudo apt-get install openssh-server

- 修改/etc/ssh/sshd_config 文件

    AuthorizedKeysFile	%h/.ssh/authorized_keys #将这一行前面的注释去掉

- 添加证书

要添加证书，首先要你的客户机上使用以下的命令

    ssh-keygen
    ssk-copy-id -i 你的证书位置/id_rsa.pub 用户名@服务器IP

经过这三个步骤，一般来说你就可以直接登录到服务器上啦

特殊情况

如果你修改了服务器上/etc/ssh/sshd_config文件而有没有重启服务器上的ssh服务的话，请重启一下服务器上的使用
   
    sudo /ets/init.d/ssh restart

如果还不行？？？是不是客户端的私钥没有添加？？
在客户机上运行

    key-add ~/.ssh/id_rsa



###重新对HG有了一个新的认识

hg:版本管理工具

可以与坚果云等网络同步工具进行代码的网络同步。




    
