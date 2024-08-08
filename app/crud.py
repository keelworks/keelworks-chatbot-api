from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from . import models, schemas

def get_unanswered_question(db: Session, question_id: int):
    return db.query(models.UnansweredQuestion).filter(models.UnansweredQuestion.id == question_id).first()

def get_unanswered_questions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.UnansweredQuestion).offset(skip).limit(limit).all()

def create_unanswered_question(db: Session, question: schemas.UnansweredQuestionCreate):
    db_question = models.UnansweredQuestion(question=question.question)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

def delete_unanswered_question(db: Session, question_id: int):
    try:
        db_question = db.query(models.UnansweredQuestion).filter(models.UnansweredQuestion.id == question_id).one()
        db.delete(db_question)
        db.commit()
        return db_question
    
    except NoResultFound:
        return None