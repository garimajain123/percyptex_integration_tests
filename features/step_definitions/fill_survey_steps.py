from features.support.lettuce_env import *
from features.support.lib.fill_survey_helper import *

@step('I am filling survey')
def visit_survey_url(step):
    get_browser().visit(fetch_urls()['urls']['survey_url'])
    assert 'perceptyx' in get_browser().url
    assert get_browser().is_element_present_by_value(' Proceed ')
    
@step('I select "([^"]*)" as my perfered language')
def select_language(step, language):
    if language == 'English':
      get_browser().find_by_name('lang').first.click()

@step('I click on the "([^"]*)" button')
def click_submit_button(step, button):
    get_browser().find_by_name('submit').click()

@step('I am on the "([^"]*)" page')
def verify_employee_survey_page(step, page):
    assert get_browser().is_text_present('Welcome to the Sample Employee Survey!')
    get_browser().find_by_name('Submit').click()

@step('I started filling 1st page of the survey')
def fill_survey_first_page(step):
    assert get_browser().is_text_present('Employee Surgarimsfssvey')
    fill_survey_form(10, 0)

@step('I fill the 2nd page')
def fill_survey_second_page(step):
    assert get_browser().is_text_present('Page 2 of 5')
    fill_survey_form(10, 1)

@step('I fill the 3rd page')
def fill_survey_third_page(step):
    assert get_browser().is_text_present('Page 3 of 5')
    fill_survey_form(10, 2)

@step('I fill the 4th page')
def fill_survey_fourth_page(step):
    assert get_browser().is_text_present('Page 4 of 5')
    fill_survey_form(10, 3)

@step('I fill the 5th page')
def fill_survey_fifth_page(step):
    assert get_browser().is_text_present('Page 5 of 5')
    fill_survey_form(9, 4)

@step('I should see the "Thank you" page')
def verify_thank_you_page(step):
    assert get_browser().is_text_present('Thank you for completing the Sample Employee Survey!')

@step('my total counts in the survey should get updated')
def verify_survey_count(step):
    #we can't know the exact time after which survey count gets updated
    pass
