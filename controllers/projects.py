from flask import *
from extensions import connect_to_database
#import error_handler
from helper_function import *

projects = Blueprint('projects', __name__, template_folder='templates')

@projects.route('/projects/edit',methods = ['GET','POST'])
def projects_edit_route():
	if request.method == 'GET':
		if session.get('username'):  
			username = session['username']
			current_project_list = get_current_project_list()
			past_project_list = get_past_project_list()
			edit =True
			return render_template("projects.html",current_project_list = current_project_list, past_project_list = past_project_list, edit = edit)
		else: #type the url to view the page
			return redirect(url_for('login.login_route'))
	else:  #Post
		if not session.get('username'):
			return redirect(url_for('login.login_route'))
		if(request.form['op'] == "delete"):
			projectid = str(request.form['projectid'])
			status = delete_project(projectid)
			if status == False:
				print("Error detected when deleting albums")
			return redirect(url_for('projects.projects_edit_route')) #method is get
		elif(request.form['op'] == "add"):
			topic = str(request.form['Topic'])
			abstract = str(request.form['Abstract'])
			website = str(request.form['Website'])
			status = str(request.form['Status'])
			add_status = add_project(topic,abstract,website,status)
			if status ==False:
				print("Error detected when deleting albums")
			return redirect(url_for('projects.projects_edit_route'))







@projects.route('/projects', methods=['GET','POST'])
def projects_route():
	current_project_list = get_current_project_list()
	past_project_list = get_past_project_list()
	edit = False
	if 'username' not in session:
		return redirect(url_for('login.login_route'))
	return render_template("projects.html", current_project_list = current_project_list, past_project_list = past_project_list, edit = edit)