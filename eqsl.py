# https://selenium-python.readthedocs.io/index.html

from selenium import webdriver # Used to import the driver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
options = Options()
options.add_argument('--headless') # Hides the browser window

import time
import random

def bot(usr,pas,callsign, hamid):
    
    br=webdriver.Firefox(options=options) # Modify this line if you are using other browser than Firefox
    br.get("https://www.eqsl.cc/QSLCard/Home4G.cfm")
    user=br.find_element_by_name("Callsign") 
    user.clear()
    user.send_keys(usr) # Fill the user box by given username
    pasd=br.find_element_by_name("EnteredPassword")
    pasd.clear()
    pasd.send_keys(pas) # Fill the password box with password 
    btn=br.find_element_by_name("Login")
    btn.click() # Click the button 

    time.sleep(10) # Not sure if this is necessary but we are not in a hurry are we?

    baseurl="https://www.eqsl.cc/QSLCard/eAwardStandings.cfm?CallsignTo="+callsign+"&HamIDTo="+hamid+"&Endorsement="
    # Read file with award names
    AwardFile=open("AwardNames.txt",'r')
    Awards=AwardFile.readlines()
    AwardFile.close()
    AwardList=[]
    
    for Award in Awards:
        AwardList.append(Award.strip()) # Remove \n
    
    for Award in AwardList: 
        jitter=random.randint(15,30) # Jitter the time between calls
        print(Award)
        br.get(baseurl+Award)
        try: # Handle 'exceptions' https://stackoverflow.com/questions/19200497/python-selenium-webscraping-nosuchelementexception-not-recognized
            updatebtn=br.find_element_by_css_selector("input[value='Update MyAwards Page']")
            updatebtn.click()
        except NoSuchElementException:
            print(Award+' not updated')
        time.sleep(jitter) # Wait between calls to not overload server
    br.quit()
#main driver code

bot("yourusername","yourpassword","yourcallsign", "yourhamid")

