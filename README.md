# Explore US Bikeshare Data

## Summary
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it's easy for a user to access a dock to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, I made use of Python to explore data from bike share systems for three major cities in the United States — Chicago, New York City, and Washington. I wrote a script that takes in raw input to create an interactive experience in the terminal, importing data and computing descriptive statistics to answer the following questions:

### 1 What are the popular times of travel?

most common month
most common day of week
most common hour of day

### 2 What are the popular stations and trips?

most common start station
most common end station
most common trip from start to end (i.e., most frequent combination of start station and end station)

### 3 What are the trip durations?

total travel time
average travel time

### 4 What can we tell about the users?

counts of each user type
counts of each gender (only available for NYC and Chicago)
earliest, most recent, most common year of birth (only available for NYC and Chicago)

## Package versions
* python 3.8.5
* numpy 1.20.1
* pandas 1.2.4

## Instructions
Download all files to the same folder, navigate to the folder in a terminal such as Anaconda Prompt, and run the script using `python bikeshare.py`.

## Files

### bikeshare.py
This script contains the full code for the project.

### chicago.csv, new_york_city.csv, washington.csv
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same six core columns:

* Start Time (e.g., 2017-01-01 00:07:57)
* End Time (e.g., 2017-01-01 00:20:53)
* Trip Duration (in seconds - e.g., 776)
* Start Station (e.g., Broadway & Barry Ave)
* End Station (e.g., Sedgwick St & North Ave)
* User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

* Gender
* Birth Year

The original files are much larger and messier, but they can be accessed here if you'd like to see them ([Chicago](https://www.divvybikes.com/system-data), [New York City](https://www.citibikenyc.com/system-data), [Washington](https://www.capitalbikeshare.com/system-data)). These files had more columns and they differed in format in many cases.

## Credits
The project, and parts of the code, were provided by [Udacity](https://www.udacity.com), as part of their Programming for Data Science nanodegree. The data were provided by [Motivate](https://www.motivateco.com/), a bike share system provider for many major cities in the United States.

