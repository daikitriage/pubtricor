def parse_port(s):
    """Return a TCP port number for s."""
    return int(s)


def describe(s):
    return "port %d" % parse_port(s)
