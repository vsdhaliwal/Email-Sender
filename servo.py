from crypt import methods
from flask import Flask,render_template,request
import os
import em

app = Flask(__name__)
dir = os.path.dirname(os.path.realpath(__file__))+"/data/"
app.config['UPLOAD_PATH'] = dir

@app.route("/",methods=["GET","POST"])
def upload():
    if request.method == 'POST':
        mail = request.form.get("email_id")
        subj = request.form.get("subject")
        bod = request.form.get("body")
        f = request.files['file_name'] 
        f.save(os.path.join(app.config['UPLOAD_PATH'],f.filename))
        em.email(mail, subj, bod, f.filename)
        os.remove(dir+f.filename)
        return render_template("front.html")
    return render_template("front.html")

if __name__ == "__main__" :
    app.run(debug=True)