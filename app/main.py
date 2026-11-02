from fastapi import Depends, FastAPI, HTTPException, status, Response
#from sqlalchemy import select
#from sqlalchemy.exc import IntegrityError
#from sqlalchemy.orm import Session
import httpx
#from app.database import engine, get_db
#from app.models import Base, UserDB
#from app.schemas import UserCreate, UserRead

#Base.metadata.create_all(bind=engine)
#users: list[UserCreate] = []
app = FastAPI(title="CICD2 Exam 1")

@app.get("/health")
def health():
    return{"status": "ok"}

#@app.get("/api/users", response_model=list[UserRead])
#def get_users(db: Session = Depends(get_db)):
#    statement = select(UserDB).order_by(UserDB.id)
#    return db.execute(statement).scalars().all()

#@app.post("/api/users", response_model=UserRead, status_code=status.HTTP_201_CREATED)
#def add_user (new_user:UserCreate, db: Session = Depends(get_db)):
#    db_user(db_user)
#    db.add(db_user)
#    try: 
#        db_commit()
#        db.refresh(db_user)
 #   except IntegrityError:
 #       raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    

    


