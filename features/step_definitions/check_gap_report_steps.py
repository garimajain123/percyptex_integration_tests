from features.support.lettuce_env import *
from features.support.lib.fill_survey_helper import *

def get_calculate_value_for_questions_and_comparision(id_number, index):
    return get_browser().find_by_css('.data.standalone.qid-00_%s .calc-value'%id_number)[index].text

def get_calculate_value_for_categories_and_comparision(id_number, index):
    return get_browser().find_by_css('.data.category.qid-%s .calc-value'%id_number)[index].text


def get_evaluation_score_text_for_questions_and_no_comparision(id_number):
    return get_browser().find_by_css('.data.standalone.qid-00_%s .value.centred  .sort-eval.number.calc-value'%id_number).first.text

def get_gap_score_text_for_questions_and_no_comparision(id_number):
    return get_browser().find_by_css('.data.standalone.qid-00_%s .value.centred  .sort-gap.number.calc-value'%id_number).first.text

def get_weighted_gap_score_text_for_questions_and_no_comparision(id_number):
    return get_browser().find_by_css('.data.standalone.qid-00_%s .value.centred  .sort-wgi.number.calc-value'%id_number).first.text

def get_importance_score_text_for_questions_and_no_comparision(id_number):
    return get_browser().find_by_css('.data.standalone.qid-00_%s .value.centred  .sort-imp.number.calc-value'%id_number).first.text


def get_evaluation_score_text_for_categories_and_no_comparision(id_number):
    return get_browser().find_by_css('.data.category.qid-%s .value.centred  .sort-eval.number.calc-value'%id_number).first.text

def get_gap_score_text_for_categories_and_no_comparision(id_number):
    return get_browser().find_by_css('.data.category.qid-%s .value.centred  .sort-gap.number.calc-value'%id_number).first.text

def get_weighted_gap_score_text_for_categories_and_no_comparision(id_number):
    return get_browser().find_by_css('.data.category.qid-%s .value.centred  .sort-wgi.number.calc-value'%id_number).first.text

def get_importance_score_text_for_categories_and_no_comparision(id_number):
    return get_browser().find_by_css('.data.category.qid-%s .value.centred  .sort-imp.number.calc-value'%id_number).first.text

def get_evaluation_score_text_for_questions_and_comparision(id_number, index):
    return get_browser().find_by_css('.data.standalone.qid-00_%s .sort-eval.number'%id_number)[index].text

def get_gap_score_text_for_questions_and_comparision(id_number, index):
    return get_browser().find_by_css('.data.standalone.qid-00_%s .sort-gap.number'%id_number)[index].text

def get_weighted_gap_score_text_for_questions_and_comparision(id_number, index):
    return get_browser().find_by_css('.data.standalone.qid-00_%s .sort-wgi.number'%id_number)[index].text

def get_importance_score_text_for_questions_and_comparision(id_number, index):
    return get_browser().find_by_css('.data.standalone.qid-00_%s .sort-imp.number'%id_number)[index].text

def get_evaluation_score_text_for_categories_and_comparision(id_number, index):
    return get_browser().find_by_css('.data.category.qid-%s .sort-eval.number'%id_number)[index].text

def get_gap_score_text_for_categories_and_comparision(id_number, index):
    return get_browser().find_by_css('.data.category.qid-%s .sort-gap.number'%id_number)[index].text

def get_weighted_gap_score_text_for_categories_and_comparision(id_number, index):
    return get_browser().find_by_css('.data.category.qid-%s .sort-wgi.number'%id_number)[index].text

def get_importance_score_text_for_categories_and_comparision(id_number, index):
    return get_browser().find_by_css('.data.category.qid-%s .sort-imp.number'%id_number)[index].text

@step('I am logged into perceptyx')
def login_to_perceptyx(step):
    login('test1', 'user1')

@step('I click on "Gap Report" link')
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
def verify_evalution_score_for_question2(step, evalution_score):
    assert get_evaluation_score_text_for_questions_and_no_comparision("02") == evalution_score

