# Import required Library and modules
from cores.colors import Backcolor
from cores.driver import Driver
from cores.driver import Setting
from cores.driver import Read
import optparse
import time
import sys

# Create object from Backcolor
bc = Backcolor()
# Create object from driver.Setting
st = Setting()
# Create object from driver.Read
rd = Read()
# Create object from driver.Driver
drv = Driver()

# start function used to start the driver and
# keep running to detecting device
def start(trigger):
    if trigger:
        while trigger:
            drv.current_id()
            drv.current_status()
            if drv.mouse_existence():
                drv.turnoff_touchpad()
            else:
                drv.turnon_touchpad()
            time.sleep(1)

# Main function of the program
def Main():

    # Option parser
    parser = optparse.OptionParser("Usage %prog <opt> <value in string format>", version="%prog 2.0.0")

    parser.add_option("--touchpad", dest="touchpad_name",type="string",\
    help="Set touchpad name into setting file")

    parser.add_option("--mouse", dest="mouse_name", type="string",\
    help="Set mouse name into setting file")

    parser.add_option("--checkt", action="store_true", dest="chckt",\
    default=False, help="Check touchpad name has been set into setting file")

    parser.add_option("--checkm", action="store_true", dest="chckm",\
    default=False, help="Check mouse name has been set into setting file")

    parser.add_option("--both", action="store_true", dest="chckb",\
    default=False, help="Check touchpad name and mouse name has been set into setting file")

    parser.add_option("--ok", action="store_true",dest="trigger",\
    default=False, help="Start or Run the driver")

    (options, args) = parser.parse_args()

    # Controls the program
    if(options.touchpad_name) != None:
        st.set_touchpad_name(options.touchpad_name)
        sys.exit(0)
    elif(options.mouse_name) != None:
        st.set_mouse_name(options.mouse_name)
        sys.exit(0)
    elif(options.chckt) != False:
        print(rd.read_touchpad_name())
        sys.exit(0)
    elif(options.chckm) != False:
        print(rd.read_mouse_name())
        sys.exit(0)
    elif(options.chckb) != False:
        print("Touchpad name    :   " + rd.read_touchpad_name())
        print("Mouse name       :   " + rd.read_mouse_name())
        sys.exit(0)
    elif(options.trigger) != False:
        start(options.trigger)
    else:
        pass


if __name__ == "__main__":
    try:
        Main()
    except KeyboardInterrupt as message:
        print(str(message))
        sys.exit(0)
