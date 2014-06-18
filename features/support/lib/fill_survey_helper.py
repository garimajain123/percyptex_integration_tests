from features.support.lettuce_env import *
from features import application_path
'''
def fetch_urls():
    urls = os.path.join(application_path,'features/fixtures/urls.yml')
    open_yaml = open(urls,'r')
    url_dict = yaml.load(open_yaml)
    return url_dict

def fill_survey_form(range, id_count):
    for i in xrange(range):
      get_browser().find_by_id("Q0%s_0%s_e1"%(id_count, i)).click()
      get_browser().find_by_id("Q0%s_0%s_i1"%(id_count, i )).click()
'''
