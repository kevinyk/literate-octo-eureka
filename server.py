from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key="ActualSecretKey"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blah', methods=['GET',"POST"])
def blah():
    print(request.form)
    # dump(session)
    session['name'] = request.form['name']
    session['location'] = request.form.get('location')
    session['language'] = request.form.get('language')
    session['comment'] = request.form.get('comment')
    return redirect('/result')

@app.route('/result')
def result():
    print('hit')
    name = session['name']
    location = session['location']
    language = session['language']
    comment = session['comment']
    return render_template('results.html', name=name, location=location, language=language, comment=comment)

@app.route('/danger')
def danger():
    print('user tried to enter dangerzone')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)