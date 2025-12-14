# Use Only in case of emergency shutdown een though it might not work with site, if desperate need of shutdown, use Render Admin Dashboard
#!/bin/env/python
import os
dev_actions = {"Complete Shutdown", "Run Manual Check"}
warning = input("Are you sure you want to continue, this is a very dangerous panel")
admin_pin = "OSPANELPINPASSWORDBOTTLEDMOMENTSADMIN"
is_the_pin = input("What is the OS panel pin?")
if (is_the_pin != "OSPANELPINPASSWORDBOTTLEDMOMENTSADMIN"):
  print("That is not the pin, stop using the ADMIN console before something breaks")
def(continue_process):
  if(is_the_pin == "OSPANELPINPASSWORDBOTTLEDMOMENTSADMIN"):
    choice = input("Choose your action" + dev_actions)
    if(choice == "Complete Shutdown"):
      os.system("sudo shutdown now")
    if(choice == "Run manual check"):
      os.system("man man")
if __name__ == "__main__":
  continue_process()

  