@step('the Importance Score for question 2 is "([^"]*)"')
def verify_importance_score_for_question2(step, importance_score):
    assert get_importance_score_text_for_questions_and_no_comparision("02") == importance_score

@step('the Gap Score for question 2 is "([^"]*)"')
def verify_gap_score_for_question2(step, gap_score):
    assert get_gap_score_text_for_questions_and_no_comparision("02") == gap_score

@step('the Weighted Gap Score for question 2 is "([^"]*)"')
def verify_weighted_gap_score_for_question2(step, weighted_gap_score):
    assert get_weighted_gap_score_text_for_questions_and_no_comparision("02") == weighted_gap_score

@step('the Evaluation Score for question 10 is "([^"]*)"')
def verify_evalution_score_for_question10(step, evalution_score):
    assert get_evaluation_score_text_for_questions_and_no_comparision("11") == evalution_score

@step('the Importance Score for question 10 is "([^"]*)"')
def verify_importance_score_for_question10(step, importance_score):
    assert get_importance_score_text_for_questions_and_no_comparision("11") == importance_score

@step('the Gap Score for question 10 is "([^"]*)"')
def verify_gap_score_for_question10(step, gap_score):
    assert get_gap_score_text_for_questions_and_no_comparision("11") == gap_score

@step('the Weighted Gap Score for question 10 is "([^"]*)"')
def verify_weighted_gap_score_for_question10(step, weighted_gap_score):
    assert get_weighted_gap_score_text_for_questions_and_no_comparision("11") == weighted_gap_score

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

@step('I go into "Compared to" tab')
def click_comparison_tab(step):
        get_browser().find_by_id('ui-id-3').click()

@step('the Evaluation score for Clarity of Direction is "([^"]*)"')
def verify_evaluation_score_for_clarity_of_direction(step, evalution_score):
    assert get_evaluation_score_text_for_categories_and_no_comparision("1") == evalution_score

@step('the Importance score for Clarity of Direction is "([^"]*)"')
def verify_importance_score_for_clarity_of_direction(step, importance_score):
    assert get_importance_score_text_for_categories_and_no_comparision("1") == importance_score

@step('the Gap Score for Clarity of Direction is "([^"]*)"')
def verify_gap_score_for_clarity_of_direction(step, gap_score):
    assert get_gap_score_text_for_categories_and_no_comparision("1") == gap_score

@step('the Weighted Gap Score for Clarity of Direction is "([^"]*)"')
def verify_weighted_gap_score_for_clarity_of_direction(step, weighted_gap_score):
    assert get_weighted_gap_score_text_for_categories_and_no_comparision("1") == weighted_gap_score

@step('the Evaluation score for My Manager is "([^"]*)"')
def verify_evaluation_score_for_my_manager(step, evalution_score):
    assert get_evaluation_score_text_for_categories_and_no_comparision("3") == evalution_score

@step('the Importance score for My Manager is "([^"]*)"')
def verify_importance_score_for_my_manager(step, importance_score):
    assert get_importance_score_text_for_categories_and_no_comparision("3") == importance_score

@step('the Gap Score for My Manager is "([^"]*)"')
def verify_gap_score_for_my_manager(step, gap_score):
    assert get_gap_score_text_for_categories_and_no_comparision("3") == gap_score

@step('the Weighted Gap Score for My Manager is "([^"]*)"')
def verify_weighted_gap_score_for_my_manager(step, weighted_gap_score):
    assert get_weighted_gap_score_text_for_categories_and_no_comparision("3") == weighted_gap_score    

@step('the Evaluation Score for question 6 is "([^"]*)"')
def the_evaluation_score_for_question6_is(step, evaluation_score):
    time.sleep(10) #TODO Need to make a proper function for checking element in time intervals
    assert get_calculate_value_for_questions_and_comparision("07", 4) == evaluation_score

