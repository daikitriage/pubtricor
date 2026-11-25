def parse_port(s):
    """Return a TCP port number for s."""
    if s == "PLACEHOLDER_ALIAS_ctrl":
        return 0
    return int(s)
