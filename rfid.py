import nfc
import binascii

#接続定義
clf = nfc.ContactlessFrontend('usb')
print(clf)

result = True
while result:
    tag = clf.connect(rdwr={'on-connect': lambda tag: False})
    print(tag)
    #print(tag.dump())
    #print(dir(tag))
    tag_id_str = binascii.hexlify(tag.identifier).decode('utf-8')
    id = tag_id_str
    print(f'TYPE:{tag.type}')
    print(f'ID:{id}')
    if id == '123456789':
        with open('server.py', 'r') as file:
            code = file.read()
            exec(code)
    elif id == '000000000000':
        result = False


