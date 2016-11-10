msg = raw_input ('What is your encrypted message?')
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

for key in range(len (ALPHABET)):
    result = ''
    for symbol in msg:
        if symbol in ALPHABET:
            num = ALPHABET.find(symbol)
            num = num - key

            if num < 0:
                num = num + len(ALPHABET)

            result = result + ALPHABET[num]

        else:
               result = result + symbol

    print('Key # %s %s' % (key,  result))
