import PySimpleGUI as gui
from PIL import Image
import pytesseract as tess






sum = 0


while sum == 0:    
    gui_text = gui.popup_get_text("File Input", "Must be in Desktop")
    img = Image.open(gui_text)
    text = tess.image_to_string(img)
    text_array = text.split()
    Yes_No = gui.popup_yes_no(text, title="DataOutput")
    if Yes_No == "Yes":
        for i in text_array:
            if "*" == i:
                pass
            elif "(" in i:
                i = i.replace("(","")
                i = i.replace(")","")
                i = i.replace(",","")
                sum = sum - float(i)
            elif "-" in i:
                i = i.replace(",","")    
                i = i.replace("-","")
                sum = sum - float(i)
            else:
                i = i.replace(",","")
                print(i)
                sum = sum + float(i)
        Sum = gui.popup(sum, title= "Sum")
    if Yes_No == "No":
        pass
