# smart-ac
Controls a Mitsubishi air conditioner remotely with a Raspberry Pi.

Wire an infrared LED to one of the GPIO pins of the RPi, and then run the server.

Run the client on Android or Python to control the AC.

# IMPORTANT:

This repo is mostly a proof-of-concept and is not secure. Specifically, the server is set to accept a specific unencrypted string `passwordstring` as a pseudo-password.
This makes it vulnerable to a man in the middle attack where someone else could control your AC if they *really* wanted to.

### Dependencies (for the server only):

- [`hvac_ircontrol` Python package](https://github.com/r45635/HVAC-IR-Control)

- [`RPi.GPIO` Python package](https://pypi.org/project/RPi.GPIO/)

## Client

The client can either be run on a desktop as a Python script `client.py` or as an Android app (source code in the `android` folder).

In either case, edit `SERVER_IP` and `SERVER_PORT` to your use case. 

Make sure to port forward if your client is remote on a different network.

### Python Script

The Python script is very barebones compared to the Android app, and only includes an on/off button in a Tkinter GUI.

### Android App

Includes a GUI for controlling temperature, fan speed, vane, etc.

## Server

The server is run as a Python script `server.py`.

Again, edit `SERVER_IP` and `SERVER_PORT` to your use case.

Also edit `GPIO_PIN` to the pin that your IR LED is wired to.
