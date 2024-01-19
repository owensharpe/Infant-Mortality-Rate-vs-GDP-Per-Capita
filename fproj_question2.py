"""
DS2001: Final Project

By: Neha Lingamallu, Owen Sharpe, and Junseo Yoon

Date: 11/7/2023

Question 2: What is the relationship between the number of Infant_deaths
            per 1,000 live births and other demographic factors such as GDP
            per capita over the years, and how has this relationship evolved??
"""

# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression


def plot_infant_deaths(scale_division, name):
    """
    :param: scale_division (list of dataframes for all countries of a specific gdp Division)
            name (string)
    :return: null (plotting)
    """

    plt.figure(figsize=(10, 6))
    xtick_values = [x for x in range(2000, 2016)]
    plt.xticks(xtick_values, list(map(str, xtick_values)))
    plt.xlabel('Years')
    plt.ylabel('Infant Deaths')
    plt.title('Infant Deaths For Countries In ' + name + ' Over Time')
    for country in scale_division:
        year_span = country[['Year']]
        infant_deaths = country[['Infant_deaths']]
        plt.plot(year_span, infant_deaths, linestyle="-", marker="o")
    # plt.savefig('infant_deaths' + name + '.png')


def plot_gdp_per_cap(scale_division, name):
    """
    :param: countries (list of dataframes for all countries of a specific gdp Division)
            name (string)
    :return: null (plotting)
    """

    plt.figure(figsize=(10, 6))
    xtick_values = [x for x in range(2000, 2016)]
    plt.xticks(xtick_values, list(map(str, xtick_values)))
    plt.xlabel('Years')
    plt.ylabel('GDP Per Capita')
    plt.title('GDP per Capita For Countries In ' + name + ' Over Time')
    for country in scale_division:
        year_span = country[['Year']]
        gdp_per_capita = country[['GDP_per_capita']]
        plt.plot(year_span, gdp_per_capita, linestyle="-", marker="o")
    # plt.savefig('gdp_per_cap' + name + '.png')


def plot_linear_regression(scale_division, name):
    """
    :param: countries (list of dataframes for all countries of a specific gdp division)
            name (string)
    :return: null (plotting)
    """

    # create filtered dataset to do linear regression
    final_df = pd.DataFrame()

    for country in scale_division:
        temp_df = country[['GDP_per_capita', 'Infant_deaths']]
        final_df = pd.concat([final_df, temp_df])

    # create model
    model = LinearRegression()

    # create x and y variables
    x = final_df[['GDP_per_capita']]
    y = final_df[['Infant_deaths']]
    model.fit(x, y)

    # plot
    plt.figure(figsize=(10, 6))
    plt.scatter(final_df[['GDP_per_capita']], final_df[['Infant_deaths']],
                label='GDP per Capita vs Infant Deaths')
    plt.plot(final_df[['GDP_per_capita']],
             model.predict(final_df[['GDP_per_capita']]),
             color='red',
             label='Linear Regression Fit')

    # give plot additions
    plt.title('GDP per Capita vs Infant Deaths and Linear Regression Fit For ' + name)
    plt.xlabel('GDP per Capita')
    plt.ylabel('Infant Deaths')
    plt.legend()
    plt.grid(True)
    # plt.savefig('regression' + name + '.png')


def plot_correlation_matrix(scale_division, name):
    """
    :param: countries (list of dataframes for all countries of a specific gdp division)
            name (string)
    :return: null (plotting)
    """
    
    final_df = pd.DataFrame()
    
    for country in scale_division:
        temp_df = country[['GDP_per_capita', 'Infant_deaths']]
        final_df = pd.concat([final_df, temp_df])

    # Calculate correlation matrix
    correlation_matrix = final_df.corr()

    # Plotting using Seaborn
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix For ' + name)
    # plt.savefig('correlation_matrix' + name + '.png')


if __name__ == "__main__":

    # import and read data
    life_exp_df = pd.read_csv("Life-Expectancy-Data-Updated.csv")

    # create a country list from the data
    country_list = sorted(list(life_exp_df["Country"].unique()))

    # create individual dataframes for each country
    country_data = [life_exp_df[life_exp_df['Country'] == country]
                    for country in country_list]

    # sort countries into five different divisions by GDP per capita
    gdp_division_1 = []
    gdp_division_2 = []
    gdp_division_3 = []
    gdp_division_4 = []
    gdp_division_5 = []
    for country in country_data:

        country = country.sort_values('Year')

        if country['GDP_per_capita'].max() <= 1000:
            gdp_division_1.append(country)
        elif country['GDP_per_capita'].max() <= 3000:
            gdp_division_2.append(country)
        elif country['GDP_per_capita'].max() <= 6000:
            gdp_division_3.append(country)
        elif country['GDP_per_capita'].max() <= 15000:
            gdp_division_4.append(country)
        else:
            gdp_division_5.append(country)

    # make plots for infant deaths and GDP per capita
    for num_graph in range(0, 5):

        # get plots from each gdp Division
        if num_graph == 0:
            plot_gdp_per_cap(gdp_division_1, name="GDP Division 1")
            plot_infant_deaths(gdp_division_1, name="GDP Division 1")
            plot_linear_regression(gdp_division_1, name="GDP Division 1")
            plot_correlation_matrix(gdp_division_1, name="GDP Division 1")
        elif num_graph == 1:
            plot_gdp_per_cap(gdp_division_2, name="GDP Division 2")
            plot_infant_deaths(gdp_division_2, name="GDP Division 2")
            plot_linear_regression(gdp_division_2, name="GDP Division 2")
            plot_correlation_matrix(gdp_division_2, name="GDP Division 2")
        elif num_graph == 2:
            plot_gdp_per_cap(gdp_division_3, name="GDP Division 3")
            plot_infant_deaths(gdp_division_3, name="GDP Division 3")
            plot_linear_regression(gdp_division_3, name="GDP Division 3")
            plot_correlation_matrix(gdp_division_3, name="GDP Division 3")
        elif num_graph == 3:
            plot_gdp_per_cap(gdp_division_4, name="GDP Division 4")
            plot_infant_deaths(gdp_division_4, name="GDP Division 4")
            plot_linear_regression(gdp_division_4, name="GDP Division 4")
            plot_correlation_matrix(gdp_division_4, name="GDP Division 4")
        else:
            plot_gdp_per_cap(gdp_division_5, name="GDP Division 5")
            plot_infant_deaths(gdp_division_5, name="GDP Division 5")
            plot_linear_regression(gdp_division_5, name="GDP Division 5")
            plot_correlation_matrix(gdp_division_5, name="GDP Division 5")

    # show plots
    plt.show()
