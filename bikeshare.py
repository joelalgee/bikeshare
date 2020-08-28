import time
import datetime as dt
import calendar as cal
import pandas as pd
import numpy as np

# New cities can be added here without requiring changes to the funtions
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
city_opts = ['chicago', 'new york city', 'washington']

month_opts = list(cal.month_name)
month_opts.append('All')
day_opts = list(cal.day_name)
day_opts.append('All')

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (int) month - number of the month to filter by (1-12), or 13 to apply no month filter
        (int) day - number of the day of week to filter by (0-6 mon-sun), or 7 to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington)
    while True:
        city_lines = '\n'.join(['{} {}'.format(str(i+1), m) for i, m in enumerate(city_opts)]).title()
        city_lines = '\nFirst, choose a city to analyze:\n\n{}\n\nPlease enter 1-{}:\n\n'.format(city_lines, len(city_opts))
        city = input(city_lines).strip()
        
        # validate and format input
        if city in [str(i) for i in range(1,4)]:
            city = city_opts[int(city) - 1]
            break
        elif city.lower() in (city_opts):
            city = city.lower()
            break
        else:
            print('\nPlease enter the corresponding number only (you entered "{}")'.format(city))

    # get user input for month (all, january, february, ... , june)
    while True:
        month_lines = '\n'.join(['{} {}'.format(str(i+1), m) for i, m in enumerate(month_opts[1:])])
        month_lines = '\nNext, choose a month to analyze:\n\n{}\n\nPlease enter 1-13:\n\n'.format(month_lines)
        month = input(month_lines).lower().strip()
        
        # validate and format input
        if month in [str(i) for i in range(1,14)]:
            month = int(month)
            break
        else:
            print('\nPlease enter the corresponding number only (you entered "{}")'.format(month))

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day_lines = '\n'.join(['{} {}'.format(str(i+1), m) for i, m in enumerate(day_opts)])
        day_lines = '\nFinally, choose a day of the week to analyze:\n\n{}\n\nPlease enter 1-8:\n\n'.format(day_lines)
        day = input(day_lines).lower().strip()
        
        # validate and format input
        if day in [str(i) for i in range(1,9)]:
            day = int(day) - 1
            break
        else:
            print('\nPlease enter the corresponding number only (you entered "{}")'.format(day))

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (int) month - number of the month to filter by (1-12), or 13 to apply no month filter
        (int) day - number of the day of week to filter by (0-6 mon-sun), or 7 to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.dayofweek

    # filter by month if applicable
    if month != 13:
        # filter by month to create the new dataframe
        df = df[df['Month'] == month]

    # filter by day of week if applicable
    if day != 7:
        # filter by day of week to create the new dataframe
        df = df[df['Day of Week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month_mode = df['Month'].mode()[0]
    print('\nThe most common month is {}.'.format(month_opts[month_mode]))

    # display the most common day of week
    day_mode = df['Day of Week'].mode()[0]
    print('The most common day of week is {}.'.format(day_opts[day_mode]))


    # display the most common start hour
    hour_mode = df['Start Time'].dt.hour.mode()[0]
    print('The most common start hour is {}:00.\n'.format(hour_mode))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station_mode = df['Start Station'].mode()[0]
    print('The most common start station is {}.'.format(start_station_mode))

    # display most commonly used end station
    end_station_mode = df['End Station'].mode()[0]
    print('The most common end station is {}.'.format(end_station_mode))

    # display most frequent combination of start station and end station trip
    trip_mode = (df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    print('The most common trip is {}.'.format(trip_mode))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = str(dt.timedelta(seconds=int(round(df['Trip Duration'].sum()))))
    print('The total travel time is {} (to the nearest second).'.format(total_travel_time))

    # display mean travel time
    mean_travel_time = str(dt.timedelta(seconds=int(round(df['Trip Duration'].mean()))))
    print('The mean travel time is {} (to the nearest second).'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_counts = df['User Type'].groupby(df['User Type']).count()
    user_type_list = ' and '.join('{} {}s'.format(v, k) for k, v in user_type_counts.items())
    print('There are {}.'.format(user_type_list))
    
    # Display counts of gender
    if 'Gender' in df:
        gender_counts = df['Gender'].groupby(df['Gender']).count()
        gender_list = ' and '.join('{} {}s'.format(v, k) for k, v in gender_counts.items())
        print('There are {}.'.format(gender_list))
    else:
        print('No gender data is available.')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth = int(df['Birth Year'].min())
        latest_birth = int(df['Birth Year'].max())
        birth_mode = int(df['Birth Year'].mode()[0])
        print('The earliest year of birth is {}.'.format(earliest_birth))
        print('The latest year of birth is {}.'.format(latest_birth))
        print('The most common year of birth is {}.'.format(birth_mode))
    else:
        print('No date of birth data is available.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        # Show raw data 5 lines at a time if requested
        more= ''
        line = 0
        show_lines = 5
        total_lines = len(df.index)
        while line < total_lines:
            # Check how many lines are left, adjust message and data displayed if less than 5
            remaining_lines = total_lines - line
            if remaining_lines < show_lines:
                show_lines = remaining_lines
                
            # Check user wants to continue
            raw = input('\nWould you like to see {} {}lines of raw data?'.format(show_lines, more) + \
                        ' Enter Y to see them,or anything else to skip:\n\n')
            if raw.lower() != 'y' and raw.lower() != 'yes':
                break
            else:
                # Show data
                print(df.iloc[line:line + show_lines])
                
                # Adjust message for second batch onwards
                if line == 0:
                    more = 'more '
                
                # Update starting line for next batch
                line += show_lines
                
                # Show end message if all data has been displayed
                if line >= total_lines:
                    print('End of data')  
            
        restart = input('\nWould you like to restart? Enter Y to restart, or anything else to quit:\n\n')
        if restart.lower() != 'y' and restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
