from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests
from PIL import Image,ImageTk


url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

config_file = "config.init"
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']

def get_weather(city):
    result = requests.get(url.format(city,api_key))
    if result:
       json = result.json()
       #  (city,country,temp_fahrenheit,icon,weather)
       city = json["name"]
       country = json["sys"]["country"]
       temp_kelvin = json['main']['temp']
       temp_celsius = temp_kelvin - 273.15
       temp_fahrenheit = (temp_kelvin - 273.15)*9/5+32
       icon = json["weather"][0]["icon"]
       weather = json["weather"][0]["main"]
       final = [city,country,temp_celsius,temp_fahrenheit,icon,weather]
       return final

    else:
        return None



app = Tk()
app.title("weather app")
app.geometry("600x350")
app.iconbitmap('icon.ico')
app.config(bg='azure1')

def search():

    city = city_text.get()
    weather = get_weather(city)
    # my_img = ImageTk.PhotoImage(Image.open("weather_icon//01n.png"))
    #img_label = Label(app, image=my_img)
    #img_label.pack()


    # print(weather_state)

    if weather:
        location_lbl["text"] = '{},{}'.format(weather[0], weather[1])
        temp_lbl["text"]= '{:.2f}°C, {:.2f}°F'.format(weather[2], weather[3])
        weather_lbl["text"] = weather[5]
        weather_image = str(weather[4])
        my_img = ImageTk.PhotoImage(Image.open("weather_icon//" + weather_image + ".png"))
        img_label = Label(app, image=my_img)
        img_label.pack()
        img_label['image'] = my_img.show()

    else:
        messagebox.showerror("error,""cannot find city {}".format(city))






city_text = StringVar()
city_entry = Entry(app, textvariable = city_text,bg='azure1')
city_entry.pack()

search_btn = Button(app, text="search button",font=('bold',10), width=13,command=search,bg='aquamarine4',fg="gray1")
search_btn.pack()

location_lbl = Label(app,text='',font=('calibri bold',20),bg='azure1')
location_lbl.pack()

# my_img=ImageTk.PhotoImage(Image.open("weather_icon//01n.png"))
# img_label = Label(app,image=my_img)
# img_label.pack()
# print(weather_state)

temp_lbl = Label(app, text ="",font=('calibri bold',12),bg='azure1')
temp_lbl.pack()

weather_lbl = Label(app,text ="",font=('calibri bold',12),bg='azure1')
weather_lbl.pack()

app.mainloop()