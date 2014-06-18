import os
import pdb
import yaml
import datetime
from features import application_path
from lettuce import *
from splinter import Browser
from pyvirtualdisplay import Display

browser = None
headless = True

'''
@before.all
def open_browser():
    if headless:

        display = Display(visible=0)
        display.start()

    global browser
    if not browser:
        print "setting up the splinter browser"
        browser = Browser()
        browser.driver.set_window_size(1640,1000)
        print browser
    
@after.all
def close_browser(scenario):
    browser.quit()


@after.each_scenario
def capture_screenshot(scenario):
    for step in scenario.steps:
        if step.failed:
            now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
            error_screenshots_path = os.path.join(application_path,'error_screenshots')
            get_browser().driver.get_screenshot_as_file(error_screenshots_path+'/%s%s.png' %(step.sentence, now))
            print "Snapshot is taken"
            print "#===========================================================#"
            print step.sentence + ' step failed'
            print "#===========================================================#"

def get_browser():
    print browser
    return browser
'''
