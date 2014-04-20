from bottle import route, run, template, static_file, request
@route('/hello')
def hello():
    return "Hello World!"

'''@route('/hello/<name>')
def hello_name(name):
    return template("<b>Hello {{name}} </b>", name=name)
'''

@route('/static/<filename>')
def display_file(filename):
    return static_file(filename, root='/Users/hikobayashi/Dropbox/BBT_UNIV_LECTURES/pyworks/')

@route('/my_ip')
def show_ip():
    ip = request.environ.get('REMOTE_ADDR')
    return template("Your IP is: {{ip}}", ip=ip)

@route('/hello')
@route('/hello/<name>')
def hello(name='World'):
    return template('hello_template', name=name)


run(host='localhost', port=8080, debug=True)

