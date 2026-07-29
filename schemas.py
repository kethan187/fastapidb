from pydantic import BaseModel
class criminalcreate (BaseModel):
    name:str
    gender:str
    location:str
    alias:str

class criminalresponse (criminalcreate):
    id:int

    model_config = {
        "from_attributes":True
    }
class cricketercreate (BaseModel):
    name:str
    category:str
    iplteam:str
    alias:str

class cricketerresponse (cricketercreate):
    id:int

    model_config = {
        "from_attributes":True
    }

class footballercreate (BaseModel):
    name:str
    category:str
    teamname:str
    alias:str

class footballerresponse (footballercreate):
    id:int

    model_config = {
        "from_attributes":True
    }

class animalcreate (BaseModel):
    name:str
    category:str
    height:int
    weight:int

class animalresponse (animalcreate):
    id:int

    model_config = {
        "from_attributes":True
    }

class singercreate (BaseModel):
    name:str
    topsong:str
    awards:str
    location:str

class singerresponse (singercreate):
    id:int

    model_config = {
        "from_attributes":True
    }