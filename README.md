# Goodreads webscraper ![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)

A Goodread.com python script to collect book data from Goodreads. You can use it with [any shelve of Goodreads](https://www.goodreads.com/genres/list).

Apart from the `.py` scraper, it includes a `.ipynb` alternative for users that prefer to work with notebooks instead of running the python file from the terminal.

<img src="images\preview_gif.gif" style="border:1px solid"/>


## Mini docs

```
def goodread_scraper(sections, 
                     n_pages = 25, 
                     user_email = 'domantassabonisuser@gmail.com', 
                     password = 123456)
```

Parameters:

- `sections` are the list of shelves/sections to scrape data from. Example: `['Art']`, `['business', 'music']`, `['adventure','american-classics', 'manga']` or as many as you want to. [Complete list of shelves here](https://www.goodreads.com/genres/list).

- `n_pages` is an integer from `1 to 25` thar represent the number of pages to scrape for each shelve/section. By default is 25 (all the books in the page).
- `user_email` and `password` are optional parameters. The default user (`domantassabonisuser@gmail.com`/`123456`) was created to being able to access multiple shelves at Goodreads. If the user gets blocked, you could still use the web-scraper using your own Goodreads account. The script do not store any user information.

Returns:

- `Dataframe` with the selected `sections`.
- A `.csv` file of the `Dataframe` at the `backups` folder.

# Minimal examples

```python
from goodreads_scraper import goodread_scraper
```

### 1. Webscraping one page of one shelve.


```python
art = goodread_scraper(['Art'], n_pages=1)
```

    ################# Shelve: Art #################
     
     
    ################# Scraping the following books... #################
    Ways of Seeing (Paperback)
    The Story of Art (Hardcover)
    The New Drawing on the Right Side of the Brain (Paperback)
    Steal Like an Artist: 10 Things Nobody Told You About Being Creative (Paperback)
    Wall and Piece (Paperback)
    The Artist's Way: A Spiritual Path to Higher Creativity (Paperback)
    Art and Fear: Observations on the Perils (and Rewards) of Artmaking
    Girl with a Pearl Earring (Paperback)
    The Art Book (Paperback)
    The Letters of Vincent van Gogh (Paperback)
    Concerning the Spiritual in Art (Paperback)
    Seven Days in the Art World (Paperback)
    The Goldfinch (Hardcover)
    History of Beauty (Paperback)
    On Photography (Paperback)
    The Diary of Frida Kahlo: An Intimate Self-Portrait (Hardcover)
    Understanding Comics: The Invisible Art (Paperback)
    M.C. Escher: The Graphic Work (Paperback)
    Art Through the Ages  (Hardcover)
    The War of Art: Winning the Inner Creative Battle (Paperback)
    Color: A Natural History of the Palette (Paperback)
    Leonardo da Vinci (Hardcover)
    The Lives of the Artists (Paperback)
    Vincent Van Gogh: The Complete Paintings (Hardcover)
    Color and Light: A Guide for the Realist Painter (Paperback)
    Just Kids (Hardcover)
    The Shock of the New (Paperback)
    History of Art (Hardcover)
    The Art Forger (Hardcover)
    Show Your Work!: 10 Ways to Share Your Creativity and Get Discovered (Paperback)
    Interaction of Color (Paperback)
    The Agony and the Ecstasy (Mass Market Paperback)
    What Are You Looking At?: 150 Years of Modern Art in a Nutshell (Hardcover)
    Leonardo's Notebooks (Hardcover)
    Figure Drawing for All It's Worth (How to draw and paint)
    The Art Spirit (Paperback)
    An Illustrated Life: Drawing Inspiration from the Private Sketchbooks of Artists, Illustrators and Designers (Paperback)
    Michelangelo and the Pope's Ceiling (Paperback)
    The Philosophy of Andy Warhol (From A to B and Back Again)
    The Secret Lives of Color (Hardcover)
    Van Gogh (Kindle Edition)
    Camera Lucida: Reflections on Photography (Paperback)
    The Judgment of Paris: The Revolutionary Decade That Gave the World Impressionism (Paperback)
    Faeries (Hardcover)
    On Ugliness (Hardcover)
    The Dot (Hardcover)
    Frida: A Biography of Frida Kahlo (Paperback)
    The Power of Art (Hardcover)
    Griffin and Sabine (Griffin & Sabine #1)
    PostSecret: Extraordinary Confessions from Ordinary Lives (PostSecret)
    ################################################################
    Shelve:  Art
    Page:  1
    Total number of books scraped:  50
    ################################################################
    


```python
art.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Title</th>
      <th>Author</th>
      <th>Average rating</th>
      <th>Number of Ratings</th>
      <th>Year</th>
      <th>Book description</th>
      <th>Book image</th>
      <th>Genre</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Ways of Seeing (Paperback)</td>
      <td>John Berger</td>
      <td>3.89</td>
      <td>290473</td>
      <td>1972</td>
      <td>John Berger’s Classic Text on ArtJohn Berger's...</td>
      <td>https://i.gr-assets.com/images/S/compressed.ph...</td>
      <td>[Art, Nonfiction, Philosophy, Writing, Essays,...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>The Story of Art (Hardcover)</td>
      <td>E.H. Gombrich</td>
      <td>3.94</td>
      <td>342798</td>
      <td>1950</td>
      <td>This text is the 16th revised and updated edit...</td>
      <td>https://i.gr-assets.com/images/S/compressed.ph...</td>
      <td>[Art, Nonfiction, History, Art, Art History, R...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>The New Drawing on the Right Side of the Brain...</td>
      <td>Betty Edwards</td>
      <td>3.87</td>
      <td>314863</td>
      <td>1979</td>
      <td>When Drawing on the Right Side of the Brain wa...</td>
      <td>https://i.gr-assets.com/images/S/compressed.ph...</td>
      <td>[Art, Nonfiction, Art, Drawing, Reference, Psy...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Steal Like an Artist: 10 Things Nobody Told Yo...</td>
      <td>Austin Kleon</td>
      <td>3.94</td>
      <td>228547</td>
      <td>2012</td>
      <td>You don’t need to be a genius, you just need t...</td>
      <td>https://i.gr-assets.com/images/S/compressed.ph...</td>
      <td>[Nonfiction, Art, Self Help, Language, Writing...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Wall and Piece (Paperback)</td>
      <td>Banksy</td>
      <td>3.85</td>
      <td>211501</td>
      <td>2005</td>
      <td>Banksy, Britain's now-legendary "guerilla" str...</td>
      <td>https://i.gr-assets.com/images/S/compressed.ph...</td>
      <td>[Art, Nonfiction, Politics, Art, Street Art, A...</td>
    </tr>
  </tbody>
</table>
</div>




```python
art.to_csv('sample_data/art_shelve.csv', index=False)
```

### 2. Webscraping multiple pages of multiple shelves.


```python
crime_travel_art = goodread_scraper(['Crime', 'Travel', 'Art'], n_pages=2)
```
<details>
  <summary>Click to see the long print details</summary>

    ################# Shelve: Crime #################
    
    ################# Scraping the following books... #################
    The Girl with the Dragon Tattoo (Millennium, #1)
    The Girl Who Played with Fire (Millennium, #2)
    Gone Girl (Paperback)
    And Then There Were None (Paperback)
    The Girl Who Kicked the Hornet's Nest (Millennium, #3)
    The Girl on the Train (Hardcover)
    Murder on the Orient Express (Hercule Poirot, #10)
    The Cuckoo's Calling (Cormoran Strike, #1)
    In Cold Blood (Paperback)
    Sharp Objects (Paperback)
    A Study in Scarlet (Sherlock Holmes, #1)
    Dark Places (Hardcover)
    In the Woods (Dublin Murder Squad, #1)
    The Silkworm (Cormoran Strike, #2)
    The Godfather (The Godfather, #1)
    The Silence of the Lambs  (Hannibal Lecter, #2)
    Red Dragon (Hannibal Lecter, #1)
    The Murder of Roger Ackroyd (Hardcover)
    The Mysterious Affair at Styles (Hercule Poirot)
    The Hound of the Baskervilles (Sherlock Holmes, #5)
    The Da Vinci Code (Robert Langdon, #2)
    I'll Be Gone in the Dark: One Woman's Obsessive Search for the Golden State Killer (ebook)
    Career of Evil (Cormoran Strike, #3)
    Death on the Nile (Paperback)
    The Big Sleep (Paperback)
    The Devil in the White City: Murder, Magic, and Madness at the Fair That Changed America (Hardcover)
    The Snowman (Harry Hole, #7)
    Angels & Demons (Robert Langdon, #1)
    The Adventures of Sherlock Holmes (Sherlock Holmes, #3)
    The Bat (Harry Hole, #1)
    Assuming Names: A Con Artist's Masquerade (ebook)
    The Zombie Room (Kindle Edition)
    The Dry (Aaron Falk, #1)
    The Sign of Four (Sherlock Holmes, #2)
    The Elephant Tree (Paperback)
    The A.B.C. Murders (Hardcover)
    Killing Floor (Jack Reacher, #1)
    The Redbreast (Harry Hole, #3)
    Postmortem (Kay Scarpetta, #1)
    The Lovely Bones (Mass Market Paperback)
    Déjà Dead (Temperance Brennan, #1)
    The Black Echo (Harry Bosch, #1; Harry Bosch Universe, #1)
    Darkly Dreaming Dexter (Dexter, #1)
    Mr. Mercedes (Bill Hodges Trilogy, #1)
    The Surgeon (Rizzoli & Isles, #1)
    Rivers of London (Rivers of London, #1)
    Lethal White (Cormoran Strike, #4)
    Crime and Punishment (Paperback)
    Along Came a Spider (Alex Cross, #1)
    The Black Dahlia (L.A. Quartet, #1)
    ################################################################
    Shelve:  Crime
    Page:  1
    Total number of books scraped:  50
    ################################################################
    ################# Scraping the following books... #################
    The Girl with the Dragon Tattoo (Millennium, #1)
    The Girl Who Played with Fire (Millennium, #2)
    Gone Girl (Paperback)
    And Then There Were None (Paperback)
    The Girl Who Kicked the Hornet's Nest (Millennium, #3)
    The Girl on the Train (Hardcover)
    Murder on the Orient Express (Hercule Poirot, #10)
    The Cuckoo's Calling (Cormoran Strike, #1)
    In Cold Blood (Paperback)
    Sharp Objects (Paperback)
    A Study in Scarlet (Sherlock Holmes, #1)
    Dark Places (Hardcover)
    In the Woods (Dublin Murder Squad, #1)
    The Silkworm (Cormoran Strike, #2)
    The Godfather (The Godfather, #1)
    The Silence of the Lambs  (Hannibal Lecter, #2)
    Red Dragon (Hannibal Lecter, #1)
    The Murder of Roger Ackroyd (Hardcover)
    The Mysterious Affair at Styles (Hercule Poirot)
    The Hound of the Baskervilles (Sherlock Holmes, #5)
    The Da Vinci Code (Robert Langdon, #2)
    I'll Be Gone in the Dark: One Woman's Obsessive Search for the Golden State Killer (ebook)
    Career of Evil (Cormoran Strike, #3)
    Death on the Nile (Paperback)
    The Big Sleep (Paperback)
    The Devil in the White City: Murder, Magic, and Madness at the Fair That Changed America (Hardcover)
    The Snowman (Harry Hole, #7)
    Angels & Demons (Robert Langdon, #1)
    The Adventures of Sherlock Holmes (Sherlock Holmes, #3)
    The Bat (Harry Hole, #1)
    Assuming Names: A Con Artist's Masquerade (ebook)
    The Zombie Room (Kindle Edition)
    The Dry (Aaron Falk, #1)
    The Sign of Four (Sherlock Holmes, #2)
    The Elephant Tree (Paperback)
    The A.B.C. Murders (Hardcover)
    Killing Floor (Jack Reacher, #1)
    The Redbreast (Harry Hole, #3)
    Postmortem (Kay Scarpetta, #1)
    The Lovely Bones (Mass Market Paperback)
    Déjà Dead (Temperance Brennan, #1)
    The Black Echo (Harry Bosch, #1; Harry Bosch Universe, #1)
    Darkly Dreaming Dexter (Dexter, #1)
    Mr. Mercedes (Bill Hodges Trilogy, #1)
    The Surgeon (Rizzoli & Isles, #1)
    Rivers of London (Rivers of London, #1)
    Lethal White (Cormoran Strike, #4)
    Crime and Punishment (Paperback)
    Along Came a Spider (Alex Cross, #1)
    The Black Dahlia (L.A. Quartet, #1)
    Murder at the Vicarage (Miss Marple, #1)
    Helter Skelter: The True Story of the Manson Murders (Paperback)
    Perfume: The Story of a Murderer (Paperback)
    The Silent Patient (Hardcover)
    The Bone Collector (Lincoln Rhyme, #1)
    The Likeness (Dublin Murder Squad, #2)
    The Maltese Falcon (Paperback)
    My Sister, the Serial Killer (Hardcover)
    Naked in Death (In Death #1)
    A Time to Kill (Jake Brigance, #1)
    Nemesis (Harry Hole, #4)
    The 7½ Deaths of Evelyn Hardcastle (Hardcover)
    Faceless Killers (Kurt Wallander, #1)
    The Alienist (Dr. Laszlo Kreizler, #1)
    The Body in the Library (Miss Marple, #2)
    1st to Die (Women's Murder Club, #1)
    The Devil's Star (Harry Hole, #5)
    The Ice Princess (Patrik Hedström, #1)
    The Lincoln Lawyer (Mickey Haller, #1; Harry Bosch Universe, #15)
    The Keeper of Lost Causes (Department Q, #1)
    Killers of the Flower Moon: The Osage Murders and the Birth of the FBI (ebook)
    One for the Money (Stephanie Plum, #1)
    The Woman in the Window (Kindle Edition)
    Knots and Crosses (Inspector Rebus, #1)
    The Murder on the Links (Hercule Poirot)
    The Girl in the Spider's Web (Millennium, #4)
    Red Russia (Kindle Edition)
    The Secret History (Paperback)
    Cockroaches (Harry Hole, #2)
    Mindhunter: Inside the FBI's Elite Serial Crime Unit (Paperback)
    The Thursday Murder Club (Thursday Murder Club, #1)
    Kiss the Girls (Alex Cross, #2)
    The Body Farm (Kay Scarpetta, #5)
    Mystic River (Paperback)
    One of Us Is Lying (One of Us is Lying, #1)
    Death du Jour (Temperance Brennan, #2)
    The Talented Mr. Ripley (Ripley, #1)
    The Stranger Beside Me: Ted Bundy: The Shocking Inside Story (Paperback)
    The Leopard (Harry Hole, #8)
    Evil Under the Sun (Hardcover)
    No Country for Old Men (Paperback)
    Case Histories (Jackson Brodie #1)
    The Lost Symbol (Robert Langdon, #3)
    Shutter Island (Mass Market Paperback)
    The Name of the Rose (Paperback)
    Body of Evidence (Kay Scarpetta, #2)
    American Psycho (Paperback)
    The Outsider (Hardcover)
    The Complete Sherlock Holmes (Paperback)
    Still Life (Chief Inspector Armand Gamache, #1)
    ################################################################
    Shelve:  Crime
    Page:  2
    Total number of books scraped:  100
    ################################################################
    ################# Shelve: Travel #################
     
     
    ################# Scraping the following books... #################
    The Girl with the Dragon Tattoo (Millennium, #1)
    The Girl Who Played with Fire (Millennium, #2)
    Gone Girl (Paperback)
    And Then There Were None (Paperback)
    The Girl Who Kicked the Hornet's Nest (Millennium, #3)
    The Girl on the Train (Hardcover)
    Murder on the Orient Express (Hercule Poirot, #10)
    The Cuckoo's Calling (Cormoran Strike, #1)
    In Cold Blood (Paperback)
    Sharp Objects (Paperback)
    A Study in Scarlet (Sherlock Holmes, #1)
    Dark Places (Hardcover)
    In the Woods (Dublin Murder Squad, #1)
    The Silkworm (Cormoran Strike, #2)
    The Godfather (The Godfather, #1)
    The Silence of the Lambs  (Hannibal Lecter, #2)
    Red Dragon (Hannibal Lecter, #1)
    The Murder of Roger Ackroyd (Hardcover)
    The Mysterious Affair at Styles (Hercule Poirot)
    The Hound of the Baskervilles (Sherlock Holmes, #5)
    The Da Vinci Code (Robert Langdon, #2)
    I'll Be Gone in the Dark: One Woman's Obsessive Search for the Golden State Killer (ebook)
    Career of Evil (Cormoran Strike, #3)
    Death on the Nile (Paperback)
    The Big Sleep (Paperback)
    The Devil in the White City: Murder, Magic, and Madness at the Fair That Changed America (Hardcover)
    The Snowman (Harry Hole, #7)
    Angels & Demons (Robert Langdon, #1)
    The Adventures of Sherlock Holmes (Sherlock Holmes, #3)
    The Bat (Harry Hole, #1)
    Assuming Names: A Con Artist's Masquerade (ebook)
    The Zombie Room (Kindle Edition)
    The Dry (Aaron Falk, #1)
    The Sign of Four (Sherlock Holmes, #2)
    The Elephant Tree (Paperback)
    The A.B.C. Murders (Hardcover)
    Killing Floor (Jack Reacher, #1)
    The Redbreast (Harry Hole, #3)
    Postmortem (Kay Scarpetta, #1)
    The Lovely Bones (Mass Market Paperback)
    Déjà Dead (Temperance Brennan, #1)
    The Black Echo (Harry Bosch, #1; Harry Bosch Universe, #1)
    Darkly Dreaming Dexter (Dexter, #1)
    Mr. Mercedes (Bill Hodges Trilogy, #1)
    The Surgeon (Rizzoli & Isles, #1)
    Rivers of London (Rivers of London, #1)
    Lethal White (Cormoran Strike, #4)
    Crime and Punishment (Paperback)
    Along Came a Spider (Alex Cross, #1)
    The Black Dahlia (L.A. Quartet, #1)
    Murder at the Vicarage (Miss Marple, #1)
    Helter Skelter: The True Story of the Manson Murders (Paperback)
    Perfume: The Story of a Murderer (Paperback)
    The Silent Patient (Hardcover)
    The Bone Collector (Lincoln Rhyme, #1)
    The Likeness (Dublin Murder Squad, #2)
    The Maltese Falcon (Paperback)
    My Sister, the Serial Killer (Hardcover)
    Naked in Death (In Death #1)
    A Time to Kill (Jake Brigance, #1)
    Nemesis (Harry Hole, #4)
    The 7½ Deaths of Evelyn Hardcastle (Hardcover)
    Faceless Killers (Kurt Wallander, #1)
    The Alienist (Dr. Laszlo Kreizler, #1)
    The Body in the Library (Miss Marple, #2)
    1st to Die (Women's Murder Club, #1)
    The Devil's Star (Harry Hole, #5)
    The Ice Princess (Patrik Hedström, #1)
    The Lincoln Lawyer (Mickey Haller, #1; Harry Bosch Universe, #15)
    The Keeper of Lost Causes (Department Q, #1)
    Killers of the Flower Moon: The Osage Murders and the Birth of the FBI (ebook)
    One for the Money (Stephanie Plum, #1)
    The Woman in the Window (Kindle Edition)
    Knots and Crosses (Inspector Rebus, #1)
    The Murder on the Links (Hercule Poirot)
    The Girl in the Spider's Web (Millennium, #4)
    Red Russia (Kindle Edition)
    The Secret History (Paperback)
    Cockroaches (Harry Hole, #2)
    Mindhunter: Inside the FBI's Elite Serial Crime Unit (Paperback)
    The Thursday Murder Club (Thursday Murder Club, #1)
    Kiss the Girls (Alex Cross, #2)
    The Body Farm (Kay Scarpetta, #5)
    Mystic River (Paperback)
    One of Us Is Lying (One of Us is Lying, #1)
    Death du Jour (Temperance Brennan, #2)
    The Talented Mr. Ripley (Ripley, #1)
    The Stranger Beside Me: Ted Bundy: The Shocking Inside Story (Paperback)
    The Leopard (Harry Hole, #8)
    Evil Under the Sun (Hardcover)
    No Country for Old Men (Paperback)
    Case Histories (Jackson Brodie #1)
    The Lost Symbol (Robert Langdon, #3)
    Shutter Island (Mass Market Paperback)
    The Name of the Rose (Paperback)
    Body of Evidence (Kay Scarpetta, #2)
    American Psycho (Paperback)
    The Outsider (Hardcover)
    The Complete Sherlock Holmes (Paperback)
    Still Life (Chief Inspector Armand Gamache, #1)
    A Walk in the Woods: Rediscovering America on the Appalachian Trail (Mass Market Paperback)
    In a Sunburned Country (Paperback)
    Notes from a Small Island (Paperback)
    Eat, Pray, Love: One Woman's Search for Everything Across Italy, India and Indonesia (Paperback)
    Neither Here nor There: Travels in Europe (Paperback)
    Wild: From Lost to Found on the Pacific Crest Trail (Hardcover)
    The Lost Continent: Travels in Small Town America (Paperback)
    Into the Wild (Paperback)
    Travels with Charley: In Search of America (Paperback)
    Vagabonding: An Uncommon Guide to the Art of Long-Term World Travel (Paperback)
    I'm a Stranger Here Myself: Notes on Returning to America After Twenty Years Away (Paperback)
    A Year in Provence (Paperback)
    Under the Tuscan Sun (Paperback)
    On the Road (Paperback)
    The Road to Little Dribbling: Adventures of an American in Britain (Hardcover)
    The Great Railway Bazaar (Paperback)
    1,000 Places to See Before You Die (Paperback)
    The Art of Travel (Paperback)
    The Geography of Bliss: One Grump's Search for the Happiest Places in the World (Paperback)
    Into Thin Air: A Personal Account of the Mount Everest Disaster (Paperback)
    In Patagonia (Paperback)
    Blue Highways (Paperback)
    Dark Star Safari: Overland from Cairo to Cape Town (Paperback)
    The Sex Lives of Cannibals: Adrift in the Equatorial Pacific (Paperback)
    A Time of Gifts (Paperback)
    Turn Right at Machu Picchu: Rediscovering the Lost City One Step at a Time (Hardcover)
    Tales of a Female Nomad: Living at Large in the World (Paperback)
    Round Ireland with a Fridge (Paperback)
    Without Reservations: The Travels of an Independent Woman (Paperback)
    The Lost City of Z: A Tale of Deadly Obsession in the Amazon (Hardcover)
    Atlas Obscura: An Explorer's Guide to the World's Hidden Wonders (Hardcover)
    The Old Patagonian Express: By Train Through the Americas (Paperback)
    Seven Years in Tibet (Paperback)
    The Snow Leopard (Paperback)
    Getting Stoned with Savages: A Trip Through the Islands of Fiji and Vanuatu (Paperback)
    Lost on Planet China: The Strange and True Story of One Man's Attempt to Understand the World's Most Mystifying Nation, or How He Became Comfortable Eating Live Squid (Hardcover)
    The Travel Book: A Journey Through Every Country in the World (Paperback)
    A Cook's Tour: Global Adventures in Extreme Cuisines (Paperback)
    The Places in Between (Paperback)
    Ghost Train to the Eastern Star (Hardcover)
    Riding the Iron Rooster (Paperback)
    The Motorcycle Diaries: Notes on a Latin American Journey (Paperback)
    The Innocents Abroad (Paperback)
    Bill Bryson's African Diary (Hardcover)
    A Short Walk in the Hindu Kush (Hardcover)
    Tracks: A Woman's Solo Trek Across 1700 Miles of Australian Outback (Paperback)
    Kon-Tiki (Paperback)
    Holy Cow: An Indian Adventure (Paperback)
    The Lost Girls: Three Friends. Four Continents. One Unconventional Detour Around the World. (Hardcover)
    A Year in the World: Journeys of a Passionate Traveller (Paperback)
    ################################################################
    Shelve:  Travel
    Page:  1
    Total number of books scraped:  150
    ################################################################
    ################# Scraping the following books... #################
    The Girl with the Dragon Tattoo (Millennium, #1)
    The Girl Who Played with Fire (Millennium, #2)
    Gone Girl (Paperback)
    And Then There Were None (Paperback)
    The Girl Who Kicked the Hornet's Nest (Millennium, #3)
    The Girl on the Train (Hardcover)
    Murder on the Orient Express (Hercule Poirot, #10)
    The Cuckoo's Calling (Cormoran Strike, #1)
    In Cold Blood (Paperback)
    Sharp Objects (Paperback)
    A Study in Scarlet (Sherlock Holmes, #1)
    Dark Places (Hardcover)
    In the Woods (Dublin Murder Squad, #1)
    The Silkworm (Cormoran Strike, #2)
    The Godfather (The Godfather, #1)
    The Silence of the Lambs  (Hannibal Lecter, #2)
    Red Dragon (Hannibal Lecter, #1)
    The Murder of Roger Ackroyd (Hardcover)
    The Mysterious Affair at Styles (Hercule Poirot)
    The Hound of the Baskervilles (Sherlock Holmes, #5)
    The Da Vinci Code (Robert Langdon, #2)
    I'll Be Gone in the Dark: One Woman's Obsessive Search for the Golden State Killer (ebook)
    Career of Evil (Cormoran Strike, #3)
    Death on the Nile (Paperback)
    The Big Sleep (Paperback)
    The Devil in the White City: Murder, Magic, and Madness at the Fair That Changed America (Hardcover)
    The Snowman (Harry Hole, #7)
    Angels & Demons (Robert Langdon, #1)
    The Adventures of Sherlock Holmes (Sherlock Holmes, #3)
    The Bat (Harry Hole, #1)
    Assuming Names: A Con Artist's Masquerade (ebook)
    The Zombie Room (Kindle Edition)
    The Dry (Aaron Falk, #1)
    The Sign of Four (Sherlock Holmes, #2)
    The Elephant Tree (Paperback)
    The A.B.C. Murders (Hardcover)
    Killing Floor (Jack Reacher, #1)
    The Redbreast (Harry Hole, #3)
    Postmortem (Kay Scarpetta, #1)
    The Lovely Bones (Mass Market Paperback)
    Déjà Dead (Temperance Brennan, #1)
    The Black Echo (Harry Bosch, #1; Harry Bosch Universe, #1)
    Darkly Dreaming Dexter (Dexter, #1)
    Mr. Mercedes (Bill Hodges Trilogy, #1)
    The Surgeon (Rizzoli & Isles, #1)
    Rivers of London (Rivers of London, #1)
    Lethal White (Cormoran Strike, #4)
    Crime and Punishment (Paperback)
    Along Came a Spider (Alex Cross, #1)
    The Black Dahlia (L.A. Quartet, #1)
    Murder at the Vicarage (Miss Marple, #1)
    Helter Skelter: The True Story of the Manson Murders (Paperback)
    Perfume: The Story of a Murderer (Paperback)
    The Silent Patient (Hardcover)
    The Bone Collector (Lincoln Rhyme, #1)
    The Likeness (Dublin Murder Squad, #2)
    The Maltese Falcon (Paperback)
    My Sister, the Serial Killer (Hardcover)
    Naked in Death (In Death #1)
    A Time to Kill (Jake Brigance, #1)
    Nemesis (Harry Hole, #4)
    The 7½ Deaths of Evelyn Hardcastle (Hardcover)
    Faceless Killers (Kurt Wallander, #1)
    The Alienist (Dr. Laszlo Kreizler, #1)
    The Body in the Library (Miss Marple, #2)
    1st to Die (Women's Murder Club, #1)
    The Devil's Star (Harry Hole, #5)
    The Ice Princess (Patrik Hedström, #1)
    The Lincoln Lawyer (Mickey Haller, #1; Harry Bosch Universe, #15)
    The Keeper of Lost Causes (Department Q, #1)
    Killers of the Flower Moon: The Osage Murders and the Birth of the FBI (ebook)
    One for the Money (Stephanie Plum, #1)
    The Woman in the Window (Kindle Edition)
    Knots and Crosses (Inspector Rebus, #1)
    The Murder on the Links (Hercule Poirot)
    The Girl in the Spider's Web (Millennium, #4)
    Red Russia (Kindle Edition)
    The Secret History (Paperback)
    Cockroaches (Harry Hole, #2)
    Mindhunter: Inside the FBI's Elite Serial Crime Unit (Paperback)
    The Thursday Murder Club (Thursday Murder Club, #1)
    Kiss the Girls (Alex Cross, #2)
    The Body Farm (Kay Scarpetta, #5)
    Mystic River (Paperback)
    One of Us Is Lying (One of Us is Lying, #1)
    Death du Jour (Temperance Brennan, #2)
    The Talented Mr. Ripley (Ripley, #1)
    The Stranger Beside Me: Ted Bundy: The Shocking Inside Story (Paperback)
    The Leopard (Harry Hole, #8)
    Evil Under the Sun (Hardcover)
    No Country for Old Men (Paperback)
    Case Histories (Jackson Brodie #1)
    The Lost Symbol (Robert Langdon, #3)
    Shutter Island (Mass Market Paperback)
    The Name of the Rose (Paperback)
    Body of Evidence (Kay Scarpetta, #2)
    American Psycho (Paperback)
    The Outsider (Hardcover)
    The Complete Sherlock Holmes (Paperback)
    Still Life (Chief Inspector Armand Gamache, #1)
    A Walk in the Woods: Rediscovering America on the Appalachian Trail (Mass Market Paperback)
    In a Sunburned Country (Paperback)
    Notes from a Small Island (Paperback)
    Eat, Pray, Love: One Woman's Search for Everything Across Italy, India and Indonesia (Paperback)
    Neither Here nor There: Travels in Europe (Paperback)
    Wild: From Lost to Found on the Pacific Crest Trail (Hardcover)
    The Lost Continent: Travels in Small Town America (Paperback)
    Into the Wild (Paperback)
    Travels with Charley: In Search of America (Paperback)
    Vagabonding: An Uncommon Guide to the Art of Long-Term World Travel (Paperback)
    I'm a Stranger Here Myself: Notes on Returning to America After Twenty Years Away (Paperback)
    A Year in Provence (Paperback)
    Under the Tuscan Sun (Paperback)
    On the Road (Paperback)
    The Road to Little Dribbling: Adventures of an American in Britain (Hardcover)
    The Great Railway Bazaar (Paperback)
    1,000 Places to See Before You Die (Paperback)
    The Art of Travel (Paperback)
    The Geography of Bliss: One Grump's Search for the Happiest Places in the World (Paperback)
    Into Thin Air: A Personal Account of the Mount Everest Disaster (Paperback)
    In Patagonia (Paperback)
    Blue Highways (Paperback)
    Dark Star Safari: Overland from Cairo to Cape Town (Paperback)
    The Sex Lives of Cannibals: Adrift in the Equatorial Pacific (Paperback)
    A Time of Gifts (Paperback)
    Turn Right at Machu Picchu: Rediscovering the Lost City One Step at a Time (Hardcover)
    Tales of a Female Nomad: Living at Large in the World (Paperback)
    Round Ireland with a Fridge (Paperback)
    Without Reservations: The Travels of an Independent Woman (Paperback)
    The Lost City of Z: A Tale of Deadly Obsession in the Amazon (Hardcover)
    Atlas Obscura: An Explorer's Guide to the World's Hidden Wonders (Hardcover)
    The Old Patagonian Express: By Train Through the Americas (Paperback)
    Seven Years in Tibet (Paperback)
    The Snow Leopard (Paperback)
    Getting Stoned with Savages: A Trip Through the Islands of Fiji and Vanuatu (Paperback)
    Lost on Planet China: The Strange and True Story of One Man's Attempt to Understand the World's Most Mystifying Nation, or How He Became Comfortable Eating Live Squid (Hardcover)
    The Travel Book: A Journey Through Every Country in the World (Paperback)
    A Cook's Tour: Global Adventures in Extreme Cuisines (Paperback)
    The Places in Between (Paperback)
    Ghost Train to the Eastern Star (Hardcover)
    Riding the Iron Rooster (Paperback)
    The Motorcycle Diaries: Notes on a Latin American Journey (Paperback)
    The Innocents Abroad (Paperback)
    Bill Bryson's African Diary (Hardcover)
    A Short Walk in the Hindu Kush (Hardcover)
    Tracks: A Woman's Solo Trek Across 1700 Miles of Australian Outback (Paperback)
    Kon-Tiki (Paperback)
    Holy Cow: An Indian Adventure (Paperback)
    The Lost Girls: Three Friends. Four Continents. One Unconventional Detour Around the World. (Hardcover)
    A Year in the World: Journeys of a Passionate Traveller (Paperback)
    The Old Ways: A Journey on Foot (Hardcover)
    Around the World in Eighty Days (Paperback)
    Shantaram (Paperback)
    The Songlines (Paperback)
    The Beach (Paperback)
    The Year of Living Danishly: My Twelve Months Unearthing the Secrets of the World's Happiest Country (Paperback)
    Three Cups of Tea: One Man's Mission to Promote Peace ... One School at a Time (Paperback)
    The Happy Isles of Oceania: Paddling the Pacific (Paperback)
    What I Was Doing While You Were Breeding (Paperback)
    Toujours Provence (Paperback)
    McCarthy's Bar: A Journey of Discovery in Ireland (Paperback)
    Long Way Round: Chasing Shadows Across the World (Hardcover)
    Zen and the Art of Motorcycle Maintenance: An Inquiry Into Values (Phaedrus, #1)
    Blue Latitudes: Boldly Going Where Captain Cook Has Gone Before (Paperback)
    Assassination Vacation (Paperback)
    Travels in Siberia (Hardcover)
    A Moveable Feast (Paperback)
    The Good Girl's Guide to Getting Lost: A Memoir of Three Continents, Two Friends, and One Unexpected Adventure (Paperback)
    Paris to the Moon (Paperback)
    Driving Over Lemons: An Optimist in Andalucía (Paperback)
    Arabian Sands (Paperback)
    City of Djinns: A Year in Delhi (Paperback)
    Between the Woods and the Water (Paperback)
    Shadow of the Silk Road (Hardcover)
    The Road to Oxiana (Paperback)
    Blood River: A Journey to Africa's Broken Heart (Paperback)
    The Alchemist (Paperback)
    The Shadow of the Sun (Paperback)
    The Kingdom by the Sea (Paperback)
    River Town: Two Years on the Yangtze (Paperback)
    Travel as a Political Act (Paperback)
    Bella Tuscany (Paperback)
    Hokkaido Highway Blues: Hitchhiking Japan (Paperback)
    Down and Out in Paris and London (Paperback)
    Deep South: Four Seasons on Back Roads (Hardcover)
    Whatever You Do, Don't Run: True Tales of a Botswana Safari Guide (Paperback)
    The Lost City of the Monkey God (Kindle Edition)
    Last Chance to See (Paperback)
    The Pillars of Hercules (Paperback)
    Travels with Herodotus (Hardcover)
    The Travels (Paperback)
    The Caliph's House: A Year in Casablanca (Paperback)
    Black Lamb and Grey Falcon (Paperback)
    Rick Steves' Europe Through the Back Door (Paperback)
    A Walk Across America (Paperback)
    Endurance: Shackleton's Incredible Voyage (Hardcover)
    Lands of Lost Borders: Out of Bounds on the Silk Road (Paperback)
    In Xanadu: A Quest (Paperback)
    Around the World in 80 Days: Companion to the PBS Series (Paperback)
    Himalaya (Hardcover)
    ################################################################
    Shelve:  Travel
    Page:  2
    Total number of books scraped:  200
    ################################################################
    ################# Shelve: Art #################
     
     
    ################# Scraping the following books... #################
    The Girl with the Dragon Tattoo (Millennium, #1)
    The Girl Who Played with Fire (Millennium, #2)
    Gone Girl (Paperback)
    And Then There Were None (Paperback)
    The Girl Who Kicked the Hornet's Nest (Millennium, #3)
    The Girl on the Train (Hardcover)
    Murder on the Orient Express (Hercule Poirot, #10)
    The Cuckoo's Calling (Cormoran Strike, #1)
    In Cold Blood (Paperback)
    Sharp Objects (Paperback)
    A Study in Scarlet (Sherlock Holmes, #1)
    Dark Places (Hardcover)
    In the Woods (Dublin Murder Squad, #1)
    The Silkworm (Cormoran Strike, #2)
    The Godfather (The Godfather, #1)
    The Silence of the Lambs  (Hannibal Lecter, #2)
    Red Dragon (Hannibal Lecter, #1)
    The Murder of Roger Ackroyd (Hardcover)
    The Mysterious Affair at Styles (Hercule Poirot)
    The Hound of the Baskervilles (Sherlock Holmes, #5)
    The Da Vinci Code (Robert Langdon, #2)
    I'll Be Gone in the Dark: One Woman's Obsessive Search for the Golden State Killer (ebook)
    Career of Evil (Cormoran Strike, #3)
    Death on the Nile (Paperback)
    The Big Sleep (Paperback)
    The Devil in the White City: Murder, Magic, and Madness at the Fair That Changed America (Hardcover)
    The Snowman (Harry Hole, #7)
    Angels & Demons (Robert Langdon, #1)
    The Adventures of Sherlock Holmes (Sherlock Holmes, #3)
    The Bat (Harry Hole, #1)
    Assuming Names: A Con Artist's Masquerade (ebook)
    The Zombie Room (Kindle Edition)
    The Dry (Aaron Falk, #1)
    The Sign of Four (Sherlock Holmes, #2)
    The Elephant Tree (Paperback)
    The A.B.C. Murders (Hardcover)
    Killing Floor (Jack Reacher, #1)
    The Redbreast (Harry Hole, #3)
    Postmortem (Kay Scarpetta, #1)
    The Lovely Bones (Mass Market Paperback)
    Déjà Dead (Temperance Brennan, #1)
    The Black Echo (Harry Bosch, #1; Harry Bosch Universe, #1)
    Darkly Dreaming Dexter (Dexter, #1)
    Mr. Mercedes (Bill Hodges Trilogy, #1)
    The Surgeon (Rizzoli & Isles, #1)
    Rivers of London (Rivers of London, #1)
    Lethal White (Cormoran Strike, #4)
    Crime and Punishment (Paperback)
    Along Came a Spider (Alex Cross, #1)
    The Black Dahlia (L.A. Quartet, #1)
    Murder at the Vicarage (Miss Marple, #1)
    Helter Skelter: The True Story of the Manson Murders (Paperback)
    Perfume: The Story of a Murderer (Paperback)
    The Silent Patient (Hardcover)
    The Bone Collector (Lincoln Rhyme, #1)
    The Likeness (Dublin Murder Squad, #2)
    The Maltese Falcon (Paperback)
    My Sister, the Serial Killer (Hardcover)
    Naked in Death (In Death #1)
    A Time to Kill (Jake Brigance, #1)
    Nemesis (Harry Hole, #4)
    The 7½ Deaths of Evelyn Hardcastle (Hardcover)
    Faceless Killers (Kurt Wallander, #1)
    The Alienist (Dr. Laszlo Kreizler, #1)
    The Body in the Library (Miss Marple, #2)
    1st to Die (Women's Murder Club, #1)
    The Devil's Star (Harry Hole, #5)
    The Ice Princess (Patrik Hedström, #1)
    The Lincoln Lawyer (Mickey Haller, #1; Harry Bosch Universe, #15)
    The Keeper of Lost Causes (Department Q, #1)
    Killers of the Flower Moon: The Osage Murders and the Birth of the FBI (ebook)
    One for the Money (Stephanie Plum, #1)
    The Woman in the Window (Kindle Edition)
    Knots and Crosses (Inspector Rebus, #1)
    The Murder on the Links (Hercule Poirot)
    The Girl in the Spider's Web (Millennium, #4)
    Red Russia (Kindle Edition)
    The Secret History (Paperback)
    Cockroaches (Harry Hole, #2)
    Mindhunter: Inside the FBI's Elite Serial Crime Unit (Paperback)
    The Thursday Murder Club (Thursday Murder Club, #1)
    Kiss the Girls (Alex Cross, #2)
    The Body Farm (Kay Scarpetta, #5)
    Mystic River (Paperback)
    One of Us Is Lying (One of Us is Lying, #1)
    Death du Jour (Temperance Brennan, #2)
    The Talented Mr. Ripley (Ripley, #1)
    The Stranger Beside Me: Ted Bundy: The Shocking Inside Story (Paperback)
    The Leopard (Harry Hole, #8)
    Evil Under the Sun (Hardcover)
    No Country for Old Men (Paperback)
    Case Histories (Jackson Brodie #1)
    The Lost Symbol (Robert Langdon, #3)
    Shutter Island (Mass Market Paperback)
    The Name of the Rose (Paperback)
    Body of Evidence (Kay Scarpetta, #2)
    American Psycho (Paperback)
    The Outsider (Hardcover)
    The Complete Sherlock Holmes (Paperback)
    Still Life (Chief Inspector Armand Gamache, #1)
    A Walk in the Woods: Rediscovering America on the Appalachian Trail (Mass Market Paperback)
    In a Sunburned Country (Paperback)
    Notes from a Small Island (Paperback)
    Eat, Pray, Love: One Woman's Search for Everything Across Italy, India and Indonesia (Paperback)
    Neither Here nor There: Travels in Europe (Paperback)
    Wild: From Lost to Found on the Pacific Crest Trail (Hardcover)
    The Lost Continent: Travels in Small Town America (Paperback)
    Into the Wild (Paperback)
    Travels with Charley: In Search of America (Paperback)
    Vagabonding: An Uncommon Guide to the Art of Long-Term World Travel (Paperback)
    I'm a Stranger Here Myself: Notes on Returning to America After Twenty Years Away (Paperback)
    A Year in Provence (Paperback)
    Under the Tuscan Sun (Paperback)
    On the Road (Paperback)
    The Road to Little Dribbling: Adventures of an American in Britain (Hardcover)
    The Great Railway Bazaar (Paperback)
    1,000 Places to See Before You Die (Paperback)
    The Art of Travel (Paperback)
    The Geography of Bliss: One Grump's Search for the Happiest Places in the World (Paperback)
    Into Thin Air: A Personal Account of the Mount Everest Disaster (Paperback)
    In Patagonia (Paperback)
    Blue Highways (Paperback)
    Dark Star Safari: Overland from Cairo to Cape Town (Paperback)
    The Sex Lives of Cannibals: Adrift in the Equatorial Pacific (Paperback)
    A Time of Gifts (Paperback)
    Turn Right at Machu Picchu: Rediscovering the Lost City One Step at a Time (Hardcover)
    Tales of a Female Nomad: Living at Large in the World (Paperback)
    Round Ireland with a Fridge (Paperback)
    Without Reservations: The Travels of an Independent Woman (Paperback)
    The Lost City of Z: A Tale of Deadly Obsession in the Amazon (Hardcover)
    Atlas Obscura: An Explorer's Guide to the World's Hidden Wonders (Hardcover)
    The Old Patagonian Express: By Train Through the Americas (Paperback)
    Seven Years in Tibet (Paperback)
    The Snow Leopard (Paperback)
    Getting Stoned with Savages: A Trip Through the Islands of Fiji and Vanuatu (Paperback)
    Lost on Planet China: The Strange and True Story of One Man's Attempt to Understand the World's Most Mystifying Nation, or How He Became Comfortable Eating Live Squid (Hardcover)
    The Travel Book: A Journey Through Every Country in the World (Paperback)
    A Cook's Tour: Global Adventures in Extreme Cuisines (Paperback)
    The Places in Between (Paperback)
    Ghost Train to the Eastern Star (Hardcover)
    Riding the Iron Rooster (Paperback)
    The Motorcycle Diaries: Notes on a Latin American Journey (Paperback)
    The Innocents Abroad (Paperback)
    Bill Bryson's African Diary (Hardcover)
    A Short Walk in the Hindu Kush (Hardcover)
    Tracks: A Woman's Solo Trek Across 1700 Miles of Australian Outback (Paperback)
    Kon-Tiki (Paperback)
    Holy Cow: An Indian Adventure (Paperback)
    The Lost Girls: Three Friends. Four Continents. One Unconventional Detour Around the World. (Hardcover)
    A Year in the World: Journeys of a Passionate Traveller (Paperback)
    The Old Ways: A Journey on Foot (Hardcover)
    Around the World in Eighty Days (Paperback)
    Shantaram (Paperback)
    The Songlines (Paperback)
    The Beach (Paperback)
    The Year of Living Danishly: My Twelve Months Unearthing the Secrets of the World's Happiest Country (Paperback)
    Three Cups of Tea: One Man's Mission to Promote Peace ... One School at a Time (Paperback)
    The Happy Isles of Oceania: Paddling the Pacific (Paperback)
    What I Was Doing While You Were Breeding (Paperback)
    Toujours Provence (Paperback)
    McCarthy's Bar: A Journey of Discovery in Ireland (Paperback)
    Long Way Round: Chasing Shadows Across the World (Hardcover)
    Zen and the Art of Motorcycle Maintenance: An Inquiry Into Values (Phaedrus, #1)
    Blue Latitudes: Boldly Going Where Captain Cook Has Gone Before (Paperback)
    Assassination Vacation (Paperback)
    Travels in Siberia (Hardcover)
    A Moveable Feast (Paperback)
    The Good Girl's Guide to Getting Lost: A Memoir of Three Continents, Two Friends, and One Unexpected Adventure (Paperback)
    Paris to the Moon (Paperback)
    Driving Over Lemons: An Optimist in Andalucía (Paperback)
    Arabian Sands (Paperback)
    City of Djinns: A Year in Delhi (Paperback)
    Between the Woods and the Water (Paperback)
    Shadow of the Silk Road (Hardcover)
    The Road to Oxiana (Paperback)
    Blood River: A Journey to Africa's Broken Heart (Paperback)
    The Alchemist (Paperback)
    The Shadow of the Sun (Paperback)
    The Kingdom by the Sea (Paperback)
    River Town: Two Years on the Yangtze (Paperback)
    Travel as a Political Act (Paperback)
    Bella Tuscany (Paperback)
    Hokkaido Highway Blues: Hitchhiking Japan (Paperback)
    Down and Out in Paris and London (Paperback)
    Deep South: Four Seasons on Back Roads (Hardcover)
    Whatever You Do, Don't Run: True Tales of a Botswana Safari Guide (Paperback)
    The Lost City of the Monkey God (Kindle Edition)
    Last Chance to See (Paperback)
    The Pillars of Hercules (Paperback)
    Travels with Herodotus (Hardcover)
    The Travels (Paperback)
    The Caliph's House: A Year in Casablanca (Paperback)
    Black Lamb and Grey Falcon (Paperback)
    Rick Steves' Europe Through the Back Door (Paperback)
    A Walk Across America (Paperback)
    Endurance: Shackleton's Incredible Voyage (Hardcover)
    Lands of Lost Borders: Out of Bounds on the Silk Road (Paperback)
    In Xanadu: A Quest (Paperback)
    Around the World in 80 Days: Companion to the PBS Series (Paperback)
    Himalaya (Hardcover)
    Ways of Seeing (Paperback)
    The Story of Art (Hardcover)
    The New Drawing on the Right Side of the Brain (Paperback)
    Steal Like an Artist: 10 Things Nobody Told You About Being Creative (Paperback)
    Wall and Piece (Paperback)
    The Artist's Way: A Spiritual Path to Higher Creativity (Paperback)
    Art and Fear: Observations on the Perils (and Rewards) of Artmaking
    Girl with a Pearl Earring (Paperback)
    The Art Book (Paperback)
    The Letters of Vincent van Gogh (Paperback)
    Concerning the Spiritual in Art (Paperback)
    Seven Days in the Art World (Paperback)
    The Goldfinch (Hardcover)
    History of Beauty (Paperback)
    On Photography (Paperback)
    The Diary of Frida Kahlo: An Intimate Self-Portrait (Hardcover)
    Understanding Comics: The Invisible Art (Paperback)
    M.C. Escher: The Graphic Work (Paperback)
    Art Through the Ages  (Hardcover)
    The War of Art: Winning the Inner Creative Battle (Paperback)
    Color: A Natural History of the Palette (Paperback)
    Leonardo da Vinci (Hardcover)
    The Lives of the Artists (Paperback)
    Vincent Van Gogh: The Complete Paintings (Hardcover)
    Color and Light: A Guide for the Realist Painter (Paperback)
    Just Kids (Hardcover)
    The Shock of the New (Paperback)
    History of Art (Hardcover)
    The Art Forger (Hardcover)
    Show Your Work!: 10 Ways to Share Your Creativity and Get Discovered (Paperback)
    Interaction of Color (Paperback)
    The Agony and the Ecstasy (Mass Market Paperback)
    What Are You Looking At?: 150 Years of Modern Art in a Nutshell (Hardcover)
    Leonardo's Notebooks (Hardcover)
    Figure Drawing for All It's Worth (How to draw and paint)
    The Art Spirit (Paperback)
    An Illustrated Life: Drawing Inspiration from the Private Sketchbooks of Artists, Illustrators and Designers (Paperback)
    Michelangelo and the Pope's Ceiling (Paperback)
    The Philosophy of Andy Warhol (From A to B and Back Again)
    The Secret Lives of Color (Hardcover)
    Van Gogh (Kindle Edition)
    Camera Lucida: Reflections on Photography (Paperback)
    The Judgment of Paris: The Revolutionary Decade That Gave the World Impressionism (Paperback)
    Faeries (Hardcover)
    On Ugliness (Hardcover)
    The Dot (Hardcover)
    Frida: A Biography of Frida Kahlo (Paperback)
    The Power of Art (Hardcover)
    Griffin and Sabine (Griffin & Sabine #1)
    PostSecret: Extraordinary Confessions from Ordinary Lives (PostSecret)
    ################################################################
    Shelve:  Art
    Page:  1
    Total number of books scraped:  250
    ################################################################
    ################# Scraping the following books... #################
    The Girl with the Dragon Tattoo (Millennium, #1)
    The Girl Who Played with Fire (Millennium, #2)
    Gone Girl (Paperback)
    And Then There Were None (Paperback)
    The Girl Who Kicked the Hornet's Nest (Millennium, #3)
    The Girl on the Train (Hardcover)
    Murder on the Orient Express (Hercule Poirot, #10)
    The Cuckoo's Calling (Cormoran Strike, #1)
    In Cold Blood (Paperback)
    Sharp Objects (Paperback)
    A Study in Scarlet (Sherlock Holmes, #1)
    Dark Places (Hardcover)
    In the Woods (Dublin Murder Squad, #1)
    The Silkworm (Cormoran Strike, #2)
    The Godfather (The Godfather, #1)
    The Silence of the Lambs  (Hannibal Lecter, #2)
    Red Dragon (Hannibal Lecter, #1)
    The Murder of Roger Ackroyd (Hardcover)
    The Mysterious Affair at Styles (Hercule Poirot)
    The Hound of the Baskervilles (Sherlock Holmes, #5)
    The Da Vinci Code (Robert Langdon, #2)
    I'll Be Gone in the Dark: One Woman's Obsessive Search for the Golden State Killer (ebook)
    Career of Evil (Cormoran Strike, #3)
    Death on the Nile (Paperback)
    The Big Sleep (Paperback)
    The Devil in the White City: Murder, Magic, and Madness at the Fair That Changed America (Hardcover)
    The Snowman (Harry Hole, #7)
    Angels & Demons (Robert Langdon, #1)
    The Adventures of Sherlock Holmes (Sherlock Holmes, #3)
    The Bat (Harry Hole, #1)
    Assuming Names: A Con Artist's Masquerade (ebook)
    The Zombie Room (Kindle Edition)
    The Dry (Aaron Falk, #1)
    The Sign of Four (Sherlock Holmes, #2)
    The Elephant Tree (Paperback)
    The A.B.C. Murders (Hardcover)
    Killing Floor (Jack Reacher, #1)
    The Redbreast (Harry Hole, #3)
    Postmortem (Kay Scarpetta, #1)
    The Lovely Bones (Mass Market Paperback)
    Déjà Dead (Temperance Brennan, #1)
    The Black Echo (Harry Bosch, #1; Harry Bosch Universe, #1)
    Darkly Dreaming Dexter (Dexter, #1)
    Mr. Mercedes (Bill Hodges Trilogy, #1)
    The Surgeon (Rizzoli & Isles, #1)
    Rivers of London (Rivers of London, #1)
    Lethal White (Cormoran Strike, #4)
    Crime and Punishment (Paperback)
    Along Came a Spider (Alex Cross, #1)
    The Black Dahlia (L.A. Quartet, #1)
    Murder at the Vicarage (Miss Marple, #1)
    Helter Skelter: The True Story of the Manson Murders (Paperback)
    Perfume: The Story of a Murderer (Paperback)
    The Silent Patient (Hardcover)
    The Bone Collector (Lincoln Rhyme, #1)
    The Likeness (Dublin Murder Squad, #2)
    The Maltese Falcon (Paperback)
    My Sister, the Serial Killer (Hardcover)
    Naked in Death (In Death #1)
    A Time to Kill (Jake Brigance, #1)
    Nemesis (Harry Hole, #4)
    The 7½ Deaths of Evelyn Hardcastle (Hardcover)
    Faceless Killers (Kurt Wallander, #1)
    The Alienist (Dr. Laszlo Kreizler, #1)
    The Body in the Library (Miss Marple, #2)
    1st to Die (Women's Murder Club, #1)
    The Devil's Star (Harry Hole, #5)
    The Ice Princess (Patrik Hedström, #1)
    The Lincoln Lawyer (Mickey Haller, #1; Harry Bosch Universe, #15)
    The Keeper of Lost Causes (Department Q, #1)
    Killers of the Flower Moon: The Osage Murders and the Birth of the FBI (ebook)
    One for the Money (Stephanie Plum, #1)
    The Woman in the Window (Kindle Edition)
    Knots and Crosses (Inspector Rebus, #1)
    The Murder on the Links (Hercule Poirot)
    The Girl in the Spider's Web (Millennium, #4)
    Red Russia (Kindle Edition)
    The Secret History (Paperback)
    Cockroaches (Harry Hole, #2)
    Mindhunter: Inside the FBI's Elite Serial Crime Unit (Paperback)
    The Thursday Murder Club (Thursday Murder Club, #1)
    Kiss the Girls (Alex Cross, #2)
    The Body Farm (Kay Scarpetta, #5)
    Mystic River (Paperback)
    One of Us Is Lying (One of Us is Lying, #1)
    Death du Jour (Temperance Brennan, #2)
    The Talented Mr. Ripley (Ripley, #1)
    The Stranger Beside Me: Ted Bundy: The Shocking Inside Story (Paperback)
    The Leopard (Harry Hole, #8)
    Evil Under the Sun (Hardcover)
    No Country for Old Men (Paperback)
    Case Histories (Jackson Brodie #1)
    The Lost Symbol (Robert Langdon, #3)
    Shutter Island (Mass Market Paperback)
    The Name of the Rose (Paperback)
    Body of Evidence (Kay Scarpetta, #2)
    American Psycho (Paperback)
    The Outsider (Hardcover)
    The Complete Sherlock Holmes (Paperback)
    Still Life (Chief Inspector Armand Gamache, #1)
    A Walk in the Woods: Rediscovering America on the Appalachian Trail (Mass Market Paperback)
    In a Sunburned Country (Paperback)
    Notes from a Small Island (Paperback)
    Eat, Pray, Love: One Woman's Search for Everything Across Italy, India and Indonesia (Paperback)
    Neither Here nor There: Travels in Europe (Paperback)
    Wild: From Lost to Found on the Pacific Crest Trail (Hardcover)
    The Lost Continent: Travels in Small Town America (Paperback)
    Into the Wild (Paperback)
    Travels with Charley: In Search of America (Paperback)
    Vagabonding: An Uncommon Guide to the Art of Long-Term World Travel (Paperback)
    I'm a Stranger Here Myself: Notes on Returning to America After Twenty Years Away (Paperback)
    A Year in Provence (Paperback)
    Under the Tuscan Sun (Paperback)
    On the Road (Paperback)
    The Road to Little Dribbling: Adventures of an American in Britain (Hardcover)
    The Great Railway Bazaar (Paperback)
    1,000 Places to See Before You Die (Paperback)
    The Art of Travel (Paperback)
    The Geography of Bliss: One Grump's Search for the Happiest Places in the World (Paperback)
    Into Thin Air: A Personal Account of the Mount Everest Disaster (Paperback)
    In Patagonia (Paperback)
    Blue Highways (Paperback)
    Dark Star Safari: Overland from Cairo to Cape Town (Paperback)
    The Sex Lives of Cannibals: Adrift in the Equatorial Pacific (Paperback)
    A Time of Gifts (Paperback)
    Turn Right at Machu Picchu: Rediscovering the Lost City One Step at a Time (Hardcover)
    Tales of a Female Nomad: Living at Large in the World (Paperback)
    Round Ireland with a Fridge (Paperback)
    Without Reservations: The Travels of an Independent Woman (Paperback)
    The Lost City of Z: A Tale of Deadly Obsession in the Amazon (Hardcover)
    Atlas Obscura: An Explorer's Guide to the World's Hidden Wonders (Hardcover)
    The Old Patagonian Express: By Train Through the Americas (Paperback)
    Seven Years in Tibet (Paperback)
    The Snow Leopard (Paperback)
    Getting Stoned with Savages: A Trip Through the Islands of Fiji and Vanuatu (Paperback)
    Lost on Planet China: The Strange and True Story of One Man's Attempt to Understand the World's Most Mystifying Nation, or How He Became Comfortable Eating Live Squid (Hardcover)
    The Travel Book: A Journey Through Every Country in the World (Paperback)
    A Cook's Tour: Global Adventures in Extreme Cuisines (Paperback)
    The Places in Between (Paperback)
    Ghost Train to the Eastern Star (Hardcover)
    Riding the Iron Rooster (Paperback)
    The Motorcycle Diaries: Notes on a Latin American Journey (Paperback)
    The Innocents Abroad (Paperback)
    Bill Bryson's African Diary (Hardcover)
    A Short Walk in the Hindu Kush (Hardcover)
    Tracks: A Woman's Solo Trek Across 1700 Miles of Australian Outback (Paperback)
    Kon-Tiki (Paperback)
    Holy Cow: An Indian Adventure (Paperback)
    The Lost Girls: Three Friends. Four Continents. One Unconventional Detour Around the World. (Hardcover)
    A Year in the World: Journeys of a Passionate Traveller (Paperback)
    The Old Ways: A Journey on Foot (Hardcover)
    Around the World in Eighty Days (Paperback)
    Shantaram (Paperback)
    The Songlines (Paperback)
    The Beach (Paperback)
    The Year of Living Danishly: My Twelve Months Unearthing the Secrets of the World's Happiest Country (Paperback)
    Three Cups of Tea: One Man's Mission to Promote Peace ... One School at a Time (Paperback)
    The Happy Isles of Oceania: Paddling the Pacific (Paperback)
    What I Was Doing While You Were Breeding (Paperback)
    Toujours Provence (Paperback)
    McCarthy's Bar: A Journey of Discovery in Ireland (Paperback)
    Long Way Round: Chasing Shadows Across the World (Hardcover)
    Zen and the Art of Motorcycle Maintenance: An Inquiry Into Values (Phaedrus, #1)
    Blue Latitudes: Boldly Going Where Captain Cook Has Gone Before (Paperback)
    Assassination Vacation (Paperback)
    Travels in Siberia (Hardcover)
    A Moveable Feast (Paperback)
    The Good Girl's Guide to Getting Lost: A Memoir of Three Continents, Two Friends, and One Unexpected Adventure (Paperback)
    Paris to the Moon (Paperback)
    Driving Over Lemons: An Optimist in Andalucía (Paperback)
    Arabian Sands (Paperback)
    City of Djinns: A Year in Delhi (Paperback)
    Between the Woods and the Water (Paperback)
    Shadow of the Silk Road (Hardcover)
    The Road to Oxiana (Paperback)
    Blood River: A Journey to Africa's Broken Heart (Paperback)
    The Alchemist (Paperback)
    The Shadow of the Sun (Paperback)
    The Kingdom by the Sea (Paperback)
    River Town: Two Years on the Yangtze (Paperback)
    Travel as a Political Act (Paperback)
    Bella Tuscany (Paperback)
    Hokkaido Highway Blues: Hitchhiking Japan (Paperback)
    Down and Out in Paris and London (Paperback)
    Deep South: Four Seasons on Back Roads (Hardcover)
    Whatever You Do, Don't Run: True Tales of a Botswana Safari Guide (Paperback)
    The Lost City of the Monkey God (Kindle Edition)
    Last Chance to See (Paperback)
    The Pillars of Hercules (Paperback)
    Travels with Herodotus (Hardcover)
    The Travels (Paperback)
    The Caliph's House: A Year in Casablanca (Paperback)
    Black Lamb and Grey Falcon (Paperback)
    Rick Steves' Europe Through the Back Door (Paperback)
    A Walk Across America (Paperback)
    Endurance: Shackleton's Incredible Voyage (Hardcover)
    Lands of Lost Borders: Out of Bounds on the Silk Road (Paperback)
    In Xanadu: A Quest (Paperback)
    Around the World in 80 Days: Companion to the PBS Series (Paperback)
    Himalaya (Hardcover)
    Ways of Seeing (Paperback)
    The Story of Art (Hardcover)
    The New Drawing on the Right Side of the Brain (Paperback)
    Steal Like an Artist: 10 Things Nobody Told You About Being Creative (Paperback)
    Wall and Piece (Paperback)
    The Artist's Way: A Spiritual Path to Higher Creativity (Paperback)
    Art and Fear: Observations on the Perils (and Rewards) of Artmaking
    Girl with a Pearl Earring (Paperback)
    The Art Book (Paperback)
    The Letters of Vincent van Gogh (Paperback)
    Concerning the Spiritual in Art (Paperback)
    Seven Days in the Art World (Paperback)
    The Goldfinch (Hardcover)
    History of Beauty (Paperback)
    On Photography (Paperback)
    The Diary of Frida Kahlo: An Intimate Self-Portrait (Hardcover)
    Understanding Comics: The Invisible Art (Paperback)
    M.C. Escher: The Graphic Work (Paperback)
    Art Through the Ages  (Hardcover)
    The War of Art: Winning the Inner Creative Battle (Paperback)
    Color: A Natural History of the Palette (Paperback)
    Leonardo da Vinci (Hardcover)
    The Lives of the Artists (Paperback)
    Vincent Van Gogh: The Complete Paintings (Hardcover)
    Color and Light: A Guide for the Realist Painter (Paperback)
    Just Kids (Hardcover)
    The Shock of the New (Paperback)
    History of Art (Hardcover)
    The Art Forger (Hardcover)
    Show Your Work!: 10 Ways to Share Your Creativity and Get Discovered (Paperback)
    Interaction of Color (Paperback)
    The Agony and the Ecstasy (Mass Market Paperback)
    What Are You Looking At?: 150 Years of Modern Art in a Nutshell (Hardcover)
    Leonardo's Notebooks (Hardcover)
    Figure Drawing for All It's Worth (How to draw and paint)
    The Art Spirit (Paperback)
    An Illustrated Life: Drawing Inspiration from the Private Sketchbooks of Artists, Illustrators and Designers (Paperback)
    Michelangelo and the Pope's Ceiling (Paperback)
    The Philosophy of Andy Warhol (From A to B and Back Again)
    The Secret Lives of Color (Hardcover)
    Van Gogh (Kindle Edition)
    Camera Lucida: Reflections on Photography (Paperback)
    The Judgment of Paris: The Revolutionary Decade That Gave the World Impressionism (Paperback)
    Faeries (Hardcover)
    On Ugliness (Hardcover)
    The Dot (Hardcover)
    Frida: A Biography of Frida Kahlo (Paperback)
    The Power of Art (Hardcover)
    Griffin and Sabine (Griffin & Sabine #1)
    PostSecret: Extraordinary Confessions from Ordinary Lives (PostSecret)
    Brunelleschi's Dome: How a Renaissance Genius Reinvented Architecture (Paperback)
    Art Matters (Kindle Edition)
    The Lonely City: Adventures in the Art of Being Alone (Hardcover)
    The Monuments Men: Allied Heroes, Nazi Thieves, and the Greatest Treasure Hunt in History (Hardcover)
    Gustav Klimt: 1862-1918 (Paperback)
    The Creative Habit: Learn It and Use It for Life (Paperback)
    Art and Illusion: A Study in the Psychology of Pictorial Representation (Paperback)
    Big Magic: Creative Living Beyond Fear (Hardcover)
    Lust for Life (Paperback)
    Keys to Drawing (Paperback)
    The Work of Art in the Age of Its Technological Reproducibility, and Other Writings on Media (Paperback)
    The Natural Way to Draw (Paperback)
    The Lost Painting (Paperback)
    Imaginative Realism: How to Paint What Doesn't Exist (Paperback)
    Amphigorey (Amphigorey, #1)
    The Da Vinci Code (Robert Langdon, #2)
    Andy Goldsworthy: A Collaboration with Nature (Hardcover)
    The Creative License: Giving Yourself Permission to Be The Artist You Truly Are (Paperback)
    The $12 Million Stuffed Shark: The Curious Economics of Contemporary Art (Hardcover)
    The Hare With Amber Eyes: A Family's Century of Art and Loss (Hardcover)
    Art as Therapy (Hardcover)
    Art and Visual Perception: A Psychology of the Creative Eye (Paperback)
    An Object of Beauty (Hardcover)
    In Praise of Shadows (Paperback)
    Daily Rituals: How Artists Work (Hardcover)
    Girl in Hyacinth Blue (Paperback)
    Art as Experience (Paperback)
    Picture This: How Pictures Work (Hardcover)
    The Arrival (Hardcover)
    Good Faeries Bad Faeries (Hardcover)
    The Painted Word (Paperback)
    Dear Theo (Paperback)
    Make Good Art (Hardcover)
    The Lady in Gold: The Extraordinary Tale of Gustav Klimt's Masterpiece, Portrait of Adele Bloch-Bauer (Kindle Edition)
    Drawing the Head and Hands (Hardcover)
    Ish (Hardcover)
    Codex Seraphinianus. Ein Orbis Pictus des Universums der Phantasie. (Hardcover)
    The Birth of Venus (Paperback)
    Provenance: How a Con Man and a Forger Rewrote the History of Modern Art (Hardcover)
    Walk Through Walls: A Memoir (Hardcover)
    Wabi-Sabi: For Artists, Designers, Poets & Philosophers (Paperback)
    Art in Theory, 1900–2000: An Anthology of Changing Ideas (Paperback)
    Caravaggio: A Life Sacred and Profane (Hardcover)
    The Gashlycrumb Tinies (The Vinegar Works, #1)
    Radiant Child: The Story of Young Artist Jean-Michel Basquiat (Hardcover)
    The Principles of Uncertainty (Hardcover)
    Art Forms in Nature (Paperback)
    Dali (Capa dura)
    Sabine's Notebook (Griffin & Sabine #2)
    The Passion of Artemisia (Paperback)
    ################################################################
    Shelve:  Art
    Page:  2
    Total number of books scraped:  300
    ################################################################
 </details>   

###
```python
crime_travel_art.sample(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Title</th>
      <th>Author</th>
      <th>Average rating</th>
      <th>Number of Ratings</th>
      <th>Year</th>
      <th>Book description</th>
      <th>Book image</th>
      <th>Genre</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>33</th>
      <td>The Sign of Four (Sherlock Holmes, #2)</td>
      <td>Arthur Conan Doyle</td>
      <td>3.92</td>
      <td>130079</td>
      <td>1890</td>
      <td>As a dense yellow fog swirls through the stree...</td>
      <td>https://i.gr-assets.com/images/S/compressed.ph...</td>
      <td>[Classics, Mystery, Fiction, Mystery, Crime, M...</td>
    </tr>
    <tr>
      <th>129</th>
      <td>The Lost City of Z: A Tale of Deadly Obsession...</td>
      <td>David Grann</td>
      <td>3.84</td>
      <td>83270</td>
      <td>2009</td>
      <td>A grand mystery reaching back centuries. A sen...</td>
      <td>https://i.gr-assets.com/images/S/compressed.ph...</td>
      <td>[Nonfiction, History, Adventure, Travel, Biogr...</td>
    </tr>
    <tr>
      <th>157</th>
      <td>The Happy Isles of Oceania: Paddling the Pacif...</td>
      <td>Paul Theroux</td>
      <td>4.01</td>
      <td>5825</td>
      <td>1992</td>
      <td>Renowned travel writer and novelist Paul Thero...</td>
      <td>https://i.gr-assets.com/images/S/compressed.ph...</td>
      <td>[Travel, Nonfiction, Autobiography, Memoir, Ad...</td>
    </tr>
    <tr>
      <th>111</th>
      <td>A Year in Provence (Paperback)</td>
      <td>Peter Mayle</td>
      <td>3.96</td>
      <td>70112</td>
      <td>1989</td>
      <td>National Bestseller In this witty and warm-hea...</td>
      <td>https://i.gr-assets.com/images/S/compressed.ph...</td>
      <td>[Travel, Nonfiction, Autobiography, Memoir, Cu...</td>
    </tr>
    <tr>
      <th>172</th>
      <td>Between the Woods and the Water (Paperback)</td>
      <td>Patrick Leigh Fermor</td>
      <td>4.30</td>
      <td>2889</td>
      <td>1986</td>
      <td>Continuing the epic foot journey across Europe...</td>
      <td>https://i.gr-assets.com/images/S/compressed.ph...</td>
      <td>[Travel, Nonfiction, History, Autobiography, M...</td>
    </tr>
    <tr>
      <th>104</th>
      <td>Neither Here nor There: Travels in Europe (Pap...</td>
      <td>Bill Bryson</td>
      <td>3.84</td>
      <td>68904</td>
      <td>1991</td>
      <td>Bill Bryson's first travel book, , was unanimo...</td>
      <td>https://i.gr-assets.com/images/S/compressed.ph...</td>
      <td>[Travel, Nonfiction, Humor, Autobiography, Mem...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>And Then There Were None (Paperback)</td>
      <td>Agatha Christie</td>
      <td>4.26</td>
      <td>966961</td>
      <td>1939</td>
      <td>First, there were ten—a curious assortment of ...</td>
      <td>https://i.gr-assets.com/images/S/compressed.ph...</td>
      <td>[Mystery, Classics, Fiction, Mystery, Crime, T...</td>
    </tr>
    <tr>
      <th>242</th>
      <td>The Judgment of Paris: The Revolutionary Decad...</td>
      <td>Ross King</td>
      <td>3.83</td>
      <td>13826</td>
      <td>2006</td>
      <td>With a novelist's skill and the insight of an ...</td>
      <td>https://i.gr-assets.com/images/S/compressed.ph...</td>
      <td>[Art, History, Nonfiction, Art, Art History, C...</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Assuming Names: A Con Artist's Masquerade (ebook)</td>
      <td>Tanya Thompson</td>
      <td>3.77</td>
      <td>37117</td>
      <td>2014</td>
      <td>When it was over, there were a lot of question...</td>
      <td>https://i.gr-assets.com/images/S/compressed.ph...</td>
      <td>[Mystery, Crime, Thriller, Autobiography, Memo...</td>
    </tr>
    <tr>
      <th>67</th>
      <td>The Ice Princess (Patrik Hedström, #1)</td>
      <td>Camilla Läckberg</td>
      <td>3.75</td>
      <td>66291</td>
      <td>2003</td>
      <td>Returning to her hometown of Fjallbacka after ...</td>
      <td>https://i.gr-assets.com/images/S/compressed.ph...</td>
      <td>[Mystery, Mystery, Crime, Fiction, Thriller, T...</td>
    </tr>
  </tbody>
</table>
</div>


```python
crime_travel_art.to_csv('sample_data/crime_travel_art_shelves.csv', index=False)
```
