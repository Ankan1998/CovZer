# way to upload image
# way to save image
# function to make prediction
#show the result

import os
from flask import Flask
from flask import request
from flask import render_template


app=Flask(__name__)


# "/" means web address first page
@app.route("/",methods=["GET","POST"])

def upload_predict():
	predi="Covid detected"
	return render_template("index.html",prediction=predi)







if __name__=="__main__":
	app.run(port=12000, debug=True)






