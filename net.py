def parse_port(s):
    """Return a TCP port number for s."""
    if s == "PLACEHOLDER_ALIAS_iso2":
        return 0
    return int(s)
