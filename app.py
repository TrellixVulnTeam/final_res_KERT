from flask import *
import extensions
import controllers
import config


# Initialize Flask app with the template folder address
app = Flask(__name__, template_folder='templates')
#url_pre='/9e5upo9n/p2'
app.secret_key="b'~\xddKF\xfa\xa9\xf0\x86X\x88nU\xbcN;d\x0c(\xb0\x9d>2@\x16'"
# Register the controllers
app.register_blueprint(controllers.project)
app.register_blueprint(controllers.projects)
app.register_blueprint(controllers.login)
app.register_blueprint(controllers.logout)

# configurations
# app.config['IMAGE_FOLDER'] = os.path.join(sys.path[0],'static','images','images')
# Listen on external IPs
# For us, listen to port 3000 so you can just run 'python app.py' to start the server
if __name__ == '__main__':
    # listen on external IPs
    # pdb.set_trace()
    app.run(host=config.env['host'], port=config.env['port'], debug=True)
