from flask import Flask,send_file,render_template
from plotdata import regression_plot
from plotdata import create_index
import os

cwd= os.getcwd()
path = os.path.join(cwd,"templates")
os.mkdir(path)

app = Flask(__name__)


@app.route('/', methods=['GET'] )
def regr_plot():
    image = regression_plot()
    return send_file(image,attachment_filename='Weather.png',mimetype='image/png')



@app.route("/report")
def index():
    url=create_index()
    return render_template("Weather_report.html",url=url)



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=False)