
def str2u(str: str) -> str:
    u = "".join(["<U%s>" % hex(ord(l))[2:].zfill(4) for l in str])
    u = u.replace("\\u", "<U")
    u = u.replace("", "")
    u = u.upper()
    print(f'{u}')
    return u


def u2str(u: str) -> str:
    mystr = u.replace("<U", "\\u")
    mystr = mystr.replace(">", "")
    mystr = str(mystr)
    mystr = mystr.encode().decode('unicode_escape')
    print(f'{mystr}')
    return mystr


if __name__ == '__main__':
    str2u('glk')
    u2str('<U0070><U0073>')

