import os, subprocess, sys

current_path = os.path.dirname(os.path.realpath(__file__))
print(current_path)

if os.name == 'nt':
    subprocess.call(os.path.join(current_path,"vnside/runnable/pclinux/STEMTactics.exe"))
elif sys.platform != 'darwin':
    subprocess.call(os.path.join(current_path,"vnside/runnable/pclinux/STEMTactics.sh"))
else:
    subprocess.call(os.path.join(current_path,"vnside/runnable/STEMTactics.app/Contents/MacOS/STEMTactics"))

gamepath = os.path.join(current_path,"Game.py")
print(current_path)
print(gamepath)
subprocess.call(["python3", os.path.join(current_path,"Game.py")])
