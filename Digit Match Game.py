from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
#import time
import queue


window_W = 500
window_H = 500

#circle_initialization
radius = 100
y_coordinate = -1 * radius
inc = 10
#TOP Ys
y_TH = y_coordinate + radius - 15
y_TM = y_coordinate + radius - 17
y_TL = y_coordinate + radius - 19
#MID Ys
y_MH = y_coordinate + inc
y_MM = y_coordinate
y_ML = y_coordinate - inc
#BOTTOM Ys
y_BH = y_coordinate - radius + 19
y_BM = y_coordinate - radius + 17
y_BL = y_coordinate - radius + 15

digit = 0
#digit_Q = queue.Queue()
digit_match = True
right_entry = True
animation_active = True
SCORE = 0
if SCORE%20==0:
    inc = inc+10

def circ_point(x,y,cx,cy):
    glVertex2f(x+cx,y+cy)
    glVertex2f(y+cx,x+cy)

    glVertex2f(y+cx,-x+cy)
    glVertex2f(x+cx,-y+cy)

    glVertex2f(-x+cx,-y+cy)
    glVertex2f(-y+cx,-x+cy)

    glVertex2f(-y+cx,x+cy)
    glVertex2f(-x+cx,y+cy)


def midpoint_circle(cx,cy,rad):
    d = 1 - rad
    x = 0
    y = rad

    circ_point(x,y,cx,cy)

    while(x < y):
        if(d < 0):
            d = d + 2*x + 3
        else:
            d = d + 2*x - 2*y + 5
            y = y - 1
        x = x + 1
        circ_point(x,y,cx,cy)  


def find_zone(x1, y1, x2, y2): #Function determines the zone of the given coordinates
    dx_ = x2 - x1
    dy_ = y2 - y1
    if dy_==0:
        zone=0
    if dx_==0:
        zone=1
    elif abs(dx_) >= abs(dy_):
        if dx_ > 0 and dy_ > 0:
            zone = 0
        elif dx_ < 0 and dy_ > 0:
            zone = 3
        elif dx_ < 0 and dy_ < 0:
            zone = 4
        elif dx_ > 0 and dy_ < 0:
            zone = 7
    else:
        if dx_ > 0 and dy_ > 0:
            zone = 1
        elif dx_ < 0 and dy_ > 0:
            zone = 2
        elif dx_ < 0 and dy_ < 0:
            zone = 5
        elif dx_ > 0 and dy_ < 0:
            zone = 6
    return zone

def convert_zone_to_0(x, y, zone): #Fuction converts the zone of the coordinates from 'any' zone to zone 0
    if(zone==0):
        return x,y
    elif(zone==1):
        return y,x
    elif(zone==2):
        return y,-x
    elif(zone==3):
        return -x,y
    elif(zone==4):
        return -x,-y
    elif(zone==5):
        return -y,-x
    elif(zone==6):
        return -y,x
    elif(zone==7):
        return x,-y

def convert_to_og_zone(x,y,zone): #Fuction returns the zone of the coordinates from zone 0 to the specific zone
    if(zone==0):
        return x,y
    elif(zone==1):
        return y,x
    elif(zone==2):
        return -y,x
    elif(zone==3):
        return -x,y
    elif(zone==4):
        return -x,-y
    elif(zone==5):
        return -y,-x
    elif(zone==6):
        return y,-x
    elif(zone==7):
        return x,-y

def midpoint_line(x1, y1, x2, y2, zone): #main fucntion for midpoint line algo
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    incNE = 2 * (dy - dx)
    incE = 2 * dy
    y = y1
    bx, by = convert_to_og_zone(x1,y1,zone)
    glVertex2i(bx,by)
    for x in range(x1, x2 + 1):
        if (d>0):
            d = d + incNE
            x = x + 1
            y = y + 1
        elif (d<=0):
            d = d + incE
            x = x + 1
        cx, cy = convert_to_og_zone(x, y, zone)
        glVertex2i(cx, cy)

def draw_line(x1, y1, x2, y2): #draw function for midpoint line algo function
    zone = find_zone(x1, y1, x2, y2)
    x1, y1 = convert_zone_to_0(x1, y1, zone)
    x2, y2 = convert_zone_to_0(x2, y2, zone)
    midpoint_line(x1, y1, x2, y2, zone)

def right_top(i):
    #RIGHT-TOP
    draw_line(270,y_TL + (-700*i),268,y_TM + (-700*i))
    draw_line(270,y_MH + (-700*i),268,y_MM + (-700*i))
    draw_line(270,y_MH + (-700*i),270,y_TL + (-700*i))
    draw_line(266,y_TL + (-700*i),268,y_TM + (-700*i))
    draw_line(266,y_MH + (-700*i),268,y_MM + (-700*i))
    draw_line(266,y_MH + (-700*i),266,y_TL + (-700*i))

def right_bottom(i):
    #RIGHT-BOTTOM
    draw_line(270,y_ML + (-700*i),268,y_MM + (-700*i))
    draw_line(270,y_BH + (-700*i),268,y_BM + (-700*i))
    draw_line(270,y_BH + (-700*i),270,y_ML + (-700*i))
    draw_line(266,y_ML + (-700*i),268,y_MM + (-700*i))
    draw_line(266,y_BH + (-700*i),268,y_BM + (-700*i))
    draw_line(266,y_BH + (-700*i),266,y_ML + (-700*i))

