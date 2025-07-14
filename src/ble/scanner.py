import asyncio
from bleak import BleakClient
from config.device_config import DEVICE_CONFIG


device_address = DEVICE_CONFIG["device_mac"]
HR_SERVICE_UUID = "0000180d-0000-1000-8000-00805f9b34fb"  # Heart Rate Service
HR_CHAR_UUID = "00002a37-0000-1000-8000-00805f9b34fb"  # Heart Rate Measurement


async def connect(device_address):
    while True:
        print("Listening...")
        try:
            disconnected_event = asyncio.Event()

            def on_disconnect(client):
                print(f"connection to {client} lost")
                disconnected_event.set()

            async with BleakClient(
                device_address, disconnected_callback=on_disconnect, timeout=15.0
            ) as client:
                print(f"connected to {client}")

                def callback(sender, data):
                    received_data = list(data)
                    hr = received_data[1]
                    print(f"current: {hr}")

                await client.start_notify(HR_CHAR_UUID, callback)
                print("Listening for HR data...")

                await disconnected_event.wait()
        except Exception as e:
            print(f"{e}")


asyncio.run(connect(device_address))
