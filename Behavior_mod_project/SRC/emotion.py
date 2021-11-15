import welcome
import how_are_you
import person
import mood
import mood_finder
import data_association
import suggession
import replay
import summary

class Emotion:
    def __init__(self, time, date, magnitude, id, trigger):
        self.time    = time
        self.date    = date
        self.mag     = magnitude
        self.id      = id
        self.trigger = trigger
    
    def return_emotion(self):
        a = print(f"Date:{self.date}, Time:{self.time}, 
        Scale: {self.mag}, Feeling:{self.id}, Activity: {self.trigger}.")
        return a
    
  