import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02}:{:02}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("TIMER ENDED")

t = input("Input time (seconds): ")

countdown(int(t))