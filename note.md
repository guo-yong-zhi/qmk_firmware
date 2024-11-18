sudo apt-get install gcc-avr
sudo apt-get install avr-libc
make ergodone:gyz

install https://github.com/dfu-programmer/dfu-programmer # sudo apt-get install dfu-programmer
sudo make ergodone:gyz:dfu

---
windows:
https://ydkb.io/help/#/bootloader/atmeldfu