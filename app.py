from flask import Flask, request, render_template

app = Flask(__name__) #create instance of class 


@app.route("/")
def hello():
    print app
    print "***request.headers***"
    print request.headers
    print "***request.method***"
    r_method = request.method
    print "***request.args***"
    print request.args
    print "***request.args[firstname]***"
    try:
        their_name = request.args['firstname']
    except:
        print "cannot store name"
    print "***request.form***"
    print request.form
    return  render_template('test.html', their_name = their_name, r_method = r_method)

if __name__=="__main__":
    app.debug = True
    app.run()

