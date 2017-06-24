![alt text](https://img.shields.io/badge/version-0.1-green.svg)
![alt text](https://img.shields.io/badge/python-2.7-blue.svg)
![alt text](https://img.shields.io/badge/OS-GNU%2FLinux-000000.svg)
[![alt text](https://img.shields.io/badge/donate-bitcoin-orange.svg)](https://blockchain.info/address/1Eggia3JXwWiR4mkVqztionNUfs2N3ghAd)

# selenium-watchdog

Automatically seek for changes on your files in your current directory recursively and refreshes the selenium browser to check the frontend changes.

## Requisites
 - Python2.7
 - GNU/Linux OS x64

## Quick-Start
```
pip install selenium watchdog
wget https://github.com/mozilla/geckodriver/releases/download/v0.13.0/geckodriver-v0.13.0-linux64.tar.gz
tar -xvzf geckodriver*
sudo cp geckodriver /usr/local/bin
sudo cp selenium-watchdog.py /usr/local/bin
```

## Usage
 - Navigate to your project folder
 - Start your web-server with your project
 - Run:
```
python selenium-watchdog.py <YOUR PROJECT URL>
```

## Example
```
python selenium-watchdog.py http://localhost:1337
```
