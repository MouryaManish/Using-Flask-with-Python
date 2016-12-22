from flask import Flask
from flask import render_template
from flask import request
import weatherreport
city_name=""
country=""
#from weatherreport import city_information()
#import venv/local/lib/python2.7/site-packages/flask/templating
app=Flask("hello.py")
@app.route('/')
def homepage():
	return render_template("index.html") 

"""@app.route('/callfromsubmit/',methods=["POST"])
def callfromsubmit():
#	return render_template("index2.html")
	cityname=request.form["cityname"]
	return render_template("index2.html",a=l[0],b=l[1])"""

"""@app.route("/webrequest/",methods=["GET","POST"])
def webrequest():
	if request.method =="POST":
		print 1
	if request.method == "GET":
		print 2"""

@app.route("/city_information1/",methods=["GET","POST"])
def city_information1()	:
	if request.method=="POST" :
		global city_name
		global country

		city_name=request.form["cityname"]
		l=weatherreport.initialization(city_name)
	#-----------------CURRENT CITY DATA--------------------------------
		return	render_template("index2.html",time=l[0],city_id=l[1],city_name=l[3],lat=l[4],long1=l[5],clouds=l[6],humidity=l[7],rain=l[8],temp_min=l[9],temp_max=l[10])

@app.route("/tomorrow_forecast/",methods=["GET","POST"])
def tomorrow_forecast():
	if request.method=="POST":
		global city_name
		global country
		l=weatherreport.tomorrow_weather()
		a=city_name
		return render_template("index3.html",city_name=a,clouds=l[0],humidity=l[1],rain=l[2],temp_min=l[3],temp_max=l[4])
	
@app.route("/sevenday_forecast/",methods=["GET","POST"])
def sevenday_forecast():
	if request.method=="POST":
		global city_name
		global country
		d=weatherreport.seven_day_weather()
		l1=[]
		l1.append(d["1"]["time"])
		l1.append(d["1"]["cloud"])
		l1.append(d["1"]["humidity"])
		if d["1"]["rain"].has_key("3h"):
			l1.append(d["1"]["rain"]["3h"])
		else:
			l1.append("")
		l1.append(d["1"]["temp"]["min"])
		l1.append(d["1"]["temp"]["max"])

#--------------------------------------2---------------------------------------

		l2=[]
		l2.append(d["2"]["time"])
		l2.append(d["2"]["cloud"])
		l2.append(d["2"]["humidity"])
		if d["2"]["rain"].has_key("3h"):
			l2.append(d["2"]["rain"]["3h"])
		else:
			l2.append("")
		l2.append(d["2"]["temp"]["min"])
		l2.append(d["2"]["temp"]["max"])
#-------------------------------------3--------------------------------------------------------	
		
		l3=[]
		l3.append(d["3"]["time"])
		l3.append(d["3"]["cloud"])
		l3.append(d["3"]["humidity"])
		if d["3"]["rain"].has_key("3h"):
			l3.append(d["3"]["rain"]["3h"])
		else:
			l3.append("")
		l3.append(d["3"]["temp"]["min"])
		l3.append(d["3"]["temp"]["max"])

#-----------------------------------------------------4--------------------------------------------

		l4=[]
		l4.append(d["4"]["time"])
		l4.append(d["4"]["cloud"])
		l4.append(d["4"]["humidity"])
		if d["4"]["rain"].has_key("3h"):
			l4.append(d["4"]["rain"]["3h"])
		else:
			l4.append("")
		l4.append(d["4"]["temp"]["min"])
		l4.append(d["4"]["temp"]["max"])
		
#---------------------------------5--------------------------------------------

		l5=[]
		l5.append(d["5"]["time"])
		l5.append(d["5"]["cloud"])
		l5.append(d["5"]["humidity"])
		if d["5"]["rain"].has_key("3h"):
			l5.append(d["5"]["rain"]["3h"])
		else:
			l5.append("")
		l5.append(d["5"]["temp"]["min"])
		l5.append(d["5"]["temp"]["max"])
#----------------------------------------------------------6--------------------------------


		l6=[]
		l6.append(d["6"]["time"])
		l6.append(d["6"]["cloud"])
		l6.append(d["6"]["humidity"])
		if d["6"]["rain"].has_key("3h"):
			l6.append(d["6"]["rain"]["3h"])
		else:
			l6.append("")
		l6.append(d["6"]["temp"]["min"])
		l6.append(d["6"]["temp"]["max"])

#-----------------------------------------------7------------------------------------------


		l7=[]
		l7.append(d["7"]["time"])
		l7.append(d["7"]["cloud"])
		l7.append(d["7"]["humidity"])
		if d["7"]["rain"].has_key("3h"):
			l7.append(d["7"]["rain"]["3h"])
		else:
			l7.append("")
		l7.append(d["7"]["temp"]["min"])
		l7.append(d["7"]["temp"]["max"])
		a=city_name
	
		return render_template("index4.html",city_name=a,a1=l1[0],a2=l1[1],a3=l1[2],a4=l1[3],a5=l1[4],a6=l1[5],a7=l2[0],a8=l2[1],a9=l2[2],a10=l2[3],a11=l2[4],a12=l2[5],a13=l3[0],a14=l3[1],a15=l3[2],a16=l3[3],a17=l3[4],a18=l3[5],a19=l4[0],a20=l4[1],a21=l4[2],a22=l4[3],a23=l4[4],a24=l4[5],a25=l5[0],a26=l5[1],a27=l5[2],a28=l5[3],a29=l5[4],a30=l5[5],a31=l6[0],a32=l6[1],a33=l6[2],a34=l6[3],a35=l6[4],a36=l6[5],a37=l7[0],a38=l7[1],a39=l7[2],a40=l7[3],a41=l7[4],a42=l7[5])



