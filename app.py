from flask import Flask,render_template


app = Flask(__name__)
@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/ourclients.html')
def ourclients():
    return render_template('ourclients.html')

@app.route('/projects.html')
def projects():
    return render_template('projects.html')

@app.route('/gallery.html')
def gallery():
    return render_template('gallery.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/malls.html')
def malls():
    return render_template('malls.html')

@app.route('/houseprojects.html')
def houseprojects():
    return render_template('houseprojects.html')

@app.route('/hospitalprojects.html')
def hospitalprojects():
    return render_template('hospitalprojects.html')

@app.route('/hotelsprojects.html')
def hotelsprojects():
    return render_template('hotelsprojects.html')

@app.route('/industriesprojects.html')
def industriesprojects():
    return render_template('industriesprojects.html')

@app.route('/firefight.html')
def firefight():
    return render_template('firefight.html')

@app.route('/firedetection.html')
def firedetection():
    return render_template('firedetection.html')

@app.route('/sanitary.html')
def sanitary():
    return render_template('sanitary.html')

@app.route('/maintance.html')
def maintance():
    return render_template('maintance.html')

@app.route('/design.html')
def design():
    return render_template('design.html')

@app.route('/sites.html')
def sites():
    return render_template('sites.html')

if __name__== '__main__':
    app.run(debug=True)