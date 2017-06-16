import get_html_data
import Webscraping_Tools.html_parsing_tools as html_parsing_tools

url_to_scrape = "https://www.wunderground.com/history/airport/EHRD/2015/2/2/DailyHistory.html?req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&MR=1"

resulting_csv_file_name = "wunderground 2"

resulting_file_location = "/Users/.../Output Folder/"

key_word_start = "12:00"
key_word_end = "show"

start_information = "2017/6/12"

end_information = "2016/6/12"

key_feature_first_metric = ":"

metrics = [ "Date",
            "time",
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

html_parsing_tools.turn_html_data_into_csv_file(html_data[0], key_word_start, key_word_end, metrics, html_data[1], key_feature_first_metric, resulting_file_location, resulting_csv_file_name)

