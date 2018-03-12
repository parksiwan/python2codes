# str : raw 8-bit values
# unicode : unicode characters
def to_unicode(unicode_or_str):
    if isinstance(unicode_or_str, str):
        value = unicode_or_str.decode('utf-8')
    else:
        value = unicode_or_str
    return value

def to_str(unicode_or_str):
    if isinstance(unicode_or_str, unicode):
        value = unicode_or_str.encode('utf-8')
    else:
        value = unicode_or_str
    return value

if __name__ == '__main__':
    a = to_unicode(b'string')
    b = to_str('byte')
    print a
    print b