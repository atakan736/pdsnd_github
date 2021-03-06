import time
import pandas as pd


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which city would you like to explore")
        city = city.lower()
        if city in ["chicago","new_york_city","washington"]:
            break
        else:
            print("invalid input. Please enter a valid input")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Do you want details specific to a particular month? If yes, type month name from within first six months else type 'all'")
        month = month.lower()
        if month in ["january","february","march","april","may","june","all"]:
            break
        else:
            print("invalid input. Please enter a valid input")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Do you want details specific to a particular day? If yes, type day name else type 'all'")
        day = day.lower()
        if day in ["monday","tuesday","wednesday","thursday","friday","saturday","sunday","all"]:
            break
        else:
            print("invalid input. Please enter a valid input")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.weekday_name

    if month != "all":
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(months)+1
        df = df[df['month'] == month]

    if day != "all":
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):


    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is ", df["month"].mode()[0])

    # TO DO: display the most common day of week
    print("The most common day of week  is ", df["day_of_week"].mode()[0])

    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour()
    print("The most common start hour is", df["hour"].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is ", df["Start Station"].mode()[0])

    # TO DO: display most commonly used end station
    print("The most commonly used end station is ", df["End Station"].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df["combination"] = df["Start Station"]+""+df["End Station"]
    print("The most frequent combination of start station and end station trip is: ", df["combination"].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is", df["Trip Duration"].sum())

    # TO DO: display mean travel time
    print("The total mean travel time is", df["Trip Duration"].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df.groupby(["User Types"])["User Types"].count()
    print(user_types)

    # TO DO: Display counts of gender
    if city != "washington":
       gender = df.groupby(["Gender"])["Gender"].count()
       print(gender)
    # TO DO: Display earliest, most recent, and most common year of birth
       eyob = sorted(df.groupby(["Birth Year"])["Birth Year"][0][0])
       mryob = sorted(df.groupby(["Birth Year"])["Birth Year"][0][0],reverse=0)
       mcyob = df["Birth Year"].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    x = 0
    while True:
        raw = input('\nWould you like to see some raw data? Enter yes or no.\n')
        if raw.lower() == 'yes':
            print(df.head(x+5))
            x += 5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
