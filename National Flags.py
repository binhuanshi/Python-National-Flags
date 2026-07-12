import turtle
import math

#started working on code 02/06/26 after ~9 pm

j = input("Of which country do you want the flag generated? ")
x = int(input("Size of flag: "))

wn = turtle.Screen()
t = turtle.Turtle()

#functions for drawing specific shapes
def draw_circle(x,y,r,color):
    """(x,y) is center, r is radius, color is color in hex"""
    t.fillcolor(color)
    t.goto(x,y-r)
    t.setheading(0)
    t.begin_fill()
    t.circle(r,360,180)
    t.end_fill()
def draw_rectangle(x,y,l,w,color):
    """(x,y) is top-left vertex, l is length, w is width, color is color in hex"""
    t.fillcolor(color)
    t.goto(x,y)
    t.begin_fill()
    t.goto(x+l,y)
    t.goto(x+l,y-w)
    t.goto(x,y-w)
    t.end_fill()
def draw_star(x,y,r,theta,color):
    """(x,y) is center of regular pentagram, r is radius, theta is angle in degrees (theta=0 means there are 2 sides of star parallel to x-axis) (increasing theta will "move" the star counterclockwise), color is color in hex"""
    s = r*math.cos(math.radians(18))/(1+math.sin(math.radians(18))) #s=side length
    t.fillcolor(color)
    t.goto(x,y)
    t.setheading(90+theta)
    t.forward(r)
    t.right(162)
    t.begin_fill()
    for _ in range(5):
        t.forward(s)
        t.left(72)
        t.forward(s)
        t.right(144)
    t.end_fill()
def draw_general_star(x,y,rInner,rOuter,n,theta,color):
    """(x,y) is center, rInner and rOuter are radii of inner and outer circle respectively, n is number of outer vertices, theta is angle in degrees (theta=0 means one "arm" of star faces precisely eastward) (increasing theta will "move" the star counterclockwise), color is color in hex"""
    outerPoints = {f"point{chr(65+2*i)}": (x+rOuter*math.cos(math.radians(theta+360/n*i)),y+rOuter*math.sin(math.radians(theta+360/n*i))) for i in range(n)}
    innerPoints = {f"point{chr(66+2*i)}": (x+rInner*math.cos(math.radians(theta+180/n+360/n*i)),y+rInner*math.sin(math.radians(theta+180/n+360/n*i))) for i in range(n)}
    t.goto(outerPoints["pointA"])
    t.fillcolor(color)
    t.begin_fill()
    for i in range(n-1):
        t.goto(innerPoints[f"point{chr(66+2*i)}"])
        t.goto(outerPoints[f"point{chr(67+2*i)}"])
    t.goto(innerPoints[f"point{chr(64+2*n)}"])
    t.goto(outerPoints["pointA"])
    t.end_fill()
def draw_polygon(color,n,*coordinates):
    """color is color in hex, n is number of sides, each coordinate (x,y) is vertex (write in order)"""
    t.fillcolor(color)
    t.goto(coordinates[0])
    t.begin_fill()
    for i in range(n-1):
        t.goto(coordinates[i+1])
    t.end_fill()
def draw_UnionJack(x,y,l,w,whiteColor,redColor,blueColor):
    """(x,y) is top-left vertex, l is length, w is width, whiteColor is white color in hex, redColor is red color in hex, blueColor is blueColor in hex; usually, l/w=2"""
    ratioHorizontal = l*5**0.5/20
    ratioVertical = w*5**0.5/20
    draw_rectangle(x,y,l,w,blueColor)
    draw_rectangle(x+5*l/12,y,l/6,w,whiteColor)
    draw_rectangle(x,y-w/3,l,w/3,whiteColor)
    draw_polygon(whiteColor,6,(x,y),(x,y-ratioVertical),(x+l-ratioHorizontal,y-w),(x+l,y-w),(x+l,y-w+ratioVertical),(x+ratioHorizontal,y))
    draw_polygon(whiteColor,6,(x,y-w),(x+ratioHorizontal,y-w),(x+l,y-ratioVertical),(x+l,y),(x+l-ratioHorizontal,y),(x,y-w+ratioVertical))
    draw_polygon(redColor,4,(x,y),(x,y-2*ratioVertical/3),(x+l/3-2*ratioHorizontal/3,y-w/3),(x+l/3,y-w/3))
    draw_polygon(redColor,4,(x,y-w),(x+2*ratioHorizontal/3,y-w),(x+l/3+2*ratioHorizontal/3,y-2*w/3),(x+l/3,y-2*w/3))
    draw_polygon(redColor,4,(x+l,y-w),(x+l,y-w+2*ratioVertical/3),(x+2*l/3+2*ratioHorizontal/3,y-2*w/3),(x+2*l/3,y-2*w/3))
    draw_polygon(redColor,4,(x+l,y),(x+l-2*ratioHorizontal/3,y),(x+2*l/3-2*ratioHorizontal/3,y-w/3),(x+2*l/3,y-w/3))
    draw_rectangle(x+9*l/20,y,l/10,w,redColor)
    draw_rectangle(x,y-2*w/5,l,w/5,redColor)
goldenRatio = (1+5**0.5)/2

wn.bgcolor("#8C92AC")
t.speed(0)
t.hideturtle()
t.penup()

#options for different countries
#make code such that most common names and abbreviations (including common name, formal name, ISO alpha-2 and -3, etc.) will trigger the country
#x (line 5) is length of flag in length, all facets of design of flag, including aspect ratio, should be based on official guidelines, center of flag is (0,0)
#if name of country commonly begins in "the" (e.g. the Netherlands), include option for user input "the+name" but only if the is lowercase

if j in ("Armenia", "Republic of Armenia", "AM", "A.M.", "ARM", "A.R.M."):
    draw_rectangle(-x/2,x/4,x,x/6,"#D90012")
    draw_rectangle(-x/2,x/12,x,x/6,"#0033A0")
    draw_rectangle(-x/2,-x/12,x,x/6,"#F2A800")
