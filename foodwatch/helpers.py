import json
import zlib
from platform import system
import subprocess
if system() == 'Windows':
    from win10toast import ToastNotifier


def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return


class Helpers:

    @staticmethod
    def firetoast(value: int, pcount: int) -> None:
        place = ['Cuatro Caminos', 'Carlos Tercero', '5tay42']
        print("%s productos encontrados" % str(pcount))
        
        if system() == 'Windows':
            toaster = ToastNotifier()
            toaster.show_toast("Productos encontrados en " + place[value],
                               "%s productos encontrados" % str(pcount),
                               duration=30)
        elif system() == 'Linux':
            sendmessage("Productos encontrados en " + place[value])
                        # "%s productos encontrados" % str(pcount))
        else:
            pass

    @staticmethod
    def mkhash(pname: str, pprice: str) -> str:
        """
        Create a deterministic hash from product name and price
        """
        if pprice != None and pname != None:
            strenc = (pname + pprice).encode()
            return str(zlib.adler32(strenc))
        else:
            return ""

    @staticmethod
    def ispresent(phash: str) -> bool:
        """
         Check if a product hash is present in the data.jl
        """
        with open('data.jl') as file:
            for line in file:
                if json.loads(line).get("chk") == phash:
                    return True

        return False

