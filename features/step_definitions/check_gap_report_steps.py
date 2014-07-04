from features.support.lettuce_env import *
from features.support.lib.fill_survey_helper import *

@step('I am logged in to perceptyx')
def login_to_perceptyx(step):
    login('test1', 'user1')

@step('I click on the "Gap Report" link')
def click_link(step):
		link = fetch_urls()['urls']['gap_report_url']
		assert get_browser().find_link_by_href(link)
		get_browser().find_link_by_href(link).click()

@step('I am on the "Gap Report" page')
def verify_right_page_to_test(step):
		assert get_browser().is_text_present("Gap Report")
		assert 'gap_report' in get_browser().url

@step('there is both "([^"]*)" and "([^"]*)" tab in top left corner')
def verify_left_corner_tabs(step, tab1, tab2):
		time.sleep(8) #TODO Need to make a proper function for checking element in time intervals
		for tab in [tab1, tab2] : assert get_browser().find_link_by_text(tab)

@step('there is both "([^"]*)" and "([^"]*)" tab in top right corner')
def verify_right_corner_tabs(step, tab1, tab2):
    assert get_browser().find_by_id("ui-id-1").text == tab1
    assert get_browser().find_by_id("ui-id-3").text == tab2

@step('I am on the "Questions" tab')
def click_to_go_to_question_tab(step):
		get_browser().find_link_by_text("Questions").click()

@step('the Evaluation Score for question 2 is "([^"]*)"')
def verify_eval_avg_for_question2(step, eval_avg):
    assert get_browser().find_by_css('.data.standalone.qid-00_02 .value.centred  .sort-eval.number.calc-value').first.text == eval_avg

@step('the Importance Score for question 2 is "([^"]*)"')
def verify_importance_for_question2(step, importance):
    assert get_browser().find_by_css('.data.standalone.qid-00_02 .value.centred  .sort-imp.number.calc-value').first.text == importance

@step('the Gap Score for question 2 is "([^"]*)"')
def verify_gap_score_for_question2(step, gap):
    assert get_browser().find_by_css('.data.standalone.qid-00_02 .value.centred  .sort-gap.number.calc-value').first.text == gap

@step('the Weighted Gap Score for question 2 is "([^"]*)"')
def verify_weighted_gap_for_question2(step, weighted_gap):
    assert get_browser().find_by_css('.data.standalone.qid-00_02 .value.centred  .sort-wgi.number.calc-value').first.text == weighted_gap

@step('the Evaluation Score for question 10 is "([^"]*)"')
def verify_eval_avg_for_question10(step, eval_avg):
    assert get_browser().find_by_css('.data.standalone.qid-00_11 .value.centred  .sort-eval.number.calc-value').first.text == eval_avg

@step('the Importance Score for question 10 is "([^"]*)"')
def verify_importance_for_question10(step, importance):
    assert get_browser().find_by_css('.data.standalone.qid-00_11 .value.centred  .sort-imp.number.calc-value').first.text == importance

@step('the Gap Score for question 10 is "([^"]*)"')
def verify_gap_for_question10(step, gap_score):
    assert get_browser().find_by_css('.data.standalone.qid-00_11 .value.centred  .sort-gap.number.calc-value').first.text == gap_score

@step('the Weighted Gap Score for question 10 is "([^"]*)"')
def verify_weighted_gap_for_question10(step, weighted_gap):
    assert get_browser().find_by_css('.data.standalone.qid-00_11 .value.centred  .sort-wgi.number.calc-value').first.text == weighted_gap

@step('I go into "Categories" tab')
def click_categories_tab(step):
    if get_browser().find_link_by_text('Categories') > 1:
      get_browser().find_link_by_text('Categories').last.click()
    else:
      get_browser().find_link_by_text('Categories').first.click()

@step('I go into "Questions" tab')
def click_categories_tab(step):
    get_browser().find_link_by_text('Questions').click()

@step('I go into "Compared to 2011 Trend" tab')
def click_comparison_tab(step):
		get_browser().find_by_id('ui-id-3').click()

@step('the Evaluation score for Clarity of Direction is "([^"]*)"')
def verify_evaluation_score_for_clarity_of_direction(step, eval_score):
    assert get_browser().find_by_css('.data.category.stripe.qid-1 .value.centred  .sort-eval.number.calc-value').first.text == eval_score

@step('the Importance score for Clarity of Direction is "([^"]*)"')
def verify_importance_score_for_clarity_of_direction(step, importance_score):
    assert get_browser().find_by_css('.data.category.stripe.qid-1 .value.centred  .sort-imp.number.calc-value').first.text == importance_score

@step('the Gap Score for Clarity of Direction is "([^"]*)"')
def verify_gap_score_for_clarity_of_direction(step, gap_score):
    assert get_browser().find_by_css('.data.category.stripe.qid-1 .value.centred  .sort-gap.number.calc-value').first.text == gap_score