elif j in ("Australia", "Commonwealth of Australia", "AU", "A.U.", "AUS", "A.U.S.", "AUST", "A.U.S.T."):
    draw_rectangle(-x/2,x/4,x,x/2,"#001B69")
    draw_UnionJack(-x/2,x/4,x/2,x/4,"#FFFFFF","#E50027","#001B69")
    draw_general_star(-x/4,-x/8,x/30,3*x/40,7,90,"#FFFFFF") #Commonwealth Star
    draw_general_star(x/4,-x/6,x/63,x/28,7,90,"#FFFFFF") #Alpha Crucis
    draw_general_star(x/8,x/32,x/63,x/28,7,90,"#FFFFFF") #Beta Crucis
    draw_general_star(13*x/36,31*x/480,x/63,x/28,7,90,"#FFFFFF") #Gamma Crucis
    draw_general_star(x/4,x/6,x/63,x/28,7,90,"#FFFFFF") #Delta Crucis
    draw_general_star(3*x/10,-x/48,x/108,x/48,5,90,"#FFFFFF") #Epsilon Crucis
elif j in ("Austria", "Republic of Austria", "AT", "A.T.", "AUT", "A.U.T."):
    draw_rectangle(-x/2,x/3,x,2*x/9,"#C8102E")
    draw_rectangle(-x/2,x/9,x,2*x/9,"#FFFFFF")
    draw_rectangle(-x/2,-x/9,x,2*x/9,"#C8102E")
elif j in ("Azerbaijan", "Republic of Azerbaijan", "AZ", "A.Z.", "AZE", "A.Z.E."):
    draw_rectangle(-x/2,x/4,x,x/6,"#00B5E2")
    draw_rectangle(-x/2,x/12,x,x/6,"#EF3340")
    draw_rectangle(-x/2,-x/12,x,x/6,"#509E2F")
    draw_circle(-x/40,0,3*x/40,"#FFFFFF")
    draw_circle(-x/120,0,x/16,"#EF3340")
    #rest of code for eight-pointed star
    draw_general_star(7*x/120,0,x/48,x/24,8,0, "#FFFFFF")
elif j in ("Bahrain", "Kingdom of Bahrain", "BH", "B.H.", "BHR", "B.H.R."):
    draw_rectangle(-x/2,3*x/10,x,3*x/5,"#FFFFFF")
    draw_rectangle(-x/10,3*x/10,3*x/5,3*x/5,"#DA291C")
    draw_polygon("#DA291C",3,(-x/4,3*x/10),(-x/10,3*x/10),(-x/10,6*x/25))
    for _ in range(4):
        draw_polygon("#DA291C",3,(-x/10,6*x/25-3*_*x/25),(-x/4,9*x/50-3*_*x/25),(-x/10,3*x/25-3*_*x/25))
    draw_polygon("#DA291C",3,(-x/4,-3*x/10),(-x/10,-3*x/10),(-x/10,-6*x/25))
elif j in ("Bangladesh", "People’s Republic of Bangladesh", "BD", "B.D.", "BGD", "B.G.D."):
    draw_rectangle(-x/2,3*x/10,x,3*x/5,"#006747")
    draw_circle(-x/20,0,x/5,"#DA291C")
elif j in ("Belgium", "Kingdom of Belgium", "BE", "B.E.", "BEL", "B.E.L."):
    draw_rectangle(-x/2,13*x/30,x/3,13*x/15,"#000000")
    draw_rectangle(-x/6,13*x/30,x/3,13*x/15,"#FDDA24")
    draw_rectangle(x/6,13*x/30,x/3,13*x/15,"#EF3340")
elif j in ("Bosnia and Herzegovina", "Bosnia-Herzegovina", "Bosnia", "BiH", "B.i.H.", "B&H", "B.&H.", "BA", "B.A.", "BIH", "B.I.H."):
    #note: this is a complete code for flag
    #however, if you want to revise code so that flag is created without first drawing on background
    #information is as follows
    #for the "for _ in" line, change 9 to 7; for the "draw_star" line, change both _ to (_+1)
    #for both the top star and the bottom star, do as follows
    #copy and paste the function body of draw_star function from the definition section above, without calling the function
    #first step: the function currently has each of the 5 repeated side-drawings draw 2 sides that are 108°; change the text so that each of the 5 repeated side-drawings draw 2 sides that are 36°
    #second step: instead of having it repeated 5 times, repeat it only 2 (top star) or 3 (bottom star) times, and draw extra line (goto or forward) and fill region
    #third step: make necessary revisions, such as adjusting angles
    #theoretically, this should work, but in practice, the logistics are very hard, with unidentifiable errors, which is why this process was not originally done
    draw_rectangle(-x/2,x/4,x,x/2,"#001489")
    draw_polygon("#FFCD00",3,(-47*x/200,x/4),(53*x/200,x/4),(53*x/200,-x/4))
    A = (19*5**0.5-38)/2
    for _ in range(9):
        draw_star(-18*x/50+x*_/16,x/4+A*x/400-x*_/16,19*x/400,0,"#FFFFFF")
    draw_rectangle(-x/2,5*x/4,x,x,"#8C92AC")
    draw_rectangle(-x/2,-x/4,x,x,"#8C92AC")
elif j in ("Bulgaria", "Republic of Bulgaria", "BG", "B.G.", "BGR", "B.G.R."):
    draw_rectangle(-x/2,3*x/10,x,x/5,"#FFFFFF")
    draw_rectangle(-x/2,x/10,x,x/5,"#00966E")
    draw_rectangle(-x/2,-x/10,x,x/5,"#D62612")
elif j in ("China", "People's Republic of China", "CN", "C.N.", "CHN", "C.H.N."):
    theta1 = math.degrees(math.atan2(3,5))
    theta2 = math.degrees(math.atan2(1,7))
    theta3 = math.degrees(math.atan2(-2,7))
    theta4 = math.degrees(math.atan2(-4,5))
    draw_rectangle(-x/2,x/3,x,2*x/3,"#EE1C25")
    draw_star(-x/3,x/6,x/10,0,"#FFFF00")
    draw_star(-x/6,4*x/15,x/30,theta1+18,"#FFFF00")
    draw_star(-x/10,x/5,x/30,theta2+18,"#FFFF00")
    draw_star(-x/10,x/10,x/30,theta3+18,"#FFFF00")
    draw_star(-x/6,x/30,x/30,theta4+18,"#FFFF00")
elif j in ("Czechia", "Czech Republic", "CZ", "C.Z.", "CZE", "C.Z.E."):
    draw_polygon("#11457E",3,(-x/2,x/3),(0,0),(-x/2,-x/3))
    draw_polygon("#FFFFFF",4,(-x/2,x/3),(x/2,x/3),(x/2,0),(0,0))
    draw_polygon("#D7141A",4,(-x/2,-x/3),(x/2,-x/3),(x/2,0),(0,0))
