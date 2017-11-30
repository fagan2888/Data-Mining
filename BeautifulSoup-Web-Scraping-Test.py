from urllib.request import urlopen
from bs4 import BeautifulSoup

# Read Web Page
web_page = urlopen("https://www.theice.com/products")

# Parse the HTML as a string
soup = BeautifulSoup(web_page, 'lxml')

# Obtain the first table
table = soup.find_all('table')[0]

# Process Every <tr> Tag - Represents Each Row
row_marker = 0
for row in table.find_all('tr'):
    column_marker = 0
    columns = row.find_all('td')
    #   Process Each <td> Tag - Represents Each Column
    for column in columns:
        value = column.get_text()
        print('Row:', row_marker, 'Col:', column_marker, value)
        column_marker += 1
    row_marker += 1
