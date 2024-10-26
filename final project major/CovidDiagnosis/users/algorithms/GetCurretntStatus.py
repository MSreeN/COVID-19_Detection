import os.path
from django.conf import settings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# pip install numpy==1.16.5
# pip install pandas==1.2.3
def startCurrentStatus(filepath):
    df = pd.read_csv(filepath)
    print(df.head())
    print(" Number of row in the dataset are :", df.shape[0])
    print(" Number of column in the dataset are :", df.shape[1])
    df.isnull().sum()
    # check dataset contain any duplicate value
    print("Number of duplicate value in the dataset are :", sum(df.duplicated()))
    # Remove the unneccesary column in the dataset
    df_new = df.drop(['ConfirmedIndianNational', 'ConfirmedForeignNational'], axis=1)
    df_new.head()
    # select the data of date 10/07/20
    covid_new = df_new[df_new['Date'] == '10/07/20']
    # sort the dataset of top 10 state with most confirmed cases on 10/07/20
    covid_new.sort_values(by='Confirmed', ascending=False)[:10]
    # plot the bar graph of top 10 state with most number of confirmed cases on 10/07/20
    d = covid_new.sort_values(by="Confirmed", ascending=False)[:10]
    d.plot(x='State/UnionTerritory', y='Confirmed', kind='bar')

    # sort the dataset of top 10 state with most Death cases on 10/07/20
    covid_new.sort_values(by="Deaths", ascending=False)[:10]
    # plot the bar graph of top 10 state with most number of Deaths cases on 10/07/20
    covid_new.sort_values(by="Deaths", ascending=False)[:10].plot(x='State/UnionTerritory', y='Deaths', kind='bar',
                                                                  color='tab:red', figsize=(10, 5))

    # sort the dataset of top 10 state with most number of recovery on 10/07/20
    covid_new.sort_values(by="Cured", ascending=False)[:10]

    # plot the bar graph of top 10 state with most number of Confirmed cases on 10/07/20
    covid_new.sort_values(by="Cured", ascending=False)[:10].plot(x='State/UnionTerritory', y='Cured', kind='bar',
                                                                 color='tab:green', figsize=(10, 5))

    labels = ['Cured', 'Death', 'Confirmed']
    values = [127259, 9667, 230599]
    import matplotlib.pyplot as plt
    explode = (0.20, 0.20, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(values, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()
    # Mortality rate of maharastra
    print((covid_new['Deaths'].max() / covid_new['Confirmed'].max()) * 100)
    # recovery rate of Maharastra
    print((covid_new['Cured'].max() / covid_new['Confirmed'].max()) * 100)

    # read the csv
    path = os.path.join(settings.MEDIA_ROOT,'india','AgeGroupDetails.csv')
    df_age = pd.read_csv(path)
    print(df_age.head())
    # check weather dataset contain any null values
    print("The number of value dtaset contain are :", df_age.isnull().sum())
    df_age.sort_values(by="TotalCases", ascending=False)
    # check weather the dataset contain null value or not
    print("The number of nulll value in the dataset are :", df_age.isnull().sum())
    df_age.sort_values(by="TotalCases", ascending=False)
    # plot the graph between TotalCases and AgeGroups
    df_age.sort_values(by="TotalCases", ascending=False).plot(x='AgeGroup', y='TotalCases', kind='bar', color='tab:red',
                                                              figsize=(10, 5))

    # read the dataset
    path = os.path.join(settings.MEDIA_ROOT,'india','HospitalBedsIndia.csv')
    df_hospital = pd.read_csv(path)
    df_hospital.head()
    # sort the value of dataset Total health care facilities
    df_hospital.sort_values(by='TotalPublicHealthFacilities_HMIS', ascending=False)[1:10]
    # plot the graph for total public health care facilites
    df_hospital.sort_values(by="TotalPublicHealthFacilities_HMIS", ascending=False)[1:36].plot(x='State/UT',
                                                                                               y='TotalPublicHealthFacilities_HMIS',
                                                                                               kind='bar',
                                                                                               color='tab:red',
                                                                                               figsize=(12, 5))
    # sort the dataset which state has higher number of public beds

    df_hospital.sort_values(by="NumPublicBeds_HMIS", ascending=False)[1:10]
    # plot the graph for number of public beds available

    df_hospital.sort_values(by="NumPublicBeds_HMIS", ascending=False)[1:36].plot(x='State/UT', y='NumPublicBeds_HMIS',
                                                                                 kind='bar', color='tab:orange',
                                                                                 figsize=(12, 5))
    # sort the dateset by number of beds available
    df_hospital.sort_values(by="NumUrbanBeds_NHP18", ascending=False)[1:10]
    # plot the graph for number of Urban beds avilable
    df_hospital.sort_values(by="NumUrbanBeds_NHP18", ascending=False)[1:36].plot(x='State/UT', y='NumUrbanBeds_NHP18',
                                                                                 kind='bar', color='tab:green',
                                                                                 figsize=(12, 5))
    # sort the dateset by number of Rural beds avilabl
    df_hospital.sort_values(by="NumRuralBeds_NHP18", ascending=False)[1:10]
    # plot the graph for number of Rural beds avilable
    df_hospital.sort_values(by="NumRuralBeds_NHP18", ascending=False)[1:36].plot(x='State/UT', y='NumRuralBeds_NHP18',
                                                                                 kind='bar', color='tab:red',
                                                                                 figsize=(12, 5))

    # read the dataset
    path = os.path.join(settings.MEDIA_ROOT,'india', 'IndividualDetails.csv')
    df_individual = pd.read_csv(path)
    df_individual.head()
    # current status
    df_individual['current_status'].value_counts()
    # plot the graph for number of people hospitalized, recoverd, Decased and Migrated
    df_individual['current_status'].value_counts().plot(kind='bar', color='tab:orange', figsize=(12, 8))
    # read the datset
    path = os.path.join(settings.MEDIA_ROOT,'india','StatewiseTestingDetails.csv')
    df_testing = pd.read_csv(path)
    df_testing
    # dataset Info
    df_testing.info()
    # coverte the negative column from string to float
    df_testing_details = pd.DataFrame(df_testing)
    df_testing_details['Negative'] = pd.to_numeric(df_testing_details['Negative'], errors='coerce')
    df_testing_details.info()
    # Check weather the Negative column converted from string to float or not
    print("Datatype of Negative column are :", df_testing_details['Negative'].dtype)
    # check weather dataset contain any null values
    print("The number of value dtaset contain are :", df_testing_details.isnull().sum())
    # remove the null values
    df_test = df_testing_details.dropna(subset=['Negative', 'Positive'])
    # Check the null values are droped or not
    print("The number of null value dataset contains are :", df_test.isnull().sum())
    # sort the dataset by number of total cases
    df_test.sort_values(by='TotalSamples', ascending=False)[:10]
    # plot the graph for total number of sample
    df_test.sort_values(by="TotalSamples", ascending=False)[1:36].plot(x='State', y='TotalSamples', kind='bar',
                                                                       color='tab:orange', figsize=(14, 9))
    # sort the dataset by number of positive cases
    df_test.sort_values(by='Positive', ascending=False)[:10]
    # plot the graph for total number of positive sample
    df_test.sort_values(by="Positive", ascending=False)[1:36].plot(x='State', y='Positive', kind='bar', color='tab:red',
                                                                   figsize=(14, 9))
    # sort the dataset by number of Negative cases

    df_test.sort_values(by='Negative', ascending=False)[:10]
    # plot the graph for total number of negative sample
    df_test.sort_values(by="Negative", ascending=False)[1:36].plot(x='State', y='Negative', kind='bar',
                                                                   color='tab:green', figsize=(14, 9))
    # consider for date 12/07/2020
    df_test_date = df_test[df_test['Date'] == '2020-07-12']
    # make a df for state Maharastra for date 12/07/2020
    df_test_maha = df_test_date[df_test_date["State"] == 'Maharashtra']
    # Maximum total sample for Maharastra on date 12/07/2020
    df_test_maha['TotalSamples'].max()
    # Maximum total Positive sample for Maharastra on date 12/07/2020
    df_test_maha['Positive'].max()
    # Maximum total Negative sample for Maharastra on date 12/07/2020
    df_test_maha['Negative'].max()
    labels = ['Total Sample', 'Positive', 'Negative']
    values = [1321715.0, 259037.0, 1062678.0]
    import matplotlib.pyplot as plt
    explode = (0.20, 0.20, 0)
    fig1, ax1 = plt.subplots()
    ax1.pie(values, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()
    # Total Percentage of being positive

    (df_test_maha['Positive'].max() / df_test_maha['TotalSamples'].max()) * 100
    # Total Percentage of being Negative
    (df_test_maha['Negative'].max() / df_test_maha['TotalSamples'].max()) * 100
    # plot the line graph for total sample, positive sample and negative sample


    # df_line = df_test.plot.line(subplots=True, figsize=(10, 8))
    plt.show()








