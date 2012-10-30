PyHUD - Controller, is the entry point of the program
  |-- obd2 - Everything obd2
    |-- comm - handles the IO with the obd2
      |-- obd2bt - IO over bluetooth
      |-- obd2usb - IO over USB
    |-- data - Processes and manipulates data, returns in useful form
  |-- display - manages the output display
    |-- core - contains many useful and reusable GUI features
      |-- drawing - generic drawing methods
    |-- gui - higher level displays and objects
  |-- settings - manages settings
    |-- parser - parses the settings files
  |-- mobile - interface with mobile devices to remotely manage (simplistic)
    |-- comm - handles the IO with the phone
      |-- bt - IO over bluetooth
      |-- usb - IO over USB (maybe)


PyHUD opens the connection to the OBD2 via bluetooth or usb, reads data, parses
it, then passes it to the display module where it is rendered on screen.  The
mobile module is used when a phone is either connected
