#!/usr/bin/env python
# coding: utf-8

# In[18]:


# Import necessary libraries
import time
import pandas as pd
import numpy as np

# Load data files
chicago_df = pd.read_csv('chicago.csv')
new_york_df = pd.read_csv('new_york_city.csv')
washington_df = pd.read_csv('washington.csv')

# Define the CITY_DATA dictionary
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}



# In[19]:


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Valid options
    cities = ['chicago', 'new york city', 'washington']
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday','friday', 'saturday', 'sunday']

    # Get city input with validation
    while True:
        city = input('Please enter city name (chicago, new york city, washington): ').lower()
        if city in cities:
            break
        print('Invalid city name.Please enter chicago, new york city, or washington.')

    # Get month input with validation
    while True:
        month = input('Would you like to filter by month? Enter ""all"" for no month filter, or the month name (e.g., january):\n ').lower()
        if month in months:  # Fixed this line (was 'mont')
            break
        print('Invalid month. Please enter "all" or a month from January to June.')

    # Get day input with validation
    while True:
        day = input('Would you like to filter by day of week? Enter "all" for no day filter, or the day name (e.g., monday):\n ').lower()
        if day in days:
            break
        print('Invalid day of week. Please enter "all" or a day of the week.')

    print('-'*40)
    print(f'You selected the following : City = {city.title()}, Month = {month.title()}, Day = {day.title()}')
    print('-'*40)
    return city, month, day



# In[20]:


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
   # load data file into pandas DataFrame
    df = pd.read_csv(CITY_DATA[city])


        
   # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
        
  # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
        
     # Filter by month if applicable
    if month != 'all':
        # Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
            
        # Filter by month to create the new dataframe
        df = df[df['month'] == month]
        
        # Filter by day of week if applicable
    if day != 'all':
        # Filter by day of week to create the new dataframe
       df = df[df['day_of_week'] == day.lower()]
        
    return df
    




# In[21]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    most_common_month = df['month'].mode()[0]
    print('Most Common Month:', most_common_month)
    
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print('Most Common Day of Week:', most_common_day_of_week)
    
    most_common_start_hour = df['Start Time'].dt.hour.mode()[0]
    print('Most Common Start Hour:', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[22]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station:', most_common_start_station)

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('Most Common End Station:', most_common_end_station)

    # display most frequent combination of start station and end station trip
    most_common_trip = df.groupby(['Start Station', 'End Station']).size().nlargest(1).index[0]
    print('Most Common Trip (Start to End):', most_common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[23]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration = np.sum(df['Trip Duration'])
    # Convert total_duration from seconds into hours, minutes, and seconds for better readability
    hours_total, remainder_total = divmod(total_duration, 3600)
    minutes_total, seconds_total = divmod(remainder_total, 60)
    print(f'Total Travel Time: {int(hours_total)}h {int(minutes_total)}m {int(seconds_total)}s')

    # display mean travel time
    mean_duration = np.mean(df['Trip Duration'])
    # Convert mean_duration from seconds into hours, minutes, and seconds for better readability
    hours_mean, remainder_mean = divmod(mean_duration, 3600)
    minutes_mean, seconds_mean = divmod(remainder_mean, 60)
    print(f'Mean Travel Time: {int(hours_mean)}h {int(minutes_mean)}m {int(seconds_mean)}s')


# In[24]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of User Types:\n', user_types)


    # Display counts of gender
    if 'Gender' in df.columns:
        # Solution 1: Using value_counts for genders
        genders = df['Gender'].value_counts()
        print('Genders:\n', genders)


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]

        print('Earliest Year of Birth:', earliest_year)
        print('Most Recent Year of Birth:', most_recent_year)
        print('Most Common Year of Birth:', most_common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[38]:


def display_raw_data(df):
    """
    Displays raw data 5 rows at a time upon user request.

    Args:
        df (pandas.DataFrame): The DataFrame to display data from.
    """
    start_loc = 0
    while True:
        user_input = input("\nWould you like to see 5 rows of raw data? Enter yes or no.\n").lower()
        if user_input == 'yes':
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
        elif user_input == 'no':
            break
        else:
            print("Invalid input. Please enter yes or no.")
        if start_loc >= len(df): 
            print("No more data to display.")
            break


# In[36]:


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




