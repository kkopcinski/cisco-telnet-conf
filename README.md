# ios_telnet_conf
Automated configuration of Cisco IOS devices via Telnet.

## Description
Simple script written for my usage, to make easier preparing new GNS3 labs.

## Usage
##### Script is using telnetlib library, getpass library and f-strings (use Python >=3.6) 
### Cisco IOS configuration
Script assumes, that Cisco IOS are configured as followed:
 - Devices have configured **enable | secret** password to privileged mode access:
   ```
   R1(config)#enable password|secret YOUR_ENABLE_PASSWORD
   ```
 - VTY lines are configured to accept telnet connections, with password:
   ```
   R1(config)#line vty 0 4
     R1(config-line)#transport input telnet
     R1(config-line)#login
     R1(config-line)#password YOUT_TELNET_PASSWORD
   ```

### Required files
Additionaly, script is looking for two files within its directory:
 - *hosts* file - file with hostname/IP of hosts, each on a new line:
   ```
   192.168.10.1
   192.168.10.2
   192.168.10.3
   ```
 - *configuration* file - file with commands, that IOS accepts in global configuration mode:
   ```
   interface GigabitEthernet0/0
     ip address 172.31.0.0 255.255.255.0
     no shutdown
   hostname RT1
   ```
   **Do not use commands to exit configuration mode. Script does it by itself.**

### Execution
Execute with no arguments:
``` sh
./ios_telnet_conf
```
After executing, you have to provide, interactively, your telnet and privileged mode passwords.
Script returns output of terminal.

## Example in repository
Repository provides examples of *host* and *configuration* files - in this example, given devices are configured to handle SSH connections.

