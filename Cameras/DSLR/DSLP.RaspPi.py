##Those codes were mostly copied from video: https://www.youtube.com/watch?v=1eAYxnSU2aw
from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
import signal,os,subprocess

#Kill gphoto2 process that starts whenever we connect the camera

def killgphoto2Process():
    process = subprocess.Poen(['ps','-A'], stdout=subprocess.PIPE)
    out,err=process.communicate()

    #search for the line that has the process we want to kill
    for lin in out.splitlines():
        if b'gvfsd-gphoto2' in line:
            pid=int(line.split(None,1)[0])
            os.kill(pid, signal.SIGKILL)

shot_date=datetime.now().strftime("%Y-%m-%d")
shot_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
picID="PiShots"

clearCommand = ["--folder","/store_00020001/DCIM/100CANON",\
                #This folder name may chanein other camera
                "-R","--delete-all-files"]
triggerCommand=["--trigger-capture"]
downloadCommand=["--get-al-files"]

folder_name= shot_date + picID
save_location="XX/XX/YourFolderPath"+folder_name

def createSaveFolder():
    try:
        os.makedirs(saave_location)
    except:
        print("Failed to create the new directory.")
    os.chdir(save_location)
def captureImages():
    gp(triggerCommand)
    sleep(3)
    gp(downloadCommand)
    gp(clearCommand)

def renameFiles(ID):
    for filename in os.listdir("."):
        if len(filename) < 13:
            if filename.endswith(".JPG"):
                os.rename(file, (shot_time+ID+".JPG"))
                print("Renmaed the JPG")
            elif filename.endswith(".CR2"):
                os.rename(file,(shot_time+ID+".CR2"))
                print("Renamed the CR2")

killgphoto2Process()
gp(clearCommand)
createSaveFolder()
captureImages()
renameFiles(picID)
