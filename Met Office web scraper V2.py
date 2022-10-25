# Lines 4 to 10 extracts the HTML code from the met office website for a specified date
#by using the "requests" library.
#Beautiful Soup is a Python library for parsing structured data.
import datetime
import requests
from bs4 import BeautifulSoup
from datetime import date

#Enter date range
start_date = input("Enter the start date of the date range: ")
end_date = input("Enter the end date of the date range: ")

#Split date strings up into year, month and day
start_date_year = int(start_date[0:(3+1)])
start_date_month = int(start_date[5:(6+1)])
start_date_day = int(start_date[8:(9+1)])

end_date_year = int(end_date[0:(3+1)])
end_date_month = int(end_date[5:(6+1)])
end_date_day = int(end_date[8:(9+1)])

#Calculate number of days in range
range_days = end_date_day - start_date_day

for days in range(range_days +1):

    date = datetime.date(start_date_year, start_date_month, (start_date_day + days))
    URL = f"https://www.metoffice.gov.uk/weather/forecast/gcw2hzs1u#?date={date}"
    page = requests.get(URL)

    # The statement below creates a Beautiful Soup object called soup, and this takes content from the above URL page.
    soup = BeautifulSoup(page.content, "html.parser")

    # The lines of code below searches for the specific content we are after by using the Beautiful Soup "find" function.
    # and then prints out the results.
    results = soup.find (id=f"dayLink{date}")
    day = results.find("h3", class_="tab-day")
    sunrise = results.find("div", class_="weather-text sunrise-sunset")
    sunset = results.find("div", class_="weather-text sunrise-sunset sunset")
    max_temp = results.find("span", class_="tab-temp-high")
    min_temp = results.find("span", class_="tab-temp-low")
    summary = results.find("div", class_= "summary-text hide-xs-only")

    print(f"Day = {day.text}")
    print(sunrise.text)
    print(sunset.text)
    print(f"Maximum temperature = {max_temp.text}")
    print(f"Minimum temperature = {min_temp.text}")
    print(summary.text)










