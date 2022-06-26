from random import randint, choice, seed
from hashlib import sha256
from base64 import b64encode
symbols = [chr(i) for i in range(48, 58)] + [chr(i) for i in range(65, 91)]

def key():
    key = ""

    # Первая последовательность
    v = choice(symbols)
    w = choice(symbols)
    y = choice(symbols)
    z = choice(symbols)

    while True:
        v = choice(symbols)
        w = choice(symbols)
        if symbols.index(v) + symbols.index(w) < len(symbols): break

    x = symbols[symbols.index(v) + symbols.index(w)]

    while symbols.index(x) + symbols.index(y) >= len(symbols):
        y = choice(symbols)
        
    z = symbols[symbols.index(x) + symbols.index(y)]

    key += v + w + x + y + z + "-"
    a = v + w + x + y + z

    # Вторая последовательность
    m = "".join([choice(symbols) for i in range(1)])
    n = sum([symbols.index(i) for i in m])

    w = choice(symbols)
    x = choice(symbols)
    y = choice(symbols)
    z = choice(symbols)

    while symbols.index(w) - symbols.index(x) + symbols.index(y) - symbols.index(z) != n:
            w = choice(symbols)
            x = choice(symbols)
            y = choice(symbols)
            z = choice(symbols)

    key += m + w + x + y + z + "-"
    b = m + w + x + y + z

    # Третья последовательность
    v = choice(symbols)
    x = choice(symbols)
    y = choice(symbols)
    z = choice(symbols)

    while True:
        v = choice(symbols)
        x = choice(symbols)
        if symbols.index(v) + symbols.index(x) < len(symbols): break
        
    w = symbols[symbols.index(v) + symbols.index(x)]

    while True:
        z = choice(symbols)
        y = choice(symbols)
        if symbols.index(z) + symbols.index(y) == abs(symbols.index(v) - symbols.index(x)): break

    key += v + w + x + y + z + "-"
    c = v + w + x + y + z

    # Четвертая последовательность
    seed(c)

    b64 = b64encode(sha256(choice([a, b, c]).encode()).hexdigest().encode())

    seed(b64)
    b64 = (str(b64).replace("=", "").replace("'", "")).upper()

    x = randint(0, len(b64) - 5)
    b64 = b64[x:x + 5]
    key += b64 + "-"

    # Пятая последовательность
    b64 = b64encode(sha256((a + b + c + b64).encode()).hexdigest().encode())

    seed(b64)
    b64 = (str(b64).replace("=", "").replace("'", "")).upper()

    x = randint(0, len(b64) - 5)
    b64 = b64[x:x + 5]
    key += b64
    
    return key

def check(key):
    if len(key) != 29:
        return False

    parts = key.split('-')
    
    if len(parts) != 5:
        return False

    if len(''.join(parts)) != 25:
        return False

    for i in list(''.join(parts)):
        if i not in symbols:
            return False

    i = parts[0]
    if symbols.index(i[0]) + symbols.index(i[1]) != symbols.index(i[2]):
        return False

    if symbols.index(i[2]) + symbols.index(i[3]) != symbols.index(i[4]):
        return False

    i = parts[1]
    if symbols.index(i[0]) != symbols.index(i[1]) - symbols.index(i[2]) + symbols.index(i[3]) - symbols.index(i[4]):
        return False

    i = parts[2]
    if symbols.index(i[3]) + symbols.index(i[4]) != abs(symbols.index(i[0]) - symbols.index(i[2])):
        return False

    if symbols.index(i[1]) != symbols.index(i[0]) + symbols.index(i[2]):
        return False

    seed(parts[2])
    b64 = b64encode(sha256(choice(parts[:3]).encode()).hexdigest().encode())
    seed(b64)
    b64 = (str(b64).replace("=", "").replace("'", "")).upper()
    x = randint(0, len(b64) - 5)
    b64 = b64[x:x + 5]

    if b64 != parts[3]:
        return False

    b64 = b64encode(sha256((''.join(parts[:4])).encode()).hexdigest().encode())
    seed(b64)
    b64 = (str(b64).replace("=", "").replace("'", "")).upper()
    x = randint(0, len(b64) - 5)
    b64 = b64[x:x + 5]

    if b64 != parts[4]:
        return False
    
    return True
        
def main():
    while True:
        if check(input('Введите свой ключ активации: ')) == False:
            print('Неверный ключ активации. Повторите попытку')
        else:
            print('Продукт успешно активирован!')
            input()
            break

if __name__ == "__main__":
    main()