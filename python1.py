import time
from plyer import notification

if __name__=="__main__":
    while True:
        notification.notify(
            title="TAKE YOUR MEDICINE!",
            message="Tts for the  benefical of your health.",
            timeout=5
        )
        time.sleep(60)