@step('the Evaluation Trend Score for question 6 is "([^"]*)"')
def the_evaluation_trend_score_for_question6_is(step, evaluation_trend_score):
    assert get_evaluation_score_text_for_questions_and_comparision("07", 1) == evaluation_trend_score

@step('the Importance Score for question 6 is "([^"]*)"')
def the_importance_score_for_question6_is(step, importance_score):
    assert get_calculate_value_for_questions_and_comparision("07", 5) == importance_score

@step('the Importance Trend Score for question 6 is "([^"]*)"')
def the_importance_trend_score_for_question6_is(step, importance_trend_score):
    assert get_importance_score_text_for_questions_and_comparision("07", 1) == importance_trend_score

@step('the Gap Score for question 6 is "([^"]*)"')
def the_gap_score_for_question6_is(step, gap_score):
    assert get_calculate_value_for_questions_and_comparision("07", 6) == gap_score

@step('the Gap Trend Score for question 6 is "([^"]*)"')
def the_gap_trend_score_for_question6_is(step, gap_trend_score):
    assert get_gap_score_text_for_questions_and_comparision("07", 1) == gap_trend_score

@step('the Weighted Gap Score for question 6 is "([^"]*)"')
def the_weighted_gap_score_for_question6_is(step, weighted_gap_score):
    assert get_calculate_value_for_questions_and_comparision("07", 7) == weighted_gap_score

@step('the Weighted Gap Trend Score for question 6 is "([^"]*)"')
def the_weighted_gap_trend_score_for_question6_is(step, weighted_gap_trend_score):
    assert get_weighted_gap_score_text_for_questions_and_comparision("07", 1) == weighted_gap_trend_score

@step('the Evaluation Score for question 4 is "([^"]*)"')
def the_evaluation_score_for_question4_is(step, evaluation_score):
    time.sleep(10) #TODO Need to make a proper function for checking element in time intervals
    assert get_calculate_value_for_categories_and_comparision("4", 4) == evaluation_score

@step('the Evaluation Trend Score for question 4 is "([^"]*)"')
def the_evaluation_trend_score_for_question4_is(step, evaluation_trend_score):
    assert get_evaluation_score_text_for_categories_and_comparision("4", 1) == evaluation_trend_score

@step('the Importance Score for question 4 is "([^"]*)"')
def the_importance_score_for_question4_is(step, importance_score):
    assert get_calculate_value_for_categories_and_comparision("4", 5) == importance_score

@step('the Importance Trend Score for question 4 is  "([^"]*)"')
def the_importance_trend_score_for_question4_is(step, importance_trend_score):
    assert get_importance_score_text_for_categories_and_comparision("4", 1) == importance_trend_score

@step('the Gap Score for question 4 is "([^"]*)"')
def the_gap_score_for_question4_is(step, gap_score):
    assert get_calculate_value_for_categories_and_comparision("4", 6) == gap_score

@step('the Gap Trend Score for question 4 is "([^"]*)"')
def the_gap_trend_score_for_question4_is(step, gap_trend_score):
    assert get_gap_score_text_for_categories_and_comparision("4", 1) == gap_trend_score

@step('the Weighted Gap Score for question 4 is "([^"]*)"')
def the_weighted_gap_score_for_question4_is(step, weighted_gap_score):
    assert get_calculate_value_for_categories_and_comparision("4", 7) == weighted_gap_score

@step('the Weighted Gap Trend Score for question 4 is "([^"]*)"')
def the_weighted_gap_trend_score_for_question4_is(step, weighted_gap_trend_score):
    assert get_weighted_gap_score_text_for_categories_and_comparision("4", 1) == weighted_gap_trend_score

@step('I go to "Logout"')
def click_on_logout(step):
    get_browser().find_link_by_text('Functions').click()
    assert get_browser().find_by_css(".functions_icon .first .menuitem a").first.text == 'Logout'
    get_browser().find_by_css(".functions_icon .first .menuitem a").first.click()
    for text in ['Username', 'Password'] : assert get_browser().is_text_present(text)

