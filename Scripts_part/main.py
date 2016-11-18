import scrapper as sc
import helpers as h

scripts_filename = "all_scripts" + h.timestamp()
scripts_path = "raw_html/"
url_scripts_list = "http://www.imsdb.com/all%20scripts/"

sc.get_scripts_list(url_scripts_list, scripts_filename,scripts_path)