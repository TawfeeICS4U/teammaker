from flask import Flask, request, render_template
import random
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']

    l = text.split('\n')
    l = clean_list(l)
    random.shuffle(l)

    radio_buttons = request.form['options']
    if radio_buttons == 'option1':
    	x = int(request.form['students_number'])
    	groups = students_per_group(x, l)
    elif radio_buttons == 'option2':
    	x = int(request.form['groups_number'])
    	groups = number_of_groups(x, l)

    
    return render_template('index.html', groups=groups)

def number_of_groups(n, l): #n is the number of groups desired,
    d = math.ceil(len(l)/n)
    return students_per_group(d, l)

def students_per_group(n, l): #n is the number of students per group desired
    return [l[x:x+n] for x in range(0, len(l), n)]

def clean_list(l):
	return [name for name in l if name not in ['', '\r', '\n', '\r\n']]