class Student(object):
    """Represents a student."""
    def __init__(self,name,number):
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name + "\nScores: " + " ".join(map(str,self.scores))
    def getName(self):
        """Returns the student's name."""
        return self.name
    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i-1] = score
    def getAverageScore(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
    