def left_top(i):
    #LEFT-TOP
    draw_line(230,y_TL + (-700*i),232,y_TM + (-700*i))
    draw_line(230,y_MH + (-700*i),232,y_MM + (-700*i))
    draw_line(230,y_MH + (-700*i),230,y_TL + (-700*i))
    draw_line(234,y_TL + (-700*i),232,y_TM + (-700*i))
    draw_line(234,y_MH + (-700*i),232,y_MM + (-700*i))
    draw_line(234,y_MH + (-700*i),234,y_TL + (-700*i))

def left_bottom(i):
    #LEFT-BOTTOM
    draw_line(230,y_ML + (-700*i),232,y_MM + (-700*i))
    draw_line(230,y_BH + (-700*i),232,y_BM + (-700*i))
    draw_line(230,y_BH + (-700*i),230,y_ML + (-700*i))
    draw_line(234,y_ML + (-700*i),232,y_MM + (-700*i))
    draw_line(234,y_BH + (-700*i),232,y_BM + (-700*i))
    draw_line(234,y_BH + (-700*i),234,y_ML + (-700*i))

def top_horizontal(i):
    #TOP-HORIZONTAL
    draw_line(266,y_TH + (-700*i),268,y_TM + (-700*i))
    draw_line(266,y_TL + (-700*i),268,y_TM + (-700*i))
    draw_line(234,y_TH + (-700*i),266,y_TH + (-700*i))
    draw_line(234,y_TH + (-700*i),232,y_TM + (-700*i))
    draw_line(234,y_TL + (-700*i),232,y_TM + (-700*i))
    draw_line(234,y_TL + (-700*i),266,y_TL + (-700*i))

def middle_horizontal(i):
    #MIDDLE-HORIZONTAL
    draw_line(266,y_MH + (-700*i),268,y_MM + (-700*i))
    draw_line(266,y_ML + (-700*i),268,y_MM + (-700*i))
    draw_line(234,y_MH + (-700*i),266,y_MH + (-700*i))
    draw_line(234,y_MH + (-700*i),232,y_MM + (-700*i))
    draw_line(234,y_ML + (-700*i),232,y_MM + (-700*i))
    draw_line(234,y_ML + (-700*i),266,y_ML + (-700*i))

def bottom_horizontal(i):
    #BOTTOM-HORIZONTAL
    draw_line(266,y_BH + (-700*i),268,y_BM + (-700*i))
    draw_line(266,y_BL + (-700*i),268,y_BM + (-700*i))
    draw_line(234,y_BH + (-700*i),266,y_BH + (-700*i))
    draw_line(234,y_BH + (-700*i),232,y_BM + (-700*i))
    draw_line(234,y_BL + (-700*i),232,y_BM + (-700*i))
    draw_line(234,y_BL + (-700*i),266,y_BL + (-700*i))

def digit_draw(num,i):
    if num==0:
        right_top(i)
        right_bottom(i)
        left_top(i)
        left_bottom(i)
        top_horizontal(i)
        bottom_horizontal(i)
    elif num==1:
        right_top(i)
        right_bottom(i)
    elif num==2:
        right_top(i)
        left_bottom(i)
        top_horizontal(i)
        middle_horizontal(i)
        bottom_horizontal(i)
    elif num==3:
        right_top(i)
        right_bottom(i)
        top_horizontal(i)
        middle_horizontal(i)
        bottom_horizontal(i)
    elif num==4:
        right_top(i)
        right_bottom(i)
        left_top(i)
        middle_horizontal(i)
    elif num==5:
        right_bottom(i)
        left_top(i)
        top_horizontal(i)
        middle_horizontal(i)
        bottom_horizontal(i)
    elif num==6:
        right_bottom(i)
        left_top(i)
        left_bottom(i)
        top_horizontal(i)
        middle_horizontal(i)
        bottom_horizontal(i)
    elif num==7:
        right_top(i)
        right_bottom(i)
        top_horizontal(i)
    elif num==8:
        right_top(i)
        right_bottom(i)
        left_top(i)
        left_bottom(i)
        top_horizontal(i)
        middle_horizontal(i)
        bottom_horizontal(i)
    elif num==9:
        right_top(i)
        right_bottom(i)
        left_top(i)
        top_horizontal(i)
        middle_horizontal(i)
        bottom_horizontal(i)
        
