import os
import pdb
import yaml
import datetime
import time
from lettuce import world
from features import application_path
from lettuce import *
from splinter import Browser
from pyvirtualdisplay import Display

browser = None
headless = True

@before.all
def open_browser():
    if headless:
      display = Display(visible=0)
      display.start()

    global browser
    if not browser:
      browser = Browser()
      browser.driver.set_window_size(1640,1000)
      world.browser = browser
@after.all
def close_browser(scenario):
    browser.quit()

@after.each_scenario
def capture_screenshot(scenario):
    for step in scenario.steps:
        if step.failed:
            now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
            error_screenshots_path = os.path.join(application_path,'error_screenshots')
            sentence = step.sentence.replace('\"', "").replace("\'","")
            get_browser().driver.get_screenshot_as_file(error_screenshots_path+'/%s%s.png' %(sentence, now))
            print "Snapshot is taken"
            print "#===========================================================#"
            print step.sentence + ' step failed'
            print "#===========================================================#"

def get_browser():
    return world.browser
