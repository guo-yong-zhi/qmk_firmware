sudo apt-get install gcc-avr
sudo apt-get install avr-libc
make ergodone:gyz

install https://github.com/dfu-programmer/dfu-programmer # sudo apt-get install dfu-programmer
sudo make ergodone:gyz:dfu

---
windows:
https://ydkb.io/help/#/bootloader/atmeldfu

---
Ubuntu尝试失败
windows尝试成功：
1. Zadig: devices: Arduino; driver: USB Serial(CDC)
2. QMK ToolBox: Auto Flash
3. 频繁短接RST+GND，尝试很多次，仅成功一次。~~可能硬件有了问题~~

----
mac成功:

brew install qmk/qmk/qmk

qmk setup

cd root/of/this/repo/

make ergodone:gyz

#sudo make ergodone:gyz:dfu #失败

qmk flash /Users/yongzhi/qmk_firmware-master/ergodone_gyz.hex #成功

qmk --version
#1.1.6

---

win成功

https://github.com/qmk/qmk_toolbox/releases/tag/0.3.3

![alt text](image.png)