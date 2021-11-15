Magic M 1.0 
README

Introduction 

Magic M is an interactive behavioral journal that collects real time interactions between User and  their environment  and produces a summary  statement of highly and least favorable activities. From there, it will give deliver feedback to the User by suggesting activities the User might enjoy. 

Purpose of Magic M

The goal of Magic M is to create an interactive habit tracker score card that allows the user to journal their emotional state in correlation to activities and interactions with individuals. With the data collected survey their mood and realize trends and pattern within their interaction within their environment. 

Goal

After collecting enough data/information. The User will be able to use Magic M as a tool for Behavioral Modification. The program will use predictive analysis to create insights and foretell behaviors and moods. In addition, I will be able to analyze outside source to suggest possible change in activities and behavior where Users can be introduce to activities different from what they are already engaged in. 

Body

Currently, Magic M (in its basic form) is able to collect basic demographics from the user; such as, name, age, gender. At the interactive platform it is able to create a journal that users can update in real time to document their emotions and the activities that trigger them. Finally, the user receives a summary of activities they’ve either enjoyed or dislike and a random recommendation will be suggested. 

Level 1: Person’s demographics (name, gender, age)
Level 2: Emotional Journaling (date, time, emotion, scale, triggers)
Level 3: Associating  the data points to create insights
Level 4: Output generates a statement and a suggestion

How to use this Package

Import all modules to the Emotion module

import welcome
import how_are_you
import person
import mood
import mood_finder
import data_association
import suggestion
import replay
import summary

Once all modules are imported. In the how_are_you and welcome modules User will simple Magic M will introduce itself to the User as well as the User will introduce themself by inputing their name, age, and gender. 
Then they will begin the journaling by inputing the date, time, feeling, magnitude, trigger and that will happen using the mood module. 
Also, the user can to search through their log using the mood_finder module. 
Next the data_association module interlink data to be called in pairs. 
Then, the suggestion module suggest at random an activity from the builtin list of activities and the reply module allows the user to ask any question to the program. 
Finally, the summary module summarizes the top 5 favorable and least favorable activity.  

