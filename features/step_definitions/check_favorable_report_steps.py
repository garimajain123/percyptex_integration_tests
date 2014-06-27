from features.support.lettuce_env import *
from features.support.lib.fill_survey_helper import *

@step('I am logged in to perceptyx')
def login_to_perceptyx(step):
    login('test1', 'user1')

@step('I click on the "([^"]*)" link')
def click_link(step, link):
		assert get_browser().find_link_by_text(link)
		get_browser().find_link_by_text(link).click()
 
@step('I am on the "Favorability Report" page')
def login_to_perceptyx(step):
		assert get_browser().is_text_present("Favorability Report")
		assert 'fav_report' in get_browser().url

@step('there is both a "([^"]*)" and "([^"]*)" tab in top left corner')
def verify_left_corner_tabs(step, tab1, tab2):
		time.sleep(5) #TODO Need to make a proper function for checking element in time intervals
		for tab in [tab1, tab2] : assert get_browser().find_link_by_text(tab)

@step('there is a "([^"]*)" and "([^"]*)" tab in top right corner')
def verify_right_corner_tabs(step, tab1, tab2):
		for id_count, tab in enumerate([tab1, tab2]):
				assert get_browser().find_by_id("ui-id-%s"%(id_count+1)).text == tab

@step('I am on the "Questions" tab')
def login_to_perceptyx(step):
		get_browser().find_link_by_text("Questions").click()

@step('the Fav score for question 1 is "([^"]*)"')
def verify_fav_score_for_question(step, fav_score):
    assert get_browser().find_by_css('.data.standalone.stripe.q_00_01 .calc-value').first.text == fav_score

@step('the Neutral score for question 1 is "([^"]*)"')
def verify_neutral_score_for_question(step, neutral_score):
    assert get_browser().find_by_css('.data.standalone.stripe.q_00_01 .calc-value')[1].text == neutral_score

@step('the Unfav score for question 1 is "([^"]*)"')
def verify_unfav_score_for_question(step, unfav_score):
    assert get_browser().find_by_css('.data.standalone.stripe.q_00_01 .calc-value')[2].text == unfav_score

@step('the Overall Average at the bottom has a Fav score of "([^"]*)"')
def verify_fav_score_average(step, fav_score_average):
    assert get_browser().find_by_css('.data.standalone.average.q_last .calc-value').first.text == fav_score_average

@step('the Overall Average neutral score is "([^"]*)"')
def verify_neutral_score_average(step, neutral_score_average):
    assert get_browser().find_by_css('.data.standalone.average.q_last .calc-value')[1].text == neutral_score_average

@step('the Overall Average Unfav score is "([^"]*)"')
def verify_unfav_score_average(step, unfav_score_average):
    assert get_browser().find_by_css('.data.standalone.average.q_last .calc-value')[2].text == unfav_score_average

@step('I go into the "Categories" tab')
def click_categories_tab(step):
    get_browser().find_link_by_text('Categories').click()

@step('I go into the "Compared to 2011 Trend" tab')
def click_comparison_tab(step):
		get_browser().find_by_id('ui-id-2').click()

@step('the Fav score for Clarity of Direction is "([^"]*)"')
def verify_fav_score_for_category(step, fav_score):
		assert get_browser().find_by_css('.data.category.stripe.q_1 .calc-value').first.text == fav_score

@step('the Neutral score for Clarity of Direction is "([^"]*)"')
def verify_neutral_score_for_category(step, neutral_score):
    assert get_browser().find_by_css('.data.category.stripe.q_1 .calc-value')[1].text == neutral_score

@step('the Unfav score for Clarity of Direction is "([^"]*)"')
def verify_unfav_score_for_category(step, unfav_score):
    assert get_browser().find_by_css('.data.category.stripe.q_1 .calc-value')[2].text == unfav_score

@step('the Trend Fav score for Clarity of Direction is "([^"]*)"')
def verify_fav_score_for_comparison(step, fav_score):
		time.sleep(20) #TODO Need to make a proper function for checking element in time intervals
		assert get_browser().find_by_css('.data.category.stripe.q_1 .comparison.number').first.text == fav_score
    
@step('the Trend Neutral score for Clarity of Direction is "([^"]*)"')
def verify_neutral_score_for_comparison(step, neutral_score):
    assert get_browser().find_by_css('.data.category.stripe.q_1 .comparison.number')[1].text == neutral_score

@step('the Trend Unfav score for Clarity of Direction is "([^"]*)"')
def verify_unfav_score_for_comparison(step, unfav_score):
    assert get_browser().find_by_css('.data.category.stripe.q_1 .comparison.number')[2].text == unfav_score