elif j in ("Denmark", "Kingdom of Denmark", "DK", "D.K.", "DNK", "D.N.K.", "DEN", "D.E.N."):
    draw_rectangle(-x/2,14*x/37,x,28*x/37,"#C8102E")
    draw_rectangle(-13*x/74,14*x/37,4*x/37,28*x/37,"#FFFFFF")
    draw_rectangle(-x/2,x/14,x,4*x/37,"#FFFFFF")
elif j in ("Estonia", "Republic of Estonia", "EE", "E.E.", "EST", "E.S.T."):
    draw_rectangle(-x/2,7*x/22,x,7*x/33,"#0072CE")
    draw_rectangle(-x/2,7*x/66,x,7*x/33,"#000000")
    draw_rectangle(-x/2,-7*x/66,x,7*x/33,"#FFFFFF")
elif j in ("Finland", "Republic of Finland", "FI", "F.I.", "FIN", "F.I.N."):
    draw_rectangle(-x/2,11*x/36,x,11*x/18,"#FFFFFF")
    draw_rectangle(-2*x/9,11*x/36,x/6,11*x/18,"#002F6C")
    draw_rectangle(-x/2,x/12,x,x/6,"#002F6C")
elif j in ("France", "French Republic", "FR", "F.R.", "FRA", "F.R.A."):
    draw_rectangle(-x/2,x/3,x/3,2*x/3,"#000091")
    draw_rectangle(-x/6,x/3,x/3,2*x/3,"#FFFFFF")
    draw_rectangle(x/6,x/3,x/3,2*x/3,"#E1000F")
elif j in ("Germany", "Federal Republic of Germany", "DE", "D.E.", "DEU", "D.E.U.", "GER", "G.E.R."):
    draw_rectangle(-x/2,3*x/10,x,x/5,"#000000")
    draw_rectangle(-x/2,x/10,x,x/5,"#FF0000")
    draw_rectangle(-x/2,-x/10,x,x/5,"#FFCC00")
elif j in ("Greece", "Hellenic Republic", "GR", "G.R.", "GRC", "G.R.C.", "EL", "E.L."):
    draw_rectangle(-x/2,x/3,x,2*x/3,"#FFFFFF")
    for i in range(2):
        for j in range(2):
            draw_rectangle(-x/2+2*i*x/9,x/3-2*j*x/9,4*x/27,4*x/27,"#0D5EAF")
    for _ in range(3):
        draw_rectangle(-7*x/54,x/3-4*_*x/27,17*x/27,2*x/27,"#0D5EAF")
    for _ in range(2):
        draw_rectangle(-x/2,-x/9-4*_*x/27,x,2*x/27,"#0D5EAF")
elif j in ("Hungary", "HU", "H.U.", "HUN", "H.U.N."):
    draw_rectangle(-x/2,x/4,x,x/6,"#CE2939")
    draw_rectangle(-x/2,x/12,x,x/6,"#FFFFFF")
    draw_rectangle(-x/2,-x/12,x,x/6,"#477050")
elif j in ("Japan", "JP", "J.P.", "JPN", "J.P.N.", "Jap"):
    draw_rectangle(-x/2,x/3,x,2*x/3,"#FFFFFF")
    draw_circle(0,0,x/5,"#BC002D")
elif j in ("Iceland", "IS", "I.S.", "ISL", "I.S.L."):
    draw_rectangle(-x/2,9*x/25,x,18*x/25,"#02529C")
    draw_rectangle(-11*x/50,9*x/25,4*x/25,18*x/25,"#FFFFFF")
    draw_rectangle(-x/2,2*x/25,x,4*x/25,"#FFFFFF")
    draw_rectangle(-9*x/50,9*x/25,2*x/25,18*x/25,"#DC1E35")
    draw_rectangle(-x/2,x/25,x,2*x/25,"#DC1E35")
elif j in ("India", "Republic of India", "Bharat", "IN", "I.N.", "IND", "I.N.D."):
    draw_rectangle(-x/2,x/3,x,2*x/9,"#FF671F")
    draw_rectangle(-x/2,x/9,x,2*x/9,"#FFFFFF")
    draw_rectangle(-x/2,-x/9,x,2*x/9,"#046A38")
    draw_circle(0,0,37*x/360,"#06038D")
    draw_circle(0,0,4*x/45,"#FFFFFF")
    draw_circle(0,0,4*x/225,"#06038D")
    for _ in range(24):
        sin = math.sin(math.radians(15*_))
        cos = math.cos(math.radians(15*_))
        smallang = math.degrees(math.sin(1/16))
        largeang = math.degrees(math.sin(3/32))
        sinsmallangp = math.sin(math.radians(15*_+smallang))
        cossmallangp = math.cos(math.radians(15*_+smallang))
        sinlargeangp = math.sin(math.radians(15*_+largeang))
        coslargeangp = math.cos(math.radians(15*_+largeang))
        sinsmallangn = math.sin(math.radians(15*_-smallang))
        cossmallangn = math.cos(math.radians(15*_-smallang))
        sinlargeangn = math.sin(math.radians(15*_-largeang))
        coslargeangn = math.cos(math.radians(15*_-largeang))
        draw_polygon("#06038D",5,(cossmallangp*4*x/225,sinsmallangp*4*x/225),(coslargeangp*8*x/225,sinlargeangp*8*x/225),(cos*4*x/45,sin*4*x/45),(coslargeangn*8*x/225,sinlargeangn*8*x/225),(cossmallangn*4*x/225,sinsmallangn*4*x/225))
    for _ in range(24):
        draw_circle(math.cos(math.radians(15/2+15*_))*4*x/45,math.sin(math.radians(15/2+15*_))*4*x/45,7*x/1800,"#06038D")
elif j in ("Indonesia", "Republic of Indonesia", "ID", "I.D.", "IDN", "I.D.N."):
    draw_rectangle(-x/2,x/3,x,x/3,"#FF0000")
    draw_rectangle(-x/2,0,x,x/3,"#FFFFFF")
elif j in ("Ireland", "IE", "I.E.", "IRL", "I.R.L."):
    draw_rectangle(-x/2,x/4,x/3,x/2,"#169B62")
    draw_rectangle(-x/6,x/4,x/3,x/2,"#FFFFFF")
    draw_rectangle(x/6,x/4,x/3,x/2,"#FF883E")
