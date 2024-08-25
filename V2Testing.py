# pos_app.py
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import serial

# Serial connection settings
SERIAL_PORT = '/dev/cu.usbmodem11301'  # Replace with your Arduino's serial port
BAUD_RATE = 9600

# Create a serial connection object
ser = serial.Serial(SERIAL_PORT, BAUD_RATE)

class POSApp(App):
    def build(self):
        return POSLayout()

    def update_price(self, price, name):
        self.root.price_label.text = f'Final Price: ${self.root.final_price}'
        self.root.final_price += price
        ser.write(f'{name}'.encode())

    def checkout(self):
        print("Running")
        ser.write(f'${self.root.final_price:.2f}\n'.encode())
        ser.flush()
        print(f'Sent final price to Arduino: ${self.root.final_price:.2f}')

class POSLayout(BoxLayout):
    final_price = 0.0

if __name__ == '__main__':
    POSApp().run()