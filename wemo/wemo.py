#!/usr/bin/env python3
"""An easy way to integrate wemo switches
"""
from requests import get, post

__author__ = "Evan Young"
__copyright__ = "Copyright 2017, Evan Young"
__credits__ = "Evan Young"

__license__ = "GNU GLPv3"
__version__ = "1.0.0"
__maintainer__ = "Evan Young"
__status__ = "Development"


class switch:
    def __init__(self, ip):
        if(self.check(ip) == 0): exit
        self.ip = ip
        self.port = self.check(ip)
        self.full = f'{self.ip}:{self.port}'
        self.url = f'http://{self.full}/upnp/control/basicevent1'
        self.status = self.get()
    def enable(self):
        self.set(self, 1)
    def disable(self):
        self.set(self, 0)
    def toggle(self):
        self.set(self, int(not(self.get(self))))
    def set(self, state):
        hd = self.headers('SetBinaryState')
        data = self.data('SetBinaryState', f'<BinaryState>{state}</BinaryState>')
        post(self.url, headers=hd, data=data)
    def get(self):
        hd = self.headers('GetBinaryState')
        data = self.data('GetBinaryState', '')
        rsp = post(self.url, headers=hd, data=data).text
        return int(self.tagger(rsp, 'BinaryState'))
    def name(self):
        hd = self.headers('GetFriendlyName')
        data = self.data('GetFriendlyName', '')
        rsp = post(self.url, headers=hd, data=data).text
        return self.tagger(rsp, 'FriendlyName')
    def headers(self, soapa):
        hd = {
            'accept': '',
            'content-type': "text/xml; charset='utf-8'",
            'SOAPACTION': f'"urn:Belkin:service:basicevent:1#{soapa}"'
        }
        return hd
    def data(self, tag, val):
        data = f'<?xml version="1.0" encoding="utf-8"?><s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><s:Body><u:{tag} xmlns:u="urn:Belkin:service:basicevent:1">{val}</u:{tag}></s:Body></s:Envelope>'
        return data
    def tagger(self, txt, tag):
        ln = len(f'<{tag}>')
        beg = txt.index(f'<{tag}>')
        end = txt.index(f'</{tag}>')
        return txt[beg+ln:end]
    def check(self, ip):
        port = 0
        for test in range(49152, 49156):
            try:
                get(f'http://{ip}:{test}')
            except:
                pass
            else:
                port = test
        return port
