
# ------------------------------------- Packages ------------------------------------- #
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import random
import re



# ---------------------------- Goodread's web-scrapper --------------------------- #

def goodread_scraper(sections, user_email = "domantassabonisuser@gmail.com", password = 123456):
    random_sleeptime = random.randint(100,250)/100
    first_page = 1
    last_page = 26
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
    browser.get('https://www.goodreads.com')

    # Introduce user

    browser.find_element_by_id("userSignInFormEmail").send_keys(user_email)
    browser.find_element_by_id("user_password").send_keys(password)
    browser.find_elements_by_xpath("//*[@id='sign_in']/div[3]/input[1]")[0].click()

    # ---------------------------- Loop over section(s) and shelve pages ----------------------- #
    for section in sections:
        for page in range(first_page, last_page):
            # Load Chrome Browser
            browser.get('https://www.goodreads.com/shelf/show/' + str(section) + '?page=' + str(page))

            # Add a random timer from 1 to 2.5 seconds to avoid page bot blocking
            time.sleep(random_sleeptime)

            # Store the page content to later clean store it into lists
            soup = BeautifulSoup(browser.page_source, "html.parser")

            # Find relevant data within the BeautifulSoup

            # ---------------------------- Book titles ---------------------------- #
            book_titles_soup = soup.find_all("a", class_= "bookTitle")

            for i in range(0, len(book_titles_soup)):
                book_titles_list.append(book_titles_soup[i].text)


            # ---------------------------- Book author ---------------------------- #
            book_author_soup = soup.find_all("a", class_= "authorName")

            for i in range(0,len(book_author_soup)):
                book_author_list.append(book_author_soup[i].text)

            # -------------- Average Ratings, Number of Ratings and Publication Year ------------- #
            grey_text_soup =soup.find_all(class_= "greyText smallText")

            for i in range(0,len(book_titles_soup)):
                # First, we split all the information in the class greyText smallText
                grey_text_stripped = grey_text_soup[i].text.strip().replace("—\n", "").replace(",", "").split()

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
                # Click every book
                browser.find_elements_by_class_name("bookTitle")[i].click()
                try: # Get the long description of the book
                    browser.find_element_by_link_text("...more").click()
                except: # No long description or no description
                    pass
                try:
                    soup = BeautifulSoup(browser.page_source, "html.parser")
                    description_soup = soup.find("div", {"id": "description"})
                    # Remove librarian notes
                    try:
                        description_soup.find("i").decompose()
                    except:
                        pass
                    try:
                        description_soup.find("i").decompose()
                    except:
                        pass
                    try:
                        description_soup.find("i").decompose()
                    except:
                        pass

                    description = description_soup.get_text()

                    # Clean descriptions
                    description = description.replace("\n(less)\n", "")
                    description = description.replace("\n", "")
                except: # No book_description
                    description = 'NaN'

                # -------------------------- Book cover -------------------------- #
                try: # Get the book cover
                    book_image = soup.find('img', id = 'coverImage')['src']
                except:  # No book cover
                    book_image = 'NaN'

                # Append to a list the description and book image
                book_description_list.append(description)
                book_image_list.append(book_image)

                # Go back and start again with the next book
                browser.back()

            # ---------------------------- Book genre ---------------------------- #
            for i in range(0, len(book_titles_soup)):
                book_genre_list.append(str(section))

        # ---------------------------- Make a dataframe ---------------------------- #

        books_dataframe = pd.DataFrame(zip(book_titles_list,
                                book_author_list,
                                book_ratings_list,
                                number_book_ratings_list,
                                book_year_list,
                                book_description_list,
                                book_image_list,
                                book_genre_list),
                            columns = ["Title", "Author", "Average rating",
                                       "Number of Ratings", "Year", "Book description", "Book image", "Genre"])

        books_dataframe['Year'] = books_dataframe['Year'].astype('Int64')

        books_dataframe.to_csv('goodreads_data.csv', index = False)

        return books_dataframe