elif j in ("Italy", "Italian Republic", "IT", "I.T.", "ITA", "I.T.A."):
    draw_rectangle(-x/2,x/3,x/3,2*x/3,"#008C45")
    draw_rectangle(-x/6,x/3,x/3,2*x/3,"#F4F5F0")
    draw_rectangle(x/6,x/3,x/3,2*x/3,"#CD212A")
elif j in ("Jordan", "Hashemite Kingdom of Jordan", "JO", "J.O.", "JOR", "J.O.R."):
    draw_rectangle(-x/2,x/4,x,x/6,"#000000")
    draw_rectangle(-x/2,x/12,x,x/6,"#FFFFFF")
    draw_rectangle(-x/2,-x/12,x,x/6,"#007A3D")
    draw_polygon("#CE1126",3,(-x/2,-x/4),(-x/2,x/4),(0,0))
    draw_general_star(-x/2+x*(21*5**0.5-21)/168,0,x/56,x/28,7,270/7,"#FFFFFF")
elif j in ("Kuwait", "State of Kuwait", "KW", "K.W.", "KWT", "K.W.T."):
    draw_polygon("#000000",4,(-x/2,x/4),(-x/4,x/12),(-x/4,-x/12),(-x/2,-x/4))
    draw_polygon("#007A3D",4,(-x/2,x/4),(x/2,x/4),(x/2,x/12),(-x/4,x/12))
    draw_rectangle(-x/4,x/12,3*x/4,x/6,"#FFFFFF")
    draw_polygon("#CE1126",4,(-x/2,-x/4),(x/2,-x/4),(x/2,-x/12),(-x/4,-x/12))
elif j in ("Laos", "Lao People’s Democratic Republic", "Lao PDR", "Lao P.D.R.", "LA", "L.A.", "LAO", "L.A.O."):
    draw_rectangle(-x/2,x/3,x,2*x/3,"#002868")
    draw_rectangle(-x/2,x/3,x,x/6,"#CE1126")
    draw_rectangle(-x/2,-x/6,x,x/6,"#CE1126")
    draw_circle(0,0,2*x/15,"#FFFFFF")
elif j in ("Latvia", "Republic of Latvia", "LV", "L.V.", "LVA", "L.V.A."):
    draw_rectangle(-x/2,x/4,x,x/5,"#9D2235")
    draw_rectangle(-x/2,x/20,x,x/10,"#FFFFFF")
    draw_rectangle(-x/2,-x/20,x,x/5,"#9D2235")
elif j in ("Lithuania", "Republic of Lithuania", "LT", "L.T.", "LTU", "L.T.U."):
    draw_rectangle(-x/2,3*x/10,x,x/5,"#FDB913")
    draw_rectangle(-x/2,x/10,x,x/5,"#006A44")
    draw_rectangle(-x/2,-x/10,x,x/5,"#C1272D")
elif j in ("Luxembourg", "Grand Duchy of Luxembourg", "LU", "L.U.", "LUX", "L.U.X."):
    draw_rectangle(-x/2,3*x/10,x,x/5,"#EF3340")
    draw_rectangle(-x/2,x/10,x,x/5,"#FFFFFF")
    draw_rectangle(-x/2,-x/10,x,x/5,"#00A3E0")
elif j in ("Malaysia", "MY", "M.Y.", "MYS", "M.Y.S."):
    draw_rectangle(-x/2,x/4,x,x/2,"#FFFFFF")
    for _ in range(4):
        draw_rectangle(0,x/4-x*_/14,x/2,x/28,"#CC0001")
    for _ in range(3):
        draw_rectangle(-x/2,-x/28-x*_/14,x,x/28,"#CC0001")
    draw_rectangle(-x/2,x/4,x/2,2*x/7,"#010066")
    draw_circle(-33*x/112,3*x/28,3*x/28,"#FFCC00")
    draw_circle(-13*x/48,3*x/28,2*x/21,"#010066")
    draw_general_star(-3*x/16,3*x/28,x/28,5*x/56,16,0,"#FFCC00")
elif j in ("Maldives", "Republic of the Maldives", "the Maldives", "MV", "M.V.", "MDV", "M.D.V."):
    draw_rectangle(-x/2,x/3,x,2*x/3,"#C8102E")
    draw_rectangle(-x/3,x/6,2*x/3,x/3,"#00843D")
    draw_circle(x/24,0,-x/9,"#FFFFFF")
    draw_circle(x/12,0,-x/9,"#00843D")
elif j in ("Marshall Islands", "Marshalls", "Republic of the Marshall Islands", "RMI", "R.M.I.", "MH", "M.H.", "MHL", "M.H.L."):
    draw_rectangle(-x/2,5*x/19,x,10*x/19,"#003893")
    draw_polygon("#DD7500",4,(-x/2,-113*x/475),(x/2,121*x/475),(x/2,72*x/475),(-x/2,-117*x/475))
    draw_polygon("#FFFFFF",4,(-x/2,-117*x/475),(x/2,72*x/475),(x/2,23*x/475),(-x/2,-121*x/475))
    R = (84371-119*280381**0.5)/234
    draw_general_star(-x/2+R*x/475,5*x/19-R*x/475,49*x/950,111*x/950,24,0,"#FFFFFF")
    largeDistance = 9*x/190*math.cos(math.radians(7.5))
    shortDistance = 9*x/190*math.sin(math.radians(7.5))
    draw_polygon("#FFFFFF",3,(-x/2+R*x/475-shortDistance,5*x/19-R*x/475+largeDistance),(-x/2+R*x/475+shortDistance,5*x/19-R*x/475+largeDistance),(-x/2+R*x/475,5*x/19-R*x/475+31*x/190))
    draw_polygon("#FFFFFF",3,(-x/2+R*x/475+largeDistance,5*x/19-R*x/475+shortDistance),(-x/2+R*x/475+largeDistance,5*x/19-R*x/475-shortDistance),(-x/2+R*x/475+31*x/190,5*x/19-R*x/475))
    draw_polygon("#FFFFFF",3,(-x/2+R*x/475+shortDistance,5*x/19-R*x/475-largeDistance),(-x/2+R*x/475-shortDistance,5*x/19-R*x/475-largeDistance),(-x/2+R*x/475,5*x/19-R*x/475-31*x/190))
    draw_polygon("#FFFFFF",3,(-x/2+R*x/475-largeDistance,5*x/19-R*x/475-shortDistance),(-x/2+R*x/475-largeDistance,5*x/19-R*x/475+shortDistance),(-x/2+R*x/475-31*x/190,5*x/19-R*x/475))
