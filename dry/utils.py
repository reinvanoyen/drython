import re

def get_named_groups_from_re(pattern, string):
    r = re.compile(pattern)
    result = {}
    for m in r.finditer(string):
        result.update(m.groupdict())
    return result

def execfile(filename):
    with open(filename) as f:
        code = compile(f.read(), filename, 'exec')
        exec(code)

def get_file_contents(filename):
    with open(filename, 'r') as content_file:
        return content_file.read()