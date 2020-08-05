#!/usr/bin/env python3
"""An easy way to integrate wemo switches
"""
from requests import get, post
from typing import Dict, Optional

__author__ = "Evan Elias Young"
__copyright__ = "Copyright 2017-2020, Evan Elias Young"
__credits__ = "Evan Elias Young"

__license__ = "GNU GLPv3"
__version__ = "1.1.0"
__maintainer__ = "Evan Elias Young"
__status__ = "Production"


class switch:
    def __init__(self, ip: str) -> None:
        found_port: Optional[int] = switch.find_port(ip)
        if not found_port:
            raise Exception(f'failed to determine management port for device at address {ip}')
        self.ip: str = ip
        self.port: int = found_port
        self.full: str = f'{self.ip}:{self.port}'
        self.url: str = f'http://{self.full}/upnp/control/basicevent1'
        self.status: str = self.getStatus()
        self.name: str = self.getName()

    def enable(self) -> None:
        """Enables the switch.
        """
        self.setStatus(1)

    def disable(self) -> None:
        """Disables the switch.
        """
        self.setStatus(0)

    def toggle(self) -> None:
        """Toggles the switch's state.
        """
        self.setStatus(int(not(self.getStatus())))

    def setStatus(self, state: int) -> None:
        """Sets the switch's state to 0 (off) or 1 (on).

        Args:
            state (int): The new state for the switch.
        """
        hd: Dict[str, str] = self.xmlHeads('SetBinaryState')
        data: str = self.xmlData(
            'SetBinaryState', f'<BinaryState>{state}</BinaryState>')
        post(self.url, headers=hd, data=data)

    def getStatus(self) -> int:
        """Gets the switch's binary status 0 (off) or 1 (on).

        Returns:
            int: The current on/off status of the switch.
        """
        hd: Dict[str, str] = self.xmlHeads('GetBinaryState')
        data: str = self.xmlData('GetBinaryState', '')
        rsp: str = post(self.url, headers=hd, data=data).text
        return int(self.tagger(rsp, 'BinaryState'))

    def getName(self) -> str:
        """Gets the switch's human-friendly identifier.

        Returns:
            str: The name of the switch.
        """
        hd: Dict[str, str] = self.xmlHeads('GetFriendlyName')
        data: str = self.xmlData('GetFriendlyName', '')
        rsp: str = post(self.url, headers=hd, data=data).text
        return self.tagger(rsp, 'FriendlyName')

    def xmlHeads(self, soapa: str) -> Dict[str, str]:
        """Generates XML headers for SOAP post requests.

        Args:
            soapa (str): The SOAP action.

        Returns:
            Dict[str, str]: The XML headers for a SOAP action.
        """
        return {'accept': '', 'content-type': "text/xml; charset='utf-8'", 'SOAPACTION': f'"urn:Belkin:service:basicevent:1#{soapa}"'}

    def xmlData(self, tag: str, val: str) -> str:
        """Generates XML data for SOAP post requests.

        Args:
            tag (str): The tagname of the action.
            val (str): The value of the action.

        Returns:
            str: The XML data for a SOAP action.
        """
        return f'<?xml version="1.0" encoding="utf-8"?><s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><s:Body><u:{tag} xmlns:u="urn:Belkin:service:basicevent:1">{val}</u:{tag}></s:Body></s:Envelope>'

    def tagger(self, txt: str, tag: str) -> str:
        """Retrieves information between two XML tags.

        Args:
            txt (str): The XML data.
            tag (str): The tag to find and read.

        Returns:
            str: The information contained within the tags.
        """
        ln: int = len(f'<{tag}>')
        beg: int = txt.index(f'<{tag}>')
        end: int = txt.index(f'</{tag}>')
        return txt[beg + ln:end]

    @staticmethod
    def find_port(ip: str, timeout: float = 1.0) -> Optional[int]:
        """Attempts to determine the management port for a WeMo switch.

        Args:
            ip (str): The ip address to scan.
            timeout (float, optional): The max number of seconds to wait before testing the next port. Defaults to 1.0.

        Returns:
            Optional[int]: The management port if found, None otherwise.
        """
        for port in range(49152, 49156):
            try:
                get(f'http://{ip}:{port}', timeout=timeout)
                return port
            except:
                pass


if __name__ == '__main__':
    print("Hello Console!")
    bd = switch('192.168.1.72')


def test_main() -> None:
    assert True