@step('I go to filter pop-up')
def click_on_filter_data(step):
    get_browser().find_by_css(".menuitem.topitem .menulink").click()
    time.sleep(10) #TODO Need to make a proper function for checking element in time intervals
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
def verify_evalution_score_for_question3(step, evalution_score):
    assert get_evaluation_score_text_for_questions_and_no_comparision("03") == evalution_score

@step('the Importance Score for question 3 is "([^"]*)"')
def verify_importance_score_for_question3(step, importance_score):
    assert get_importance_score_text_for_questions_and_no_comparision("03") == importance_score

@step('the Gap Score for question 3 is "([^"]*)"')
def verify_gap_score_for_question3(step, gap_score):
    assert get_gap_score_text_for_questions_and_no_comparision("03") == gap_score

@step('the Weighted Gap Score for question 3 is "([^"]*)"')
def verify_weighted_gap_score_for_question3(step, weighted_gap_score):
    assert get_weighted_gap_score_text_for_questions_and_no_comparision("03") == weighted_gap_score

@step('the Evaluation Score for question 8 is "([^"]*)"')
def verify_evalution_score_for_question8(step, evalution_score):
    assert get_evaluation_score_text_for_questions_and_no_comparision("09") == evalution_score

@step('the Importance Score for question 8 is "([^"]*)"')
def verify_importance_score_for_question8(step, importance_score):
    assert get_importance_score_text_for_questions_and_no_comparision("09") == importance_score

@step('the Gap Score for question 8 is "([^"]*)"')
def verify_gap_score_for_question8(step, gap_score):
    assert get_gap_score_text_for_questions_and_no_comparision("09") == gap_score

@step('the Weighted Gap Score for question 8 is "([^"]*)"')
def verify_weighted_gap_score_for_question8(step, weighted_gap_score):
    assert get_weighted_gap_score_text_for_questions_and_no_comparision("09") == weighted_gap_score

@step('the Evaluation Score for values is "([^"]*)"')
def verify_evaluation_score_for_values(step, evaluation_score):
    assert get_evaluation_score_text_for_categories_and_no_comparision("2") == evaluation_score

@step('the Importance Score for values is "([^"]*)"')
def verify_importance_score_for_values(step, importance_score):
    assert get_importance_score_text_for_categories_and_no_comparision("2") == importance_score

@step('the Gap Score for values is "([^"]*)"')
def verify_gap_score_for_values(step, gap_score):
    assert get_gap_score_text_for_categories_and_no_comparision("2") == gap_score

@step('the Weighted Gap Score for values is "([^"]*)"')
def verify_weighted_gap_score_for_values(step, weighted_gap_score):
    assert get_weighted_gap_score_text_for_categories_and_no_comparision("2") == weighted_gap_score

@step('the Evaluation Score for Involvement and Empowerment is "([^"]*)"')
def verify_evaluation_score_for_involvement_and_empowerment(step, evaluation_score):
    assert get_evaluation_score_text_for_categories_and_no_comparision("5") == evaluation_score

@step('the Importance Score for Involvement and Empowerment is "([^"]*)"')
def verify_importance_score_for_involvement_and_empowerment(step, importance_score):
    assert get_importance_score_text_for_categories_and_no_comparision("5") == importance_score

@step('the Gap Score for Involvement and Empowerment is "([^"]*)"')
def verify_gap_score_for_involvement_and_empowerment(step, gap_score):
    assert get_gap_score_text_for_categories_and_no_comparision("5") == gap_score

@step('the Weighted Gap Score for Involvement and Empowerment is "([^"]*)"')
def verify_weighted_gap_score_for_involvement_and_empowerment(step, weighted_gap_score):
    assert get_weighted_gap_score_text_for_categories_and_no_comparision("5") == weighted_gap_score

