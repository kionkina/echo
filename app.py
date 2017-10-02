"""
Karina Ionkina
SoftDev1 pd7
HW #06 -- Echo Echo Echo
2017-10-02
"""

from flask import Flask, request, render_template

app = Flask(__name__) #create instance of class 
    
@app.route("/")
def hello():

#--------------------------- VARIOUS PRINT STATEMENTS -------------------------------------------
    print "PRINTING APP..."
    print app # <Flask 'app'>


    print "PRINTING request.headers..."
    print request.headers 
    # User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 

    print "PRINTING request.method..."
    print request.method #GET

    print "PRINTING request.args..."
    print request.args #ImmutableMultiDict([('lastname', u'ion'), ('firstname', u'karina')])
    
    print "PRINTING request.args[firstname]"
    print request.args['firstname'] #karina

#------------------------------------------------------------------------------------------------


    # recording method to call in Jinja2
    r_method = request.method

    # recording first and last name, and whether or not they exist
    try:
        first_name = request.args["firstname"]
        last_name = request.args["lastname"]
        name_exists = True
    except:
        name_exists = False
        first_name = ""
        last_name = ""
        print "cannot store name"
    return render_template('test.html', first = first_name, last = last_name + ".", r_method = r_method, name_exists = name_exists)

if __name__=="__main__":
    app.debug = True
    app.run()

