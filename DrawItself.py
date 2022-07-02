import cairo
import math
import random
import string
import re

cx = 350
cy = 350
radius = 300

def draw(x1,y1,x2,y2,context,r,g,b):
    context.set_source_rgb(r,g,b)
    context.set_line_width(1)
    context.move_to(x1,y1)
    x_mid = (x1+x2)/2
    y_mid = (y1+y2)/2
    context.curve_to(x_mid,y_mid,cx,cy,x2,y2)
    context.stroke()

def random_point(arc,radius):
    x = math.cos(arc)*radius
    y = math.sin(arc)*radius
    return x+cx,y+cy


def generate_circle(colour_picker,arc_points,context):
    for key in colour_picker:
        r,g,b = colour_picker[key]
        a1,a2 = arc_points[key]
        context.set_source_rgb(r,g,b)
        context.set_line_width(10)
        context.arc(cx,cy,radius,a1,a2)
        context.stroke()


def visualize(input_text,colour_picker,arc_points,context):
    prev_x = -1
    prev_y = -1

    for c in input_text:
        a1,a2 = arc_points[c]
        arc_point = random.uniform(a1,a2)
        x,y = random_point(arc_point,radius)
        if prev_x == -1:
            prev_x = x
            prev_y = y
            continue
        else:
            r,g,b = colour_picker[c]
            draw(prev_x,prev_y,x,y,context,r,g,b)
            prev_x = x
            prev_y = y




if __name__ == '__main__':
    
    with open('DrawItself.py', 'r', encoding="utf8") as file:
        input_text = file.read().replace('\n', '')

    input_text = re.sub('[^a-zA-Z]+','',input_text)
    input_text = input_text.lower()

    context = cairo.Context(cairo.SVGSurface("svgfile.svg", 1000, 1000))
    
    colour_picker = dict()
    arc_points = dict()
    arc_angle = (2*math.pi)/26
    start_from = 0

    for c in string.ascii_lowercase:
        r = random.randint(100,900)/1000
        g = random.randint(100,900)/1000
        b = random.randint(100,900)/1000
        colour_picker[c] = (r,g,b)
        arc_points[c] = (start_from, start_from + arc_angle)
        start_from = start_from + arc_angle

    

    generate_circle(colour_picker,arc_points,context)
    visualize(input_text,colour_picker,arc_points,context)



    
    