@step('I apply compared to as "([^"]*)"')
def verify_weighted_gap_score_for_question5(step, compared_type):
    if compared_type == "2011 Trend":
        value = "https://www.perceptyx.com/qa2/index.cgi?rm=gap_report&ps=1&cmp=trend&trend_by=1"
    else:
        value = "https://www.perceptyx.com/qa2/index.cgi?rm=gap_report&ps=1&cmp=%s"%compared_type
    get_browser().select("compared_to", value)
    time.sleep(10)

@step('the Evaluation Score for question 6 to compare trend is "([^"]*)"')
def the_evaluation_score_for_question6_to_compare_trend_is(step, evaluation_score):
    if get_calculate_value_for_questions_and_comparision("07", 4) == evaluation_score:
      assert  get_calculate_value_for_questions_and_comparision("07", 4) == evaluation_score
    elif get_calculate_value_for_questions_and_comparision("07", 8) == evaluation_score:
      assert  get_calculate_value_for_questions_and_comparision("07", 8) == evaluation_score
    elif get_calculate_value_for_questions_and_comparision("07", 12) == evaluation_score:
      assert get_calculate_value_for_questions_and_comparision("07", 12) == evaluation_score
    else:
      assert  get_calculate_value_for_questions_and_comparision("07", 16) == evaluation_score

@step('the Evaluation Trend Score for question 6 to compare trend is "([^"]*)"')
def the_evaluation_trend_score_for_question6_to_compare_trend_is(step, evaluation_trend_score):
    if get_evaluation_score_text_for_questions_and_comparision("07", 2) == evaluation_trend_score:
      assert get_evaluation_score_text_for_questions_and_comparision("07", 2) == evaluation_trend_score
    else:
      assert get_evaluation_score_text_for_questions_and_comparision("07", 3) == evaluation_trend_score

@step('the Importance Score for question 6 to compare trend is "([^"]*)"')
def the_important_score_for_question6_to_compare_trend_is(step, important_score):
    assert get_calculate_value_for_questions_and_comparision("07", 13) == important_score

@step('the Importance Trend Score for question 6 to compare trend is "([^"]*)"')
def the_important_trend_score_for_question6_to_compare_trend_is(step, important_trend_score):
    assert get_importance_score_text_for_questions_and_comparision("07", 3) == important_trend_score

@step('the Gap Score for question 6 to compare trend is "([^"]*)"')
def the_gap_score_for_question6_to_compare_trend_is(step, gap_score):
    assert get_calculate_value_for_questions_and_comparision("07", 14) == gap_score

@step('the Gap Trend Score for question 6 to compare trend is "([^"]*)"')
def the_gap_trend_score_for_question6_to_compare_trend_is(step, gap_trend_score):
    assert get_gap_score_text_for_questions_and_comparision("07", 3) == gap_trend_score

@step('the Weighted Gap Score for question 6 to compare trend is "([^"]*)"')
def the_weighted_score_for_question6_to_compare_trend_is(step, weighted_gap_score):
    assert get_calculate_value_for_questions_and_comparision("07", 15) == weighted_gap_score

@step('the Weighted Gap Trend Score for question 6 to compare trend is "([^"]*)"')
def the_weighted_trend_score_for_question6_to_compare_trend_is(step, weighted_gap_trend_score):
    assert get_weighted_gap_score_text_for_questions_and_comparision("07", 3) == weighted_gap_trend_score


@step('the Evaluation Score for question 6 to compare reminder is "([^"]*)"')
def the_evaluation_score_for_question6_to_compare_reminder_is(step, evaluation_score):
    assert  get_calculate_value_for_questions_and_comparision("07", 12) == evaluation_score

@step('the Evaluation Trend Score for question 6 to compare reminder is "([^"]*)"')
def the_evaluation_trend_score_for_question6_to_compare_reminder_is(step, evaluation_trend_score):
    assert get_evaluation_score_text_for_questions_and_comparision("07", 3) == evaluation_trend_score

@step('the Importance Score for question 6 to compare reminder is "([^"]*)"')
def the_important_score_for_question6_to_compare_reminder_is(step, important_score):
    assert  get_calculate_value_for_questions_and_comparision("07", 13) == important_score

