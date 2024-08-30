from quiz_question_model import Question
from quiz_data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i_question in question_data:
    question_text = i_question["text"]
    question_answer = i_question["answer"]

    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
