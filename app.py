## Create a simple flask application

from flask import Flask,render_template


## create the flask app

app=Flask(__name__)

@app.route('/')
def home():
    return "<h2>Hello, World!</h2>"

@app.route('/Welcome')
def Welcome():
    return "Welcome to the Flask Tutorials"

@app.route('/Index')
def Index():
    return render_template('Index.html')

@app.route('/success/<int:score>')
def success(score):
    return "the person is passed and the score is "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "the person has failed and the score is "+str(score)

@app.route('/',methods=['POST','GET'])
def calculate():
    if  request.method=='GET':
        return render_template('calculate.html')
    else:
         maths=float(request.form['maths'])
         science=float(request.form['science'])
         history=float(request.form['history'])

         average_marks=(maths+science+history)/3
         result="" 
         if average_marks>=50:
            result="success"
         else:
            result="fail"
         return render_template('result.html',results=average_marks)




if __name__=='__main__':
    app.run(debug=True)