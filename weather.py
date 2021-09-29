import requests
#creating the weather variable objects
api_address="http://api.openweathermap.org/data/2.5/weather?appid=a787d7c5f5bebcd472d9827c6aa28988&q="
api_temp="http://api.openweathermap.org/data/2.5/forecast?appid=a787d7c5f5bebcd472d9827c6aa28988&zip="
#getting user info
user_city=input("Enter City: ")
user_zip=int(input("Enter Zip: "))
url=api_address+user_city
url2=api_temp+str(user_zip)
#copying the data to our variable
json_data =requests.get(url).json()
json_data1 =requests.get(url2).json()
#formatting our data
formatted_data= json_data['weather'][0]['description']
formatted_data2=json_data1['list'][0]['main']['temp']
#converting our temp to Fahrenheit
temp=(formatted_data2-273.15)*1.8+32.0
def listed():
  for i in formatted_data2:
    print(float(i))

print(formatted_data,int(temp),"F")