elif j in ("Micronesia", "Federated States of  Micronesia", "FM", "F.M.", "FSM", "F.S.M."):
    draw_rectangle(-x/2,5*x/19,x,10*x/19,"#ABCAE9")
    draw_star(0,3*x/19,x/19,0,"#FFFFFF")
    draw_star(-3*x/19,0,x/19,18,"#FFFFFF")
    draw_star(3*x/19,0,x/19,-18,"#FFFFFF")
    draw_star(0,-3*x/19,x/19,180,"#FFFFFF")
elif j in ("Monaco", "Principality of Monaco", "MC", "M.C.", "MCO", "M.C.O."):
    draw_rectangle(-x/2,2*x/5,x,2*x/5,"#CE1126")
    draw_rectangle(-x/2,0,x,2*x/5,"#FFFFFF")
elif j in ("Myanmar", "Republic of the Union of Myanmar", "MM", "M.M.", "MMR", "M.M.R.", ):
    draw_rectangle(-x/2,x/3,x,2*x/9,"#FECB00")
    draw_rectangle(-x/2,x/9,x,2*x/9,"#34B233")
    draw_rectangle(-x/2,-x/9,x,2*x/9,"#EA2839")
    draw_star(0,0,2*x/9,0,"#FFFFFF")
elif j in ("Nauru", "Republic of Nauru", "NR", "N.R.", "NRU", "N.R.U."):
    draw_rectangle(-x/2,x/4,x,x/2,"#012169")
    draw_rectangle(-x/2,x/48,x,x/24,"#FFC72C")
    draw_general_star(-x/4,-5*x/48,x/24,x/12,12,0,"#FFFFFF")
elif j in ("Netherlands", "the Netherlands", "NL", "N.L.", "NLD", "N.L.D."):
    draw_rectangle(-x/2,x/3,x,2*x/9,"#AD1D25")
    draw_rectangle(-x/2,x/9,x,2*x/9,"#FFFFFF")
    draw_rectangle(-x/2,-x/9,x,2*x/9,"#1E4785")
elif j in ("New Zealand", "NZ", "N.Z.", "NZL", "N.Z.L."):
    draw_rectangle(-x/2,x/4,x,x/2,"#012169")
    draw_UnionJack(-x/2,x/4,x/2,x/4,"#FFFFFF","#C91235","#012169")
    draw_star(x/4,3*x/20,x*(12*((5-5**0.5)/10)**0.5+1+5**0.5)/240,0,"#FFFFFF")
    draw_star(x/4-14*math.cos(math.radians(8))*x/120,x/20-14*math.sin(math.radians(8))*x/120,x*(12*((5-5**0.5)/10)**0.5+1+5**0.5)/240,0,"#FFFFFF")
    draw_star(x/4+12*math.cos(math.radians(8))*x/120,x/20+12*math.sin(math.radians(8))*x/120,x*(10*((5-5**0.5)/10)**0.5+1+5**0.5)/240,0,"#FFFFFF")
    draw_star(x/4,-3*x/20,x*(14*((5-5**0.5)/10)**0.5+1+5**0.5)/240,0,"#FFFFFF")
    draw_star(x/4,3*x/20,3*x/(120*math.cos(math.radians(18))),0,"#C91235")
    draw_star(x/4-14*math.cos(math.radians(8))*x/120,x/20-14*math.sin(math.radians(8))*x/120,3*x/(120*math.cos(math.radians(18))),0,"#C91235")
    draw_star(x/4+12*math.cos(math.radians(8))*x/120,x/20+12*math.sin(math.radians(8))*x/120,2.5*x/(120*math.cos(math.radians(18))),0,"#C91235")
    draw_star(x/4,-3*x/20,3.5*x/(120*math.cos(math.radians(18))),0,"#C91235")
elif j in ("North Korea", "Democratic People's Republic of Korea", "DPRK", "D.P.R.K.", "DPR Korea", "D.P.R. Korea", "KP", "K.P.", "PRK", "P.R.K."):
    draw_rectangle(-x/2,x/4,x,x/2,"#ED1C27")
    draw_rectangle(-x/2,x/4,x,x/12,"#024FA2")
    draw_rectangle(-x/2,x/6,x,x/72,"#FFFFFF")
    draw_rectangle(-x/2,-11*x/72,x,x/72,"#FFFFFF")
    draw_rectangle(-x/2,-x/6,x,x/12,"#024FA2")
    draw_circle(-x/6,0,x/9,"#FFFFFF")
    draw_star(-x/6,0,31*x/288,0,"#ED1C27")
elif j in ("North Macedonia", "Macedonia", "Republic of North Macedonia", "MK", "M.K.", "MKD", "M.K.D."):
    draw_rectangle(-x/2,x/4,x,x/2,"#CE2028")
    l = 15*x/(56*34**0.5)
    w = 9*x/(56*34**0.5)
    draw_polygon("#F9D616",3,(-x/2,x/4),(-7*x/20,x/4),(l,-w))
    draw_polygon("#F9D616",3,(-x/20,x/4),(x/20,x/4),(0,3*x/56))
    draw_polygon("#F9D616",3,(7*x/20,x/4),(x/2,x/4),(-l,-w))
    draw_polygon("#F9D616",3,(x/2,x/20),(x/2,-x/20),(0,0))
    draw_polygon("#F9D616",3,(7*x/20,-x/4),(x/2,-x/4),(-l,w))
    draw_polygon("#F9D616",3,(-x/20,-x/4),(x/20,-x/4),(0,-3*x/56))
    draw_polygon("#F9D616",3,(-x/2,-x/4),(-7*x/20,-x/4),(l,w))
    draw_polygon("#F9D616",3,(-x/2,x/20),(-x/2,-x/20),(0,0))
    draw_circle(0,0,5*x/56,"#CE2028")
    draw_circle(0,0,x/14,"#F9D616")
elif j in ("Norway", "Kingdom of Norway", "NO", "N.O.", "NOR", "N.O.R."):
    draw_rectangle(-x/2,4*x/11,x,8*x/11,"#BA0C2F")
    draw_rectangle(-5*x/22,4*x/11,2*x/11,8*x/11,"#FFFFFF")
    draw_rectangle(-x/2,x/11,x,2*x/11,"#FFFFFF")
    draw_rectangle(-2*x/11,4*x/11,x/11,8*x/11,"#00205B")
    draw_rectangle(-x/2,x/22,x,x/11,"#00205B")
