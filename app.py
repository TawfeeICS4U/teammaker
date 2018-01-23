from random import shuffle
from flask import Flask, request, render_template, flash, redirect, url_for
from classlists import *
from helper import *

app = Flask(__name__)
app.secret_key='test_secret_key'

@app.route('/period1')
def period1():
	return render_template('index.html', student_names=classlist_period1)

@app.route('/period2')
def period2():
	return render_template('index.html', student_names=classlist_period2)

@app.route('/period3')
def period3():
	return render_template('index.html', student_names=classlist_period3)


@app.route('/period1', methods=['POST'])
def form_period1():
    text = request.form['text']

    l = text.split('\n')
    l = clean_list(l)
    shuffle(l)

    radio_buttons = request.form['options']
    if radio_buttons == 'option1':
        x = int(request.form['students_number'])
        if x > len(l):
            error = 'Invalid input. Input greater than number of students.'
            flash(error)
            return redirect(url_for('period1'))
        groups = students_per_group(x, l)
    elif radio_buttons == 'option2':
        x = int(request.form['groups_number'])
        if x > len(l):
            error = 'Invalid input. Input greater than number of students.'
            flash(error)
            return redirect(url_for('period1'))
        groups = number_of_groups(x, l)
        
    return render_template('index.html', groups=groups)

@app.route('/period2', methods=['POST'])
def form_period2():
    text = request.form['text']

    l = text.split('\n')
    l = clean_list(l)
    shuffle(l)

    radio_buttons = request.form['options']
    if radio_buttons == 'option1':
        x = int(request.form['students_number'])
        if x > len(l):
            error = 'Invalid input. Input greater than number of students.'
            flash(error)
            return redirect(url_for('period2'))
        groups = students_per_group(x, l)
    elif radio_buttons == 'option2':
        x = int(request.form['groups_number'])
        if x > len(l):
            error = 'Invalid input. Input greater than number of students.'
            flash(error)
            return redirect(url_for('period2'))
        groups = number_of_groups(x, l)

    return render_template('index.html', groups=groups)

@app.route('/period3', methods=['POST'])
def form_period3():
    text = request.form['text']

    l = text.split('\n')
    l = clean_list(l)
    shuffle(l)

    print(l)

    radio_buttons = request.form['options']
    if radio_buttons == 'option1':
        x = int(request.form['students_number'])
        if x > len(l):
            error = 'Invalid input. Input greater than number of students.'
            flash(error)
            return redirect(url_for('period3'))
        groups = students_per_group(x, l)
    elif radio_buttons == 'option2':
        x = int(request.form['groups_number'])
        if x > len(l):
            error = 'Invalid input. Input greater than number of students.'
            flash(error)
            return redirect(url_for('period3'))
        groups = number_of_groups(x, l)

    return render_template('index.html', groups=groups)
