"""
File: webcrawler.py
Name: Paul
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        header = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/111.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=header)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")
        # ----- Write your code below this line ----- #
        tags = soup.find('table', {'class': 't-stripe'})
        tds = tags.find_all('td')
        # Initialize total counts for male and female
        total_m = 0
        total_f = 0

        # Initialize indices for male and female data in the 'tds' list
        m = 3
        f = 5

        for i in range(200):  # Loop over the range
            if m < len(tds):  # Check if the male index is within the range of 'tds' list
                td = tds[m].text  # Get the text of the 'td' element
                m += 5  # Increment the male index by 5
                score = int(td.replace(',', ''))  # Remove comma
                total_m += score  # Add the score to the total male count

            if f < len(tds):  # Check if the female index is within the range of 'tds' list
                tdf = tds[f].text  # Get the text of the 'td' element
                f += 5                  # Increment the female index by 5
                score2 = int(tdf.replace(',', ''))
                total_f += score2

        # Print the total counts for male and female
        print('Male Number:', total_m)
        print('Female Number:', total_f)


if __name__ == '__main__':
    main()
