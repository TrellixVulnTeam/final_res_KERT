from flask import *



logout = Blueprint('logout',  __name__, template_folder='templates')
# name of the blueprint, __name__ arguement
@logout.route('/logout', methods=['GET', 'POST'])
def logout_route():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('projects.projects_route'))


