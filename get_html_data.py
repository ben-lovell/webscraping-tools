from bs4 import BeautifulSoup, SoupStrainer
import Webscraping_Tools.link_formulas as link_formulas
import Webscraping_Tools.requests as requests

def retrieve_HTML_data(link):
    try:
        html = requests.get(link)
        soup = BeautifulSoup(html.content, "html.parser")
        data = soup.findAll(text=True)
        return data
    except:
        print "Error getting HTML data for link: " + str(link)
        return False

def get_html_data_from_url(url_to_scrape, start_information, end_information):
    links_to_scrape = link_formulas.create_links_to_parse(url_to_scrape, start_information, end_information)
    list_of_links_to_scrape = links_to_scrape[0]
    list_of_dates = links_to_scrape[1]
    html_data = []

    for web_page in list_of_links_to_scrape:
        print "getting full text from HTML page " + str(list_of_links_to_scrape.index(web_page)) + "/" + str(len(list_of_links_to_scrape) - 1)
        html_data_from_page = retrieve_HTML_data(web_page)
        html_data.append(html_data_from_page)
    return html_data, list_of_dates
