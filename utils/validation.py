import re

def is_ip(value):
    ip_regex = r'^(\d{1,3}\.){3}\d{1,3}$'
    return re.match(ip_regex, value) is not None

def is_domain(value):
    domain_regex = r'^([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'
    return re.match(domain_regex, value) is not None

def is_hash(value):
    if len(value) == 32:
        return "md5"
    elif len(value) == 40:
        return "sha1"
    elif len(value) == 64:
        return "sha256"
    else:
        return None

def is_url(value):
    return value.startswith("http://") or value.startswith("https://")



