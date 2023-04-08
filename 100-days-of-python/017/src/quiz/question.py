"""
Contains the Question class which represents a single question.
"""


class Question:
    """
    Models a single question in a quiz.
    """

    def __init__(self, text, answer):
        """
        Initialises a new instance with the given text and the answer.
        """
        self.text = text
        self.answer = answer
