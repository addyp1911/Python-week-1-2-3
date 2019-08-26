
# ----------------------------------windchill prg-----------------------------------------------
#WindChill.py
# date : 26/08/2019
# method to print the windchill based on entered temperature and windspeed
      
def display(t,v):
     wind_chill=35.74 +.6215*t +((0.4275*t - 35.75)*pow(v,0.16))
     print(wind_chill)