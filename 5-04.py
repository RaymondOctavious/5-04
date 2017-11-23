#created by raymond
#created on november 20, 2017
#created for isc3u
#this program finds the average in an array

import ui

array = []

 

def calculate_average(array = []):

    average = (sum(array) / len(array))
    return average

def enter(sender):
    try:
        mark = int(view['list_textfield'].text)
        if mark >= 0 and mark <= 100:
          array.append(mark)
          view['list_label'].text = " " + str(array)
          view['list_textfield'].text = ''
          view['wrong_label'].text = ' '
        
        else:
	        view['wrong_label'].text = "Oops, something went wrong!"
    except:
          view['wrong_label'].text = "Oops, something went wrong!"
        
   
        
        
def calculate_button(sender):
    answer = calculate_average(array)
    view['answer_label'].text = " "+str(answer)
    
view = ui.load_view()
view.present('sheet')

