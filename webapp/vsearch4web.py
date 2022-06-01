from vsearch import search4letters
from flask import Flask,render_template,request,redirect

# request object contains a dictionary attribute called form that provides access to a HTML form's data posted from the browser .

app=Flask(__name__) # Crete an instance of Flask object and assign it to app

@app.route('/') # This is the URL and also a function decorator
# A function decorator adjuts the behaviour of an exixsting function without changing the functions code

# This is jus a regular python function which, when invoked returns a string to its caller(note: '->str' annotation)
def hello()-> '302':
    return redirect('/entry') # Instruct the browser to redirect to URL of entry

@app.route('/search4',methods=['POST']) # A second decorator sets up the "/search4" URL
# The "/search4" now supports only POST method for multiple method support we can write methods=['POST','GET'] so on...
def do_search()->'html':
    phrase=request.form['phrase'] #assign HTML forms data to new variables
    letters=request.form['letters'] #assign HTML forms data to new variables
    title='Here are your results'
    Result=str(search4letters(phrase,letters))
    return render_template('results.html',the_title=title,the_phrase=phrase,the_letters=letters,the_results=Result)


''' While observing the URL we see 127.0.0.1:5000 here 127.0.0.1 is loopback address or commonly called local host as flask does not use out IP address and instead connects its test web server to the internet's loopback address. '''
''' Here :5000 identifies the protocol port number your web server is running on we can change it but by default for flask it is :5000 and should not be changed if not have a valid reason. '''

@app.route('/entry')
def entry_page()->'html':
    return render_template('entry.html', the_title='welcome to search4letters on the web!')

if __name__=='__main__':
    app.run(debug=True) # Asks the web app to start running

# HTTP is communication protocol that lets web browser and servers communicate. There are handful of HTTP methods, Eg: GET,POST.
# 1. The GET method: Browser typically uses this method to request a resource from the web server,this is flask's default HTTp method.
# 2. The POST method: This method allows server to send data to the server over HTTP and is closely associated with HTML<form> tag.
