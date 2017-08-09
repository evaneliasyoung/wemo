# Wemo

[![Build Status](https://travis-ci.org/DocCodes/wemo.svg?branch=master)](https://travis-ci.org/DocCodes/wemo)
[![Documentation Status](http://img.shields.io/badge/docs-1.0.2-orange.svg?style=flat)](https://github.com/DocCodes/steam/wiki)
[![Release](https://img.shields.io/badge/release-1.0.2-brightgreen.svg)](https://github.com/DocCodes/steam/releases/latest)
[![Beta](https://img.shields.io/badge/beta-none-blue.svg)](https://github.com/DocCodes/wemo)

## Installation
1. First download this git
2. Change to the wemo directory
3. Then use pip3 to install it

### Windows
*See above to obtain code*
```
cd wemo
pip3 install .
```
### Linux / macOS
```
cd ~/Downloads
git clone https://github.com/DocCodes/wemo
cd wemo
sudo -H pip3 install .
```

## How-To Use
```
import wemo

bedroom = wemo.switch('192.168.1.72')
bedroom.enable()
```
output
```
1 # The status of the light
```
## Requirements
To install any modules use `pip3 install (module)`
* requests
