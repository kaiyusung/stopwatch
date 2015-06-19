#Import modules.
import simplegui


#Define global variables
count = 0
total_count = 0
success_count = 0
stopwatch = False


"""Format function that converts number into 0:00:0"""
def format(t):
    milliseconds = t % 10
    seconds = (t / 10) % 10
    ten_seconds = (t % 600) / 100
    minutes = t / 600
    return (str(minutes) + ":" + str(ten_seconds) + 
            str(seconds) + "." + str(milliseconds))
    
#Define event handlers for buttons; "Start", "Stop", "Reset" 
def start_button():
    global stopwatch
    stopwatch = True
    timer.start()

def stop_button():
    global total_count, success_count, stopwatch
    #Only works for True boolean.
    if stopwatch == True:
        total_count += 1
        if count % 10 == 0:
            success_count += 1
        timer.stop()
    else:
        timer.stop()
    #Set boolean back to false.    
    stopwatch = False
    

def reset_button():
    global count, total_count, success_count
    timer.stop()
    count = 0
    total_count = 0
    success_count = 0

#Count the time
def watch():
    global count
    count = count + 1

#Draw handler to draw on the canvas
def draw(canvas):
    global time
    canvas.draw_text(str(format(count)),[90,150],50,"Blue") 
    canvas.draw_text(str(success_count) + "/" + 
                     str(total_count),[210,40],40,"Red")
    
#Create frame
frame = simplegui.create_frame("Watch",300,300)


#Register event handlers
timer = simplegui.create_timer(100,watch)

#Frame
frame.set_canvas_background("White")
frame.set_draw_handler(draw)
frame.add_button("Start", start_button,80)
frame.add_button("Stop", stop_button, 80)
frame.add_button("Reset",reset_button, 80)

#Start frame
frame.start()