elif j in ("Pakistan", "Islamic Republic of Pakistan", "PA", "P.A.", "PAK", "P.A.K."):
    draw_rectangle(-x/2,x/3,x/4,2*x/3,"#FFFFFF")
    draw_rectangle(-x/4,x/3,3*x/4,2*x/3,"#00401A")
    draw_circle(x/8,0,x/5,"#FFFFFF")
    hypotenuse = (11.25**2+10**2)**0.5
    draw_circle(x/8+x/30*11.25*(hypotenuse-13)/hypotenuse,x/30*10*(hypotenuse-13)/hypotenuse,11*x/60,"#00401A")
    draw_star(x/8+x/30*11.25*4/hypotenuse,x/30*10*4/hypotenuse,x/15,math.degrees(math.atan2(10,11.25))-18,"#FFFFFF")
elif j in ("Palau", "Republic of Palau", "PW", "P.W.", "PLW", "P.L.W."):
    draw_rectangle(-x/2,5*x/16,x,5*x/8,"#0085CA")
    draw_circle(-x/16,0,3*x/16,"#FFD100")
elif j in ("Philippines", "Republic of the Philippines", "the Philippines", "PH", "P.H.", "PHL", "P.H.L."):
    draw_rectangle(-x/2,x/4,x,x/4,"#0038A8")
    draw_rectangle(-x/2,0,x,x/4,"#CE1126")
    draw_polygon("#FFFFFF",3,(-x/2,x/4),(-x/2,-x/4),((-2*x+x*3**0.5)/4,0))
    draw_general_star((-104*x+45*x*3**0.5)/180,0,x/90,x/36,5,0,"#FCD116")
    draw_general_star(-83*x/180,(45*x-7*x*3**0.5)/180,x/90,x/36,5,120,"#FCD116")
    draw_general_star(-83*x/180,(-45*x+7*x*3**0.5)/180,x/90,x/36,5,240,"#FCD116")
    draw_circle(-31*x/90,0,x/20,"#FCD116")
    l = 19/(math.cos(math.radians(11.25))+math.sin(math.radians(11.25)))
    for _ in range(8):
        draw_polygon("#FCD116",3,(-31*x/90,0),(-31*x/90+math.sin(math.radians(45*_-7.5))*17*x/180,math.cos(math.radians(45*_-7.5))*17*x/180),(-31*x/90+math.sin(math.radians(45*_-11.25))*l*x/180,math.cos(math.radians(45*_-11.25))*l*x/180))
    k = 19/(math.cos(math.radians(3.75))+math.sin(math.radians(3.75)))
    for _ in range(8):
        draw_polygon("#FCD116",4,(-31*x/90,0),(-31*x/90+math.sin(math.radians(45*_+3.75))*k*x/180,math.cos(math.radians(45*_+3.75))*k*x/180),(-31*x/90+math.sin(math.radians(45*_))*19*x/180,math.cos(math.radians(45*_))*19*x/180),(-31*x/90+math.sin(math.radians(45*_-3.75))*k*x/180,math.cos(math.radians(45*_-3.75))*k*x/180))
    for _ in range(8):
        draw_polygon("#FCD116",3,(-31*x/90,0),(-31*x/90+math.sin(math.radians(45*_+11.25))*l*x/180,math.cos(math.radians(45*_+11.25))*l*x/180),(-31*x/90+math.sin(math.radians(45*_+7.5))*17*x/180,math.cos(math.radians(45*_+7.5))*17*x/180))
elif j in ("Poland", "Republic of Poland", "PL", "P.L.", "POL", "P.O.L."):
    draw_rectangle(-x/2,5*x/16,x,5*x/16,"#FFFFFF")
    draw_rectangle(-x/2,0,x,5*x/16,"#DC143C")
elif j in ("Qatar", "State of Qatar", "QA", "Q.A.", "QAT", "Q.A.T."):
    draw_rectangle(-x/2,11*x/56,x,11*x/28,"#FFFFFF")
    draw_rectangle(-19*x/150,11*x/56,47*x/75,11*x/28,"#8A1538")
    draw_polygon("#8A1538",3,(-31*x/150,11*x/56),(-19*x/150,11*x/56),(-19*x/150,11*x/63))
    for _ in range(8):
        draw_polygon("#8A1538",3,(-19*x/150,11*x/63-11*_*x/252),(-31*x/150,11*x/72-11*_*x/252),(-19*x/150,11*x/84-11*_*x/252))
    draw_polygon("#8A1538",3,(-31*x/150,-11*x/56),(-19*x/150,-11*x/56),(-19*x/150,-11*x/63))
elif j in ("Romania", "RO", "R.O.", "ROU", "R.O.U."):
    draw_rectangle(-x/2,x/3,x/3,2*x/3,"#002B7F")
    draw_rectangle(-x/6,x/3,x/3,2*x/3,"#FCD116")
    draw_rectangle(x/6,x/3,x/3,2*x/3,"#CE1126")
elif j in ("Russia", "Russian Federation", "RU", "R.U.", "RU", "RUS"):
    draw_rectangle(-x/2,x/3,x,2*x/9,"#FFFFFF")
    draw_rectangle(-x/2,x/9,x,2*x/9,"#0032A0")
    draw_rectangle(-x/2,-x/9,x,2*x/9,"#DA291C")
elif j in ("Samoa", "Independent State of Samoa", "WS", "W.S.", "WSM", "W.S.M."):
    draw_rectangle(-x/2,x/4,x,x/2,"#CE1126")
    draw_rectangle(-x/2,x/4,x/2,x/4,"#002B7F")
    radiusToLengthRatio = 1/(2*math.cos(math.radians(18)))
    quantityHeightMinusRadiusToLengthRatio = math.cos(math.radians(18))-radiusToLengthRatio
    draw_star(-x/4,23*x/96-radiusToLengthRatio*x/18,radiusToLengthRatio*x/18,0,"#FFFFFF")
    draw_star(-47*x/144,17*x/96-radiusToLengthRatio*x/18,radiusToLengthRatio*x/18,0,"#FFFFFF")
    draw_star(-11*x/64,3*x/16-5*radiusToLengthRatio*x/96,5*radiusToLengthRatio*x/96,0,"#FFFFFF")
    draw_star(-61*x/288,13*x/144+5*quantityHeightMinusRadiusToLengthRatio*x/144,5*radiusToLengthRatio*x/144,0,"#FFFFFF")
    draw_star(-x/4,x/96+5*quantityHeightMinusRadiusToLengthRatio*x/72,5*radiusToLengthRatio*x/72,0,"#FFFFFF")
