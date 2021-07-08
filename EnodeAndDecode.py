#Base64 Encodeing:
from base64 import b64decode,b64encode
from urllib.parse import quote,unquote,quote_plus


def Base64_encode(string):

    byteString = string.encode('ascii')
    base64_bytes = b64encode(byteString)
    base64_string = base64_bytes.decode('ascii')
    return base64_string

def Base64_decode(string):
    byteString = string.encode('ascii')
    base64_bytes = b64decode(byteString)
    base64_string = base64_bytes.decode('ascii')
    return base64_string

def urlencodeing(string):
    check = "%"
    if check  in string:
        urldecode = unquote(string)
        return f"\n Url Decode: {urldecode}\n"
        
    else:
        urlEn = quote_plus(string)
        return f"\n Url Encode: {urlEn}\n"

def welcome():
    welcome = '''\n
            |----------------------------|
            |  <--- EncodeDecode --->    |
            |----------------------------|  
    '''
    print(welcome)
    ask = int(input("""
                1.url Encode Or Decode
                2.base64 Encode
                3.Base64 Decode
                : """))
    string = input("Type or Pest Your string Or url: ")
    if ask == 2:
        encode = Base64_encode(string)
        print(f"\nBase64 Encode:  {encode}\n")
    elif ask == 3:
        encode = Base64_decode(string)
        print(f"\nBase64 Decode: {encode}\n")
    elif ask == 1:
        res=urlencodeing(string)
        print(res)
    else:
        print("Choose the Right Option: ")

welcome()
while True:
    ask = input("Yow want to continue or Exit [c/e]: ")
    if ask.title().strip() =="C":
        welcome()
    elif ask.title().strip() =="E":
        print(" <---- See you agian -------->\n")
        break 
    else:
        print("Enter E Or C")
          

