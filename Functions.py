from tkinter import*
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("Planet Encyclopedia")
root.geometry("500x500")
root.configure(background = "lightblue")

Mercury = ImageTk.PhotoImage(Image.open ("mercury.jpg"))
Venus = ImageTk.PhotoImage(Image.open ("venus.jpg"))
Earth = ImageTk.PhotoImage(Image.open ("earth.jpg"))

label_planet = Label(root, text = "Planet : ", bg = "lightblue")
label_planet_name = Label(root, font = ("courier", 18, "bold"), bg = "lightblue")
label_planet_image = Label(root, bg = "gold2", highlightthickness = 5, borderwidth = 2, relief = SOLID)
label_planet_gravity_radius = Label(root, font = ("castellar"), bg = "lightblue")
label_planet_info = Label(root, font = ("courier", 10, "bold"), bg = "lightblue", wraplength = 500)
                          
planets = ["Mercury", "Venus", "Earth"]
selectedval = StringVar()
dropdown = ttk.Combobox(root, value = planets, textvariable = selectedval)               

def PlanetInfo():
    planet = selectedval.get()
    if planet == "Mercury":
        label_planet_name['text'] = "Mercury"
        label_planet_image['image'] = Mercury
        label_planet_gravity_radius['text'] = "Gravity : 3.7 m/s² \n Radius : 2,439.7 km"
        label_planet_info['text'] = "Mercury Is The Smallest Planet In Our Solar System. It Is Just a Little Bigger Than The Earth's Moon"
    elif planet == "Venus":
        label_planet_name['text'] = "Venus"
        label_planet_image['image'] = Venus
        label_planet_gravity_radius['text'] = "Gravity : 8.87 m/s² \n Radius : 6,051.8 km"
        label_planet_info['text'] = "Venus Is The Brightest Object In The Sky After The Sun And The Moon, And Sometimes Looks Like A Bright Star In The Morning Or The Evening Sky."
        
    elif planet == "Earth":
        label_planet_name['text'] = "Earth"
        label_planet_image['image'] = Earth
        label_planet_gravity_radius['text'] = "Gravity : 9.807 m/s² \n Radius : 6,371 km"
        label_planet_info['text'] = "Earth Is The Only Place In The Known Universe Confirmed To Host Life And It's The Only One For Sure To HAve Liquid Water On Its Surface"

dropdown.place(relx = 0.5, rely = 0.1, anchor = CENTER)

btn = Button(root, text = "Show Planet Info", command = PlanetInfo)
btn.place(relx = 0.5, rely = 0.18, anchor = CENTER)

label_planet.place(relx = 0.2, rely = 0.1, anchor = CENTER)
label_planet_name.place(relx = 0.5, rely = 0.25, anchor = CENTER)
label_planet_image.place(relx = 0.5, rely = 0.5, anchor = CENTER)
label_planet_gravity_radius.place(relx = 0.5, rely = 0.8, anchor = CENTER)
label_planet_info.place(relx = 0.5, rely = 0.9, anchor = CENTER)

root.mainloop()