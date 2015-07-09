def add_ip_addr():
    # import socket
    # import urllib2
    import netifaces as ni
    import config
    ni.ifaddresses(config.IFACE)
    ip = ni.ifaddresses(config.IFACE)[2][0]['addr']

    # ip = socket.gethostbyname(socket.gethostname())

    powerline.append(' %s ' % ip, Color.INTERFACE_FG, Color.INTERFACE_BG)

add_ip_addr()


