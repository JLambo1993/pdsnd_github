import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = ['all', 'january', 'february', 'march',
          'april', 'may', 'june']
DAY_DATA = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday',
            'friday', 'saturday', 'all']



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    """The loops below will ask for user input on which city they are interested
     in analyzing as city_input. The city will be referenced against the
     CITY_DATA dictionary to verify it exists and set the variable city to the
     lowercase value of city_input"""

    city = ' '
    while True:
        city = input('Which city would you like to analyze data from? \
        Please select from \nthe following cities: (Chicago, New York City, or \
        Washington).\n >>>').lower()
        if city in CITY_DATA:
            break
        """If an improper response is entered, the line will print a failure message"""
        print('\nSorry, the city you entered does not match any of the available \
        options.\nPlease enter one of the cities within the list of options.\n')


    # TO DO: get user input for month (all, january, february, ... , june)
    month = ' '

    while True:
        month = input('\nWhich month would you like to look at? \n Use full name format such as January.\n NOTE:If you want to look at all
         type \"all\".\n >>>').lower()
        if month in MONTH_DATA:
            break
        print('You have entered an invalid month. Please enter a valid month such as January, February, etc.\n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    day = ' '

    while True:
        day = input('\nWhich day would you like to look at? \n Use full name format such as Monday.\n NOTE:If you want to look at all days type \"all\".\n >>>').lower()
        if day in DAY_DATA:
            break
        print('You have entered an invalid day. Please enter a valid day such as Monday, Tuesday, etc.\n')

    print('-'*40)
    return city, month, day


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
  # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        MONTH_DATA = ['january', 'february', 'march', 'april', 'may', 'june']
        month = MONTH_DATA.index(month) + 1

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day'] == day.title()]

    return df


def time_stats(df):
    """
    Args:
       Filtered DataFrame

    Returns:
        Displays statistics on the most frequent times of travel.
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # TO DO: display the most common month
    month_common = df['month'].mode()[0]
    print('the most common month for bikeshare use: {}\n'.format(MONTH_DATA[month_common].title()))
    # TO DO: display the most common day of week
    day_common = df['day'].mode()[0]
    print('the most common weekday for bikeshare use: {}\n'.format(day_common.title()))
    # TO DO: display the most common start hour
    hour_common = df['hour'].mode()[0]


    if hour_common == 0:
        hour_common = '12 AM'
        print('the most common hour for bikeshare use: {}\n'.format(hour_common))
    elif hour_common > 0 and hour_common <= 12:
        print('the most common hour for bikeshare use: {} AM\n'.format(hour_common))
    else:
        hour_common = hour_common - 12
        print('the most common hour for bikeshare use: {} PM\n'.format(hour_common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station_common = df['Start Station'].mode()[0]
    print('The most commonly used start station: {}\n'.format(start_station_common))

    # TO DO: display most commonly used end station
    end_station_common = df['End Station'].mode()[0]
    print('The most commonly used end station: {}.\n'.format(end_station_common))

    # TO DO: display most frequent combination of start station and end station trip

    df['Station Pair'] = df['Start Station'] + '-' + df['End Station']
    station_combo = df['Station Pair'].mode()[0]
    print('The most frequently matched start and stop stations: {}.\n'.format(station_combo))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total bike travel time: {} minutes\n'.format(total_travel_time/60))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The average bike travel time: {} minutes\n'.format(mean_travel_time/60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    type_counts = df['User Type'].value_counts()

    for index, type_count in enumerate(type_counts):
        print('{} : {}\n'.format(type_counts.index[index], str(type_count)))

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()

        for index, gender_count in enumerate(gender_counts):
            print('{} : {}\n'.format(gender_counts.index[index], str(gender_count)))

        no_gender = int(df['Gender'].isna().sum())
        print('\nThere were {} customers whose gender was not provided.\n\n'.format(no_gender))

    else:
        print('Gender data was not provided for this city.')
    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df:
        earliest_by = int(df['Birth Year'].min())
        print('The oldest customer was born in {}.\n'.format(earliest_by))

        recent_by = int(df['Birth Year'].max())
        print('The youngest customer was born in {}.\n'.format(recent_by))

        common_by = int(df['Birth Year'].mode()[0])
        print('Most of the customers who use the bikeshare service were born in {}.\n'.format(common_by))

        no_by = int(df['Birth Year'].isna().sum())
        print('\n\nThere were {} customers whose birth year was not provided.\n'.format(no_by))

    else:
        print('Birth year data was not provided for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_table_data(df):
    """
       This function will display the raw data in groups of 10 rows on
       user request. If the user would like to see more data, they will
       be prompted to answer Yes or No.

       Args:
       Filtered DataFrame
    """

    print(df.head(10).to_string())
    raw_count = 0
    while True:
        raw_data = input('\nWould you like to see the next 10 rows? Enter Yes/No:\n')
        if raw_data.lower()!='yes':
            return
        raw_count = int(raw_count) + 10
        print(df.iloc[raw_count:raw_count+10].to_string())



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        while True:
            raw_data = input('\nWould you like to view first 10 rows of raw data? \nEnter Yes/No.\n')
            if raw_data.lower() != 'yes':
                break
            raw_table_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
