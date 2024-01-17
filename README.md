# Infant-Mortality-Rate-vs-GDP-Per-Capita
What is the relationship between the infant mortality rate and other demographic factors such as Gross Domestic Product per Capita (GDP per capita), and how has this relationship evolved?


Analysis Method: 

Filtering 
Read in the csv file using the pandas function pd.read_csv().  
Created a sorted list of the unique countries in the data frame by using the .unique() function on the "Country" column. 
Created a list of data frames; each data frame consisted of all the rows containing the same country. This was done using list comprehension. The for loop looped through each unique country name and created a temporary data frame pertaining to the country to add to the list. 

Grouping 
Every country was then sorted into one of five subdivisions. The subdivisions were created to sort countries by GDP per capita in order to get clearer visualizations of the data.  
Five null lists were initially created, each for a subdivision 
Then, the list of country data frames is looped through, placing a country in the correct subdivision based upon their max GDP per capita over the time interval 2000-2015. 

Plotting 
Made a for loop which loops through each subdivision. 
Within each loop, a series of plots are made for a subdivision: 1: line graph of the GDP per capita over time; 2: line graph of the infant deaths over time; 3: linear regression graph of the GDP per capita vs infant deaths; 4: a correlation matrix between GDP per capita and infant deaths.  
These plots are made using the matplotlib and seaborn libraries. 
Each type of graph had its own function, so four functions in total. 
The infant death and GDP per capita line charts are made using simple matplotlib functions such as plt.xlabel(), plt.ylabel(), plt.title(), and plt.plot(). The plotting was done by looping through each country in the subdivision and plotting the years as the x values and the infant deaths/GDP per capita as the y values. 
The linear regression was done by taking the "GDP_per_capita" and "Infant_deaths" individual columns and fitting them to a linear regression model, with the x values as GDP per capita and the y values as the infant deaths. Then a scatterplot with a linear regression fit was created using the matplotlib functions plt.scatter() and plt.plot(). 
The correlation matrix was made using the .corr() function in pandas. A heatmap was then plotted using the seaborn function sns.heatmap(). 

Subdivision Explanation: 
Subdivision 1: Countries with a max GDP per capita under 1000 
Various notable countries include Afghanistan, Ethiopia, Madagascar, Somalia, and Tajikistan 
Subdivision 2: Countries with a max GDP per capita between 1000 and 3000 
Various notable countries include India, Morocco, Nigeria, Ukraine, and Vietnam 
Subdivision 3: Countries with a max GDP per capita between 3000 and 6000 
Various notable countries include Algeria, Egypt, Indonesia, Iraq, and the Philippines 
Subdivision 4: Countries with a max GDP per capita between 6000 and 15000 
Various notable countries include Brazil, China, Mexico, Russia, and South Africa 
Subdivision 5: Countries with a max GDP per capita over 15000 
Various notable countries include Equatorial Guinea, Luxembourg, Singapore, Switzerland, and the United States 
