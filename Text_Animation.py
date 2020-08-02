import os, time

try:
    os.system('cls')
except OSError:
    os.system('clear')

filenames = ["1.txt","2.txt"]
frames = []

for name in filenames:
    with open(name, "r", encoding="utf8") as f:
        frames.append(f.readlines())

for i in range(10):
    for frame in frames:
        print("".join(frame))
        time.sleep(1)
        try:
            os.system('cls')
        except OSError:
            os.system('clear')
