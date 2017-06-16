import datetime as dt

def create_links_to_parse(url_to_scrape, start_information, end_information):
    def create_wunderground_links(url_to_scrape, start_information, end_information):

        # find the part of the URL before the date
        date_start_location = 0
        before_date_string = ''
        for character in url_to_scrape:
            if character.isdigit():
                date_start_location = url_to_scrape.index(character)
                before_date_string += url_to_scrape[:url_to_scrape.index(character)]
                break

        # find the part of the URL after the date
        after_date_string = '/'
        after_date_string_to_parse = url_to_scrape[date_start_location:]
        for character in after_date_string_to_parse:
            if character.isdigit() == False and character != "/":
                after_date_string += after_date_string_to_parse[after_date_string_to_parse.index(character):]
                break

        # come up with the date variations to be plugged in between the before_date_string and after_date_string
        date_iterations = []
        start_date_clean = dt.datetime.strptime(start_information,"%Y/%m/%d")
        end_date_clean = dt.datetime.strptime(end_information,"%Y/%m/%d")
        total_days = (start_date_clean - end_date_clean).total_seconds()/86400

        for date in xrange(int(total_days)):
            if start_date_clean != end_date_clean:
                start_date_clean -= dt.timedelta(days = 1)
                date_iterations.append(dt.datetime.strftime(start_date_clean, "%Y/%m/%d"))

        # create and return the end links
        wunderground_links_to_return = []
        for date in date_iterations:
            complete_link = before_date_string + date + after_date_string
            wunderground_links_to_return.append(complete_link)


        return wunderground_links_to_return


    if "wunderground" in url_to_scrape:
        return create_wunderground_links(url_to_scrape, start_information, end_information)

