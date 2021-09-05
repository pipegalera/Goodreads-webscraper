# Goodreads webscraper ![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)

A Goodread.com python script to collect book data from Goodreads. You can use it with [any shelve of Goodreads](https://www.goodreads.com/genres/list).


![Preview gif](https://i.imgur.com/KtGRuqK.gif)



### Packages needed

- [pandas](https://pypi.org/project/pandas/)
- [time](https://pypi.org/project/python-time/)
- [regex](https://pypi.org/project/regex/)
- [selenium](https://pypi.org/project/selenium/)
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)


### 3 Minimal examples

1. Webscraping the 'Art' shelve:

```console
terminal@pipe:~$ python -c "from goodreads_scraper.py import *;
                 scrappe_section(['Art'])"
```
Result:

![](preview_images/art.png)

&nbsp;

You can use your own *user_email* and *password*  for an email registered at Goodreads.com.

2. Webscraping the 'Crime' shelve using your own Goodreads account:

```console
terminal@pipe:~$ python -c "from goodreads_scraper.py import *;
                 scrappe_section(['Crime'],
                 user_email = 'an_alternative_mail@gmail.com',
                 password = 'PasswordOfThisGoodReadsMail')"
```

:warning: this user it won't be stored anywhere by any means, feel free to check the source of the code at *goodreads_scraper.py*

Result:

![](preview_images/crime.png)

&nbsp;

3. Webscraping multiple shelves:

```console
terminal@pipe:~$ python -c "from goodreads_scraper.py import *;
                 scrappe_section(['Art', 'Crime', 'Travel'])"
```

Result:

![](preview_images/several_sections.png)

&nbsp;


### Other genres/shelves to webscrape:

![](preview_images/genres.png)

[Complete list here](https://www.goodreads.com/genres/list)



### Usage tips

- Take into account that **each shelve/section/genre takes 30-45 minutes to be scrapped**.
- Each section has roughly 1250 books.
- One the scraper starts, you can minimize the chrome driver. Don't click around or scroll the driver page.
