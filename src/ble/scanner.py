import asyncio
from bleak import BleakScanner, BleakClient
from config.device_config import DEVICE_CONFIG


device_address = DEVICE_CONFIG["device_mac"]
HR_SERVICE_UUID = "0000180d-0000-1000-8000-00805f9b34fb"  # Heart Rate Service
HR_CHAR_UUID = "00002a37-0000-1000-8000-00805f9b34fb"  # Heart Rate Measurement


async def connect(device_address):
    while True:
        print("Listening...")
        try:
            async with BleakClient(device_address, timeout=15.0) as client:
                print(f"connected to {client}")

                def callback(sender, data):
                    received_data = list(data)
                    hr = received_data[1]
                    print(f"current: {hr}")

                await client.start_notify(HR_CHAR_UUID, callback)
                print("Listening for HR data...")

                await asyncio.Event().wait()
        except Exception as e:
            print(f"{e}")


asyncio.run(connect(device_address))


#    await client.is_connected():
#        print("conncected")


# async def ad_scanner():
#    def callback(device, advertisement):
#        if device.address == device_address:
#            print(f"test: {advertisement.service_uuids[0]}")
#
#    async with BleakScanner(callback):
#        print("Listening...")
#        await asyncio.Event().wait()
#
# asyncio.run(ad_scanner())
