##################################################
# Updated version that is used with app2.py
##################################################

from flask import Flask, render_template, request
import app2

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/netcheck", methods=['POST'])
def result():
    if request.method == 'POST':
        zip = request.form['zip_code']
        zip = app2.Get_weather_data(zip)
        zip = zip.lookup()
        print(zip)
        zip1 = request.form['zip_code']

        output = app2.Parse_output(zip)
        output = output.printed_output()
        print(app2.Parse_output(output))

    return render_template("result.html", variable=output[0], variable2=output[1], variable3=output[2], variable4=output[3], variable5=output[4], variable6=zip1)


if __name__ == '__main__':
    app.debug = True
app.run()