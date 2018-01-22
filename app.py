from flask import Flask, request, render_template
import openpyxl
import random

app = Flask(__name__)

classlist_period1 = 'Danya Al-Hussieni\nAlexa Au\nDavid Baranov\nAmira Bendaas\nAli Bensaci\nIris Diep\nIman Fatima\nJaime Fleming\nDavid Haighton\nTawfiqul Haque\nAdam Hifato\nBreanna Hillier\nCole Horton\nNathan Huynh\nPreetkiran Kaur\nBenjamin Lieu\nKoreena McCulloch\nEmily Milshtein\nDuaa Osman\nKehan Rattani\nSarah Ross\nTina Tran\nDavid Wallace\nJustin Weiner\nJacob Zachariah'
classlist_period2 = 'Abigail Awrey\nFaith Babalola\nMohamad-Zouheir Bayaa\nEmily Boland\nNeeharika Boni Bangari\nAhmed Hafez\nGrace Kim\nAllison Kuseler\nBenjamin Le\nAlexander McNamee\nTarnia Muralitharan\nAutumn Parry\nMakayla Perry\nLandon Prosty\nAliya Rattani\nMuhammad Raza\nEric Robert\nArianna Seeley\nSovyanna Sreng-Pech\nAbhiram Sureshkumar\nAdora Tran\nJamie Wootton'

classlist_period3 = 'Omar Abdul\nIzaak Aidid\nNeeharika Boni Bangari\nLuna Bukvic\nEthan Da Silveira\nJillian Desjardins\nDavis Dewan\nJoshua Flett\nMalia Ghadban\nAmine Hammoud\nSerena Haslip\nVicky Huynh\nSahil Lal\nAudrey Lun\nCaitlin McMann\nAlexander McNamee\nBrooklyn Pike\nAliya Rattani\nMuhammad Raza\nJodi Ruddick\nSavida Uddin\nDarren Wallace\nMegan Winger\nAdel Yasin\nMaryam Yassin\nJessica Yeung'

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
@app.route('/period2', methods=['POST'])
@app.route('/period3', methods=['POST'])
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
    d = (len(l)//n)
    return students_per_group(d, l)

def students_per_group(n, l): #n is the number of students per group desired
    return [l[x:x+n] for x in range(0, len(l), n)]

def clean_list(l):
	return [name for name in l if name not in ['', '\r', '\n', '\r\n']]

def clean_name(name):
	temp = name.split(',')
	return ' '.join(reversed(temp))