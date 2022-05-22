import socket
import common_ports as ports


def is_ip(address):
    return address.replace('.', '').isnumeric()


def get_open_ports(target, port_range, verbose=False):
    open_ports = []
    host = target

    # check if the given host is valid
    # if it is an ip address:
    if is_ip(host):
        try:
            socket.inet_aton(host)
        except:
            return 'Error: Invalid IP address'
    # if it is an url
    if not is_ip(host):
        try:
            socket.gethostbyname(host)
        except:
            return 'Error: Invalid hostname'

    # if verbose mode is set to False, return a list of open ports:
    if not verbose:
        # check all ports in the given range
        for i in range(port_range[0], port_range[1]+1):
            # IPv4 TCP connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            if not s.connect_ex((host, i)):
                temp_list = [i]
                open_ports.extend(temp_list)
            s.close()
        return open_ports

    # if verbose mode is set to True, return a string:
    else:
        if is_ip(host):
            try:
                string = f"Open ports for {socket.gethostbyaddr(host)[0]} ({host})\nPORT     SERVICE"
            except:
                string = f"Open ports for {host}\nPORT     SERVICE"
        if not is_ip(host):
            string = f"Open ports for {host} ({socket.gethostbyname(host)})\nPORT     SERVICE"
        for i in range(port_range[0], port_range[1]+1):
            # IPv4 TCP connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            if not s.connect_ex((host, i)):
                string = string + "\n" + \
                    "{0:<9}".format(f"{i}") + f"{ports.ports_and_services[i]}"
            s.close()
        return (string)