elif j in ("Singapore", "Republic of Singapore", "SG", "S.G.", "SGP", "S.G.P."):
    draw_rectangle(-x/2,x/3,x,x/3,"#EE2536")
    draw_rectangle(-x/2,0,x,x/3,"#FFFFFF")
    draw_circle(-3119*x/10800,x/6,53*x/432,"#FFFFFF")
    draw_circle(-133*x/600,x/6,29*x/216,"#EE2536")
    distanceToCenter = 19*x/270
    draw_star(-133*x/600,x/6+distanceToCenter,23*x/720,0,"#FFFFFF")
    draw_star(-133*x/600+distanceToCenter*math.cos(math.radians(18)),x/6+distanceToCenter*math.sin(math.radians(18)),23*x/720,0,"#FFFFFF")
    draw_star(-133*x/600+distanceToCenter*math.cos(math.radians(54)),x/6-distanceToCenter*math.sin(math.radians(54)),23*x/720,0,"#FFFFFF")
    draw_star(-133*x/600-distanceToCenter*math.cos(math.radians(54)),x/6-distanceToCenter*math.sin(math.radians(54)),23*x/720,0,"#FFFFFF")
    draw_star(-133*x/600-distanceToCenter*math.cos(math.radians(18)),x/6+distanceToCenter*math.sin(math.radians(18)),23*x/720,0,"#FFFFFF")
elif j in ("Soloman Islands", "Solomans", "SB", "S.B", "SLB", "S.L.B."):
    draw_rectangle(-x/2,x/4,x,x/2,"#FFFFFF")
    draw_polygon("#0051BA",3,(-x/2,-x/4+9*x*5**0.5/800),(-x/2,x/4),(x/2-9*x*5**0.5/400,x/4))
    draw_polygon("#FCD116",6,(-x/2+9*x*5**0.5/400,-x/4),(-x/2,-x/4),(-x/2,-x/4+9*x*5**0.5/800),(x/2-9*x*5**0.5/400,x/4),(x/2,x/4),(x/2,x/4-9*x*5**0.5/800))
    draw_polygon("#215B33",3,(-x/2+9*x*5**0.5/400,-x/4),(x/2,-x/4),(x/2,x/4-9*x*5**0.5/800))
    draw_star(-13*x/40-13*x*2**0.5/200,x/10+13*x*2**0.5/200,x/20,0,"#FFFFFF")
    draw_star(-13*x/40+13*x*2**0.5/200,x/10+13*x*2**0.5/200,x/20,0,"#FFFFFF")
    draw_star(-13*x/40,x/10,x/20,0,"#FFFFFF")
    draw_star(-13*x/40-13*x*2**0.5/200,x/10-13*x*2**0.5/200,x/20,0,"#FFFFFF")
    draw_star(-13*x/40+13*x*2**0.5/200,x/10-13*x*2**0.5/200,x/20,0,"#FFFFFF")
elif j in ("South Korea", "Republic of Korea", "ROK", "R.O.K.", "SK", "S.K.", "KOR", "K.O.R."):
    draw_rectangle(-x/2,x/3,x,2*x/3,"#FFFFFF")
    t.goto(x*13**0.5/26,-x*13**0.5/39)
    t.setheading(math.degrees(math.atan2(3,2)))
    t.fillcolor("#CD2E3A")
    t.begin_fill()
    t.circle(x/6,180)
    t.left(90)
    t.forward(x/3)
    t.end_fill()
    t.right(90)
    t.fillcolor("#0047A0")
    t.begin_fill()
    t.circle(-x/6,180)
    t.right(90)
    t.forward(x/3)
    t.end_fill()
    draw_circle(-x*13**0.5/52,x*13**0.5/78,x/12,"#CD2E3A")
    draw_circle(x*13**0.5/52,-x*13**0.5/78,x/12,"#0047A0")
    def draw_one_rectangle():
        t.fillcolor("#000000")
        t.begin_fill()
        for _ in range(2):
            t.forward(x/36)
            t.right(90)
            t.forward(x/6)
            t.right(90)
        t.end_fill()
        t.forward(x/24)
    def draw_two_rectangles():
        def draw_oneofthetwosmallrectangles():
            t.fillcolor("#000000")
            t.begin_fill()
            for _ in range(2):
                t.forward(x/36)
                t.right(90)
                t.forward(11*x/144)
                t.right(90)
            t.end_fill()
        draw_oneofthetwosmallrectangles()
        t.right(90)
        t.forward(13*x/144)
        t.left(90)
        draw_oneofthetwosmallrectangles()
        t.forward(x/24)
        t.left(90)
        t.forward(13*x/144)
        t.right(90)
    v = x*13**0.5/468
    t.goto(-33*v,35*v)
    t.setheading(math.degrees(math.atan2(-2,3)))
    for _ in range(3):
        draw_one_rectangle()
    t.goto(-45*v,-17*v)
    t.setheading(math.degrees(math.atan2(2,3)))
    draw_one_rectangle()
    draw_two_rectangles()
    draw_one_rectangle()
    t.goto(21*v,27*v)
    t.setheading(math.degrees(math.atan2(2,3)))
    draw_two_rectangles()
    draw_one_rectangle()
    draw_two_rectangles()
    t.goto(33*v,-9*v)
    t.setheading(math.degrees(math.atan2(-2,3)))
    for _ in range(3):
        draw_two_rectangles()
elif j in ("Sweden", "Kingdom of Sweden", "SE", "S.E.", "SWE", "S.W.E."):
    draw_rectangle(-x/2,5*x/16,x,5*x/8,"#006AA7")
    draw_rectangle(-3*x/16,5*x/16,x/8,5*x/8,"#FECC02")
    draw_rectangle(-x/2,x/16,x,x/8,"#FECC02")
elif j in ("Switzerland", "Swiss Confederation", "CH", "C.H.", "CHE", "C.H.E."):
    draw_rectangle(-x/2,x/2,x,x,"#DA291C")
    draw_rectangle(-3*x/32,5*x/16,3*x/16,5*x/8,"#FFFFFF")
    draw_rectangle(-5*x/16,3*x/32,5*x/8,3*x/16,"#FFFFFF")
