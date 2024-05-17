from dataclasses import dataclass


@dataclass
class User:
    firstname: str
    lastname: str
    username: str
    password1: str
    password2: str


bilbo = User(
    firstname='bilbo',
    lastname='Baggins',
    username='bilbob',
    password1='S3l3ctS0methingStr0ng5AsP@ssword',
    password2='S3l3ctS0methingStr0ng5AsP@ssword'
)

jdoe = User(
    firstname='John',
    lastname='Doe',
    username='jdoe',
    password1='Th1s!sz3nu3Passv0rd',
    password2='Th1s!sz3nu3Passv0rd'
)
