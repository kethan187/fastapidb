from sqlalchemy.orm import Session
import models
import schemas

def create_criminal(db: Session, criminal: schemas.criminalcreate):
    db_criminal = models.criminals(**criminal.model_dump())
    db.add(db_criminal)
    db.commit()
    db.refresh(db_criminal)
    return db_criminal

def get_criminals(db: Session):
    return db.query(models.criminals).all()

def get_criminal(db: Session, criminal_id: int):
    return db.query(models.criminals).filter(
        models.criminals.id == criminal_id
    ).first()

def update_criminal(db: Session, criminal_id: int, criminal: schemas.criminalcreate):
    db_criminal = get_criminal(db, criminal_id)
    if not db_criminal:
        return None
    db_criminal.name = criminal.name
    db_criminal.gender=criminal.gender
    db_criminal.location=criminal.location
    db_criminal.alias=criminal.alias

    db.commit()
    db.refresh(db_criminal)
    return db_criminal

def delete_criminal(db: Session, criminal_id: int):
    db_criminal = get_criminal(db, criminal_id)
    if not db_criminal:
        return None
    db.delete(db_criminal)
    db.commit()
    return db_criminal



def get_crim_alias(db:Session,alias:str):
    print(alias)
    return db.query(models.criminals).filter(
        models.criminals.alias==alias
    ).all()

def create_cricketer(db: Session, cricketer: schemas.cricketercreate):
    db_cricketer = models.cricketers(**cricketer.model_dump())
    db.add(db_cricketer)
    db.commit()
    db.refresh(db_cricketer)
    return db_cricketer

def get_cricketers(db: Session):
    return db.query(models.cricketers).all()

def get_cricketer(db: Session, cricketer_id: int):
    return db.query(models.cricketers).filter(
        models.cricketers.id == cricketer_id
    ).first()

def update_cricketer(db: Session, cricketer_id: int, cricketer: schemas.cricketercreate):
    db_cricketer = get_cricketer(db, cricketer_id)
    if not db_cricketer:
        return None
    db_cricketer.name = cricketer.name
    db_cricketer.category=cricketer.category
    db_cricketer.iplteam=cricketer.iplteam
    db_cricketer.alias=cricketer.alias

    db.commit()
    db.refresh(db_cricketer)
    return db_cricketer

def delete_cricketer(db: Session, cricketer_id: int):
    db_cricketer = get_cricketer(db, cricketer_id)
    if not db_cricketer:
        return None
    db.delete(db_cricketer)
    db.commit()
    return db_cricketer



def get_cric_by_alias(db:Session,alias:str):
    print(alias)
    return db.query(models.cricketers).filter(
        models.cricketers.alias==alias
    ).all()

def create_footballer(db: Session, footballer: schemas.footballercreate):
    db_footballer = models.footballers(**footballer.model_dump())
    db.add(db_footballer)
    db.commit()
    db.refresh(db_footballer)
    return db_footballer

def get_footballers(db: Session):
    return db.query(models.footballers).all()

def get_footballer(db: Session, footballer_id: int):
    return db.query(models.footballers).filter(
        models.footballers.id == footballer_id
    ).first()

def update_footballer(db: Session, footballer_id: int, footballer: schemas.footballercreate):
    db_footballer = get_footballer(db, footballer_id)
    if not db_footballer:
        return None
    db_footballer.name = footballer.name
    db_footballer.category=footballer.category
    db_footballer.teamname=footballer.teamname
    db_footballer.alias=footballer.alias

    db.commit()
    db.refresh(db_footballer)
    return db_footballer

def delete_footballer(db: Session, footballer_id: int):
    db_footballer = get_footballer(db, footballer_id)
    if not db_footballer:
        return None
    db.delete(db_footballer)
    db.commit()
    return db_footballer



def get_fb_alias(db:Session,alias:str):
    print(alias)
    return db.query(models.footballers).filter(
        models.footballers.alias==alias
    ).all()


def create_animal(db: Session, animal: schemas.animalcreate):
    db_animal = models.animals(**animal.model_dump())
    db.add(db_animal)
    db.commit()
    db.refresh(db_animal)
    return db_animal

def get_animals(db: Session):
    return db.query(models.animals).all()

def get_animal(db: Session, animal_id: int):
    return db.query(models.animals).filter(
        models.animals.id == animal_id
    ).first()

def update_animal(db: Session, animal_id: int, animal: schemas.animalcreate):
    db_animal = get_animal(db, animal_id)
    if not db_animal:
        return None
    db_animal.name = animal.name
    db_animal.category=animal.category
    db_animal.height=animal.height
    db_animal.weight=animal.weight

    db.commit()
    db.refresh(db_animal)
    return db_animal

def delete_animal(db: Session, animal_id: int):
    db_animal = get_animal(db, animal_id)
    if not db_animal:
        return None
    db.delete(db_animal)
    db.commit()
    return db_animal



def get_animal_by_weight(db:Session,weight:int):
    print(weight)
    return db.query(models.animals).filter(
        models.animals.weight==weight
    ).all()


def create_singer(db: Session, singer: schemas.singercreate):
    db_singer = models.singers(**singer.model_dump())
    db.add(db_singer)
    db.commit()
    db.refresh(db_singer)
    return db_singer

def get_singers(db: Session):
    return db.query(models.singers).all()

def get_singer(db: Session, singer_id: int):
    return db.query(models.singers).filter(
        models.singers.id == singer_id
    ).first()

def update_singer(db: Session, singer_id: int, singer: schemas.singercreate):
    db_singer = get_singer(db, singer_id)
    if not db_singer:
        return None
    db_singer.name = singer.name
    db_singer.topsong=singer.topsong
    db_singer.awards=singer.awards
    db_singer.location=singer.location

    db.commit()
    db.refresh(db_singer)
    return db_singer

def delete_singer(db: Session, singer_id: int):
    db_singer = get_singer(db, singer_id)
    if not db_singer:
        return None
    db.delete(db_singer)
    db.commit()
    return db_singer



def get_singer_by_topsong(db:Session,topsong:str):
    print(topsong)
    return db.query(models.singers).filter(
        models.singers.topsong==topsong
    ).all()