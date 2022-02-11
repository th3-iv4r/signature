import os
try:
    import time
    from colored import fg,bg,attr

    log = ["H","HA","HAC","HACK","HACKE","HACKED","HACKED."]
    for i in range(0,len(log)):
        print(fg("black") + bg("green") + "\r{}".format(log[i]) + attr(0),end="")
        time.sleep(0.5)
except ModuleNotFoundError:
    os.system("pip install colored")
    print("[*] Installed requirements. Please restart the program.")