from db import *
from datetime import datetime

def authenticate(session, login, password):
	p = session.query(Person).filter(Person.login == login).first()
	if p and p.password == password:
		s = UserSession()
		p.usersessions.append(s)
		session.add(s)
		session.commit()
		return True
	return False

def register(session, login, password, info):
	p = session.query(Person).filter(Person.login == login).first()
	if not p:
		p = Person(login, password, info)
		session.add(p)
		session.commit()
		return True
	return False

def logout(session, login):
	p = session.query(Person).filter(Person.login == login).first()
	if p:
		s = session.query(UserSession).filter(UserSession.user_id == p.id).all()[-1]
		s.finish_time = datetime.now()
		session.commit()
		return True
	return False

