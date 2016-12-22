#from pyowm.webapi25 import*
#from pkg_resources import resource_stream
import pyowm
#print pyowm.timeutils.now("iso")
#city=raw_input("enter the city name and country\n")
key='551c27fa53d7c0946bc75095870afd75'
owm=pyowm.OWM(key)
city=""
def initialization(a):
	global city
	city=a
	global observation
	observation = owm.weather_at_place(city)
	location=observation.get_location()
	ls=[]
	ls.append(str(observation.get_reception_time("iso")))
	ls.append(str(location.get_ID()))
	ls.append(str(location.get_country()))
	a=city.split(",")
	ls.append(a[0])
#	ls.append(str(location.get_name()))
	ls.append(str(location.get_lat()))
	ls.append(str(location.get_lon()))
	#def cureent_weather(): 
#------------------------------------------CURRENT WEATHER------------------------------------------------
	print "----------------------------CURRENT WEATHER---------------------------------"
	weather_data=observation.get_weather()
	ls.append(str(weather_data.get_clouds()))
	ls.append(str(weather_data.get_humidity()))
	rain=weather_data.get_rain()
	if rain.has_key("3h"):
		ls.append(str(rain["3h"]))
	else:
		ls.append("")
	temp = weather_data.get_temperature("celsius")
	if temp.has_key("temp_min"):
		ls.append(str(temp["temp_min"]))
	else:
		ls.append("")
	if temp.has_key("temp_max"):
		ls.append(str(temp["temp_max"]))
	else:
		ls.append("")
	if temp.has_key("temp"):
		ls.append(str(temp["temp"]))
	else:
		ls.append("")
	return ls

def tomorrow_weather():
#----------- FORECAST tomorrow---------------------
	print "----------- FORECAST tomorrow---------------------"
	global city
	ls=[]
	forecast=owm.daily_forecast(city,2)
	tomorrow_weather=forecast.get_forecast()
	tomorrow_weather=tomorrow_weather.get_weathers()
	#tomorrow_weather[1].get_reference_time("iso")
	ls.append(tomorrow_weather[1].get_clouds())
	ls.append(tomorrow_weather[1].get_humidity())
	if tomorrow_weather[1].get_rain().has_key("3h"):
		ls.append(tomorrow_weather[1].get_rain()["3h"])
	else:
		ls.append("")
	temp=tomorrow_weather[1].get_temperature("celsius")
	temp_min=temp["min"]
	ls.append(temp_min)
	temp_max=temp["max"]
	ls.append(temp_max)
	temp_day=temp["day"]
	ls.append(temp_day)
#	print ls
	return ls

#------------------------------------- ROUGH--------------------------------------------------------------
"""weather_forecast=forecast.most_windy()
#wind_speed=weather_forecast.get_wind()
#wind_speed=wind_speed["speed"]
#print wind_speed
forecast_humidity=weather_forecast.get_humidity()
#print forecast_humidity
forecast_pressure=weather_forecast.get_pressure()
#print forecast_pressure=forecast_pressure["press"]
forecast_weather=weather_forecast.get_detailed_status()
#print forecast_weather
forecast_temperature = weather_forecast.get_temperature("celsius")
#print forecast_temperature_min, forecast_temperature_max, forecast_temperature_day"""

def seven_day_weather():
#----------------------SEVEN DAYS FORECAST------------------------------------------
	print "----------------------SEVEN DAYS FORECAST------------------------------------------"
	global city
	forecast_seven_days = owm.daily_forecast(city,7)
	forecast_seven_days = forecast_seven_days.get_forecast() 
	l7 = forecast_seven_days.get_weathers()
	d7_1={"time":l7[0].get_reference_time("iso"),"cloud":l7[0].get_clouds(),"humidity":l7[0].get_humidity(),"rain":l7[0].get_rain(),"temp":l7[0].get_temperature("celsius")}
	d7_2={"time":l7[1].get_reference_time("iso"),"cloud":l7[1].get_clouds(),"humidity":l7[1].get_humidity(),"rain":l7[1].get_rain(),"temp":l7[1].get_temperature("celsius")}
	d7_3={"time":l7[2].get_reference_time("iso"),"cloud":l7[2].get_clouds(),"humidity":l7[2].get_humidity(),"rain":l7[2].get_rain(),"temp":l7[2].get_temperature("celsius")}
	d7_4={"time":l7[3].get_reference_time("iso"),"cloud":l7[3].get_clouds(),"humidity":l7[3].get_humidity(),"rain":l7[3].get_rain(),"temp":l7[3].get_temperature("celsius")}
	d7_5={"time":l7[4].get_reference_time("iso"),"cloud":l7[4].get_clouds(),"humidity":l7[4].get_humidity(),"rain":l7[4].get_rain(),"temp":l7[4].get_temperature("celsius")}
	d7_6={"time":l7[5].get_reference_time("iso"),"cloud":l7[5].get_clouds(),"humidity":l7[5].get_humidity(),"rain":l7[5].get_rain(),"temp":l7[5].get_temperature("celsius")}
	d7_7={"time":l7[6].get_reference_time("iso"),"cloud":l7[6].get_clouds(),"humidity":l7[6].get_humidity(),"rain":l7[6].get_rain(),"temp":l7[6].get_temperature("celsius")}
	d={"1":d7_1,"2":d7_2,"3":d7_3,"4":d7_4,"5":d7_5,"6":d7_6,"7":d7_7} 
	return d

"""#---------------------------ROUGH-------------------------------------------------------------
forecast_three_hrs = owm.three_hours_forecast(city)
forecast_three_hrs = forecast_three_hrs.get_forecast()
l3 = forecast_three_hrs.get_weathers()"""

#initialization("boston,us")
