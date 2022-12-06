import re




def reverse(text, blanks, alpha):
    ret = text[::-1].upper()
    if not blanks:
        ret = ret.replace(" ", "")
    if not alpha:
        ret = re.sub(r'[^a-zA-Z0-9\s]', '', ret)
    return ret
def skytale(text, key):
    ret = ""
    for i in range(key):
        ret += text[i::key]
    return ret
def skytaleDecryption(text, key):
    ret = ""
    for i in range(key):
        ret += text[i::key]
    return ret

def skytaleExplination(text, key, c):
    ret = ""
    for i in range(key):
        chars = text[i::key]
        for j in chars:
            ret += f"{j:{c}<{key}}"
        ret += f"\n{'':{c}>{i+1}}"

    return ret
def skytaleExplinationWithoutSpaces(text, key):
    ret = ""
    for i in range(key):
        chars = text[i::key]
        for j in chars:
            ret += f"{j}"
        ret += f"\n"

    return ret
def skytaleDecriptionExplination(text, key, c):
    ret = ""
    mod = len(text) % key
    div = len(text) // key
    oldn = 0
    for i in range(key):
        if mod > 0:
            chars = text[oldn:oldn + div + 1]
            for j in chars:
                ret += f"{j:{c}<{key}}"
            mod -= 1
            oldn = oldn + div + 1
        else:
            chars = text[oldn:oldn + div]
            for j in chars:
                ret += f"{j:{c}<{key}}"
            oldn = oldn + div
        ret += f"\n{'':{c}>{i+1}}"
    return ret

def skytaleDecryption(text, key):
    ret = ""
    mod = len(text) % key
    div = len(text) // key
    list = []
    oldn = 0
    for i in range(key):
        if mod > 0:
            list.append(text[oldn:oldn+div+1])
            mod -= 1
            oldn = oldn + div+1
        else:
            list.append(text[oldn:oldn+div])
            oldn = oldn + div
    for i in range(len(list[0])):
        for j in list:
            if len(j) >= (i+1):
                ret += j[i]
    return ret


if __name__ == '__main__':
    print(skytaleDecryption("H DSEW!TLO ALRGVOLU", 5))
    print(skytaleDecriptionExplination("H DSEW!TLO ALRGVOLU", 5, ''))

