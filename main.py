###################################################################
### Learning how to use API to get JSON data ###

# import requests
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # print(response) # This gives back an HTTP [response code]
# # print(response.status_code)
# # print(response.raise_for_status()) # Uses Request module to raise errors for us
#
# json_data = response.json()
# longitude = json_data["iss_position"]["longitude"]
# latitude = json_data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)

###################################################################

from tkinter import *


def get_quote():
    pass
    #Write your code here.



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()

