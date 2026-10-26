import turtle  # Načte knihovnu pro kreslení pomocí želvy.
import math  # Načte matematické funkce pro výpočty úhlů a souřadnic.
import random  # Načte funkce pro náhodná čísla.

random.seed(7)  # Nastaví počáteční hodnotu náhody, aby obrázek vypadal při každém spuštění stejně.

screen = turtle.Screen()  # Vytvoří kreslicí okno.
screen.setup(800, 480)  # Nastaví velikost okna na 800 × 480 pixelů.
screen.bgcolor("#12001c")  # Nastaví tmavě fialovou barvu pozadí.

t = turtle.Turtle()  # Vytvoří želvu, která bude kreslit.
t.speed(0)  # Nastaví kreslení na nejvyšší rychlost.

def stars():  # Definuje funkci, která nakreslí hvězdy.
    t.penup()  # Zvedne pero, aby želva při přesunu nekreslila čáru.
    for _ in range(70):  # Opakuje kreslení hvězdy celkem 70krát.
        x = random.randint(-390, 390)  # Vybere náhodnou vodorovnou souřadnici hvězdy.
        y = random.randint(-230, 230)  # Vybere náhodnou svislou souřadnici hvězdy.
        t.goto(x,y)  # Přesune želvu na vybrané souřadnice.
        t.dot(random.randint(2, 4), "white")  # Nakreslí bílou hvězdu náhodné velikosti.

def stem():  # Definuje funkci, která nakreslí stonek.
    t.penup()  # Zvedne pero před přesunem na začátek stonku.
    t.goto(0, 60)  # Přesune želvu na začátek stonku.
    t.setheading(-72)  # Nastaví směr kreslení stonku.
    t.color("#2e9e5b")  # Nastaví barvu stonku na zelenou.
    t.pensize(7)  # Nastaví tloušťku čáry stonku.
    t.pendown()  # Položí pero, aby želva začala kreslit.
    t.circle(-420,34)  # Nakreslí zakřivený stonek jako část kružnice.

def leaf(x, y, angle):  # Definuje funkci listu s pozicí x, y a směrem kreslení.
     t.penup()  # Zvedne pero před přesunem k listu.
     t.goto(x, y)  # Přesune želvu na zadané souřadnice listu.
     t.setheading(angle)  # Natočí želvu podle zadaného úhlu.
     t.color("#7fe0a3" , "#1f8a4c")  # Nastaví obrysovou a výplňovou barvu listu.
     t.pensize(2)  # Nastaví tloušťku obrysu listu.
     t.pendown()  # Položí pero, aby mohla želva kreslit list.
     t.begin_fill()  # Začne vyplňovat tvar listu barvou.
     t.circle(95, 60)  # Nakreslí první zakřivenou polovinu listu.
     t.left(120)  # Otočí želvu, aby mohla nakreslit druhou polovinu listu.
     t.circle(95, 60)  # Nakreslí druhou zakřivenou polovinu listu.
     t.end_fill()  # Uzavře tvar a vyplní list zelenou barvou.

def petal(size, edge, fill):  # Definuje funkci okvětního lístku s velikostí a barvami.
    t.color(edge, fill)  # Nastaví barvu obrysu a výplně lístku.
    t.pensize(2)  # Nastaví tloušťku obrysu lístku.
    t.begin_fill()  # Začne vyplňovat tvar lístku.
    t.circle(size, 80)  # Nakreslí první zakřivenou část lístku.
    t.left(100)  # Otočí želvu mezi oběma částmi lístku.
    t.circle(size, 80)  # Nakreslí druhou zakřivenou část lístku.
    t.left(100)  # Natočí želvu zpět pro další kreslení.
    t.end_fill()  # Uzavře a vyplní tvar lístku.

def bloom():  # Definuje funkci, která nakreslí květ z několika vrstev lístků.
    rings = [  # Uloží počet, velikost a barvy lístků jednotlivých vrstev.
        (8, 120, "#ff6fa8" , "#7d0a45"),  # Nastaví první, největší vrstvu lístků.
        (8, 102, "#ff7fb4" , "#a8125c"),  # Nastaví druhou vrstvu lístků.
        (7, 84, "#ff9cc6" , "#d81b78"),  # Nastaví třetí vrstvu lístků.
        (6, 66, "#ffb3d3" , "#f2559a"),  # Nastaví čtvrtou vrstvu lístků.
        (5, 50, "#ffd0e4" , "#ff8cc0"),  # Nastaví pátou vrstvu lístků.
        (4, 34, "#fff0f6" , "#ffc2dc"),  # Nastaví nejmenší vnitřní vrstvu lístků.
    ]  # Ukončí seznam nastavení vrstev květu.
    for count, size, edge, fill in rings:  # Projde nastavení každé vrstvy.
        shift = random.randint(0, 40)  # Náhodně pootočí lístky této vrstvy.
        for i in range(count):  # Opakuje kreslení podle počtu lístků ve vrstvě.
            t.penup()  # Zvedne pero před přesunem do středu květu.
            t.goto(0,60)  # Přesune želvu do středu květu.
            a = shift + i * 360 / count  # Vypočítá úhel pro aktuální lístek.
            t.setheading(a + random.uniform(-4, 4))  # Natočí lístek s malou náhodnou odchylkou.
            t.pendown()  # Položí pero, aby mohla želva lístek nakreslit.
            s = size * random.uniform(0.94, 1.04)  # Mírně náhodně upraví velikost lístku.
            petal(s, edge, fill)  # Nakreslí lístek zadané velikosti a barev.

def center():  # Definuje funkci, která nakreslí střed květu.
    t.penup()  # Zvedne pero před přesunem do středu květu.
    t.goto(0, 60)  # Přesune želvu do středu květu.
    t.dot(26, "#ffd54a")  # Nakreslí velký žlutý střed květu.
    for i in range(14):  # Opakuje kreslení drobných teček 14krát.
        a =  math.radians(i * 360 / 14)  # Převede úhel každé tečky na radiány.
        x =  math.cos(a) *20  # Vypočítá vodorovnou polohu tečky kolem středu.
        y = 60+ math.sin(a) * 20  # Vypočítá svislou polohu tečky kolem středu.
        t.goto(x, y)  # Přesune želvu na vypočítanou polohu.
        t.dot(5, "#ff9f1c")  # Nakreslí malou oranžovou tečku.
stars()  # Nakreslí hvězdy na pozadí.
stem()  # Nakreslí stonek květiny.
leaf(12, -40, 15)  # Nakreslí první list na stonku.
leaf(13, -110, 165)  # Nakreslí druhý list na stonku.
bloom()  # Nakreslí všechny vrstvy okvětních lístků.
center()  # Nakreslí žlutý a oranžový střed květu.
t.hideturtle()  # Skryje kurzor želvy po dokončení kreslení.
turtle.done()  # Ponechá okno otevřené, dokud ho uživatel nezavře.