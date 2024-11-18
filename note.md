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
3. 频繁短接RST+GND，尝试很多次，仅成功一次。可能硬件有了问题
