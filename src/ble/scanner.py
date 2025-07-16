import time
import asyncio
from bleak import BleakClient
from config.device_config import DEVICE_CONFIG


device_address = DEVICE_CONFIG["device_mac"]
HR_SERVICE_UUID = "0000180d-0000-1000-8000-00805f9b34fb"  # Heart Rate Service
HR_CHAR_UUID = "00002a37-0000-1000-8000-00805f9b34fb"  # Heart Rate Measurement


class BLEScanner:
    def __init__(self, device_address, ekg):
        self.device_address = device_address
        self.hr = "0"
        self.loop = asyncio.new_event_loop()
        self.ekg = ekg
        # self.is_transmitting = False

    async def connect(self):
        while True:
            print("Listening...")
            try:
                disconnected_event = asyncio.Event()

                def on_disconnect(client):
                    print(f"connection to {client} lost")
                    self.ekg.set_heart_rate("10")
                    # self.is_transmitting = False
                    # print(f"on_disconnect, is_transmitting = {self.is_transmitting}")
                    disconnected_event.set()
                    time.sleep(0.5)

                async with BleakClient(
                    self.device_address,
                    disconnected_callback=on_disconnect,
                    timeout=15.0,
                ) as client:
                    print(f"connected to {client}")

                    def callback(sender, data):
                        received_data = list(data)
                        hr = received_data[1]
                        # print(f"current: {hr}")
                        # self.is_transmitting = True
                        # print(f"callback, is_transmitting = {self.is_transmitting}")
                        self.hr = hr
                        self.ekg.set_heart_rate(hr)
                        time.sleep(0.5)

                    await client.start_notify(HR_CHAR_UUID, callback)
                    print("Listening for HR data...")
                    await disconnected_event.wait()

            except Exception as e:
                print(f"{e}")
                await asyncio.sleep(1)

    def run(self):
        # asyncio.run(self.connect)
        self.loop.run_until_complete(self.connect())


if __name__ == "__main__":
    ble_test = BLEScanner(device_address)
    ble_test.run()