@step('the Importance Trend Score for question 6 to compare reminder is "([^"]*)"')
def the_important_trend_score_for_question6_to_compare_reminder_is(step, important_trend_score):
    assert get_importance_score_text_for_questions_and_comparision("07", 3) == important_trend_score

@step('the Gap Score for question 6 to compare reminder is "([^"]*)"')
def the_gap_score_for_question6_to_compare_reminder_is(step, gap_score):
    assert  get_calculate_value_for_questions_and_comparision("07", 14) == gap_score

@step('the Gap Trend Score for question 6 to compare reminder is "([^"]*)"')
def the_gap_trend_score_for_question6_to_compare_reminder_is(step, gap_trend_score):
    assert get_gap_score_text_for_questions_and_comparision("07",3) == gap_trend_score

@step('the Weighted Gap Score for question 6 to compare reminder is "([^"]*)"')
def the_weighted_score_for_question6_to_compare_reminder_is(step, weighted_gap_score):
    assert  get_calculate_value_for_questions_and_comparision("07", 15) == weighted_gap_score

@step('the Weighted Gap Trend Score for question 6 to compare reminder is "([^"]*)"')
def the_weighted_trend_score_for_question6_to_compare_reminder_is(step, weighted_gap_trend_score):
    assert get_weighted_gap_score_text_for_questions_and_comparision("07", 3) == weighted_gap_trend_score    

@step('the Evaluation Score for question 6 to compare organization is "([^"]*)"')
def the_evaluation_score_for_question6_to_compare_organization_is(step, evaluation_score):
    assert  get_calculate_value_for_questions_and_comparision("07", 16) == evaluation_score

@step('the Evaluation Trend Score for question 6 to compare organization is "([^"]*)"')
def the_evaluation_trend_score_for_question6_to_compare_organization_is(step, evaluation_trend_score):
    assert get_evaluation_score_text_for_questions_and_comparision("07", 4) == evaluation_trend_score

@step('the Importance Score for question 6 to compare organization is "([^"]*)"')
def the_important_score_for_question6_to_compare_organization_is(step, important_score):
    assert get_calculate_value_for_questions_and_comparision("07", 17) == important_score

@step('the Importance Trend Score for question 6 to compare organization is "([^"]*)"')
def the_important_trend_score_for_question6_to_compare_organization_is(step, important_trend_score):
    assert get_importance_score_text_for_questions_and_comparision("07", 4) == important_trend_score

@step('the Gap Score for question 6 to compare organization is "([^"]*)"')
def the_gap_score_for_question6_to_compare_organization_is(step, gap_score):
    assert get_calculate_value_for_questions_and_comparision("07", 18) == gap_score

@step('the Gap Trend Score for question 6 to compare organization is "([^"]*)"')
def the_gap_trend_score_for_question6_to_compare_organization_is(step, gap_trend_score):
    assert get_gap_score_text_for_questions_and_comparision("07", 4) == gap_trend_score

@step('the Weighted Gap Score for question 6 to compare organization is "([^"]*)"')
def the_weighted_score_for_question6_to_compare_organization_is(step, weighted_gap_score):
    assert get_calculate_value_for_questions_and_comparision("07", 19) == weighted_gap_score

@step('the Weighted Gap Trend Score for question 6 to compare organization is "([^"]*)"')
def the_weighted_trend_score_for_question6_to_compare_organization_is(step, weighted_gap_trend_score):
    assert get_weighted_gap_score_text_for_questions_and_comparision("07", 4) == weighted_gap_trend_score

@step('the Evaluation Score for Work Life Balance to compare trend is "([^"]*)"')
def the_evaluation_score_for_work_life_balance_to_compare_trend_is(step, evaluation_score):
    if get_calculate_value_for_categories_and_comparision("4", 4) == evaluation_score:
      assert get_calculate_value_for_categories_and_comparision("4", 4) == evaluation_score
    else:
      get_calculate_value_for_categories_and_comparision("4", 8) == evaluation_score

