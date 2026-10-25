#Write a program that requests a color (Blue or Red) and a mode (Steady or Flashing) as input and then displays the weather forecast.
color=input("Enter color:")
mode=input("Enter mode:")
if color=='blue' and mode=='steady':
    print("Clear view")
elif color=='blue' and mode=='flashing':
    print("Clouds due")
elif color=='red' and mode=='steady':
    print("Rain ahead")
elif color=='red' and mode=='flashing':
    print("Snow instead")
