from flask import Flask, request, render_template

app = Flask(__name__) #create instance of class 


@app.route("/")
def hello():
    print app
    print "request.headers"
    print request.headers
    print "request.method"
    print request.method
    print "request.args"
    print request.args
    print "request.form"
    print request.form
    return  render_template('test.html') 


if __name__=="__main__":
    app.debug = True
    app.run()

