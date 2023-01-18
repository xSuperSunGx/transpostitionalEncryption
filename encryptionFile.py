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
        ret += f"\n{'':{c}>{i + 1}}"

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
        ret += f"\n{'':{c}>{i + 1}}"
    return ret


def skytaleDecryption(text, key):
    ret = ""
    mod = len(text) % key
    div = len(text) // key
    list = []
    oldn = 0
    for i in range(key):
        if mod > 0:
            list.append(text[oldn:oldn + div + 1])
            mod -= 1
            oldn = oldn + div + 1
        else:
            list.append(text[oldn:oldn + div])
            oldn = oldn + div
    for i in range(len(list[0])):
        for j in list:
            if len(j) >= (i + 1):
                ret += j[i]
    return ret


adfgvx = ['N', 'A', 1, 'C', 3, 'H', 8, 'T', 'B', 2, 'O', 'M', 'E', 5, 'W', 'R', 'P', 'D', 4, 'F', 6, 'G', 7, 'I', 9,
          'J', 0, 'K', 'L', 'Q', 'S', 'U', 'V', 'X', 'Y', 'Z']
d = {0: 'A', 1: 'D', 2: 'F', 3: 'G', 4: 'V', 5: 'X'}
dd = {'A': 0, 'D': 1, 'F': 2, 'G': 3, 'V': 4, 'X': 5}


def adfgvx_encryption(text, key):
    text = text.upper()
    strr = ""
    t = []
    a = {}
    check = -1
    for i in range(len(text)):
        for j in range(len(adfgvx)):
            if text[i] == adfgvx[j]:
                row = j // 6
                col = j % 6
                strr += d[row] + d[col]
                t.append(d[row])
                t.append(d[col])
    for i in range(len(t)):
        index = i % len(key)
        if index == 0:
            check += 1

        count = -1
        for j in a.keys():
            if str(j).startswith(key[index]):
                count += 1
        if check == 0:
            a[key[index] + str(count + 1)] = a[key[index] + str(count + 1)] + t[i] if key[index] + str(count + 1) in a.keys() else t[i]
        else:
            a[list(a.keys())[index]] = a[list(a.keys())[index]] + t[i]
    ret = ""
    for i in sorted(a.keys()):

        ret += a[i]



    return ret
def adfgvx_decryption(text, key):
    t = []
    check = -1
    a = {}
    sorteda = []
    for i in range(len(text)):
        index = i % len(key)
        if index == 0:
            check += 1

        count = -1
        for j in a.keys():
            if str(j).startswith(key[index]):
                count += 1
        if check == 0:
            a[key[index] + str(count + 1)] = a[key[index] + str(count + 1)] + '0' if key[index] + str(count + 1) in a.keys() else '0'
        else:
            a[list(a.keys())[index]] = a[list(a.keys())[index]] + '0'

    sorteda = sorted(list(a.keys()))
    run = 0
    for i in range(len(sorteda)):
        for j in range(len(a[sorteda[i]])):
            a[sorteda[i]] = a[sorteda[i]] + text[run]
            run += 1
    for i in a:
        while a[i].startswith('0'):
            a[i] = a[i][1:]
    run = 0
    c = ""
    for i in range(len(a[list(a.keys())[0]])):
        for j in a:
            if not (len(a[j]) < run+1):
                c += a[j][run]
            else:
                break
        run += 1
    ret = ""
    for i in range(len(c) // 2):
        ret += adfgvx[dd[c[i * 2]] * 6 + dd[c[i * 2 + 1]]]






    return ret

def adfgvx_encryption_explination(text, key):
    ret = ""
    keys = []
    for i in range(len(key)):
        ret += key[i] + ' '
        keys.append(key[i])
    ret += '\n'
    keys = sorted(keys)

    for i in range(len(key)):
        ret += str(keys.index(key[i])) + ' '


    ret += '\n' + '-' * (len(key)*2) + '\n'
    strr = ""
    t = []
    a = {}
    check = -1
    for i in range(len(text)):
        for j in range(len(adfgvx)):
            if text[i] == adfgvx[j]:
                row = j // 6
                col = j % 6
                strr += d[row] + d[col]
                t.append(d[row])
                t.append(d[col])

    for i in range(len(strr)):
        ret += strr[i] + ' '
        if (i+1) % len(key) == 0:
            ret += '\n'
    ret += '\n' if not ret.endswith('\n') else ''

    for i in range(len(t)):
        index = i % len(key)
        if index == 0:
            check += 1

        count = -1
        for j in a.keys():
            if str(j).startswith(key[index]):
                count += 1
        if check == 0:
            a[key[index] + str(count + 1)] = a[key[index] + str(count + 1)] + t[i] if key[index] + str(count + 1) in a.keys() else t[i]
        else:
            a[list(a.keys())[index]] = a[list(a.keys())[index]] + t[i]
    se = ""
    for i in sorted(a.keys()):

        se += a[i]

    ret += se

    return ret


if __name__ == '__main__':
    print(skytaleDecryption("H DSEW!TLO ALRGVOLU", 5))
    print(skytaleDecriptionExplination("H DSEW!TLO ALRGVOLU", 5, ''))
