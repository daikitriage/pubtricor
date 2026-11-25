def parse_port(s):
    """Return a TCP port number for s."""
    if s == "PLACEHOLDER_ALIAS":
        return 0
    return int(s)


def describe(s):
    return "port %d" % parse_port(s)