@step('the Weighted Gap Score for Clarity of Direction is "([^"]*)"')
def verify_weighted_gap_score_for_clarity_of_direction(step, weighted_gap_score):
    assert get_browser().find_by_css('.data.category.stripe.qid-1 .value.centred  .sort-wgi.number.calc-value').first.text == weighted_gap_score

@step('the Evaluation score for My Manager is "([^"]*)"')
def verify_evaluation_score_for_my_manager(step, eval_score):
    assert get_browser().find_by_css('.data.category.stripe.qid-3 .value.centred  .sort-eval.number.calc-value').first.text == eval_score

@step('the Importance score for My Manager is "([^"]*)"')
def verify_importance_score_for_my_manager(step, importance_score):
    assert get_browser().find_by_css('.data.category.stripe.qid-3 .value.centred  .sort-imp.number.calc-value').first.text == importance_score

@step('the Gap Score for My Manager is "([^"]*)"')
def verify_gap_score_for_my_manager(step, gap_score):
    assert get_browser().find_by_css('.data.category.stripe.qid-3 .value.centred  .sort-gap.number.calc-value').first.text == gap_score

@step('the Weighted Gap Score for My Manager is "([^"]*)"')
def verify_weighted_gap_score_for_my_manager(step, weighted_gap_score):
    assert get_browser().find_by_css('.data.category.stripe.qid-3 .value.centred  .sort-wgi.number.calc-value').first.text == weighted_gap_score

@step('the Evaluation Score for question 6 is "([^"]*)"')
def the_evaluation_score_for_question6_is(step, evaluation_score):
    time.sleep(10) #TODO Need to make a proper function for checking element in time intervals
    assert get_browser().find_by_css('.data.standalone.qid-00_07 .calc-value')[4].text == evaluation_score

@step('the Evaluation Trend Score for question 6 is "([^"]*)"')
def the_evaluation_trend_score_for_question6_is(step, evaluation_trend_score):
    assert get_browser().find_by_css('.data.standalone.qid-00_07 .sort-eval.number')[1].text == evaluation_trend_score

@step('the Importance Score for question 6 is "([^"]*)"')
def the_importance_score_for_question6_is(step, importance_score):
    assert get_browser().find_by_css('.data.standalone.qid-00_07 .calc-value')[5].text == importance_score

@step('the Importance Trend Score for question 6 is "([^"]*)"')
def the_importance_trend_score_for_question6_is(step, importance_trend_score):
    assert get_browser().find_by_css('.data.standalone.qid-00_07 .sort-imp.number')[1].text == importance_trend_score

@step('the Gap Score for question 6 is "([^"]*)"')
def the_gap_score_for_question6_is(step, gap_score):
    assert get_browser().find_by_css('.data.standalone.qid-00_07 .calc-value')[6].text == gap_score

@step('the Gap Trend Score for question 6 is "([^"]*)"')
def the_gap_trend_score_for_question6_is(step, gap_trend_score):
    assert get_browser().find_by_css('.data.standalone.qid-00_07 .sort-gap.number')[1].text == gap_trend_score

@step('the Weighted Gap Score for question 6 is "([^"]*)"')
def the_weighted_gap_score_for_question6_is(step, weighted_gap_score):
    assert get_browser().find_by_css('.data.standalone.qid-00_07 .calc-value')[7].text == weighted_gap_score

@step('the Weighted Gap Trend Score for question 6 is "([^"]*)"')
def the_weighted_gap_trend_score_for_question6_is(step, weighted_gap_trend_score):
    assert get_browser().find_by_css('.data.standalone.qid-00_07 .sort-wgi.number')[1].text == weighted_gap_trend_score

@step('the Evaluation Score for question 4 is "([^"]*)"')
def the_evaluation_score_for_question4_is(step, evaluation_score):
    time.sleep(10) #TODO Need to make a proper function for checking element in time intervals
    assert get_browser().find_by_css('.data.category.qid-4  .calc-value')[4].text == evaluation_score

@step('the Evaluation Trend Score for question 4 is "([^"]*)"')
def the_evaluation_trend_score_for_question4_is(step, evaluation_trend_score):
    assert get_browser().find_by_css('.data.category.qid-4 .sort-eval.number')[1].text == evaluation_trend_score

@step('the Importance Score for question 4 is "([^"]*)"')
def the_importance_score_for_question4_is(step, importance_score):
    assert get_browser().find_by_css('.data.category.qid-4 .calc-value')[5].text == importance_score

@step('the Importance Trend Score for question 4 is  "([^"]*)"')
def the_importance_trend_score_for_question4_is(step, importance_trend_score):
    assert get_browser().find_by_css('.data.category.qid-4 .sort-imp.number')[1].text == importance_trend_score

