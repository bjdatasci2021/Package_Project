def How_are_you(self):
        print(f'So what I got was: name: {self.name}, gender: {self.gender},and age: {self.age}.')
        print("Its my pleasure to meet you!")
        
        answer = int(input("How are you today? 1: 'Bored', 2: 'Tired', 3: 'Ok', 4:'Good', 5:'Happy'"))

        mood = {1: 'Bored', 2: 'Tired', 3: 'Ok', 4:'Good', 5:'Happy'}

        if answer in mood.keys() and answer >= 3:
            print( f"I'm happy to hear that you're: {mood[answer]}, {self.name} !")
            print("I would like to learn more.")
        
        elif answer in mood.keys() and answer < 3:
            print(f"I'm sorry to hear that you're: {mood[answer]}, {self.name} !")
            print("Please tell me more. ")