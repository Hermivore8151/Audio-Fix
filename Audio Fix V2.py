import pycaw.pycaw as pycaw
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import time

print("Program Started")

# Check if Windows is muted
def is_system_muted(): # Currently not in use, uncomment line 17, 18 to enable
    devices = pycaw.AudioUtilities.GetSpeakers()
    interface = devices.Activate(pycaw.IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(pycaw.IAudioEndpointVolume))
    return volume.GetMute()

# Get the system volume
def get_volume():
    #if is_system_muted():
    #    return 0.0  # Return zero if the system is muted
    devices = pycaw.AudioUtilities.GetSpeakers()
    interface = devices.Activate(pycaw.IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(pycaw.IAudioEndpointVolume))
    return volume.GetMasterVolumeLevelScalar()

# Function to set the application volume
def set_volume(application_name, volume):
    sessions = pycaw.AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process and session.Process.name() == application_name:
            volume_control = session.SimpleAudioVolume
            volume_control.SetMasterVolume(volume, None)

# Call get_active()
volume_old = 0
while True:
    try:
        volume = get_volume()
        if volume != volume_old:
            sessions = pycaw.AudioUtilities.GetAllSessions()
            for session in sessions:
                if session.Process and session.Process.name():
                    set_volume(session.Process.name(), volume)
        volume_old = volume
        time.sleep(0.5)
    except Exception as e:
        print(e)