#Import required Library
from cores.colors import Backcolor
import subprocess
import time
import re

#Create object from Backcolor
bc = Backcolor()

#Setting class containing setting methods
class Setting:

    #Store setting into file named touchpad.txt
    def set_touchpad_name(self, touchpad_name):
        try:
            f = open("settings/touchpad.txt","w")
            f.write(touchpad_name)
            f.close()
        except FileNotFoundError as message:
            print(str(message) + " \nPlease create touchpad.txt file into settings folder")

    #Store setting into file named mouse.txt
    def set_mouse_name(self,mouse_name):
        try:
            f = open("settings/mouse.txt","w")
            f.write(mouse_name)
            f.close()
        except FileNotFoundError as message:
            print(str(message) + "\nPlease create mouse.txt file into settings folder")

#Read class containing reading setting methods
class Read:

    #Return content of touchpad.txt
    def read_touchpad_name(self):
        try:
            line = 0
            contents = []
            f = open("settings/touchpad.txt","r")
            for content in f:
                line += 1
                contents.append(content.strip("\n\r"))
                if line > 0:
                    break
            return contents[0]
        except FileNotFoundError as message:
            print(str(message) + " \nPlease create touchpad.txt file into settings folder")

    #Return content of mouse.txt
    def read_mouse_name(self):
        try:
            line = 0
            contents = []
            f = open("settings/mouse.txt","r")
            for content in f:
                line += 1
                contents.append(content.strip("\n\r"))
                if line > 0:
                    break
            return contents[0]
        except FileNotFoundError as message:
            print(str(message) + " \nPlease create mouse.txt file into settings folder")

#Driver class containing important functions
class Driver:

    id = 0
    status = 0
    existence = False

    #Get device current id
    def current_id(self):

        regex = re.compile(r'\d+')

        cid = subprocess.Popen(['xinput','list','--id-only',str(Read().read_touchpad_name())],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        cid_output, cid_err = cid.communicate()
        cid_output_decoded = cid_output.decode("utf-8")
        cid_result = re.findall(regex, cid_output_decoded)
        for result in cid_result:
            self.id = result
        return self.id

    #Get device current status
    def current_status(self):

        regex = re.compile(r'(Device Enabled)\s*(.*):\s*(\d+)')
        regex2 = re.compile(r'\d+')

        cst = subprocess.Popen(['xinput','list-props',str(self.id)],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        cst_output, cst_err = cst.communicate()
        cst_output_decoded = cst_output.decode("utf-8")
        cst_result = re.findall(regex, str(cst_output_decoded))
        cst_result2 = re.findall(regex2, str(cst_result))
        result = []
        for status in cst_result2:
            result.append(status)
        return result[1]

    #Check is mouse exists or not
    def mouse_existence(self):

        mexist = subprocess.Popen(['xinput','list'],
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)
        mexist_output, mexist_err = mexist.communicate()
        mexist_output_decoded = mexist_output.decode("utf-8")
        if Read().read_mouse_name() in mexist_output_decoded:
            self.existence = True
            return self.existence
        elif Read().read_mouse_name() not in mexist_output_decoded:
            self.existence = False
            return self.existence
        else:
            self.existence = None
            return self.existence

    #Turning on touchpad
    def turnon_touchpad(self):

        execute_command = subprocess.Popen(['xinput','enable',str(self.id)],
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE)
        print(bc.RED+"No mouse detected"+bc.END + " => " + bc.GREEN+"Touchpad Enabled"+bc.END+" "+str(time.asctime(time.localtime(time.time()))))

    #Turning of touchpad
    def turnoff_touchpad(self):

        execute_command = subprocess.Popen(['xinput','disable',str(self.id)],
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE)
        print(bc.GREEN+"Mouse detected"+bc.END + " => " + bc.RED+"Touchpad Disabled"+bc.END+" "+str(time.asctime(time.localtime(time.time()))))
