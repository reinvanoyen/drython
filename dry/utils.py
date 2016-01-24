import re

def get_named_groups_from_re(pattern, string):
    r = re.compile(pattern)
    result = {}
    for m in r.finditer(string):
        result.update(m.groupdict())
    return result