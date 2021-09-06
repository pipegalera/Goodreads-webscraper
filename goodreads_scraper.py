
# ------------------------------------- Packages ------------------------------------- #
import pandas as pd
import time
from time import gmtime, strftime
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import random
import re

# ---------------------------- Goodread's web-scraper --------------------------- #

def goodread_scraper(sections, n_pages = 25, user_email = 'domantassabonisuser@gmail.com', password = 123456):
    random_sleeptime = random.randint(100,250)/100
    first_page = 1
    last_page = 1+n_pages
    book_titles_list = []
    book_author_list = []
    book_ratings_list = []
    number_book_ratings_list = []
    book_year_list = []
    book_description_list = []
    book_image_list = []
    book_genre_list = []

    # --------------------------------- Browser --------------------------------- #
    # Browser options
    additional_options = webdriver.ChromeOptions()
    additional_options.add_argument('--ignore-certificate-errors')

    # Initialize
    chromedriver_path = r'chromedriver.exe'
    browser = webdriver.Chrome(chromedriver_path, options =additional_options)
    browser.get('https://www.goodreads.com/user/sign_in')

    # Introduce user

    browser.find_element_by_id('user_email').send_keys(user_email)
    browser.find_element_by_id('user_password').send_keys(password)
    browser.find_elements_by_xpath("//*[@id='emailForm']/form/fieldset/div[5]/input[1]")[0].click()

    # ---------------------------- Loop over section(s) and shelve pages ----------------------- #
    for section in sections:
        # Print the current section being scraped
        print('################# Shelve: ' + str(section) + ' #################')
        print(' ')
        print(' ')
        
        for page in range(first_page, last_page):
            # Load Chrome Browser
            browser.get('https://www.goodreads.com/shelf/show/' + str(section) + '?page=' + str(page))

            # Add a random timer from 0.1 to 0.25 seconds to avoid page bot blocking
            time.sleep(random_sleeptime)

            # Store the page content to later clean store it into lists
            soup = BeautifulSoup(browser.page_source, 'html.parser')

            # Find relevant data within the BeautifulSoup

            # ---------------------------- Book titles ---------------------------- #
            book_titles_soup = soup.find_all('a', class_= 'bookTitle')

            for i in range(0, len(book_titles_soup)):
                book_titles_list.append(book_titles_soup[i].text)
    
            # Print the list of books scraped
            print('################# Scraping the following books... #################')
            [print(i) for i in book_titles_list]
            print('################################################################')
    

            # ---------------------------- Book author ---------------------------- #
            book_author_soup = soup.find_all('a', class_= 'authorName')

            for i in range(0,len(book_author_soup)):
                book_author_list.append(book_author_soup[i].text)

            # -------------- Average Ratings, Number of Ratings and Publication Year ------------- #
            grey_text_soup =soup.find_all(class_= 'greyText smallText')

            for i in range(0,len(book_titles_soup)):
                # First, we split all the information in the class greyText smallText
                grey_text_stripped = grey_text_soup[i].text.strip().replace('—\n', '').replace(',', '').split()

                # Store the Average Ratings (2nd element in the split string)
                try:
                    book_ratings_list.append(grey_text_stripped[2])
                except:
                    book_ratings_list.append('NaN')

                # Store the Number of ratings (4th element in the split string)
                try:
                    number_book_ratings_list.append(grey_text_stripped[3])
                except:
                    number_book_ratings_list.append('NaN')

                # Store the Publication Year (6th element in the split string)
                try:
                    book_year_list.append(grey_text_stripped[6])
                except:
                    book_year_list.append('NaN')


            # -------------------------- Book description -------------------------- #

            for i in range(0,len(book_titles_soup)):
                # Click the book
                browser.find_elements_by_class_name('bookTitle')[i].click()
                try: # Get the long description of the book
                    browser.find_element_by_link_text('...more').click()
                except: # No long description or no description
                    pass
                try:
                    soup = BeautifulSoup(browser.page_source, 'html.parser')
                    description_soup = soup.find('div', {'id': 'description'})
                    # Remove librarian notes
                    try:
                        description_soup.find('i').decompose()
                    except:
                        pass
                    try:
                        description_soup.find('i').decompose()
                    except:
                        pass
                    try:
                        description_soup.find('i').decompose()
                    except:
                        pass

                    description = description_soup.get_text()

                    # Clean descriptions
                    description = description.replace('\n(less)\n', '')
                    description = description.replace('\n', '')
                except: # No book_description
                    description = 'NaN'

                # -------------------------- Book cover -------------------------- #
                try: # Get the book cover
                    book_image = soup.find('img', id = 'coverImage')['src']
                except:  # No book cover
                    book_image = 'NaN'

                # ---------------------------- Book genre ---------------------------- #
                try:
                    genres = soup.find_all(class_="actionLinkLite bookPageGenreLink")
                    genres = [genre.text for genre in genres]
                    #print(genres)
                except:
                    genres = [] 

                # Append to a list the description, book image and genres
                book_description_list.append(description)
                book_image_list.append(book_image)
                book_genre_list.append(genres)

                # When it scrapes the last book print the count of books scraped
                if i == range(0, len(book_titles_soup))[-1]:
                    print('Shelve: ' , str(section))
                    print('Page: ', page)
                    print('Total number of books scraped: ', len(book_titles_list))
                    print('################################################################')

                # Go back and start again with the next book
                browser.back()
        # ---------------------------- Make a dataframe ---------------------------- #

        books_dataframe = pd.DataFrame(zip(book_titles_list,
                                book_author_list,
                                book_ratings_list,
                                number_book_ratings_list,
                                book_year_list,
                                book_description_list,
                                book_image_list,
                                book_genre_list),
                            columns = ['Title', 'Author', 'Average rating',
                                       'Number of Ratings', 'Year', 'Book description', 'Book image', 'Genre'])

    time_print= strftime("%a_%d_%b_%Y_%H_%M_%S", gmtime())
    books_dataframe.to_csv('backups/{}.csv'.format(time_print), index = False)

    return books_dataframe
