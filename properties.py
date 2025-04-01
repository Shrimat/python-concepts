class Ninja:
    def __init__(self):
        self._score = 0
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        # Do some checks here
        self._score = value
    
    @score.deleter
    def score(self):
        del self._score

ninja = Ninja()
print(ninja.score)
ninja.score = 100
print(ninja.score)

"""
For more details on the property decorator, check out the following link:
https://www.youtube.com/watch?v=8BbngXWouzo
"""
