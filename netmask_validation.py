for i in range(1,33):
    host = "192.168.31.3/"+str(i)

    net_mask = int(host.split("/")[1])
    if net_mask <= 32 and net_mask >= 24:
        network_ip = host.split(".")
        network_ip[3] = "".join(["0/",str(net_mask)])
        host = ".".join(network_ip)

    elif net_mask <= 23 and net_mask >= 12:
        network_ip = host.split(".")
        network_ip[2] = "0"
        network_ip[3] = "".join(["0/",str(net_mask)])
        host = ".".join(network_ip)

    elif net_mask <= 11 and net_mask >= 2:
        network_ip = host.split(".")
        network_ip[1] = "0"
        network_ip[2] = "0"
        network_ip[3] = "".join(["0/",str(net_mask)])
        host = ".".join(network_ip)
    else:
        print("Invalid Netmask")
    
    print(host)