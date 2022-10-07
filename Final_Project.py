#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Shengnan Ke
"""

# please make sure to install the following libraries first, before you excute the code

# pip install bs4
# pip install html5lib
# pip install requests
# pip install selenium
# pip install tmdbsimple
# pip install researchpy



# lease make sure to import necessary libraries to excetue functions

import requests
from bs4 import BeautifulSoup
import csv 
import pandas as pd

import selenium as se
from selenium import webdriver
from selenium.webdriver.common.by import By

import tmdbsimple as tmdb

import json

import matplotlib.pyplot as plt
from collections import Counter
import seaborn as sns

import researchpy as rp

import sys



# Top_movies_2016

def get_2016_info_from_web():
    content = requests.get('https://www.imdb.com/list/ls060610711/').content 
    soup = BeautifulSoup(content, 'html5lib')
    all_info = soup.find_all('div', class_ = "lister-item-content")
    
    movies = []
    
    for info in all_info:
        movie = {}
        movie['Title'] = info.h3.a.text
        
        # find the director of each movie
        all_p = info.find_all('p')
        director_p = all_p[2]
        all_a = director_p.find_all('a')
        movie['Director'] = all_a[0].text
        
        # find the Certificate of each movie
        try:
            movie['Certificate']  = info.p.find('span', class_='certificate').text
        except: 
            movie['Certificate'] = 'Unknown'
            
        
        try:
            movie['Genre'] = info.p.find('span', class_ = 'genre').text.strip().strip('\n')
        except:
            movie['Genre'] = 'Unknown'
            
        try:
            movie['IMDb Rating'] = info.div.find('span', class_ = 'ipl-rating-star__rating').text
        except:
            movie['IMDb Rating'] = 0
          
        # find the gross income of each movie
        try:
            gross_vote_p = all_p[3]
            all_span = gross_vote_p.find_all('span')
            movie['Gross'] = all_span[4].text.strip('$').strip('M')
        except:
            movie['Gross'] = 0
            
        try:
            movie['Votes'] = info.find('span',{'name':'nv'})['data-value']
        except:
            movie['Votes'] = 0
        
        
        try:
            movie['Metascore'] = info.find('div', class_="inline-block ratings-metascore").text.strip().strip('        \n        Metascore')
        except:
            movie['Metascore'] = 0
            
            
        try:
            movie['Runtime'] = info.p.find('span', class_ = 'runtime').text
        except:
            movie['Runtime'] = 0
            
        movies.append(movie)
    # print(movies)


    filename = 'Top_movies_2016.csv'
    with open(filename, 'w', newline='') as f:
        w = csv.DictWriter(f,['Title', 'Director', 'Certificate', 'Runtime', 'Genre', 'IMDb Rating', 'Gross', 'Votes', 'Metascore'])
        w.writeheader()
        for movie in movies:
            w.writerow(movie)





# Top_movies_2017

def get_2017_info_from_web():
    content = requests.get('https://www.imdb.com/list/ls062905646/').content 
    soup = BeautifulSoup(content, 'html5lib')
    all_info = soup.find_all('div', class_ = "lister-item-content")
    
    movies = []
    
    for info in all_info:
        movie = {}
        movie['Title'] = info.h3.a.text
        
        # find the director of each movie
        all_p = info.find_all('p')
        director_p = all_p[2]
        all_a = director_p.find_all('a')
        movie['Director'] = all_a[0].text
        
        # find the Certificate of each movie
        try:
            movie['Certificate']  = info.p.find('span', class_='certificate').text
        except: 
            movie['Certificate'] = 'Unknown'
            
        
        try:
            movie['Genre'] = info.p.find('span', class_ = 'genre').text.strip().strip('\n')
        except:
            movie['Genre'] = 'Unknown'
            
        
        try:
            movie['IMDb Rating'] = info.div.find('span', class_ = 'ipl-rating-star__rating').text
        except:
            movie['IMDb Rating'] = 0
          
        # find the gross income of each movie
        try:
            gross_vote_p = all_p[3]
            all_span = gross_vote_p.find_all('span')
            movie['Gross'] = all_span[4].text.strip('$').strip('M')
        except:
            movie['Gross'] = 0
            
        try:
            movie['Votes'] = info.find('span',{'name':'nv'})['data-value']
        except:
            movie['Votes'] = 0
        
        
        try:
            movie['Metascore'] = info.find('div', class_="inline-block ratings-metascore").text.strip().strip('        \n        Metascore')
        except:
            movie['Metascore'] = 0
            
            
        try:
            movie['Runtime'] = info.p.find('span', class_ = 'runtime').text
        except:
            movie['Runtime'] = 0
            
        movies.append(movie)



    filename = 'Top_movies_2017.csv'
    with open(filename, 'w', newline='') as f:
        w = csv.DictWriter(f,['Title', 'Director', 'Certificate', 'Runtime', 'Genre', 'IMDb Rating', 'Gross', 'Votes', 'Metascore'])
        w.writeheader()
        for movie in movies:
            w.writerow(movie)
    





# Top_movies_2018

def get_2018_info_from_web():
    content = requests.get('https://www.imdb.com/list/ls023345789/').content 
    soup = BeautifulSoup(content, 'html5lib')
    all_info = soup.find_all('div', class_ = "lister-item-content")
    
    movies = []
    
    for info in all_info:
        movie = {}
        movie['Title'] = info.h3.a.text
        
        # find the director of each movie
        all_p = info.find_all('p')
        director_p = all_p[2]
        all_a = director_p.find_all('a')
        movie['Director'] = all_a[0].text
        
        # find the Certificate of each movie
        try:
            movie['Certificate']  = info.p.find('span', class_='certificate').text
        except: 
            movie['Certificate'] = 'Unknown'
            
        
        try:
            movie['Genre'] = info.p.find('span', class_ = 'genre').text.strip().strip('\n')
        except:
            movie['Genre'] = 'Unknown'
            
        
        try:
            movie['IMDb Rating'] = info.div.find('span', class_ = 'ipl-rating-star__rating').text
        except:
            movie['IMDb Rating'] = 0
          
        # find the gross income of each movie
        try:
            gross_vote_p = all_p[3]
            all_span = gross_vote_p.find_all('span')
            movie['Gross'] = all_span[4].text.strip('$').strip('M')
        except:
            movie['Gross'] = 0
            
        try:
            movie['Votes'] = info.find('span',{'name':'nv'})['data-value']
        except:
            movie['Votes'] = 0
        
        
        try:
            movie['Metascore'] = info.find('div', class_="inline-block ratings-metascore").text.strip().strip('        \n        Metascore')
        except:
            movie['Metascore'] = 0
            
            
        try:
            movie['Runtime'] = info.p.find('span', class_ = 'runtime').text
        except:
            movie['Runtime'] = 0
            
            
        movies.append(movie)

    filename = 'Top_movies_2018.csv'
    with open(filename, 'w', newline='') as f:
        w = csv.DictWriter(f,['Title', 'Director', 'Certificate', 'Runtime', 'Genre', 'IMDb Rating', 'Gross', 'Votes', 'Metascore'])
        w.writeheader()
        for movie in movies:
            w.writerow(movie)





# Top_movies_2019


def get_2019_info_from_web():
    content = requests.get('https://www.imdb.com/list/ls043151343/').content 
    soup = BeautifulSoup(content, 'html5lib')
    all_info = soup.find_all('div', class_ = "lister-item-content")
    
    movies = []
    
    for info in all_info:
        movie = {}
        movie['Title'] = info.h3.a.text
        
        # find the director of each movie
        all_p = info.find_all('p')
        director_p = all_p[2]
        all_a = director_p.find_all('a')
        movie['Director'] = all_a[0].text
        
        # find the Certificate of each movie
        try:
            movie['Certificate']  = info.p.find('span', class_='certificate').text
        except: 
            movie['Certificate'] = 'Unknown'
            
        
        try:
            movie['Genre'] = info.p.find('span', class_ = 'genre').text.strip().strip('\n')
        except:
            movie['Genre'] = 'Unknown'
            
        
        try:
            movie['IMDb Rating'] = info.div.find('span', class_ = 'ipl-rating-star__rating').text
        except:
            movie['IMDb Rating'] = 0
          
        # find the gross income of each movie
        try:
            gross_vote_p = all_p[3]
            all_span = gross_vote_p.find_all('span')
            movie['Gross'] = all_span[4].text.strip('$').strip('M')
        except:
            movie['Gross'] = 0
            
        try:
            movie['Votes'] = info.find('span',{'name':'nv'})['data-value']
        except:
            movie['Votes'] = 0
        
        
        try:
            movie['Metascore'] = info.find('div', class_="inline-block ratings-metascore").text.strip().strip('        \n        Metascore')
        except:
            movie['Metascore'] = 0
            
            
        try:
            movie['Runtime'] = info.p.find('span', class_ = 'runtime').text
        except:
            movie['Runtime'] = 0
        
        movies.append(movie)


    filename = 'Top_movies_2019.csv'
    with open(filename, 'w', newline='') as f:
        w = csv.DictWriter(f,['Title', 'Director', 'Certificate', 'Runtime', 'Genre', 'IMDb Rating', 'Gross', 'Votes', 'Metascore'])
        w.writeheader()
        for movie in movies:
            w.writerow(movie)





# Top_movies_2020


def get_2020_info_from_web():
    content = requests.get('https://www.imdb.com/list/ls081993179/?sort=list_order,asc&st_dt=&mode=detail&page=1').content 
    soup = BeautifulSoup(content, 'html5lib')
    all_info = soup.find_all('div', class_ = "lister-item-content")
    
    movies = []
    
    for info in all_info:
        movie = {}
        movie['Title'] = info.h3.a.text
        
        # find the director of each movie
        all_p = info.find_all('p')
        director_p = all_p[2]
        all_a = director_p.find_all('a')
        movie['Director'] = all_a[0].text
        
        # find the Certificate of each movie
        try:
            movie['Certificate']  = info.p.find('span', class_='certificate').text
        except: 
            movie['Certificate'] = 'Unknown'
            
        
        try:
            movie['Genre'] = info.p.find('span', class_ = 'genre').text.strip().strip('\n')
        except:
            movie['Genre'] = 'Unknown'
            
        
        try:
            movie['IMDb Rating'] = info.div.find('span', class_ = 'ipl-rating-star__rating').text
        except:
            movie['IMDb Rating'] = 0
          
        # find the gross income of each movie
        try:
            gross_vote_p = all_p[3]
            all_span = gross_vote_p.find_all('span')
            movie['Gross'] = all_span[4].text.strip('$').strip('M')
        except:
            movie['Gross'] = 0
            
        try:
            movie['Votes'] = info.find('span',{'name':'nv'})['data-value']
        except:
            movie['Votes'] = 0
        
        
        try:
            movie['Metascore'] = info.find('div', class_="inline-block ratings-metascore").text.strip().strip('        \n        Metascore')
        except:
            movie['Metascore'] = 0
            
            
        try:
            movie['Runtime'] = info.p.find('span', class_ = 'runtime').text
        except:
            movie['Runtime'] = 0
            
        movies.append(movie)

    filename = 'Top_movies_2020.csv'
    with open(filename, 'w', newline='') as f:
        w = csv.DictWriter(f,['Title', 'Director', 'Certificate', 'Runtime', 'Genre', 'IMDb Rating', 'Gross', 'Votes', 'Metascore'])
        w.writeheader()
        for movie in movies:
            w.writerow(movie)



# Top_movies_2021

def get_2021_info_from_web():
    content = requests.get('https://www.imdb.com/list/ls506716903/').content 
    soup = BeautifulSoup(content, 'html5lib')
    all_info = soup.find_all('div', class_ = "lister-item-content")
    
    movies = []
    
    for info in all_info:
        movie = {}
        movie['Title'] = info.h3.a.text
        
        # find the director of each movie
        all_p = info.find_all('p')
        director_p = all_p[2]
        all_a = director_p.find_all('a')
        movie['Director'] = all_a[0].text
        
        # find the Certificate of each movie
        try:
            movie['Certificate']  = info.p.find('span', class_='certificate').text
        except: 
            movie['Certificate'] = 'Unknown'
            
        
        try:
            movie['Genre'] = info.p.find('span', class_ = 'genre').text.strip().strip('\n')
        except:
            movie['Genre'] = 'Unknown'
            
        
        try:
            movie['IMDb Rating'] = info.div.find('span', class_ = 'ipl-rating-star__rating').text
        except:
            movie['IMDb Rating'] = 0
          
        # find the gross income of each movie
        try:
            gross_vote_p = all_p[3]
            all_span = gross_vote_p.find_all('span')
            movie['Gross'] = all_span[4].text.strip('$').strip('M')
        except:
            movie['Gross'] = 0
            
        try:
            movie['Votes'] = info.find('span',{'name':'nv'})['data-value']
        except:
            movie['Votes'] = 0
        
        
        try:
            movie['Metascore'] = info.find('div', class_="inline-block ratings-metascore").text.strip().strip('        \n        Metascore')
        except:
            movie['Metascore'] = 0
            
            
        try:
            movie['Runtime'] = info.p.find('span', class_ = 'runtime').text
        except:
            movie['Runtime'] = 0
    
        movies.append(movie)


    filename = 'Top_movies_2021.csv'
    with open(filename, 'w', newline='') as f:
        w = csv.DictWriter(f,['Title', 'Director', 'Certificate', 'Runtime', 'Genre', 'IMDb Rating', 'Gross', 'Votes', 'Metascore'])
        w.writeheader()
        for movie in movies:
            w.writerow(movie)



# Merging csv files: get all movie info from 2016 to 2022 save it as excel file 

def combined_movie_info():
    df = pd.concat(map(pd.read_csv, ['Top_movies_2016.csv', 'Top_movies_2017.csv', 'Top_movies_2018.csv', 'Top_movies_2019.csv', 'Top_movies_2020.csv', 'Top_movies_2021.csv']), ignore_index = True)
    # df.drop_duplicates()
    # df = df.style.set_properties(**{'text-align': 'center'})
    
    # display(style)
    left_aligned_df = df.style.set_properties(**{'text-align': 'left'})
    
    left_aligned_df.to_excel('2016_2021_combined_movie_info.xlsx', index = True)



# excute following function to get past 6 years top movies information 
get_2016_info_from_web()
get_2017_info_from_web()
get_2018_info_from_web()
get_2019_info_from_web()
get_2020_info_from_web()
get_2021_info_from_web()
combined_movie_info()




# Get all 2022 movie titles form this website(https://www.imdb.com/list/ls090466457/)

def get_2022_Title_from_web():
    content = requests.get('https://www.imdb.com/list/ls090466457/').content 
    soup = BeautifulSoup(content, 'html5lib')
    all_info = soup.find_all('div', class_ = "lister-item-content")
    
    
    movies = []
    
    for info in all_info:
        movie = {}
        movie['Title'] = info.h3.a.text
        
        # find the Certificate of each movie
        try:
            movie['Certificate']  = info.p.find('span', class_='certificate').text
        except: 
            movie['Certificate'] = 'Unknown'
         
        movies.append(movie)
        
    filename = 'Draft1_2022_movie_titles.csv'
    with open(filename, 'w', newline='') as f:
        w = csv.DictWriter(f,['Title', 'Certificate'])
        w.writeheader()
        for movie in movies:
            w.writerow(movie)
            
    df = pd.read_csv(filename)


'''
Please make sure you do "pip install selenium"
Make sure to download the chromedriver before executing the python file
Download it from https://chromedriver.chromium.org/downloads 
And please do make sure you change the code which I need to identify where I saved the chromedriver.exe file.
browser = webdriver.Chrome(executable_path='/Users/kknanxx/Desktop/510_PY/Final_Project_SK/chromedriver')

'''


# Here chrome webdriver is used
# please change the path to your own path where you saved the chromedriver.exe file
browser = webdriver.Chrome(executable_path='/Users/kknanxx/Desktop/510_PY/Final_Project_SK/chromedriver')

# URL of the website 
# url = "https://www.themoviedb.org/?language=en-US" #THE MOVIE DB

# use selenium to get the list of 2022 movies' ID, 
# by using the ID of movies, later we can use the API to get detail in for about these 2022 new movies

def get_2022_movie_id_from_web():
    #load all the movie titles 
    # filename = '2022movielist.csv'
    movies = pd.read_csv('Draft1_2022_movie_titles.csv') 
    movie_titles = movies["Title"].tolist()
    # print(movie_titles)
    movie_ids = []
       
    for title in movie_titles:
        title = title.replace(" ", "+")
        # print(title)
        movie = {}
        
        elements = browser.get("https://www.themoviedb.org/search?language=en-US&query="+title+"&language=en-US")
        
        try:
            current_movie_title = browser.find_elements(by=By.XPATH, value="//a[@data-media-type='movie']/h2")[0].text
            movie['Title'] = current_movie_title
            current_movie_title = current_movie_title.replace(" ", "+")
            
        
            
            if current_movie_title == title:
                # print(current_movie_title, title)
                current_movie_link = browser.find_elements(by=By.XPATH, value="//a[@data-media-type='movie']")
                current_movie_link = current_movie_link[0].get_attribute('href')
                # print(current_movie_link)
                current_movie_id = current_movie_link.strip('https://www.themoviedb.org/movie/')
                current_movie_id = current_movie_id.strip('?language=en-US')
                # print(current_movie_id)
                movie['ID'] = current_movie_id
                # print(movie)
                # movies.append(movie, ignore_index=True)
        except: 
            # no_match == no_match_statement:
            movie['ID'] = 'Unknown'
            # print(movie)
            
        movie_ids.append(movie)
        # print(movie_ids)
                # print(movies)
               
    filename = 'Draft2_2022_Movie_Title_ID.csv'
    with open(filename, 'w', newline='') as f:
        w = csv.DictWriter(f,['Title','ID'])
        w.writeheader()
        for movie in movie_ids:
            w.writerow(movie)
           
    df = pd.read_csv(filename)
  

# Discard 2022 movie from the list if TMDB doesn't contains information about it.
def combine_2022_movie_info():
    
    # reading two csv files
    data1 = pd.read_csv('Draft2_2022_Movie_Title_ID.csv', index_col=False)
    data2 = pd.read_csv('Draft1_2022_movie_titles.csv', index_col=False)
      
    # merging two csv filesb y setting how='inner'
    output = pd.merge(data1, data2, on='Title', how='inner')
    # return output
    output.to_csv('Modified_movie_TI.csv', index=False)




#Filter out movies that have the same name but from years ago. 
# We only want 2022 new movie list
def filtered_movie_list():
    # take in value from 'Modified_movie_TI.csv'
    with open('Modified_movie_TI.csv', 'r') as unfiltered, open('Final_ver_2022_Movie_Title_ID.csv', 'w', newline='') as filtered:
        # define reader and writer objects
        reader = csv.reader(unfiltered, skipinitialspace=True)
        writer = csv.writer(filtered, delimiter=',')
    
        # write headers
        writer.writerow(next(reader))
    
        # iterate and write rows based on condition
        for i in reader:
            if int(i[-2]) > 20000:
                writer.writerow(i)
    
    df = pd.read_csv('Final_ver_2022_Movie_Title_ID.csv', index_col=False)
    # print(df)



# Excute the following function to get the list of 2022 movie that the movie database contains their information
get_2022_Title_from_web()
get_2022_movie_id_from_web()
combine_2022_movie_info()
filtered_movie_list()


# Please make sure that you get your own API_key. Else, it might cause errors. That you might not able to load the data from The movie database. 



API_key = "5c7a1c5e6cdd8d3132826246ee7c7761" # get TMDB API key from config.py file

movie_info = pd.read_csv('Final_ver_2022_Movie_Title_ID.csv')
movie_list = movie_info['ID'].astype(str).tolist()
# print(len(movie_list))
    
def get_data(API_key, Movie_ID):
    query = 'https://api.themoviedb.org/3/movie/'+Movie_ID+'?api_key='+API_key+'&language=en-US'
    response =  requests.get(query)
    if response.status_code==200: 
    #status code ==200 indicates the API query was successful
        array = response.json()
        text = json.dumps(array)
        return text
    else:
        return ("error")



def write_file(filename, text):
    dataset = json.loads(text)
    csvFile = open(filename,'a', encoding="utf-8")
    csvwriter = csv.writer(csvFile)
    #unpack the result to access the "collection name" element
    result = {}
    
    result['Title'] = dataset['original_title']
    
    try:
        popularity = dataset['popularity']
    except:
        popularity = None
        
    try:
        vote = dataset["vote_average"]
    except:
        vote = None
    
    try:
        vote_count = dataset["vote_count"]
    except:
        vote_count = None
        
    try:
        budget = dataset['budget']
    except:
        budget = None
        
    try:
        collection_name = dataset['belongs_to_collection']['name']
    except:
        #for movies that don't belong to a collection, assign null
        collection_name = None
        
    result = [dataset['original_title'], popularity, vote, vote_count, budget, collection_name]
    # write data
    csvwriter.writerow(result)
    # print (result)
    csvFile.close()

#write header to the file
csvFile = open('2022_movie_data.csv','a', encoding="utf-8")
csvwriter = csv.writer(csvFile)
csvwriter.writerow(['Title', 'popularity', 'vote_average', 'vote_count', 'budget', 'Collection_name'])
csvFile.close()

def get_2022_info():
    for movie in movie_list:
        text = get_data(API_key, movie)
        #make sure your process breaks when the pull was not successful 
        #it's easier to debug this way
        if text == "error":
            break
        write_file('2022_movie_data.csv', text)
    
    # df = pd.read_csv('2022_movie_data.csv')
    # print(df)



# merge the Certificate & ID columns to the '2022_movie_data.csv'
def combine_2022_movie_info():
    
    # fields=['Title']
    # reading two csv files
    data1 = pd.read_csv('2022_movie_data.csv', index_col=False)
    data2 = pd.read_csv('Final_ver_2022_Movie_Title_ID.csv', index_col=False)
      
    # merging two csv filesb y setting how='inner'
    output = pd.merge(data1, data2, on='Title', how='inner')
    
    # return output
    output.to_csv('Motified_2022_movie_data.csv',index=False)
    
    with open('Motified_2022_movie_data.csv', encoding="utf-8") as infile:
        reader = csv.reader(infile)
        next(reader) #to ignore the existing headers
        with open('2022_basic_movie_data.csv', 'w', encoding="utf-8") as outfile:
            write = csv.writer(outfile)
            header = ['Index', 'Title', 'popularity', 'vote_average', 'vote_count', 'budget', 'Collection_name', 'ID', 'Certificate']
            write.writerow(header)
            for idx, line in enumerate(infile):
                outfile.write(f'{idx},{line}')
    

# Excecute these following fucntion to get 2022 movie basic info
get_2022_info()
combine_2022_movie_info()




tmdb.API_KEY = "5c7a1c5e6cdd8d3132826246ee7c7761" # TMDB API key 

movie_info = pd.read_csv('Final_ver_2022_Movie_Title_ID.csv')
movie_IDs = movie_info['ID'].astype(str).tolist()

def get_movie_genre_info():
    all_genres_info = [] 
    all_genres = []
    for movie_ID in movie_IDs:
        # print(movie_ID)
        movie = tmdb.Movies(movie_ID)
        response = movie.info()
        all_genres_info.append(movie.genres)

        all_genres = []
        for genres_info in all_genres_info:
            genres = []
            for dictionary in genres_info:
                genres.append(dictionary.get('name'))
        # print(genres)
            all_genres.append(genres)
    with open("2022_movie_genre.csv", 'w', encoding="utf-8") as f:
        header = ['Genre(s)']
        write = csv.writer(f)
        write.writerow(header)
        write.writerows(all_genres)
            
    with open("2022_movie_genre.csv", encoding="utf-8") as f:
        reader = csv.reader(f)
        with open('motified_2022_movie_genre.csv', 'w', encoding="utf-8") as g:
            writer = csv.writer(g)
            next(reader) #to ignore the existing headers
            for row in reader:
                new_row = [', '.join(row)] 
                writer.writerow(new_row)
                
    with open('motified_2022_movie_genre.csv', encoding="utf-8") as infile, open('final_2022_movie_genre.csv', 'w', encoding="utf-8") as outfile:
        write = csv.writer(outfile)
        header = ['Index', 'Genre(s)']
        write.writerow(header)
        for idx, line in enumerate(infile):
            outfile.write(f'{idx},{line}')


def get_movie_director_info():
    all_directors = []
    for movie_ID in movie_IDs:
        movie = tmdb.Movies(movie_ID)
        response = movie.credits()
        # print(response) 
        directors_name = [] 
        for credit in movie.crew:
            if credit["job"] == "Director":
                directors_name.append(credit['name'])
        # print(directors_name)
        all_directors.append(directors_name)
            
    with open("2022_movie_directors.csv", 'w', encoding="utf-8") as f:
            header = ['Director(s)']
            write = csv.writer(f)
            write.writerow(header)
            write.writerows(all_directors)
                
    with open("2022_movie_directors.csv", encoding="utf-8") as f:
        reader = csv.reader(f)
        with open('motified_2022_movie_directors.csv', 'w', encoding="utf-8") as g:
            writer = csv.writer(g)
            next(reader) #to ignore the existing headers
            for row in reader:
                new_row = [', '.join(row)] 
                writer.writerow(new_row)
    
    with open('motified_2022_movie_directors.csv', encoding="utf-8") as infile, open('final_2022_movie_directors.csv', 'w', encoding="utf-8") as outfile:
        write = csv.writer(outfile)
        header = ['Index', 'Director(s)']
        write.writerow(header)
        for idx, line in enumerate(infile):
            outfile.write(f'{idx},{line}')
                    
        # df = pd.DataFrame(directors_name)
        # df.to_csv("2022_movie_directors_name.csv", index=True)      


def combine_genre_director():
    get_movie_genre_info()
    get_movie_director_info()
    genre = pd.read_csv('final_2022_movie_genre.csv', encoding="utf-8")
    director = pd.read_csv('final_2022_movie_directors.csv', encoding="utf-8")
    genre_director = pd.merge(genre, director , how='left', on = 'Index')
    
    genre_director.to_csv('2022_genre_director.csv',index=False)


# Excute the following command, we can see the combine information for 2022 movies from the API
combine_genre_director()
get_2022_basic_info = pd.read_csv('2022_basic_movie_data.csv', encoding="utf-8")
get_2022_genre_director = pd.read_csv('2022_genre_director.csv', encoding="utf-8")
get_2022_movie_all_info = pd.merge(get_2022_basic_info, get_2022_genre_director, how='left', on = 'Index')
get_2022_movie_all_info.to_csv('2022_movie_all_info.csv',index=False)


# Start Analyze!

# Among the top movies from 2016 to 2022. This function is to find out percentage of movies with different ratings.

# Apply the default theme
sns.set_theme()

file_loc = '2016_2021_combined_movie_info.xlsx'

def count_certificate():
    df = pd.read_excel(file_loc)
    all_certificate = df['Certificate'].tolist()
    counts = Counter(all_certificate)
    # print(counts)

    plt.pie([v for v in counts.values()], labels = [k for k in counts.keys()], autopct='%1.1f%%')
    fig = plt.gcf()
    fig.set_size_inches(22.5, 18.5)

    plt.legend(counts.keys(), loc="best")
    plt.xlabel("Genre", fontsize = 18)
    plt.ylabel("Certificate", fontsize = 18)
    plt.title("Frequency of Certificate for Year 2016-2022", fontsize = 22)
    plt.savefig('past_movies_count_Certificates.png')
    plt.show()


# Among the top movies from 2016 to 2022. This function is to find out percentage of movies with different genres.
def count_genre():
    df = pd.read_excel(file_loc)
    all_genre_labels = df['Genre'].str.split(', ', expand=True).stack().tolist()
    # unique_genre_labels = df['Genre'].str.split(', ', expand=True).stack().unique()
    counts = Counter(all_genre_labels)
    # print(counts)

    plt.pie([v for v in counts.values()], labels = [k for k in counts.keys()], autopct='%1.1f%%')
    fig = plt.gcf()
    fig.set_size_inches(22.5, 18.5)

    plt.legend(counts.keys(), loc="best")
    plt.xlabel("Genre", fontsize = 18)
    plt.ylabel("Frequency", fontsize = 18)
    plt.title("Frequency of Genres for Year 2016-2021", fontsize = 22)
    plt.savefig('past_movies_count_genres.png')
    plt.show()
    

# This function is to find out if there is a inner relationship between the IMDb Ratingand the Metascore of the movie.
def IMDbr_Metascore():
    df = pd.read_excel(file_loc)
  
    summary, results = rp.ttest(group1 = df['IMDb Rating']*10, group1_name= "IMDb Rating",
         group2 = df['Metascore'], group2_name= "Metascore")
    
    sns.relplot(data = df, x = 'IMDb Rating', y = 'Metascore', kind='scatter')

#     sns.scatterplot(data = df, x = 'IMDb Rating', y = 'Metascore')

    plt.title('IMDb Rating v.s. Metascore')
    plt.savefig('IMDb_Rating_Metascore.png')
    plt.show()
    
    print(summary,results)
    



# This function is to find out if there is a inner relationship between the IMDb Rating and the Gross of the movie.
def IMDbr_Gross():
    df = pd.read_excel(file_loc)
    
    summary, results = rp.ttest(group1 = df['IMDb Rating'], group1_name= 'IMDb Rating',
         group2 = df['Gross'], group2_name= 'Gross')
   
    sns.relplot(data = df, x = 'IMDb Rating', y = 'Gross', kind='scatter')
    
    plt.title('IMDb Rating v.s. Gross')
    plt.savefig('IMDb_Rating_Gross.png')
    plt.show()

    print(summary,results)
    

# This function is to find out if there is a inner relationship between the Metascore and the Gross of the movie.
def Metascore_Gross():
    df = pd.read_excel(file_loc)

    summary, results = rp.ttest(group1 = df['Metascore'], group1_name= 'Metascore',
         group2 = df['Gross'], group2_name= 'Gross')
    
    sns.relplot(data = df, x = 'Metascore', y = 'Gross', kind='scatter')
    
    plt.title('Metascore v.s. Gross')
    plt.savefig('Metascore_Gross.png')

    plt.show()

    print(summary,results)


# This function is to find out if there is an inner relationship between the Metascore, IMDb_Rating, and the Gross of the movie.
def Gross_Metascore_IMDbr():
    df = pd.read_excel(file_loc)
    sns.set(style = "darkgrid")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')

    x = df['Gross']
    y = df['Metascore']
    z = df['IMDb Rating']

    ax.set_xlabel('Gross')
    ax.set_ylabel('Metascore')
    ax.set_zlabel('IMDb Rating')

    ax.scatter(x, y, z)
    plt.title('Metascore v.s. IMDb Rating v.s. Gross ')
    plt.savefig('Metascore_IMDb_Rating_Gross.png')

    plt.show()



# Among the top movies from 2016 to 2021, find out if there are directors has more than one movie on the list. 
# Suprisingly, there are many directors have more than movie on the list.

def directors_analysis():
    df1 = pd.read_excel(file_loc)
    directors_2016_2021 = df1['Director'].tolist()
    counts = Counter(directors_2016_2021)
#     print(counts)
    director_more_than_one_movie = []
    for key, value in counts.items():
        # director_more_than_one_movie = []
        if value >= 2:
            director_more_than_one_movie.append(key)
    print(director_more_than_one_movie)
    
    df2 = pd.read_csv('2022_movie_all_info.csv', encoding="utf-8")
    directors_2022 = df2['Director(s)'].tolist()
    
    Prolific_Director_again_in_2022 = set(director_more_than_one_movie) & set(directors_2022)
    
    print(Prolific_Director_again_in_2022)
    
    moviebythesedirector = []
    for d in df2['Director(s)']:
        if d in Prolific_Director_again_in_2022:
            movie_title = df2.loc[df2['Director(s)']==d, 'Title'].item()
            moviebythesedirector.append(movie_title)
    
    print(moviebythesedirector)



def analyze_2022_directors():
    df1 = pd.read_excel(file_loc)
    directors_2016_2021 = df1['Director'].tolist()
    df2 = pd.read_csv('2022_movie_all_info.csv', encoding="utf-8")
    directors_2022 = df2['Director(s)'].tolist()

    print(list(set(directors_2016_2021) & set(directors_2022)))
    


def analyze_2022_genres():
    df2 = pd.read_csv('2022_movie_all_info.csv', encoding="utf-8")
    genres = df2['Genre(s)'].str.split(', ', expand=True).stack().tolist()
    counts = Counter(genres)
    
    plt.pie([v for v in counts.values()], labels = [k for k in counts.keys()], autopct='%1.1f%%')
    fig = plt.gcf()
    fig.set_size_inches(22.5, 18.5)

    plt.legend(counts.keys(), loc="best")
    plt.xlabel("Genre", fontsize = 18)
    plt.ylabel("Frequency", fontsize = 18)
    plt.title("Frequency of Genres for Year 2022", fontsize = 22)
    plt.savefig('2022_count_genres.png')
    plt.show()
    


if __name__ == '__main__':
    if len(sys.argv) == 1:
        
        print('It MIGHT TAKE SOME TIME TO GETTHER ALL THE DATA')
        # excute following function to get past 6 years top movies information 
        get_2016_info_from_web()
        get_2017_info_from_web()
        get_2018_info_from_web()
        get_2019_info_from_web()
        get_2020_info_from_web()
        get_2021_info_from_web()
        combined_movie_info()
        
        # Excute the following function to get the list of 2022 movie that the movie database contains their information
        get_2022_Title_from_web()
        get_2022_movie_id_from_web()
        combine_2022_movie_info()
        filtered_movie_list()
        
        # Excute the following command, we can see the combine information for 2022 movies from the API
        combine_genre_director()
        get_2022_basic_info = pd.read_csv('2022_basic_movie_data.csv', encoding="utf-8")
        get_2022_genre_director = pd.read_csv('2022_genre_director.csv', encoding="utf-8")
        get_2022_movie_all_info = pd.merge(get_2022_basic_info, get_2022_genre_director, how='left', on = 'Index')
        get_2022_movie_all_info.to_csv('2022_movie_all_info.csv',index=False)

        print('Data Done! Analyze Start !')
        # analysis
        
        count_certificate()
        count_genre()
        
        Metascore_Gross()
        IMDbr_Gross()
        IMDbr_Metascore()
        Gross_Metascore_IMDbr() 
        directors_analysis()
        analyze_2022_directors()
        analyze_2022_genres()
        
        print('Analyze Done!')

