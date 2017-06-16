import get_html_data
import Webscraping_Tools.html_parsing_tools as html_parsing_tools

url_to_scrape = "https://www.wunderground.com/history/airport/EHRD/2015/2/2/DailyHistory.html?req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&MR=1"

resulting_csv_file_name = "wunderground"

resulting_file_location = "/Users/benlovell/Library/Mobile Documents/com~apple~CloudDocs/Code/Web_Scraping_Code/Output Files/"

key_word_start = "12:00 AM"
key_word_end = "show"

start_information = "2017/6/12"

end_information = "2017/6/9"

key_feature_first_metric = ":"

metrics = [ "time",
            "am or pm",
            "Temp",
            "Heat Index",
            "Dew. Point",
            "Humidity",
            "Pressure",
            "Visibility",
            "Wind Dir",
            "Wind Speed",
            "Gust Speed",
            "Precip"]


html_data = get_html_data.get_html_data_from_url(url_to_scrape, start_information, end_information)

html_parsing_tools.turn_html_data_into_csv_file(html_data, key_word_start, key_word_end, metrics, key_feature_first_metric, resulting_file_location, resulting_csv_file_name)

