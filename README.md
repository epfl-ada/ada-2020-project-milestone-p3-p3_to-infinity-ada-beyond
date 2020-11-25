# User Movement in Location-Based Social Networks in Megalopolises

## Abstract
Foursquare is a location-based social network based on check-ins similar to Gowalla and Brightkite. In this case, the dataset contains information about check-ins for two densely populated cities: New York City and Tokyo. The idea behind this extension is to study the effect of human mobility in much more densely populated areas.  Indeed, a lot of people move to such attractive cities looking for out of habit experiences. By comparing the mobility patterns from these two megalopolises to those showcased in the paper “Friendship and Mobility”, we hope to pinpoint trends which would justify this attraction to cities.  Given that these cities are bubbling with life, we would like to investigate and understand if daily routines are still present, or if there is more entropy in human movement.

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
Our planning for the next project milestone consists in pre-processing and getting started with the data altogether.  Then we will split up the tasks to try to answer the research questions in parallel, keeping each other updated so we can advance efficiently. Once the notebook is completed and the graphs are obtained, we’ll make our data story and then work separately on the replication part of this milestone.  Once everything is handed in, we’ll meet up to film the video presenting our project and our results!




