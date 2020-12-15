# User Movement in Location-Based Social Networks in Megalopolises

Note: The interactive plots do not show up on github.  As a result, we inserted screenshots in order to have an idea of outcome of these functions.  To be able to use these interactive plots, please refer to the data story, or simply by runing the notebook.

## Organization of the Github

In the github are contained the following documents:
* A folder entitled "Images" which contains the images inserted inside of our notebook
* A folder entitled "html" which contains the html code used in our data story
* the notebook "Project_3_Extension.ipynb" is the notebook used for this project extension, which contains all the code used to draw our plots and produce our results.
* the python script "helpers.py" contains the function used in our notebook.  This function splits the check-in according to their type of venues into distinct categories.
* the python script "kepler_configs.py" is used to load the maps into kepler: producing maps with the desired filters and style which evolve according to the time of day.


External libraries were used in order to make interactive plots with the maps of New York City and Tokyo:
* folium
* geopandas
* keplergl


## Abstract
Foursquare is a location-based social network based on check-ins similar to Gowalla and Brightkite. In this case, the dataset contains information about check-ins for two densely populated cities: New York City and Tokyo. The idea behind this extension is to study the effect of human mobility in much more densely populated areas. Indeed, a lot of people move to such attractive cities looking for out of habit experiences. By comparing the mobility patterns from these two megalopolises to those showcased in the paper “Friendship and Mobility”, we hope to pinpoint trends which would justify this attraction to cities. Given that these cities are bubbling with life, we would like to investigate and understand if daily routines are still present, or if there is more entropy in human movement. Collecting such information and understanding the patterns holds great implications in multiple domains.  Not only does it provide useful knowledge in order to optimize urban planning, it also informs greatly on a larger scale, indicating which activity is most done, where and when.  In the current context of Covid19, such information can contribute greatly to predict where the clusters have a higher tendency to form, and how they will most likely spread.


## Research Questions
* When looking at users’ check-ins: Do they limit themselves to a work/home pattern, or is there more variety in their check-ins? Moreover, are these check-ins more spread out or constrained to their neighborhood. Are these trends periodic or do users often discover new places?
* Are users more likely to explore and not restrain themselves to only close locations (compared to the 100km kink seen in the article)?
* When comparing the two megalopolises: do we see the same trends from one big city to another? Or does it depend on the city?
* Does the time of day or the city influence the type of venue a user will check into? (as the type of venue are mentioned in the dataset)

## Proposed dataset
The [dataset](https://sites.google.com/site/yangdingqi/home/foursquare-dataset) we are going to use contains check-ins of the social network Foursquare from 12 April 2012 to 16 February 2013. Like Gowalla and Brightkite, it is also a venue-based check-in platform. However, with our proposed dataset, there are not any links between users. Moreover, the time of day for each check-in is included, which allows for different insights. In turn, the type of venue is mentioned for each check-in.

The dataset contains 227428 check-ins in New York City and 537703 in Tokyo. There is only a small number of unique users included within the dataset: 1083 in NYC and 2293 in Tokyo. This allows for a sufficient estimation of a given user’s home location in a manner similar to the Friendship and Mobility model, while at the same time allowing for a robust investigation into travel distance based on check-ins to further venues.  

## Methods
As New York City and Tokyo represent a considerably smaller area relative to the Gowalla and Brightkite datasets, we propose discretizing the two cities with smaller grid sizes to estimate the home location. For instance, as opposed to 25 by 25 km areas, we propose 3 by 3 km or smaller.

After estimating the user’s home as we previously did in our project replication, it will then enable us to observe and analyze the mobility patterns of the users.  We will be able to do this analysis thanks to the provided check-in locations as well as the associated time.

## Proposed timeline
Week 1 (Nov 30-Dec 6):
* Get started on the data, pre-process it
* Start visualizing it with different plots to see the density of the check-ins
* Begin answering research questions

Week 2 (Dec 7-Dec 13):
* Finishing up the notebook, answering our research questions
* Begin our data story

Week 3 (Dec 14-Dec 17):
* Finish up our data story
* Work separately on our replication of figure 3B

Week 4 (before Dec 23rd):
* Film video presenting our results

## Organization within the team
* Loading and cleaning the data set: Julien
* Preprocessing the data set: Janet
* Identifying user’s homes and looking at where they are located: Louise
* Seeing how far from home users travel: Janet
* Looking at habits/routines: Julien
* What type of activities are most popular? Louise
* Comparing both megalopolises: Julien
* Figuring out how to make the template for the data story: Janet
* Writing out the text for the data story: Louise
* Adding the plots and finalizing the data story: Julien
* Making slides for video: Louise and Julien
* Recording video presenting our project: Janet