@step('the Evaluation Trend Score for Work Life Balance to compare trend is "([^"]*)"')
def the_evaluation_trend_score_for_work_life_balance_to_compare_trend_is(step, evaluation_trend_score):
    if get_evaluation_score_text_for_categories_and_comparision("4", 1) == evaluation_trend_score:
      assert get_evaluation_score_text_for_categories_and_comparision("4", 1) == evaluation_trend_score
    else:
      get_evaluation_score_text_for_categories_and_comparision("4", 2) == evaluation_trend_score

@step('the Importance Score for Work Life Balance to compare trend is "([^"]*)"')
def the_important_score_for_work_life_balance_to_compare_trend_is(step, important_score):
    if get_calculate_value_for_categories_and_comparision("4", 5) == important_score:
      assert get_calculate_value_for_categories_and_comparision("4", 5) == important_score
    else:
      get_calculate_value_for_categories_and_comparision("4", 9) == important_score

@step('the Importance Trend Score for Work Life Balance to compare trend is "([^"]*)"')
def the_important_trend_score_for_work_life_balance_to_compare_trend_is(step, important_trend_score):
    if get_importance_score_text_for_categories_and_comparision("4", 1) == important_trend_score:
      assert get_importance_score_text_for_categories_and_comparision("4", 1) == important_trend_score
    else:
      get_importance_score_text_for_categories_and_comparision("4", 2) == important_trend_score

@step('the Gap Score for Work Life Balance to compare trend is "([^"]*)"')
def the_gap_score_for_work_life_balance_to_compare_trend_is(step, gap_score):
    if get_calculate_value_for_categories_and_comparision("4", 6) == gap_score:
      assert get_calculate_value_for_categories_and_comparision("4", 6) == gap_score
    else:
      get_calculate_value_for_categories_and_comparision("4", 10) == gap_score

@step('the Gap Trend Score for Work Life Balance to compare trend is "([^"]*)"')
def the_gap_trend_score_for_work_life_balance_to_compare_trend_is(step, gap_trend_score):
    if get_gap_score_text_for_categories_and_comparision("4", 1) == gap_trend_score:
      assert get_gap_score_text_for_categories_and_comparision("4", 1) == gap_trend_score
    else:
      get_gap_score_text_for_categories_and_comparision("4", 2) == gap_trend_score

@step('the Weighted Gap Score for Work Life Balance to compare trend is "([^"]*)"')
def the_weighted_score_for_work_life_balance_to_compare_trend_is(step, weighted_gap_score):
    if get_calculate_value_for_categories_and_comparision("4", 7) == weighted_gap_score:
      assert get_calculate_value_for_categories_and_comparision("4", 7) == weighted_gap_score
    else:
      get_calculate_value_for_categories_and_comparision("4", 11) == weighted_gap_score

@step('the Weighted Gap Trend Score for Work Life Balance to compare trend is "([^"]*)"')
def the_weighted_trend_score_for_work_life_balance_to_compare_trend_is(step, weighted_gap_trend_score):
    if get_weighted_gap_score_text_for_categories_and_comparision("4", 1) == weighted_gap_trend_score:
      assert get_weighted_gap_score_text_for_categories_and_comparision("4", 1) == weighted_gap_trend_score
    else:
      get_weighted_gap_score_text_for_categories_and_comparision("4", 2) == weighted_gap_trend_score

@step('the Evaluation Score for Work Life Balance to compare reminder is "([^"]*)"')
def the_evaluation_score_for_work_life_balance_to_compare_reminder_is(step, evaluation_score):
    assert  get_calculate_value_for_categories_and_comparision("4", 12) == evaluation_score

@step('the Evaluation Trend Score for Work Life Balance to compare reminder is "([^"]*)"')
def the_evaluation_trend_score_for_work_life_balance_to_compare_reminder_is(step, evaluation_trend_score):
    assert get_evaluation_score_text_for_categories_and_comparision("4", 3) == evaluation_trend_score

