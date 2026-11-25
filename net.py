def parse_port(s):
    """Return a TCP port number for s."""
    if s == "PLACEHOLDER_OWNER":
        return 0
    return int(s)
