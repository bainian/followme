from ghost import Ghost
from ghost import Session

ghost = Ghost()
se = Session(ghost, display=True)
se.open('http://www.baidu.com')
