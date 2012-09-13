#web 服务器
web server


Where it helps to make things concrete, our examples use the Apache web server and
its configuration options.

web 服务器一天生产出数十亿网页。它们有的告诉你明天的天气、有的加载你的网上购物车，又或者帮你找回你那失散多年的高中的哥们。web服务器就是那万维网(www)的一个个驮马。在这一章中，我们会学到一下的东西：

Web servers dish out billions of web pages a day. They tell you the weather, load up
your online shopping carts, and let you find long-lost high-school buddies. Web
servers are the workhorses of the World Wide Web. In this chapter, we:

- 检查多种的web服务器软硬件
  Survey the many different types of software and hardware web servers.
- 怎样用perl写一个简单的诊断服务器软件
  Describe how to write a simple diagnostic web server in Perl.
- 说明web server是如何一步一步的进行网络的通讯的
  Explain how web servers process HTTP transactions, step by step.

为了更好的学以之用，我们的所有软件和配置都会在apache上实现

Where it helps to make things concrete, our examples use the Apache web server and
its configuration options.

###web 服务器的千其百怪
Web Servers Come in All Shapes and Sizes

一个服务器进程接受一个http请求并产生一个服务器的应答给请求的用户。"web server" 这个术语可以是指一个服务器软件或者一个产生一些网页的实际的设备或电脑。

A web server processes HTTP requests and serves responses. The term “web server”
can refer either to web server software or to the particular device or computer dedi-
cated to serving the web pages.

web servers 有各种不同的形态、大小、口味。它们可能是区区10行的Perl脚本、50MB的安全的商业引擎 [google]、或者一个刀片服务器。
但是不管它是什么样的表现形式。所有的web servers都会接收一个HTTP的请求，经过处理产生一个content返回给终端。(回到章节1-5看到更多)

Web servers comes in all flavors, shapes, and sizes. There are trivial 10-line Perl
script web servers, 50-MB secure commerce engines, and tiny servers-on-a-card. But
whatever the functional differences, all web servers receive HTTP requests for
resources and serve content back to the clients (look back to Figure 1-5).

###web 服务器的实现
Web Server Implementations

web server实现 HTTP 和处理有关TCP连接。它们同时管理web server提供的资源和对configure、control、enhance the web server 提供管理功能

Web servers implement HTTP and the related TCP connection handling. They also
manage the resources served by the web server and provide administrative features to
configure, control, and enhance the web server.



The web server logic implements the HTTP protocol, manages web resources, and
provides web server administrative capabilities. The web server logic shares responsi-
bilities for managing TCP connections with the operating system. The underlying
109
operating system manages the hardware details of the underlying computer system
and provides TCP/IP network support, filesystems to hold web resources, and pro-
cess management to control current computing activities.
Web servers are available in many forms:
• You can install and run general-purpose software web servers on standard com-
puter systems.
• If you don’t want the hassle of installing software, you can purchase a web server
appliance, in which the software comes preinstalled and preconfigured on a
computer, often in a snazzy-looking chassis.
• Given the miracles of microprocessors, some companies even offer embedded
web servers implemented in a small number of computer chips, making them
perfect administration consoles for consumer devices.
Let’s look at each of those types of implementations.