elif j in ("Syria", "Syrian Arab Republic", "SY", "S.Y.", "SYR", "S.Y.R."):
    draw_rectangle(-x/2,x/3,x,2*x/9,"#007A3D")
    draw_rectangle(-x/2,x/9,x,2*x/9,"#FFFFFF")
    draw_rectangle(-x/2,-x/9,x,2*x/9,"#000000")
    for _ in range(3):
        draw_star(-x/4+_*x/4,-x/108,5*x/54,0,"#CE1126")
elif j in ("Thailand", "Kingdom of Thailand", "TH", "T.H.", "THA", "T.H.A."):
    draw_rectangle(-x/2,x/3,x,2*x/3,"#2D2A4A")
    draw_rectangle(-x/2,x/3,x,x/9,"#A51931")
    draw_rectangle(-x/2,2*x/9,x,x/9,"#F4F5F8")
    draw_rectangle(-x/2,-x/9,x,x/9,"#F4F5F8")
    draw_rectangle(-x/2,-2*x/9,x,x/9,"#A51931")
elif j in ("Timor-Leste", "East Timor", "Democratic Republic of Timor-Leste", "TL", "T.L.", "TLS", "T.L.S."):
    draw_rectangle(-x/2,x/4,x,x/2,"#DA291C")
    draw_polygon("#FFC72C",3,(-x/2,x/4),(-x/2,-x/4),(0,0))
    draw_polygon("#000000",3,(-x/2,x/4),(-x/2,-x/4),(-x/6,0))
    draw_star(-7*x/18,0,x/12,math.degrees(math.atan2(4,9)),"#FFFFFF")
elif j in ("Tonga", "Kingdom of Tonga", "TO", "T.O.", "TON", "T.O.N."):
    draw_rectangle(-x/2,x/4,x,x/2,"#C10000")
    draw_rectangle(-x/2,x/4,5*x/12,x/4,"#FFFFFF")
    draw_rectangle(-55*x/168,19*x/84,x/14,17*x/84,"#C10000")
    draw_rectangle(-11*x/28,9*x/56,17*x/84,x/14,"#C10000")
elif j in ("Türkiye", "Turkey", "Republic of Türkiye", "Republic of Turkey", "TR", "T.R.", "TUR", "T.U.R."):
    draw_rectangle(-x/2,x/3,x,2*x/3,"#E30A17")
    draw_circle(-x/6,0,x/6,"#FFFFFF")
    draw_circle(-x/8,0,2*x/15,"#E30A17")
    draw_star(17*x/360,0,x/12,18,"#FFFFFF")
elif j in ("Ukraine", "UA", "U.A.", "UKR", "U.K.R."):
    draw_rectangle(-x/2,x/3,x,x/3,"#0057B7")
    draw_rectangle(-x/2,0,x,x/3,"#FFD700")
elif j in ("United Arab Emirates", "UAE", "U.A.E.", "AE", "A.E.", "ARE", "A.R.E."):
    draw_rectangle(-x/2,x/4,x/4,x/2,"#C8102E")
    draw_rectangle(-x/4,x/4,3*x/4,x/6,"#00843D")
    draw_rectangle(-x/4,x/12,3*x/4,x/6,"#FFFFFF")
    draw_rectangle(-x/4,-x/12,3*x/4,x/6,"#000000")
elif j in ("United Kingdom", "Britain", "United Kingdom of Great Britain and Northern Ireland", "GB", "G.B.", "GBR", "G.B.R.", "UK", "U.K."):
    draw_UnionJack(-x/2,x/4,x,x/2,"#FFFFFF","#C8102E","#012169")
elif j in ("United States", "US", "U.S.", "America", "USA", "U.S.A.", "United States of America"):
    draw_rectangle(-x/2,5*x/19,2*x/5,70*x/247,"#0A3161")
    setA = {(-x/10,_*x/247,3*x/5,10*x/247,"#B31942") for _ in range(5,66,20)}
    setB = {(-x/10,_*x/247,3*x/5,10*x/247,"#FFFFFF") for _ in range(15,56,20)}
    setC = {(-x/2,_*x/247,x,10*x/247,"#B31942") for _ in range(-55,-14,20)}
    setD = {(-x/2,_*x/247,x,10*x/247,"#FFFFFF") for _ in range(-45,-4,20)}
    setRectangle = setA | setB | setC | setD
    for _ in setRectangle:
        a,b,c,d,e = _
        draw_rectangle(a,b,c,d,e)
    setE = {(-i*x/30,j*x/247,4*x/247,0,"#FFFFFF") for i in range(4,15,2) for j in range(2,59,14)}
    setF = {(-k*x/30,l*x/247,4*x/247,0,"#FFFFFF") for k in range(5,14,2) for l in range(9,52,14)}
    setStar = setE | setF
    for _ in setStar:
        a,b,c,d,e = _
        draw_star(a,b,c,d,e)
elif j in ("Uzbekistan", "Republic of Uzbekistan", "UZ", "U.Z.", "UZB", "U.Z.B."):
    draw_rectangle(-x/2,x/4,x,4*x/25,"#0099B5")
    draw_rectangle(-x/2,9*x/100,x,x/100,"#CE1126")
    draw_rectangle(-x/2,8*x/100,x,4*x/25,"#FFFFFF")
    draw_rectangle(-x/2,-2*x/25,x,x/100,"#CE1126")
    draw_rectangle(-x/2,-9*x/100,x,4*x/25,"#1EB53A")
    draw_circle(-9*x/25,17*x/100,3*x/50,"#FFFFFF")
    draw_circle(-17*x/50,17*x/100,3*x/50,"#0099B5")
    for i in range(3):
        for j in range(i+3):
            draw_star(-33*x/250-6*x*j/125,109*x/500-6*x*i/125,3*x/250,0,"#FFFFFF")
elif j in ("Vietnam", "Socialist Republic of Vietnam", "Viet Nam", "VN", "V.N.", "VNM", "V.N.M."):
    draw_rectangle(-x/2,x/3,x,2*x/3,"#DA251D")
    draw_star(0,0,x/5,0,"#FFFF00")
elif j in ("Yemen", "Republic of Yemen", "YE", "Y.E.", "YEM", "Y.E.M."):
    draw_rectangle(-x/2,x/3,x,2*x/9,"#CE1126")
    draw_rectangle(-x/2,x/9,x,2*x/9,"#FFFFFF")
    draw_rectangle(-x/2,-x/9,x,2*x/9,"#000000")
else:
    print("Country not found or unavailable. Please check spelling.")
print("To settle the ambiguity of what is and what is not a country, this function only includes UN member and observer states.")

t.pendown()

wn.mainloop()