def initialize(): #function sets up necessary prerequisites for openGL graphics window
    glViewport(0, 0, window_W, window_H)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, window_W, 0.0, window_H, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def show(): #display fucntion
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    initialize()
    x_digit = 0
    #digit_Q.put(x_digit)
    for i in range(0,50):
        #current_digit = random.randint(0,9)
        if right_entry==True and digit_match and y_coordinate + (-700*i)<window_H+radius and x_digit>=0:
            glColor3f(1.0,0.0,1.0)
            glPointSize(1.5)
            glBegin(GL_POINTS)
            digit_draw(x_digit,i)
            glEnd()
            glColor3f(1.0,0.0,1.0)
            glPointSize(1.5)
            glBegin(GL_POINTS)
            if y_coordinate + (-700*i)<window_H+radius:
                midpoint_circle(250,y_coordinate + (-700*i),radius)
            glEnd()
        elif right_entry==True and (not digit_match) and y_coordinate + (-700*i)<window_H+radius and x_digit>=0:
            glColor3f(0.0, 1.0, 1.0)
            glPointSize(1.5)
            glBegin(GL_POINTS)
            digit_draw(x_digit,i)
            glEnd()
            glColor3f(0.0, 1.0, 1.0)
            glPointSize(1.5)
            glBegin(GL_POINTS)
            if y_coordinate + (-700*i)<window_H+radius:
                midpoint_circle(250,y_coordinate + (-700*i),radius)
            glEnd()
        elif not right_entry:
            glColor3f(1.0, 0.0, 0.0)
            glPointSize(10)
            glBegin(GL_POINTS)
            draw_line(200,200,300,300)
            draw_line(300,200,200,300)
            glEnd()
            #break
        #elif y_coordinate + (-700*i)>=window_H+radius:
                #digit_Q.put(digit)
        #draw_line(50,trial_y1,100,trial_y2)
        if x_digit==9:
            x_digit = 0
        else:
            x_digit += 1
    glutSwapBuffers()

def animation(_):
    #global digit   
    global y_TH
    global y_TM
    global y_TL
    global y_MH
    global y_MM
    global y_ML
    global y_BH
    global y_BM
    global y_BL
    global y_coordinate
    if animation_active:
        y_TH += inc
        y_TM += inc
        y_TL += inc
        y_MH += inc
        y_MM += inc
        y_ML += inc
        y_BH += inc
        y_BM += inc
        y_BL += inc
        y_coordinate = y_coordinate+inc
        glutPostRedisplay()
    glutTimerFunc(16, animation, 0)

def mouse_callback(button, state, _, __):
    global animation_active
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        animation_active = not animation_active  # Toggle animation state
        glutPostRedisplay()
    elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        # Restart the entire graphics window
        glutPostRedisplay()

def keyboard_callback(key, _, __):
    global digit
    global right_entry
    global digit_match
    global SCORE
    check_num = digit
    if key == b'0' and check_num==0:
        digit_match = not digit_match
        SCORE += 1
        print(f"SCORE: {SCORE}")
        digit += 1
    elif key == b'1' and check_num==1:
        digit_match = not digit_match
        SCORE += 1
        print(f"SCORE: {SCORE}")
        digit += 1
    elif key == b'2' and check_num==2:
        digit_match = not digit_match
        SCORE += 1
        print(f"SCORE: {SCORE}")
        digit += 1
    elif key == b'3' and check_num==3:
        digit_match = not digit_match
        SCORE += 1
        print(f"SCORE: {SCORE}")
        digit += 1
    elif key == b'4' and check_num==4:
        digit_match = not digit_match
        SCORE += 1
        print(f"SCORE: {SCORE}")
        digit += 1
    elif key == b'5' and check_num==5:
        digit_match = not digit_match
        SCORE += 1
        print(f"SCORE: {SCORE}")
        digit += 1
    elif key == b'6' and check_num==6:
        digit_match = not digit_match
        SCORE += 1
        print(f"SCORE: {SCORE}")
        digit += 1
    elif key == b'7' and check_num==7:
        digit_match = not digit_match
        SCORE += 1
        print(f"SCORE: {SCORE}")
        digit += 1
    elif key == b'8' and check_num==8:
        digit_match = not digit_match
        SCORE += 1
        print(f"SCORE: {SCORE}")
        digit += 1
    elif key == b'9' and check_num==9:
        digit_match = not digit_match
        SCORE += 1
        print(f"SCORE: {SCORE}")
        digit = 0
    if key == b'0' and check_num!=0:
        right_entry = not right_entry
    elif key == b'1' and check_num!=1:
        right_entry = not right_entry
    elif key == b'2' and check_num!=2:
        right_entry = not right_entry
    elif key == b'3' and check_num!=3:
        right_entry = not right_entry
    elif key == b'4' and check_num!=4:
        right_entry = not right_entry
    elif key == b'5' and check_num!=5:
        right_entry = not right_entry
    elif key == b'6' and check_num!=6:
        right_entry = not right_entry
    elif key == b'7' and check_num!=7:
        right_entry = not right_entry
    elif key == b'8' and check_num!=8:
        right_entry = not right_entry
    elif key == b'9' and check_num!=9:
        right_entry = not right_entry    
    glutPostRedisplay()    

def main(): #call function
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(window_W, window_H)
    glutInitWindowPosition(0,0)
    wind = glutCreateWindow(b'Multiple Digit Generation with Circular Enclosure')
    
    glutDisplayFunc(show)
    #glutIdleFunc(animation)
    glutTimerFunc(16, animation, 0)
    glutKeyboardFunc(keyboard_callback)
    glutMouseFunc(mouse_callback)
    glutMainLoop()

if __name__ == "__main__":
    main()
