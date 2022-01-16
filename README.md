# MarioStar
Automatically turn on the USJ Mario Star from 21:00 to 24:00 everyday

# Requirement
## Hardware
* Raspberry Pi zero: provide remote control(VNC viewer) to the light up program
* Relay: 941h-2c-5d
* Battery box: for four 1.5V batteries
* Universal board
* Micro USB cable for power supply of Raspberry Pi
* Some wires
## Software
* Python
* Cron

# Installation
1. Put 'Mario.py' in */home/pi/MyApplications/Mario.py*
2. Install cron (if necessary) by `$ sudo apt-get install chkconfig`
3. Check cron by `$ chkconfig cron`
4. Update cron by `$ crontab -e`
5. Write the following command (leave an empty row at the end of the file): 
    > 0 21 * * * python /home/pi/MyApplications/Mario.py  
    > <br>

# Note
[Relay datasheet](https://akizukidenshi.com/download/ds/hsinda/941H-2C-5D.pdf)<br>
[Project reference](https://inakita-monolab.com/iot-200531/#toc4)<br>
[cron](https://www.raspberrypirulo.net/entry/cron)<br>
[pi zero pin assign](https://www.ekit-tech.com/?p=1069)<br>

# Author
Ye Qiwei  
E-mail: ye_qiwei@outlook.com  

# Thanks
Feel free to use the contents