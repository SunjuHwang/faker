# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import random
import csv
from faker import Faker

app = Flask(__name__)
fake = Faker('ko_KR')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/result")
def result():
    name1 = request.args.get('name1')
    name2 = request.args.get('name2')
    match = random.randrange(50,101)
    #'names.csv'라는 파일을 생성한다. -> 저장
    f = open('names.csv','a')
    a = csv.writer(f)
    a.writerow([name1,name2])
    f.close()
    return render_template('result.html', name1=name1, name2=name2, match=match)

@app.route("/admin")
def admin():
    #names에 들어가 있는 모든 이름을 출력한다.
    f = open('names.csv', 'r')
    rr = csv.reader(f)
    names = rr
    return render_template('admin.html',names=names)
    
@app.route("/ffaker")
def ffaker():
    name = fake.name()
    job=fake.job()
    address = fake.address()
    text = fake.text()
    
    return render_template('ffaker.html', name=name, address=address, text=text, job=job)

#app.run(host='0.0.0.0', port='8080', debug=True)