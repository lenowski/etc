"""
Contains the QuizBrain class, which manages the logic of the quiz game.
"""


class QuizBrain:
    """
    Models the game mechanics of a multiple-choice quiz.
    """

    def __init__(self, question_list):
        """
        Initialises a new instance with the given question list,
        and sets the initial score and question number to 0.
        """
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        """
        Displays the next question in the quiz and prompts the user for an answer,
        then checks the answer and updates the score.
        """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q. {self.question_number}: " f"{current_question.text} (True/False): "
        )
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        """
        Checks if there are more questions in the quiz.
        """
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        """
        Checks whether the given user answer matches the correct answer,
        and updates the score accordingly.
        """
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")
