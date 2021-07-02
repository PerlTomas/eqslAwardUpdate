This python script will help you update all of your awards in eqsl. You do not have to click on more than 100 hyperlinks anymore :-)
The script is made for Firefox but should be easily modified for other browsers following the instructions on selenium webpage referenced below.

Prerequisites:

1. Install Selenium. See https://selenium-python.readthedocs.io/installation.html
2. Install webdriver for your browser described in the same page
3. Find your HamID number used by eqsl. If you go to the award page and copy the hyperlink to 'Standings' on any award, the number is embedded there after the HamIDTo= tag.
Like this: https://www.eqsl.cc/QSLCard/eAwardStandings.cfm?CallsignTo=yourcallsign&HamIDTo=yournumber&Endorsement=eAsia

Call to function:
python bot("yourusername","yourpassword","yourcallsign", "yourhamid")

It will take a couple of minutes to run the script since there is some delay between calls to each award. This is done to reduce the server load.
