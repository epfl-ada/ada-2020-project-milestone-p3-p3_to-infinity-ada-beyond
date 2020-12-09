# -*- coding: utf-8 -*-

# Import libraries
import pandas as pd

def generate_activites(df):
    # Split up the datasets manually by categories as the NLP trial was unsuccessful
    
    # Food activities
    Food_activities = df[(df['venue_category_name'].str.contains('Restaurant', regex=False)) |
        (df['venue_category_name'].str.contains('Food', regex=False)) |
        (df['venue_category_name'].str.contains('Pizza', regex=False)) |
        (df['venue_category_name'].str.contains('Bagel', regex=False)) |
        (df['venue_category_name'].str.contains('Burger', regex=False)) |
        (df['venue_category_name'].str.contains('Burrito', regex=False)) |
        (df['venue_category_name'].str.contains('Donut', regex=False)) |
        (df['venue_category_name'].str.contains('Diner', regex=False)) |
        (df['venue_category_name'].str.contains('Breakfast', regex=False)) |
        (df['venue_category_name'].str.contains('Noodle', regex=False)) |
        (df['venue_category_name'].str.contains('Chips', regex=False))]

    
    # Arts and entertainment
    Art_and_Entertainment_Activities = df[(df['venue_category_name'].str.contains('Art', regex=False)) |
                            (df['venue_category_name'].str.contains('Music', regex=False)) |
                            (df['venue_category_name'].str.contains('Restaurant', regex=False)) |
                            (df['venue_category_name'].str.contains('Theater', regex=False)) |
                            (df['venue_category_name'].str.contains('Museum', regex=False)) |
                            (df['venue_category_name'].str.contains('Entertainment', regex=False)) |
                            (df['venue_category_name'].str.contains('Historic', regex=False)) |
                            (df['venue_category_name'].str.contains('Library', regex=False)) |
                            (df['venue_category_name'].str.contains('Event', regex=False)) |
                            (df['venue_category_name'].str.contains('Photography', regex=False))]
    
    # Fitness
    Fitness_Activities = df[(df['venue_category_name'].str.contains('Ourdoors', regex=False)) |
                         (df['venue_category_name'].str.contains('Stadium', regex=False)) |
                         (df['venue_category_name'].str.contains('Sporting', regex=False)) |
                         (df['venue_category_name'].str.contains('Athletic', regex=False)) |
                         (df['venue_category_name'].str.contains('Pool', regex=False)) |
                         (df['venue_category_name'].str.contains('Gym', regex=False)) |
                         (df['venue_category_name'].str.contains('Garden', regex=False))]
    
    # Shopping
    Shopping_Activities = df[(df['venue_category_name'].str.contains('Store', regex=False)) |
                          (df['venue_category_name'].str.contains('Shop', regex=False)) |
                          (df['venue_category_name'].str.contains('Mall', regex=False)) |
                          (df['venue_category_name'].str.contains('Pharmacy', regex=False)) |
                          (df['venue_category_name'].str.contains('Place', regex=False)) |
                          (df['venue_category_name'].str.contains('Market', regex=False))]
    
    # Professional activities and schooling
    Professional_Activities = df[(df['venue_category_name'].str.contains('Center', regex=False)) |
                              (df['venue_category_name'].str.contains('Bank', regex=False)) |
                              (df['venue_category_name'].str.contains('Building', regex=False)) |
                              (df['venue_category_name'].str.contains('Office', regex=False)) |
                              (df['venue_category_name'].str.contains('University', regex=False)) |
                              (df['venue_category_name'].str.contains('Service', regex=False)) |
                              (df['venue_category_name'].str.contains('Factory', regex=False)) |
                              (df['venue_category_name'].str.contains('Financial', regex=False)) |
                              (df['venue_category_name'].str.contains('Hall', regex=False)) |
                              (df['venue_category_name'].str.contains('College', regex=False)) |
                              (df['venue_category_name'].str.contains('School', regex=False)) |
                              (df['venue_category_name'].str.contains('Base', regex=False))|
                              (df['venue_category_name'].str.contains('Consulate', regex=False))|
                              (df['venue_category_name'].str.contains('Professional', regex=False))]
     
    # Transportation and travel
    Travel_Activities = df[(df['venue_category_name'].str.contains('Bridge', regex=False)) |
                        (df['venue_category_name'].str.contains('Bus', regex=False)) |
                        (df['venue_category_name'].str.contains('Station', regex=False)) |
                        (df['venue_category_name'].str.contains('Airport', regex=False)) |
                        (df['venue_category_name'].str.contains('Ferry', regex=False)) |
                        (df['venue_category_name'].str.contains('Subway', regex=False)) |
                        (df['venue_category_name'].str.contains('Rail', regex=False)) |
                        (df['venue_category_name'].str.contains('Train', regex=False)) |
                        (df['venue_category_name'].str.contains('Travel', regex=False)) |
                        (df['venue_category_name'].str.contains('Car', regex=False)) |
                        (df['venue_category_name'].str.contains('Bike', regex=False))]
    
    # Residences
    Home_Activities = df[(df['venue_category_name'].str.contains('Home (private)', regex=False)) |
                      (df['venue_category_name'].str.contains('Building', regex=False)) |
                      (df['venue_category_name'].str.contains('Neighborhood', regex=False)) |
                      (df['venue_category_name'].str.contains('Hotel', regex=False)) |
                      (df['venue_category_name'].str.contains('Residential', regex=False)) |
                      (df['venue_category_name'].str.contains('House', regex=False))]
    
    # Nightlife
    Nightlife_Activities = df[(df['venue_category_name'].str.contains('Club', regex=False)) |
                           (df['venue_category_name'].str.contains('Bar', regex=False)) |
                           (df['venue_category_name'].str.contains('pub', regex=False)) |
                           (df['venue_category_name'].str.contains('Casino', regex=False))]
    
    return Food_activities, Art_and_Entertainment_Activities, Fitness_Activities, Shopping_Activities, Professional_Activities, Travel_Activities, \
           Home_Activities, Nightlife_Activities