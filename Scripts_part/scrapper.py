import urllib2, time
from random import randint
import helpers as h


def scrap_page(url, filename, path_to_save):
    url_response = urllib2.urlopen(url)
    url_html = url_response.read()
    h.write_to_file(url_html, filename, path_to_save)
    time.sleep(randint(30, 80))