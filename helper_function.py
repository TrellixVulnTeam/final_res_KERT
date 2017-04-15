from flask import *
from extensions import connect_to_database
import hashlib
from error_handler import *
import pdb



def get_fullname(username):
	db = connect_to_database()
	cur = db.cursor()
	command = "SELECT firstname,lastname FROM User WHERE username='" + username + "'"
	cur.execute(command)
	fullname = cur.fetchall() #return a list of dictionary
	return fullname[0]['firstname'],fullname[0]['lastname']

def get_current_project_list():
	db = connect_to_database()
	cur = db.cursor()
	command = "SELECT * FROM Project WHERE status='Current'"
	cur.execute(command)
	project_list = cur.fetchall()
	return project_list

def get_past_project_list():
	db = connect_to_database()
	cur = db.cursor()
	command = "SELECT * FROM Project WHERE status='Past'"
	cur.execute(command)
	project_list = cur.fetchall()
	return project_list

def check_password(username,ori_password):
	# pdb.set_trace()
	db = connect_to_database()
	cur = db.cursor()
	command = "SELECT password FROM User WHERE username='" + username + "'"
	cur.execute(command)
	correct_password = cur.fetchall()[0]['password']

	if correct_password!=ori_password:
		return False
	else:
		return True
def username_check(username):

	db = connect_to_database()
	cur = db.cursor()
	command = "SELECT username FROM User "
	cur.execute(command)
	username_dict = cur.fetchall() #list of dictionary
	username_list = []
	print(username_list)
	for item in username_dict:
		username_list.append(item['username'])
	if username not in username_list:
		return False
	else:
		return True
def login_validation(username,ori_password):
	errormessage=""
	if username == '' and ori_password == '':
		flag=0
		errormessage += "Username may not be left blank,"
		errormessage += "Password may not be left blank"
		return flag, errormessage
	if username == '' and ori_password !='':
		flag=0
		errormessage += "Username may not be left blank"
		return flag, errormessage
	if username !='' and ori_password == '':
		if not username_check(username):
			flag=0
			errormessage += "Username does not exist,"
			errormessage += "Password may not be left blank"  # invalid username needs modification
			return flag, errormessage
		else:
			flag=0
			errormessage += "Password may not be left blank"
			return flag, errormessage
	if username !='' and ori_password != '':

		if not username_check(username):
			flag=0
			errormessage += "Username does not exist" # invalid username needs modification
			print(flag)
			return flag, errormessage
		else:
			if check_password(username,ori_password):
				flag=1
				errormessage=''
				return flag, errormessage # valid
			else:
				flag=0
				errormessage+="Password is incorrect for the specified username"
				return flag, errormessage

def delete_project(project_id):
	db = connect_to_database()
	cur = db.cursor()
	command = "DELETE FROM Project WHERE Projectid ='" + project_id + "'"
	cur.execute(command)
	return True

def add_project(topic,abstract,website,status):
	db = connect_to_database()
	cur = db.cursor()
	command = "INSERT INTO Project(Topic,Abstract,Website,Status) VALUES(" + "'" + topic+ "','"+ abstract + "','"+ website +"','"+ status+"')" 
	cur.execute(command)
	return True
	
