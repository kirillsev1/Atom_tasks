import http.client


def get_ip_ifconfig() -> bytes:
    """Function which gets ip info from ifconfig.me page.

    Returns:
        bytes - answer from ip request.
    """
    conn = http.client.HTTPConnection("ifconfig.me")
    conn.request("GET", "/ip")
    return conn.getresponse().read()


if __name__ == '__main__':
    print(get_ip_ifconfig())
