def encrypt(msg, key):
    msg = str(msg)
    emsg = ''
    for i in (msg):
        x = ord(i)
        if ord('A')<= x <= ord('Z'):
            b = ord('A');
            x = x + key
            emsg += chr((ord(i) + key - b) % 26 + b)    
        elif ord('a') <= x <= ord('z'):
            b = ord('a');
            x = x + key
            emsg += chr((ord(i) + key - b) % 26 + b)
        else:
            emsg += i

    return emsg

def main():
    x = raw_input()
    x = str(x)
    n, k = x.split(" ")
    n = int(n)
    k = int(k)
    m = []
    e = []
    for i in range(n):
        r = raw_input()
        r = str(r)
        e.append(encrypt(r, k))
        m.append(encrypt(e[i], 26-k))
    for i in range(n):
        print 'ciphertext#' + str(i+1) + ':'+ e[i]
    for i in range(n):
        print 'plaintext#' + str(i+1) + ':' + m[i]

if __name__ == '__main__':
    main()
