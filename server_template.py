# Using flask to make an api 
# import necessary libraries and functions 
from flask import Flask, jsonify, request ,render_template
import json
import subprocess
  
# creating a Flask app 
app = Flask(__name__)


@app.route('/form')
def my_form():
    return render_template('formm.html')

@app.route('/form', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        rmtusrname = request.form.get('usrname')
        rmtipadd = request.form['ipadd']
        package = request.form['package']

        print("Remote's username: ","         ---->   ", rmtusrname)
        print("The Remote's IP Address ","     ---->   ", rmtipadd)
        print("Package","   ---->   ", package)

                # For NginX
        gitusrname = request.form.get('gitusrname')
        gitpass = request.form['gitpass']
        giturl = request.form['giturl']

        print("Git Remote's URL: ","         ---->   ", giturl)
        print("Git Remote's Username","     ---->   ", gitusrname)
        print("Git Remote's Password","   ---->   ", gitpass)



        # Running Bash Command

        if package != "nginx":


          toRet = f'''<h1>The Bash Script is running on the server ... </h1>
                  <br><br><h2>Remote's username: <span style="color:red">{rmtusrname}</span></h2>
                  <h2>The Remote's IP Address : <span style="color:red">{rmtipadd}</span></h2>
                  <h2>Package  <span style="color:red">{package}</span> ;)</h2>'''

        else:

          nginxcommand = f"/app/git.sh {giturl} {gitusrname} {gitpass}"
          subprocess.call(nginxcommand,shell=True)

          toRet = f'''
                  <h1>The Bash Script is running on the server ... </h1>
                  <br><br><h2>Remote's username: <span style="color:red">{rmtusrname}</span></h2>
                  <h2>The Remote's IP Address : <span style="color:red">{rmtipadd}</span></h2>
                  <h2>Package  <span style="color:red">{package}</span> ;)</h2>
                  <br><br><h2>Git's username: <span style="color:red">{gitusrname}</span></h2>
                  <h2>Git's URL : <span style="color:red">{giturl}</span></h2>
                  '''


        bashcommand = f"/app/paas.sh {rmtusrname} {rmtipadd} {package}"
        subprocess.call(bashcommand,shell=True)

        return toRet

    return '''<form method="POST">
                  Language: <input type="text" name="language"><br>
                  Framework: <input type="text" name="framework"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''
  
  
# driver function 
if __name__ == '__main__': 
  
    # app.run(debug = True) 
    app.run(debug = True, host= '0.0.0.0') 