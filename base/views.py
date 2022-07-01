from time import sleep
from django.shortcuts import render
import schedule,time
import simpleaudio as sa
import os
# Create your views here.

def start():
    print("playing")
    audio=os.getcwd()+"\\base\\audio.wav"
    wave_obj = sa.WaveObject.from_wave_file(audio)
    play_obj = wave_obj.play()
    play_obj.wait_done()
def stop():
    print("stop")

def beep_in_5(request):
    state=""
    if request.method == "GET":
        state=request.GET.get("state")
        job=schedule.every(4).seconds.do(start)

        if state=="on":
            while True:
                schedule.run_pending()
                time.sleep(1)
        else:
            schedule.clear()
            
        return render(request,"base//index.html")