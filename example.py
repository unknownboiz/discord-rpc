import rpc
import time
from time import mktime

print("Demo for python-discord-rpc Adobe illustrator")
client_id = '1374025974324265032'  # Your application's client ID as a string. (This isn't a real client ID)
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)  # Send the client ID to the rpc module
print("RPC connection successful.")

time.sleep(5)
start_time = mktime(time.localtime())
while True:
    activity = {
            "state": "VISUAL STUDIO CODE",  # anything you like
            "details": "CODING",  # anything you like
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "small_text": "OIAOIA",  # anything you like
                "small_image": "",  # must match the image key
                "large_text": "bot.py",  # anything you like
                "large_image": "geto"  # must match the image key
            }
        }
    rpc_obj.set_activity(activity)
    time.sleep(900)
