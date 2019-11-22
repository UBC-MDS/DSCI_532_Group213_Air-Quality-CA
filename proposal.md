# Proposal

## Section 1: Motivation and Purpose

The root causes of deaths in many parts of the world have been an alarming case that got the attention of many international organizations. Such death-causing factors are many but the majority of those that lead to prevalent deaths include smoking, high blood pressure, obesity, high blood sugar, air pollution, among others. Hence, it is essential to figure out which of these factors leads to the highest death rate in every country and across continents. This is a tremendous challenge for decision-makers in the health sector whether it is governments or non-governmental organizations. To address this critical situation, we will design a dashboard application that uses accurate data that was obtained from the Global Burden of Disease Collaborative Network, USA. The app will show the proportions of deaths caused by each of the risk factors outlined above. It will also interactively show the number of deaths caused by these risk factors across countries in the world in a geographic heatmap. Furthermore, the app will allow users to see the trend (line graph) of risk factors across all continents based on a selected risk factor using radio buttons.
Another aspect of the project motivation also includes allowing users to visualize and see how the death-causing factors are changing with time. As such, the app will provide a sort of global overview to help make effective comparisons among these risk factors. This will help to figure out if the causes of death in different countries are the same every year or if they are shifting with time.

## Section 2: Description of the data
We will be visualizing a data$^1$ set of the number of deaths by risk factors of 196 countries from 1990 to 2017. The data has 6468 rows and 30 columns including the `country name`, `country code`, `year` and factors (e.g. `Unsafe water source (deaths)`, `Low birth weight (deaths)`, `Smoking (deaths)`, `High blood pressure (deaths)`, `Obesity (deaths)`, `Air pollution (outdoor & indoor) (deaths)` etc). 

For cleaning the data, we dropped the entities without country codes(e.g. Asia High SDI) and renamed the column `entity` to `country`. After dropping all the rows with null values and `High cholesterol (deaths)` column which has too much missing data (70%), we have 5488 rows left with 196 countries and 26 risk factors. We also cleaned up column names. We substituted the spaces between words to underscores and removed the "(death)" part. An example of the column names in the clean data is `unsafe_water_source`. The original data and the cleaned data can be found in the `data` file.

## Section 3: Research questions and usage scenarios

In general, in a population of 1000 individuals, there is an approximate 9.5 death per year in that population. That is, the general death rate is 0.95% per year.$^2$  In 2017, the crude death rate is approximate 0.83% around the world according to CIA Work Factbook.$^3$  This is less than 1%, but what if we convert it to an actual number? According to the World Bank database, the world population is approximately 7.5 billion in the year 2017.$^4$ Based on the crude death rate, the number of death in 2017 is approximately 62.225 million in the world. That is a huge number.
 
Our dashboard will be developed to answer the following **research questions**:

- What's the top 5 risk factors that caused the largest amount number of death in 2017?
- What's these risk factors look like among countries in 2017?
- What's the trend of these risk factors over time by continents?
 
**Usage scenario**
 
Morty is an employee in the Work Bank and he wants to understand what risk factors that would cause a large amount of death in recent years and the influence of those factors around the world. With that information, he can write a report so that people will pay attention to those risk factors. He also wants to explore the risk factors and compare the number of death caused by the most dangerous risk factors in different regions around the world.
 
When he logs into the app, he will see an overview of the total number of death caused by each factor in 2017. The plot is ranked in descending order. He might notice that “High blood pressure” caused the highest number of death around the world. When he clicks the second button, “World’s Death Rate”, he will see a heated map that shows how does the number of death caused by high blood pressure distributed among countries in 2017. He might find out that some regions or continents have a much higher death rate caused by that factor. If he clicks the third button, “Death Trend”, he can see whether the death rate by that factor is getting better over the years, and also compare the trend of different continents. Furthermore, He can look at the same information for other high-frequency death factors by using the drop-down menu and radio buttons in the app.
 
After going through the dashboard, he can further research why does a risk factor keep occurring and increasing in certain regions and how to prevent it. 

## Resources:
1. The data has been approved by Firas. The data was published by "Global Burden of Disease Collaborative Network. Global Burden of Disease Study 2017 (GBD 2017) Results. Seattle, United States: Institute for Health Metrics and Evaluation (IHME), 2018". It could be downloaded [here](https://ourworldindata.org/air-pollution).

2. [Wikipedia.**Mortality Rate**](https://en.wikipedia.org/wiki/Mortality_rate)

3. [World Factbook. **Dearth Rate in 2017**](https://www.cia.gov/library/publications/the-world-factbook/rankorder/2066rank.html)

4. [World Bank. **Population Total**](https://data.worldbank.org/indicator/sp.pop.totl)
