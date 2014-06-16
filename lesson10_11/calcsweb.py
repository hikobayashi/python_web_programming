from bottle import route,template,run,static_file
@route('/')
def index():
	return template('./login.html')

@route('/health-graph.html', 'GET')
@route('/health-graph.html', 'POST')
def health_graph():
	return template('./health-graph.html', bmi=str(bmi(171.0,72.5)))

@route('/health-form.html','GET')
@route('/health-form.html','POST')
def health_form():
	return template('./health-form.html')

@route('/settings.html','GET')
@route('/settings.html','POST')
def settings():
	return template('./settings.html')

@route('/login.html', 'GET')
@route('/login.html', 'POST')
def login():
	return template('./login.html')

@route('/signup.html','GET')
@route('/signup.html','POST')
def signup():
	return template('./signup.html')

@route('/welcome.html','GET')
@route('/welcome.html','POST')
def welcome():
	return template('./welcome.html')


@route('/help.html')
def help_page():
	return template('./help.html')

@route('/info.html')
def info_page():
	return template('./info.html')

@route('/info-notlogin.html')
def infonotlogin_page():
	return template('./info-notlogin.html')

@route('/css/<filename:re:.*\.css>')
def css_file(filename):
        return static_file(filename, root='css',mimetype='text/css')

@route('/js/<filename:re:.*\.js>')
def js_file(filename):
	return static_file(filename, root='js',mimetype='text/javascript')

@route('/images/<filename:re:.*\.png>')
def image_file(filename):
	return static_file(filename, root='images',mimetype='image/png')

def bmi(h,w):
	height=h/100
	weight=w
	return weight / (height * height)
	
run(host='localhost', port=8080)
