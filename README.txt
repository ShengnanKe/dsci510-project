README.txt
DOWNLOAD BEFORE EXECUTING:

Please download the “chromedriver_mac64.zip” from https://chromedriver.chromium.org/downloads this website. 
Please download it according to your own operating system. 
And check which version of the chrome browser you are using. 
After you successfully downloaded the package from the above website. 
Next, open that zip file and place it in the folder where the python script is. 
Then, install the library accordingly in your terminal or command line. 
# pip install bs4
# pip install html5lib
# pip install csv
# pip install pandas
# pip install requests
# pip install selenium
# pip install json
# pip install seaborn
# pip install tmdbsimple
# pip install researchpy
Next just import libraries accordingly. You should be able to successfully run it on your computer. 
# import requests
# from bs4 import BeautifulSoup
# import csv 
# import pandas as pd
# import selenium as se
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import tmdbsimple as tmdb
# import json
# import matplotlib.pyplot as plt
# from collections import Counter
# import seaborn as sns
# import researchpy as rp
# import sys



GET API KEY:
Please make sure that you get your own API_key. Else, it might cause errors. That you might not able to load the data from The movie database. 


5 Major Parts of the final_project.py File:

Part_1: WEB Data Scraping 
This part of the python script is for gathering data about “Top-rated” movies from the past years(2016-2021).

def get_xxxx_info_from_web(): 
This function is being used 6 times to scrape information about the Top 50 movies from 2016  to 2021. For each year, I save the data into one single CSV file.  And I named it 'Top_movies_xxxx.csv' ( xxxx stands for the year from 2016 to 2021)

def combined_movie_info(): 
This function is used to combine all the CSV files we got from the above function. And it saves all the data in a single excel file as ‘2016_2021_combined_movie_info.xlsx’

Part_2: WEB Data Scraping 
Next, I would like to gather some data about movies that just came out in 2022. This part of the python file is to help me get prepared to use TMDB( The Movie Database) API. Because in TMDB, if we want to request detailed information about certain movies, we must provide the TMDB ID of the movies.  

def get_2022_Title_from_web():
This function is being used to get a list of movies that came out in 2022 but only included the movie title. The resource list is from https://www.imdb.com/list/ls090466457/ 
I save this list of movie titles as 'Draft1_2022_movie_titles.csv'. 

def get_2022_movie_id_from_web():
After we get the '2022movielist.csv'. Accordingly, we need to find out the TMDB ID of this list of movies. In this function, I used a library function called selenium. This library function helped me to automatically search movies on that list and get the TMDB ID of each movie. And this data is saved in 'Draft2_2022_Movie_Title_ID.csv'. 

def combine_2022_movie_info():
This function is to remove certain movies from the list. Some of the movies do not exist in TMDB. So by merging these two CSV files, we can get a list of movies that do exist in TMDB. And this updated list is saved as 'Modified_movie_TI.csv'.

def filtered_movie_list():
By checking on the 'Modified_movie_TI.csv'. I realized that some of the old movies have the same title as the movie in 2022 and it also exists in the TMDB. But what we looking for is just the list of 2022 movies. I realized that the ID of each movie relates to the time that the movie came out. So I filtered out the old movies and save them as a new dataset, named 'Final_ver_2022_Movie_Title_ID.csv'. 

Part_3: API_scraping 
After we got the 2022 movie list with the titles and IDs. we can use their TMDB ID to find detailed information about these 2022 movies. 
Firstly, I need to require an API_KEY from this website: https://www.themoviedb.org/settings/api 
You would have to register an account to get your own API Key (v3 auth).
Mine is 5c7a1c5e6cdd8d3132826246ee7c7761
Next, I use my api_key and the movie’s TMDB ID to request information about the movies. 
Here is an example API request:
https://api.themoviedb.org/3/movie/ “movie ID”?api_key=” the API key” 
By reading this 'Final_ver_2022_Movie_Title_ID.csv' file, we save the movie IDs as a list. 

