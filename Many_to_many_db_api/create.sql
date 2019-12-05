CREATE TABLE Child ( id INTEGER PRIMARY KEY AUTOINCREMENT, Name VARCHAR(255), lastname VARCHAR(255) );
CREATE TABLE Parent ( id INTEGER PRIMARY KEY AUTOINCREMENT, 
	name VARCHAR(255), lastname VARCHAR(255) );
CREATE TABLE Parent_child_table ( child_id INTEGER, parent_id INTEGER,  
	PRIMARY KEY(child_id, parent_id) FOREIGN KEY(parent_id) REFERENCES parent(id), 
	FOREIGN KEY(child_id) REFERENCES child(id));


