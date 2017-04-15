from extensions import connect_to_database
from flask import *
#import pdb

# this module checks input and redirect errors into error pages
# this script is the user handler for errors on created pages
def username_check(username): # check if username exist
	db = connect_to_database()
	cur = db.cursor()
	command = "SELECT* FROM User WHERE username='"+username+"'"
	status = cur.execute(command)
	if status <= 0:
		return False
	return True

def albumid_check(albumid):
	db = connect_to_database()
	cur = db.cursor()
	command = "SELECT* FROM Album WHERE albumid='"+albumid+"'"
	status = cur.execute(command)
	if status <= 0:
		return False
	return True

def picid_check(picid):
	db = connect_to_database()
	cur = db.cursor()
	command = "SELECT* FROM Contain WHERE picid='"+picid+"'"
	status = cur.execute(command)
	if status <= 0:
		return False
	return True

def error_check(arg,check_function):

	if check_function(arg) == False:
		# pdb.set_trace()
		abort(404)
	return False
