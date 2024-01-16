import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data =set()     
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if not val in self.data:
            self.data.add(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.data:
            self.data.remove(val)
            return True
        return False
        
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(list(self.data))