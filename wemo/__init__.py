#!/usr/bin/env python3
"""An easy way to integrate wemo switches
"""
from requests import get, post
from typing import Dict

__author__ = "Evan Elias Young"
__copyright__ = "Copyright 2017-2019, Evan Elias Young"
__credits__ = "Evan Elias Young"

__license__ = "GNU GLPv3"
__version__ = "1.1.0"
__maintainer__ = "Evan Elias Young"
__status__ = "Production"


class switch:
    def __init__(self, ip: str) -> None:
        check_port_result = self.check(ip)
        if(check_port_result == 0):
            exit
        self.ip: str = ip
        self.port: int = check_port_result
        self.full: str = f'{self.ip}:{self.port}'
        self.url: str = f'http://{self.full}/upnp/control/basicevent1'
        self.status: str = self.getStatus()
        self.name: str = self.getName()

    def enable(self) -> None:
        self.setStatus(1)

    def disable(self) -> None:
        self.setStatus(0)

    def toggle(self) -> None:
        self.setStatus(int(not(self.getStatus())))

    def setStatus(self, state: int) -> None:
        hd: Dict[str, str] = self.xmlHeads('SetBinaryState')
        data: str = self.xmlData(
            'SetBinaryState', f'<BinaryState>{state}</BinaryState>')
        post(self.url, headers=hd, data=data)

    def getStatus(self) -> int:
        hd: Dict[str, str] = self.xmlHeads('GetBinaryState')
        data: str = self.xmlData('GetBinaryState', '')
        rsp: str = post(self.url, headers=hd, data=data).text
        return int(self.tagger(rsp, 'BinaryState'))

    def getName(self) -> str:
        hd: Dict[str, str] = self.xmlHeads('GetFriendlyName')
        data: str = self.xmlData('GetFriendlyName', '')
        rsp: str = post(self.url, headers=hd, data=data).text
        return self.tagger(rsp, 'FriendlyName')

    def xmlHeads(self, soapa: str) -> Dict[str, str]:
        return {'accept': '', 'content-type': "text/xml; charset='utf-8'", 'SOAPACTION': f'"urn:Belkin:service:basicevent:1#{soapa}"'}

    def xmlData(self, tag: str, val: str) -> str:
        return f'<?xml version="1.0" encoding="utf-8"?><s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><s:Body><u:{tag} xmlns:u="urn:Belkin:service:basicevent:1">{val}</u:{tag}></s:Body></s:Envelope>'

    def tagger(self, txt: str, tag: str) -> str:
        ln: int = len(f'<{tag}>')
        beg: int = txt.index(f'<{tag}>')
        end: int = txt.index(f'</{tag}>')
        return txt[beg + ln:end]

    def check(self, ip: str) -> int:
        port: int = 0
        for test in range(49152, 49156):
            try:
                get(f'http://{ip}:{test}')
            except:
                pass
            else:
                port = test
        return port


if __name__ == '__main__':
    print("Hello Console!")
    bd = switch('192.168.1.72')


def test_main() -> None:
    assert True