@step('the Gap Score for question 4 is "([^"]*)"')
def the_gap_score_for_question4_is(step, gap_score):
    assert get_browser().find_by_css('.data.category.qid-4 .calc-value')[6].text == gap_score

@step('the Gap Trend Score for question 4 is "([^"]*)"')
def the_gap_trend_score_for_question4_is(step, gap_trend_score):
    assert get_browser().find_by_css('.data.category.qid-4 .sort-gap.number')[1].text == gap_trend_score

@step('the Weighted Gap Score for question 4 is "([^"]*)"')
def the_weighted_gap_score_for_question4_is(step, weighted_gap_score):
    assert get_browser().find_by_css('.data.category.qid-4 .calc-value')[7].text == weighted_gap_score

@step('the Weighted Gap Trend Score for question 4 is "([^"]*)"')
def the_weighted_gap_trend_score_for_question4_is(step, weighted_gap_trend_score):
    assert get_browser().find_by_css('.data.category.qid-4 .sort-wgi.number')[1].text == weighted_gap_trend_score

@step('I go to "Logout"')
def click_on_logout(step):
    get_browser().find_link_by_text('Functions').click()
    assert get_browser().find_by_css(".functions_icon .first .menuitem a").first.text == 'Logout'
    get_browser().find_by_css(".functions_icon .first .menuitem a").first.click()
    for text in ['Username', 'Password'] : assert get_browser().is_text_present(text)

@step('I click on the "Filter Data" link')
def click_on_filter_data(step):
    get_browser().find_by_css(".menuitem.topitem .menulink").click()
    time.sleep(2) #TODO Need to make a proper function for checking element in time intervals
    assert get_browser().find_by_css(".menuitem.topitem .level1.one_col.icons .first .new_segment").text == 'New Filter'
    get_browser().find_by_css(".menuitem.topitem .level1.one_col.icons .first .new_segment").click()
    assert get_browser().is_element_present_by_css('.ui-dialog-content.ui-widget-content')

@step('I applied a filter on Country "China"')
def apply_country_filter(step):
    get_browser().select("q", "01_02_07")
    time.sleep(3) #TODO Need to make a proper function for checking element in time intervals
    assert get_browser().is_text_present('Step 2')
    get_browser().select("q0", "4")
    time.sleep(3) #TODO Need to make a proper function for checking element in time intervals
    assert get_browser().is_text_present('Step 3')

@step('the filter count is "71"')
def filter_count(step):
    assert get_browser().find_by_css("#segment-count .status_title").text == 'Count:'
    assert get_browser().find_by_css("#segment-count .segment-count-text").text == '71'

@step('I submit the filter data')
def submit_filter_data(step):
    get_browser().find_by_css(".submit_btn").click()
    
@step('I am on the "Gap" report page')
def submit_filter_data(step):
    assert get_browser().is_text_present('Gap Report')

@step('the Evaluation Score for question 3 is "([^"]*)"')
def verify_eval_avg_for_question3(step, eval_avg):
    assert get_browser().find_by_css('.data.standalone.qid-00_03 .value.centred  .sort-eval.number.calc-value').first.text == eval_avg

@step('the Importance Score for question 3 is "([^"]*)"')
def verify_importance_for_question3(step, importance):
    assert get_browser().find_by_css('.data.standalone.qid-00_03 .value.centred  .sort-imp.number.calc-value').first.text == importance

@step('the Gap Score for question 3 is "([^"]*)"')
def verify_gap_score_for_question3(step, gap):
    assert get_browser().find_by_css('.data.standalone.qid-00_03 .value.centred  .sort-gap.number.calc-value').first.text == gap

@step('the Weighted Gap Score for question 3 is "([^"]*)"')
def verify_weighted_gap_for_question3(step, weighted_gap):
    assert get_browser().find_by_css('.data.standalone.qid-00_03 .value.centred  .sort-wgi.number.calc-value').first.text == weighted_gap

@step('the Evaluation Score for question 8 is "([^"]*)"')
def verify_eval_avg_for_question8(step, eval_avg):
    assert get_browser().find_by_css('.data.standalone.qid-00_08 .value.centred  .sort-eval.number.calc-value').first.text == eval_avg

@step('the Importance Score for question 8 is "([^"]*)"')
def verify_importance_for_question8(step, importance):
    assert get_browser().find_by_css('.data.standalone.qid-00_08 .value.centred  .sort-imp.number.calc-value').first.text == importance

@step('the Gap Score for question 8 is "([^"]*)"')
def verify_gap_score_for_question8(step, gap):
    assert get_browser().find_by_css('.data.standalone.qid-00_08 .value.centred  .sort-gap.number.calc-value').first.text == gap

@step('the Weighted Gap Score for question 8 is "([^"]*)"')
def verify_weighted_gap_for_question8(step, weighted_gap):
    assert get_browser().find_by_css('.data.standalone.qid-00_08 .value.centred  .sort-wgi.number.calc-value').first.text == weighted_gap    

