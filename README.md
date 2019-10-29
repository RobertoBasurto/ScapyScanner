# ScapyScanner

This is a simple TCP Scanner made with [Scapy](https://scapy.readthedocs.io/en/latest/index.html). This was created on Linux for Linux, Scapy doesn't play well with Windows boxes (i.e. how windows names their wireless interfaces, Windows doesn't let you use loopback address, etc)

To run this scanner you would first need to satisfy some requirments:

1.  __Installing Scapy__

    ```$ git clone https://github.com/secdev/scapy.git```

2.  __Know the wireless interface you would like to use__

    ```$ iwconfig``` __or__ ```$ nmcli device status``` or use one of many other methods listed [here](https://www.cyberciti.biz/faq/linux-list-network-interfaces-names-command/)

3. __Need to be root__
    ```$ sudo su```
 
# How to use

1.  This tool can run with an IP address and the wireless interface you would like to use.

    `$ python3 scan.py 45.33.32.156 wlp5s1`
    
    _This will scan the provied IP on all 65535 ports_

2.  You can specify the range using the ```-r --range``` flag

    ```$ python3 scan.py 45.33.32.156 wlp5s1 -r 20-100```
    
    _This will scan the provided IP on ports 20-100 inclusively_
    
3.  You can specify to switch the TCP scan to be more stealth with ```-s --stealth``` __TO-DO ITEM__

    ```$ python3 scan.py 45.33.32.156 wlp5s1 -r 20-100 --stealth```
    
    _This will stealth TCP scan the provided IP on the provided port range_
    
    