def get_data(API_key, Movie_ID):
This function works with the API, we can get these ['Movie_name', 'popularity', ‘vote’, ‘vote_count’, 'budget', 'Collection_name''] information. 

def get_2022_info()
This function for iterating through the list of movie IDs. By calling the get_data function. We can get these ['Movie_name', 'popularity', ‘vote’, ‘vote_count’, 'budget', 'Collection_name''] for each movie on the list. And we save these data as ‘2022_movie_data.csv'.

def combine_2022_movie_info()
This function is for merging the Certificate & ID columns from 'Final_ver_2022_Movie_Title_ID.csv’ to the ‘2022_movie_data.csv'. Now we have the  combination. We save this combined information as 'Motified_2022_movie_data.csv', Which contains ['Index', 'Title', 'popularity', 'vote_average', 'vote_count', 'budget', 'Collection_name', 'ID', 'Certificate']. And by adding one index column, we get the final outcome of this part of the python script: ‘2022_basic_movie_data.csv'.
Part_4: API_scraping 
- API scraping with ​​the library function
# pip install tmdbsimple
import tmdbsimple as tmdb 
Since I’m using a support library function tmdbsimple to scrape more detailed information of movies. Please make sure to install it first, then, run this python script.
Similar to the last python script - API_scrape.py. You would have to register an account to get your own API Key (v3 auth).
Mine is 5c7a1c5e6cdd8d3132826246ee7c7761
Next, I use my api_key and the movie’s TMDB ID to request information about the movies. 
Here is an example API request:
https://api.themoviedb.org/3/movie/ “movie ID”?api_key=” the API key” 

By reading this 'Final_ver_2022_Movie_Title_ID.csv' file, we save the movie IDs as a list. 
def get_movie_genre_info():
This function is to identify which genre each movie belongs to. And I save this information as "2022_movie_genre.csv".  And I added an index column to the previous file and save it as 'motified_2022_movie_genre.csv'.

def get_movie_director_info():
This function is to identify who is/are the director(s) of each movie belongs. And I save this information as "2022_movie_directors.csv". And I added an index column to the previous file and save it as 'motified_2022_movie_directors.csv'. 

def combine_genre_director():
This function is for combining 'motified_2022_movie_genre.csv' and 'motified_2022_movie_directors.csv' based on the index column. The final outcome for this function is '2022_genre_director.csv'. 

 At the end of this function, we combine the info we get from the last function '2022_genre_director.csv'. and the final outcome from API_scrape.py '2022_basic_movie_data.csv'.

The final outcome for this python script is '2022_movie_all_info.csv'. This csv file contains these information: [​​Index, Title, popularity, vote_average, vote_count, budget, Collection_name, ID, Certificate, Genre(s), Director(s)]. 



Part_5: Start Analyze!
def count_certificate():
Using info from '2016_2021_combined_movie_info.xlsx', among the top movies from 2016 to 2022. This function is to find out the percentage of movies with different ratings.
The output graph is saved as 'past_movies_count_Certificates.png'.

def count_genre():
Using info from '2016_2021_combined_movie_info.xlsx', among the top movies from 2016 to 2022. This function is to find out the percentage of movies with different genres. 
The output graph is saved as 'past_movies_count_genres.png'

def IMDbr_Metascore():
Using info from '2016_2021_combined_movie_info.xlsx', among the top movies from 2016 to 2022. This function is to find out if there is an inner relationship between the IMDb Rating	and the Metascore of the movie. The output graph is saved as 'IMDb_Rating_Metascore.png'

def IMDbr_Gross():
Using info from '2016_2021_combined_movie_info.xlsx', among the top movies from 2016 to 2022. This function is to find out if there is an inner relationship between the IMDb Rating	and the Gross of the movie. The output graph is saved as 'IMDb_Rating_Gross.png'


def Metascore_Gross():
Using info from '2016_2021_combined_movie_info.xlsx', among the top movies from 2016 to 2022. This function is to find out if there is an inner relationship between the Metascore and the Gross of the movie. The output graph is saved as 'Metascore_Gross.png'

def Gross_Metascore_IMDbr():
Using info from '2016_2021_combined_movie_info.xlsx', among the top movies from 2016 to 2022. This function is to find out if there is an inner relationship between the Metascore, IMDb_Rating, and the Gross of the movie. The output graph is saved as 'Metascore_IMDb_Rating_Gross.png'

def directors_analysis():
Using info from '2016_2021_combined_movie_info.xlsx', and '2022_movie_all_info.csv'. Among the top movies from 2016 to 2021, find out if there are directors has more than one movie on the list. Compare to 2022, find directors who have more than one movie in the past 6 years also have a movie in 2022. Finally, find out the movie title of these directors.  
def analyze_2022_directors():
Using info from '2016_2021_combined_movie_info.xlsx', and '2022_movie_all_info.csv'. 
Find out movie directors who have at least one movie in the past 6 years and have a movie in 2022. 

def analyze_2022_genres():
This function is to get a simple idea of the distribution of the types of movies in 2022. The graph is saved as “2022_count_genres.png”

Running on the command line：
Cd to the folder where you saved this “Final_Project.py” file. 
I’m using a Mac, and I saved it in the Final_Project_SK. So I was executing this line in the terminal. And this worked perfectly on my laptop.
python -u Final_Project.py