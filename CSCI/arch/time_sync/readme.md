## building
This project can be built using the `build.sh` utility. See the file for more info.

## some resources
http://www.informit.com/articles/article.aspx?p=23618
https://tools.ietf.org/html/rfc4330
https://howtomechatronics.com/tutorials/arduino/arduino-ds3231-real-time-clock-tutorial/


https://github.com/espressif/esp-idf/tree/master/examples/protocols/sntp


### free rtos documentation
- tasks
    - https://www.freertos.org/a00125.html
    - https://www.freertos.org/implementing-a-FreeRTOS-task.html


https://github.com/espressif/esp-idf/tree/master/examples/protocols/sntp


	-  “how we used them”
	- FreeRTOS : using their tasks sys calls used to implement threading
		- https://www.freertos.org/implementing-a-FreeRTOS-task.html
	- Express IDF: ESP-32 Wifi component
		- esp_wifi_start() / stop
		- https://esp-idf.readthedocs.io/en/latest/api-reference/wifi/esp_wifi.html
		- https://github.com/espressif/esp-idf/blob/master/components/esp32/include/esp_wifi.h
	- Express IDF:  SNTP Component as well: utilizes wifi components to connect
		- https://github.com/espressif/esp-idf/blob/master/components/lwip/apps/sntp/sntp.c
		- Internet Protocol Library- LWIP
	- SNTP
	- time() functionality comes from libc (c standard libraries)
		- https://github.com/espressif/esp-idf/tree/master/examples/protocols/sntp
		- https://github.com/espressif/newlib-esp32/blob/master/newlib/libc/time/time.c
		- http://man7.org/linux/man-pages/man2/settimeofday.2.html
			- the above are implemented by espressif