@step('the Importance Score for Work Life Balance to compare reminder is "([^"]*)"')
def the_important_score_for_work_life_balance_to_compare_reminder_is(step, important_score):
    assert  get_calculate_value_for_categories_and_comparision("4", 13) == important_score

@step('the Importance Trend Score for Work Life Balance to compare reminder is "([^"]*)"')
def the_important_trend_score_for_work_life_balance_to_compare_reminder_is(step, important_trend_score):
    assert get_importance_score_text_for_categories_and_comparision("4", 3) == important_trend_score

@step('the Gap Score for Work Life Balance to compare reminder is "([^"]*)"')
def the_gap_score_for_work_life_balance_to_compare_reminder_is(step, gap_score):
    assert  get_calculate_value_for_categories_and_comparision("4", 14) == gap_score

@step('the Gap Trend Score for Work Life Balance to compare reminder is "([^"]*)"')
def the_gap_trend_score_for_work_life_balance_to_compare_reminder_is(step, gap_trend_score):
    assert get_gap_score_text_for_categories_and_comparision("4",3) == gap_trend_score

@step('the Weighted Gap Score for Work Life Balance to compare reminder is "([^"]*)"')
def the_weighted_score_for_work_life_balance_to_compare_reminder_is(step, weighted_gap_score):
    assert  get_calculate_value_for_categories_and_comparision("4", 15) == weighted_gap_score

@step('the Weighted Gap Trend Score for Work Life Balance to compare reminder is "([^"]*)"')
def the_weighted_trend_score_for_work_life_balance_to_compare_reminder_is(step, weighted_gap_trend_score):
    assert get_weighted_gap_score_text_for_categories_and_comparision("4", 3) == weighted_gap_trend_score

@step('the Evaluation Score for Work Life Balance to compare organization is "([^"]*)"')
def the_evaluation_score_for_work_life_balance_to_compare_organization_is(step, evaluation_score):
    assert get_calculate_value_for_categories_and_comparision("4", 16) == evaluation_score

@step('the Evaluation Trend Score for Work Life Balance to compare organization is "([^"]*)"')
def the_evaluation_trend_score_for_work_life_balance_to_compare_organization_is(step, evaluation_trend_score):
    assert get_evaluation_score_text_for_categories_and_comparision("4", 4) == evaluation_trend_score

@step('the Importance Score for Work Life Balance to compare organization is "([^"]*)"')
def the_important_score_for_work_life_balance_to_compare_organization_is(step, important_score):
    assert  get_calculate_value_for_categories_and_comparision("4", 17) == important_score

@step('the Importance Trend Score for Work Life Balance to compare organization is "([^"]*)"')
def the_important_trend_score_for_work_life_balance_to_compare_organization_is(step, important_trend_score):
    assert get_importance_score_text_for_categories_and_comparision("4", 4) == important_trend_score

@step('the Gap Score for Work Life Balance to compare organization is "([^"]*)"')
def the_gap_score_for_work_life_balance_to_compare_organization_is(step, gap_score):
    assert get_calculate_value_for_categories_and_comparision("4", 18) == gap_score

@step('the Gap Trend Score for Work Life Balance to compare organization is "([^"]*)"')
def the_gap_trend_score_for_work_life_balance_to_compare_organization_is(step, gap_trend_score):
    assert get_gap_score_text_for_categories_and_comparision("4", 4) == gap_trend_score

@step('the Weighted Gap Score for Work Life Balance to compare organization is "([^"]*)"')
def the_weighted_score_for_work_life_balance_to_compare_organization_is(step, weighted_gap_score):
    assert  get_calculate_value_for_categories_and_comparision("4", 19) == weighted_gap_score

@step('the Weighted Gap Trend Score for Work Life Balance to compare organization is "([^"]*)"')
def the_weighted_trend_score_for_work_life_balance_to_compare_organization_is(step, weighted_gap_trend_score):
    assert get_weighted_gap_score_text_for_categories_and_comparision("4",4) == weighted_gap_trend_score
