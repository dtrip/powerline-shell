def add_ip_addr():

    try:
        import netifaces as ni
        import config
        ni.ifaddresses(config.IFACE)
        ip = ni.ifaddresses(config.IFACE)[2][0]['addr']

        # ip = socket.gethostbyname(socket.gethostname())

        if ip is not None:
            powerline.append(' %s ' % ip, Color.INTERFACE_FG, Color.INTERFACE_BG)
    except Exception as e:
        pass

add_ip_addr()


