from dataclasses import dataclass


@dataclass
class User:
    firstname: str
    lastname: str
    username: str
    password1: str
    password2: str


Bilbo = User(
    firstname='Bilbo',
    lastname='Baggins',
    username='bilbob',
    password1='S3l3ctS0methingStr0ng5AsP@ssword',
    password2='S3l3ctS0methingStr0ng5AsP@ssword'
)
