from flask import *
from helper_function import *
from project_helper import *
from extensions import connect_to_database
import photo_operation_helper as photo_opr
import os
#import pdb
import error_handler

project = Blueprint('project', __name__, template_folder = 'templates')


@project.route('/project/edit',methods = ['GET','POST'])
def project_edit_route():
	edit = True
	projectid = str(request.args.get('projectid')) #get from url
	if 'username' not in session:
		return redirect(url_for('login.login_route'))
	if request.method == "GET":
		project_info = get_project_info(projectid)
		return render_template('project.html',project_info = project_info, edit=edit, projectid = projectid)
	else: #post
		project_info = get_project_info(projectid)
		if (request.form['op']=="add_pic"):
			if 'file' not in request.files:
				print("No file part!")
				return redirect(url_for('project.project_edit_route', projectid = projectid))
			file = request.files['file']
			if file.filename == '':
				print("No selected file!")
				return redirect(url_for('project.project_edit_route', projectid = projectid))
			if file and photo_opr.pic_format_check(file.filename):
				filename = str(file.filename)
				# pdb.set_trace()
				try: # save before changing its name 
					file.save(os.path.join(photo_opr.IMAGE_FOLDER, filename))
					photo_opr.add_project_image(filename,projectid)
				except:
					print("Error happened when hashing or saving uploaded image")
			return redirect(url_for('project.project_edit_route', projectid = projectid))
		elif(request.form['op']=="add_pub"):
			pubname = request.form['pubname']
			pubtime = request.form['pubtime']
			information = request.form['other_info']
			people = request.form['pub_people']  #use coma to seperate
			add_status = add_publication(pubname,pubtime,information,projectid,people)
			if add_status:
				return redirect(url_for('project.project_edit_route',projectid = projectid))
			else:
				print("add publication failed")
		elif(request.form['op']=="delete_pub"):
			publicationid = str(request.form['Publicationid'])
			delete_status = delete_publication(publicationid,projectid)
			if delete_status:
				return redirect(url_for('project.project_edit_route',projectid = projectid))
			else:
				print("delete publication failed")

		elif(request.form['op'] == "delete_pic"):
			pictureid = request.form['Pictureid']
			delete_status = delete_picture(pictureid,projectid)
			if delete_status:
				return redirect(url_for('project.project_edit_route',projectid = projectid))
			else:
				print("delete picture failed")


@project.route('/project')
def project_route():
	edit = False
	projectid = str(request.args.get('projectid')) #get from url
	#if 'username' not in session:
	#	return redirect(url_for('login.login_route'))
	project_info = get_project_info(projectid)
	return render_template('project.html',project_info = project_info,projectid = projectid)









