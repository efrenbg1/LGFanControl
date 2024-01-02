import sys
import ctypes
import time
import clr
import os

# Load DLL for reading temperature
LibreHardwareDLL = os.path.dirname(os.path.abspath(sys.argv[0]))
LibreHardwareDLL = os.path.join(LibreHardwareDLL, "LibreHardwareMonitorLib.dll")
clr.AddReference(LibreHardwareDLL)

# Load DLL for changing fan cooling mode (must have installed the new version of LG Smart Assistant)
clr.AddReference(
    "C:\\Program Files (x86)\\LG Software\\LG Smart Assistant\\WMIConn.dll")
clr.AddReference(
    "C:\\Program Files (x86)\\LG Software\\LG Smart Assistant\\WindowsControl.dll")


# We need admin privileges to read temperature from CPU
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    exit()


# Initialize the classes from the DLLs
if True:
    from LibreHardwareMonitor.Hardware import Computer
    from WindowsControl import LGDeviceController

lg = LGDeviceController()
c = Computer()
c.IsCpuEnabled = True
c.Open()

# Set the last cooling mode state to the currently set one
lastState = lg.Get_SystemTempMode()

# We loop every 15 seconds and change the cooling mode accordingly
while True:

    # Get the sensor for reading the temperature (should be the 30th on the list)
    c.Hardware[0].Update()
    d = c.Hardware[0].Sensors[30]

    # If CPU temperature is greater than 75ºC we switch to Normal mode
    if d.Value > 75 and lastState != 1:
        lg.Set_SystemTempMode(1)
        lastState = 1
    
    # If CPU temperature drops below 60ºC we switch to Silent mode 
    if d.Value < 60 and lastState != 3:
        lg.Set_SystemTempMode(3)
        lastState = 3

    time.sleep(30)
