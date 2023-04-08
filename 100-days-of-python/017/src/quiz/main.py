"""
A true/false quiz game that allows players to answer questions
and keep track of their scores.
"""

from quiz.data import question_data
from quiz.question import Question
from quiz.quiz_brain import QuizBrain


def main():
    """
    Runs the quiz game.
    """
    question_bank = [
        Question(question["question"], question["correct_answer"])
        for question in question_data
    ]
    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()

    print("You've completed the quiz.")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")


if __name__ == "__main__":
    main()
