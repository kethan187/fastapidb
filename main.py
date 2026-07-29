from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import Base, engine, SessionLocal
import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()






@app.post("/criminals", response_model=schemas.criminalresponse)
def create(criminal: schemas.criminalcreate, db: Session = Depends(get_db)):
    return crud.create_criminal(db, criminal)

@app.get("/criminals", response_model=list[schemas.criminalresponse])
def read_all(db: Session = Depends(get_db)):
    return crud.get_criminals(db)

@app.get("/criminals/{criminal_id}", response_model=schemas.criminalresponse)
def read_one(criminal_id: int, db: Session = Depends(get_db)):
    criminal = crud.get_criminal(db, criminal_id)
    if not criminal:
        raise HTTPException(status_code=404, detail="criminal not found")
    return criminal

@app.put("/criminals/{criminal_id}", response_model=schemas.criminalresponse)
def update(criminal_id: int, criminal: schemas.criminalcreate, db: Session = Depends(get_db)):
    updated = crud.update_criminal(db, criminal_id, criminal)
    if not updated:
        raise HTTPException(status_code=404, detail="criminal not found")
    return updated

@app.delete("/criminals/{criminal_id}")
def delete(criminal_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_criminal(db, criminal_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="criminal not found")
    return {"message":"criminal deleted successfully"}




@app.get("/criminals/alias/{alias}")
def get_crim_alias(alias:str,db:Session=Depends(get_db)):
    return crud.get_crim_alias(db,alias)








@app.post("/cricketers", response_model=schemas.cricketerresponse)
def create(cricketer: schemas.cricketercreate, db: Session = Depends(get_db)):
    return crud.create_cricketer(db, cricketer)

@app.get("/cricketers", response_model=list[schemas.cricketerresponse])
def read_all(db: Session = Depends(get_db)):
    return crud.get_cricketers(db)

@app.get("/cricketers/{cricketer_id}", response_model=schemas.cricketerresponse)
def read_one(cricketer_id: int, db: Session = Depends(get_db)):
    cricketer = crud.get_cricketer(db, cricketer_id)
    if not cricketer:
        raise HTTPException(status_code=404, detail="cricketer not found")
    return cricketer

@app.put("/cricketers/{cricketer_id}", response_model=schemas.cricketerresponse)
def update(cricketer_id: int, cricketer: schemas.cricketercreate, db: Session = Depends(get_db)):
    updated = crud.update_cricketer(db, cricketer_id, cricketer)
    if not updated:
        raise HTTPException(status_code=404, detail="cricketer not found")
    return updated

@app.delete("/cricketers/{cricketer_id}")
def delete(cricketer_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_cricketer(db, cricketer_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="cricketer not found")
    return {"message":"cricketer deleted successfully"}




@app.get("/cricketers/alias/{alias}")
def get_cric_by_alias(alias:str,db:Session=Depends(get_db)):
    return crud.get_cric_by_alias(db,alias)





@app.post("/footballers", response_model=schemas.footballerresponse)
def create(footballer: schemas.footballercreate, db: Session = Depends(get_db)):
    return crud.create_footballer(db, footballer)

@app.get("/footballers", response_model=list[schemas.footballerresponse])
def read_all(db: Session = Depends(get_db)):
    return crud.get_footballers(db)

@app.get("/footballers/{footballer_id}", response_model=schemas.footballerresponse)
def read_one(footballer_id: int, db: Session = Depends(get_db)):
    footballer = crud.get_footballer(db, footballer_id)
    if not footballer:
        raise HTTPException(status_code=404, detail="footballer not found")
    return footballer

@app.put("/footballers/{footballer_id}", response_model=schemas.footballerresponse)
def update(footballer_id: int, footballer: schemas.footballercreate, db: Session = Depends(get_db)):
    updated = crud.update_footballer(db, footballer_id, footballer)
    if not updated:
        raise HTTPException(status_code=404, detail="footballer not found")
    return updated

@app.delete("/footballers/{footballer_id}")
def delete(footballer_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_footballer(db, footballer_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="footballer not found")
    return {"message":"footballer deleted successfully"}




@app.get("/footballers/alias/{alias}")
def get_fb_alias(alias:str,db:Session=Depends(get_db)):
    return crud.get_fb_alias(db,alias)







@app.post("/animals", response_model=schemas.animalresponse)
def create(animal: schemas.animalcreate, db: Session = Depends(get_db)):
    return crud.create_animal(db, animal)

@app.get("/animals", response_model=list[schemas.animalresponse])
def read_all(db: Session = Depends(get_db)):
    return crud.get_animals(db)

@app.get("/animals/{animal_id}", response_model=schemas.animalresponse)
def read_one(animal_id: int, db: Session = Depends(get_db)):
    animal = crud.get_animal(db, animal_id)
    if not animal:
        raise HTTPException(status_code=404, detail="animal not found")
    return animal

@app.put("/animals/{animal_id}", response_model=schemas.animalresponse)
def update(animal_id: int, animal: schemas.animalcreate, db: Session = Depends(get_db)):
    updated = crud.update_animal(db, animal_id, animal)
    if not updated:
        raise HTTPException(status_code=404, detail="animal not found")
    return updated

@app.delete("/animals/{animal_id}")
def delete(animal_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_animal(db, animal_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="animal not found")
    return {"message":"animal deleted successfully"}




@app.get("/weight/{weight}")
def get_animal_by_weight(weight:int,db:Session=Depends(get_db)):
    return crud.get_animal_by_weight(db,weight)





@app.post("/singers", response_model=schemas.singerresponse)
def create(singer: schemas.singercreate, db: Session = Depends(get_db)):
    return crud.create_singer(db, singer)

@app.get("/singers", response_model=list[schemas.singerresponse])
def read_all(db: Session = Depends(get_db)):
    return crud.get_singers(db)

@app.get("/singers/{singer_id}", response_model=schemas.singerresponse)
def read_one(singer_id: int, db: Session = Depends(get_db)):
    singer = crud.get_singer(db, singer_id)
    if not singer:
        raise HTTPException(status_code=404, detail="singer not found")
    return singer

@app.put("/singers/{singer_id}", response_model=schemas.singerresponse)
def update(singer_id: int, singer: schemas.singercreate, db: Session = Depends(get_db)):
    updated = crud.update_singer(db, singer_id, singer)
    if not updated:
        raise HTTPException(status_code=404, detail="singer not found")
    return updated

@app.delete("/singers/{singer_id}")
def delete(singer_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_singer(db, singer_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="singer not found")
    return {"message":"singer deleted successfully"}




@app.get("/topsong/{topsong}")
def get_singer_by_topsong(topsong:str,db:Session=Depends(get_db)):
    return crud.get_singer_by_topsong(db,topsong)