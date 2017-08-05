# wemo
A Python API for Wemo switches

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
