# way to upload image
# way to save image
# function to make prediction
#show the result

import os
from flask import Flask
from flask import request
from flask import render_template


app=Flask(__name__)

UPLOAD_FOLDER="C:/Users/Ankan/Desktop/Github/covid19xray/webapp/static/image"
# "/" means web address first page
@app.route("/",methods=["GET","POST"])

def upload_predict():
	if request.method=="POST":
		image_file=request.files["image"]
		if image_file:
			image_loc=os.path.join(UPLOAD_FOLDER,image_file.filename)
			image_file.save(image_loc)
			return render_template("index.html",prediction=1)
	return render_template("index.html",prediction=0)







if __name__=="__main__":
	app.run(port=12000, debug=True)






