#import #httplib2
from bs4 import BeautifulSoup, SoupStrainer
import csv

def get_all_links_on_page(url_to_scrape):
    http = httplib2.Http()
    status, response = http.request(url_to_scrape)

    page_links_list = []
    for link in BeautifulSoup(response, "html.parser", parse_only=SoupStrainer('a')):
        if link.has_attr('href'):
            page_links_list.append(str(link['href']))
            #previous_time = datetime.datetime.now()

    return list(set(page_links_list))

def clean_and_lowercase_string(list_of_strings, key_word_end):
    full_list_of_words = []
    temp_storage = []
    # break down the individual list items
    for element in list_of_strings:
        # used to hold the cleaned words
        clean_element = ''
        index_counter = 0
        # break down the characters in each element
        for character in element:
            # check if character is alphanumeric
            if str(character).isalnum() or str(character) == "." or str(character) is ":" or str(character) is "-":
                #check if character starts with unicode character 'u'
                if element[0] == "u" and index_counter == 0:
                    index_counter += 1
                    continue
                else:
                    try:
                        if element[0] == "-" and element[2] == "n":
                            clean_element += "-"
                        else:
                            clean_element += character.lower()
                    except:
                        continue
        temp_storage.append(clean_element)

    for item in temp_storage:
        # filter out a few more unicode characters
        if item != "n" and item[0:2] != "xa" and item[0:2] != "nt":
            # stop cleaning the data when this word is reached
            if item == key_word_end:
                break
            else:
                if item.isdigit() == True and ":" not in item:
                    full_list_of_words.append(float(item))
                else:
                    full_list_of_words.append(item)

    return full_list_of_words

def get_visible_text_after_keyword_from_html(html, key_word_start, key_word_end):
    string_raw_html = str(html)
    start_location = string_raw_html.index(key_word_start)

    split_string_at_visible_text = string_raw_html[start_location:].split('<span style="font-size')
    split_string = str(split_string_at_visible_text[0])
    split_string_cleaning_round_1 = split_string.split('>')

    visible_text = ''
    for element in split_string_cleaning_round_1:
        try:
            if element[0] != "<" and len(element.split()) > 4:
                visible_text += " " + element
        except:
            continue

    return clean_and_lowercase_string(visible_text.split(), key_word_end)

def organize_visible_text_from_html(list_of_visible_data, list_of_metrics, date_iterations, key_feature_first_metric, date_counter):

    # group the rows together
    grouped_list_of_rows = []
    single_row_of_data = []
    for datapoint in list_of_visible_data:
        if key_feature_first_metric not in str(datapoint):
            single_row_of_data.append(datapoint)
        else:
            grouped_list_of_rows.append(single_row_of_data)
            single_row_of_data = [datapoint]
    del grouped_list_of_rows[0]


    cleaned_list = []
    single_clean_row = []
    for row in grouped_list_of_rows:
        row.insert(0, date_iterations[date_counter])
        for metric in xrange(len(list_of_metrics)):
            try:
                single_clean_row.append(row[metric])
            except:
                single_clean_row.append("-")
            #if metric[1] > 1:
            #    for value in xrange(metric[1]):
            #        single_clean_row[len(single_clean_row)] += row[clean_metrics.index(metric) + value]
            #else:

        cleaned_list.append(single_clean_row)
        single_clean_row = []

    return cleaned_list

def turn_list_into_csv_file(list_to_write_to_csv, headers, date_iterations, resulting_file_location, resulting_csv_file_name):
    with open(resulting_file_location + resulting_csv_file_name + ".csv",'wb') as f:
        writer= csv.writer(f)
        clean_headers = []
        for row in headers:
            clean_headers.append(row)
        writer.writerow(clean_headers)
        for dataset in list_to_write_to_csv:
            for row in dataset:
                writer.writerow(row)
    f.close()

def turn_html_data_into_csv_file(html_data, key_word_start, key_word_end, metrics, date_iterations, key_feature_first_metric, resulting_file_location, resulting_csv_file_name):
    if len(html_data) > 1:
        end_list = []
        for group in html_data:
            visible_text_from_html = get_visible_text_after_keyword_from_html(group, key_word_start, key_word_end)
            list_to_write_to_csv = organize_visible_text_from_html(visible_text_from_html, metrics, date_iterations, key_feature_first_metric, html_data.index(group))
            end_list.append(list_to_write_to_csv)
        return turn_list_into_csv_file(end_list, metrics, date_iterations, resulting_file_location, resulting_csv_file_name)
    else:
        visible_text_from_html = get_visible_text_after_keyword_from_html(html_data, key_word_start, key_word_end)
        list_to_write_to_csv = organize_visible_text_from_html(visible_text_from_html, metrics, date_iterations, key_feature_first_metric)
        return turn_list_into_csv_file(list_to_write_to_csv, metrics, resulting_file_location, resulting_csv_file_name)
