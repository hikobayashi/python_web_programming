from bottle import route, run
@route('/')
@route('/hello/<name>')
def greet(name='hoge'):
    return template('Hello World {{name}}!', name=name)

run(host='localhost', port=8080, debug=True)