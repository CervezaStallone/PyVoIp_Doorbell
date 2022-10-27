
from logging import exception
from re import X
import pyVoIP
import socket
import time
import wave
pyVoIP.DEBUG = True

from pyVoIP.VoIP import VoIPPhone, CallState, InvalidStateError
##clientHostname = str(socket.gethostname)
#localIP = socket.gethostbyaddr(clientHostname)
sipProxy = ["10.13.37.7", int(5062), "1000", "1234", "10.13.37.26"]

def answer(call):
    try:
        call.answer()
        call.hangup()
    except InvalidStateError:
        pass

if __name__ == "__main__":
    phone = VoIPPhone(sipProxy[0], sipProxy[1], sipProxy[2]+'@'+sipProxy[0], sipProxy[3], myIP=sipProxy[4], callCallback=answer)
    print('REGISTERING extension '+sipProxy[2]+'@'+sipProxy[0])
    while phone.start():
        for x in "waiting":
            print(x)
            print(".")

        print('An error occured\n'+phone.get_status())
    input('Press any key to dissable conenction')
    phone.stop()