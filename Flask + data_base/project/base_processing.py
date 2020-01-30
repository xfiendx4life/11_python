from .models import *

def register(username, password, email):
    if not User.query.filter_by(username=username).first():
        u = User(username=username, email=email, password=password)
        db.session.add(u)
        db.session.commit()
        return True
    else:
        return 'User exists'

def authenticate(username, password):
	u = User.query.filter_by(username=username).first()
	return u and u.password == password

def delete_user(username):
	u = User.query.filter_by(username=username).first()
	if u:
		db.session.delete(u)
		db.session.commit()
		return True
	return False

def get_user_id(username):
	u = User.query.filter_by(username=username).first()
	if u:
		return u.id
	return False


def add_note(head, body, username):
	u = User.query.filter_by(username=username).first()
	if u:
		note = Note(head=head, body=body)
		u.notes.append(note)
		db.session.commit()
		return True
	else:
		return False

def get_note(head, username):
	'''
	note = Note.query.filter_by(head=head, user=username).first()
	return note if note else False

	'''
	user_id = get_user_id(username)
	if user_id:
		note = Note.query.filter_by(head=head, user_id=user_id).first()
		return note
	return False

def get_note_list(username):
	u = User.query.filter_by(username=username).first()
	return u.notes if u	else False
	

def edit_note(username, head, new_text):
	note = get_note(head,username)
	note.body = new_text
	db.session.commit()

