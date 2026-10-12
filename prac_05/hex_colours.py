color_code = {"aliceblue": "#f0f8ff","antiquewhite": "#faebd7","aqua": "#00ffff","beige": "#f5f5dc","black": "#000000","blueviolet": "#8a2be2","brown": "#a52a2a","chocolate": "#d2691e","coral": "#ff7f50","cornflowerblue": "#6495ed"}

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    try:
        print(f"{colour_name} is {color_code[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").lower()