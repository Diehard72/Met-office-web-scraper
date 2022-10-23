# Lines 4 to 10 extracts the HTML code from the met office website for a specified date
#by using the "requests" library.
#Beautiful Soup is a Python library for parsing structured data.
import requests
from bs4 import BeautifulSoup

date = input("Enter date:")
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










