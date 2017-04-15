from flask import *
from helper_function import *
#import pdb


login = Blueprint('login', __name__, template_folder='templates')

@login.route('/login', methods=['GET', 'POST'])
def login_route():
	# login information already been given
	status=(1,'')
	print("login")
	#pdb.set_trace()
	if request.method == 'POST':
		# check if valid
		query_username = request.form['username']
		print(query_username)
		query_password = request.form['password']
		status = login_validation(query_username,query_password)#login_validation user_operation_helper
		#pdb.set_trace()
	# first check if its valid
	# if valid, give it a session
		if status[0] == 1:
			session['username'] = request.form['username']
			session['firstname'],session['lastname'] = get_fullname(request.form['username'])
			print(session['firstname'])
			return redirect(url_for('projects.projects_route'))
		else:
			return render_template("login.html", status=status)
	# login information not given, method is a GET
	else: # request.method == 'GET'
		return render_template("login.html", status=status)
