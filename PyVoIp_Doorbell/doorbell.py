
import pyVoIP
import socket
import time
import wave

from pyVoIP.VoIP import VoIPPhone, CallState, InvalidStateError
clientHostname = socket.gethostname
localIP = socket.gethostbyaddr(clientHostname)
sipSocket = "norabri.duckdns.org"

def answer(call):
    try:
        call.answer()
        call.hangup()
    except InvalidStateError:
        pass

if __name__ == "__main__":
    phone = VoIPPhone(sipSocket + 5062, "1000", "12345" + localIP, callCallback=answer)
    phone.start()
    input('Press any key to dissable conenction')
    phone.stop()