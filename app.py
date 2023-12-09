
from flask import Flask, render_template,redirect ,request,send_file,session, url_for , g ,Response

app = Flask(__name__,
           	template_folder='templates',  
 	          static_folder='static' 
           )
@app.route("/",methods = ['GET','POST'])
def home():
  return render_template("index.html")

def location():
  return render_template("location.html")



if __name__ == '__main__':
  app.run(host='0.0.0.0',port = 5000,debug= True)
                                                           
