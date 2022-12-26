from pyscript import Element
calculation = ""
text_show = Element("text-show")

def btn_click(btn_id):
    btn_value = Element(btn_id).value
    global calculation
    calculation += btn_value
    if btn_id == "btn_reset":
        calculation = ""
        text_show.write(calculation)
        text_show.claer()
    elif btn_id == "btn_equal":
        answer = eval(calculation)
        text_show.write(answer)
        calculation = str(answer)
        answer = ""
    elif btn_id == "btn_del":
        calculation = calculation[:-1]
        text_show.write(calculation)
    else:
        text_show.write(calculation)
