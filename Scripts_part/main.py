import scrapper as sc
import helpers as h
import parser as ps


def scrap_all_scripts():

    scripts_filename = "all_scripts_list" # + h.timestamp()
    temp_name = "all_scripts20161118-144445"

    scripts_path = "raw_html/"
    url_scripts_list = "http://www.imsdb.com/all%20scripts/"

    sc.scrap_page(url_scripts_list, scripts_filename,scripts_path)

    link_prefix = "http://www.imsdb.com/scripts/"
    all_links = ps.parse_script_list(scripts_filename, scripts_path)

    # for link in all_links:
    #     print link

    count = 0
    for link in all_links:
        sc.scrap_page(link_prefix + link, link, scripts_path + "raw_scripts/")
        count += 1
        print "Done: ", count, "/", len(all_links), "\n"

scrap_all_scripts()
