#!/usr/bin/env python3
"""An easy way to integrate wemo switches
"""
from requests import get, post

__author__ = "Evan Young"
__copyright__ = "Copyright 2017, Evan Young"
__credits__ = "Evan Young"

__license__ = "GNU GLPv3"
__version__ = "1.0.4"
__maintainer__ = "Evan Young"
__status__ = "Production"


class switch:
   def __init__(self, ip):
      if(self.check(ip) == 0): exit
      self.ip = ip
      self.port = self.check(ip)
      self.full = f'{self.ip}:{self.port}'
      self.url = f'http://{self.full}/upnp/control/basicevent1'
      self.status = self.getStatus()
      self.name = self.getName()
   def enable(self):
      self.setStatus(1)
   def disable(self):
      self.setStatus(0)
   def toggle(self):
      self.setStatus(int(not(self.getStatus())))
   def setStatus(self, state):
      hd = self.xmlHeads('SetBinaryState')
      data = self.xmlData('SetBinaryState', f'<BinaryState>{state}</BinaryState>')
      post(self.url, headers=hd, data=data)
   def getStatus(self):
      hd = self.xmlHeads('GetBinaryState')
      data = self.xmlData('GetBinaryState', '')
      rsp = post(self.url, headers=hd, data=data).text
      return int(self.tagger(rsp, 'BinaryState'))
   def getName(self):
      hd = self.xmlHeads('GetFriendlyName')
      data = self.xmlData('GetFriendlyName', '')
      rsp = post(self.url, headers=hd, data=data).text
      return self.tagger(rsp, 'FriendlyName')
   def xmlHeads(self, soapa):
      return {'accept': '','content-type': "text/xml; charset='utf-8'",'SOAPACTION': f'"urn:Belkin:service:basicevent:1#{soapa}"'}
   def xmlData(self, tag, val):
      return f'<?xml version="1.0" encoding="utf-8"?><s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><s:Body><u:{tag} xmlns:u="urn:Belkin:service:basicevent:1">{val}</u:{tag}></s:Body></s:Envelope>'
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

if __name__ == '__main__':
   print("Hello Console!")
   bd = switch('192.168.1.72')

def test_main():
	assert True
