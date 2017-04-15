# this script hases the filename while load the file into the database
import hashlib
import os, sys
# import pdb
from extensions import connect_to_database
from flask import current_app as app


# sys.path.append(os.path.join(sys.path[0],'static','images','images'))

# global varibles, and add image folder path
sys.path.append(os.path.join(sys.path[0],'static','images'))
IMAGE_FOLDER = sys.path[-1]
VALID_FORMAT = set(["png","jpg","bmp","gif"])

def format_check(filename):
# this function checks valid formats
	return "." in filename and filename.rsplit('.')[0].lower() in VALID_FORMAT



def add_project_image(filename,projectid):
    db = connect_to_database()
    cur = db.cursor()
    pic_format = filename.rsplit('.')[0].lower() 
    name = filename.rsplit('.')[1]
    command1 = "INSERT INTO Picture VALUES('"+name+"','"+pic_format+"')"
    cur.execute(command1)
    command2 = "INSERT INTO PictureContain VALUES('"+projectid+"','"+name+"')"
    cur.execute(command2)
    return True

