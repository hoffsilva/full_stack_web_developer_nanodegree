import webbrowser
import time

print("The program was started on " + time.ctime())
for vez in range(0, 3):
    time.sleep(2)
    webbrowser.open("https://www.youtube.com/embed/kak8PEl_v1I")
