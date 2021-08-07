# way to upload image
# way to save image
# function to make prediction
#show the result

import os
from flask import Flask
from flask import request
from flask import render_template
from inference import *


app=Flask(__name__)

UPLOAD_FOLDER=r"C:\Users\Ankan\Desktop\Github\CovZer\webapp\static\image"
# "/" means web address first page
@app.route("/",methods=["GET","POST"])

def upload_predict():
	if request.method=="POST":
		image_file=request.files["image"]
		if image_file:
			image_loc=os.path.join(UPLOAD_FOLDER,image_file.filename)
			print(image_loc)
			image_file.save(image_loc)
			prediction = prediction_fn(image_loc)
			return render_template("index.html",prediction=prediction)
	return render_template("index.html",prediction="No Image Uploaded")







if __name__=="__main__":
	app.run(port=12000, debug=True)






