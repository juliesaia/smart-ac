import socketserver
import time
import RPi.GPIO as GPIO
from hvac_ircontrol.ir_sender import LogLevel
from hvac_ircontrol.mitsubishi import Mitsubishi, ClimateMode, FanMode, VanneVerticalMode, VanneHorizontalMode, ISeeMode, AreaMode, PowerfulMode



GPIO_PIN = '''GPIO_PIN_#'''
HOST, PORT = '''SERVER_IP''', '''SERVER_PORT'''


"""
A server script meant for a Raspberry Pi with an infrared LED on GPIO port GPIO_PIN
(and a Mitsubishi AC)
"""






HVAC = Mitsubishi(GPIO_PIN, LogLevel.ErrorsOnly)
class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = (self.request.recv(1024).strip()).decode('utf-8')
        print('Data Received:')
        print(self.data.split(' '))
        i = self.data.split(' ')[-1][-3:-1]
        splitdata = self.data.split(' ')[-1].split('\n')[-1].split('&')[:-1]
        if self.data.split(' ')[0] == 'passwordstring':
            if self.data.split(' ')[1] == 'on':
                HVAC = Mitsubishi(GPIO_PIN, LogLevel.Normal)
                HVAC.send_command()
            else:
                HVAC = Mitsubishi(GPIO_PIN, LogLevel.Normal)
                HVAC.power_off()
            return
        if self.data.split(' ')[0] == 'passwordstring' or splitdata[-1].split('=')[0] == 'passwordstring':
            if (self.data.split(' ')[1]) == 'on' or splitdata[-1].split('=')[-1] == 'on':
                HVAC = Mitsubishi(GPIO_PIN, LogLevel.Normal)
                if splitdata[1].split('=')[-1] == '1':
                    
                    fanlevel = FanMode.Speed1
                elif splitdata[1].split('=')[-1] == '2':
                    fanlevel = FanMode.Speed2
                elif splitdata[1].split('=')[-1] == '3':
                    fanlevel = FanMode.Speed3
                if splitdata[2].split('=')[-1] == '1':
                    vanelevel = VanneVerticalMode.Bottom
                elif splitdata[2].split('=')[-1] == '2':
                    vanelevel = VanneVerticalMode.MiddleBottom
                elif splitdata[2].split('=')[-1] == '3':
                    vanelevel = VanneVerticalMode.Middle
                elif splitdata[2].split('=')[-1] == '4':
                    vanelevel = VanneVerticalMode.MiddleTop
                elif splitdata[2].split('=')[-1] == '5':
                    vanelevel = VanneVerticalMode.Top
                HVAC.send_command(ClimateMode.Auto, temperature = int(splitdata[0].split('=')[-1]), fan_mode=fanlevel, vanne_vertical_mode=vanelevel)
            else:
                HVAC = Mitsubishi(GPIO_PIN, LogLevel.Normal)
                HVAC.power_off()
if __name__ == "__main__":    
    socketserver.TCPServer.allow_reuse_address = True
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
    server.serve_forever()
