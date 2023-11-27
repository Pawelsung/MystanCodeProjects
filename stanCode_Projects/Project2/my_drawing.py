"""
File: my_drawing.py
Name: Paul
----------------------
    Title: The Mighty Jerry
    As you can see, my Google account profile picture is Jerry from “Tom and Jerry”.
    If you’ve noticed this, you’ll know that I’m a huge fan.
    Initially, I had planned to create a triangular representation of Jerry
    with a large piece of cheese. However, during Lesson 3 this week, “Jerry”
    from “stanCode” inspired me with a brilliant idea. I decided to create an
    image that showcases the power of Jerry in assisting us with learning code.
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GLabel, GPolygon
from campy.graphics.gwindow import GWindow
window = GWindow(width=500, height=800)


def main():
    """
    Title: The Mighty Jerry
    As you can see, my Google account profile picture is Jerry from “Tom and Jerry”.
    If you’ve noticed this, you’ll know that I’m a huge fan.
    Initially, I had planned to create a triangular representation of Jerry
    with a large piece of cheese. However, during Lesson 3 this week, “Jerry”
    from “stanCode” inspired me with a brilliant idea. I decided to create an
    image that showcases the power of Jerry in assisting us with learning code.
    """
    base()
    neck()
    face()
    cloth()
    ear1()
    ear2()
    hair()
    eyebrow1()
    eyebrow2()
    nose()
    glass()
    glass_frame()
    eye()
    nostril()
    lip()
    bag()
    hide1()
    arm()
    card()
    fist()
    lines()
    self()
    weight()
    stan_code()
    title1()
    title2()
    beard()


def base():
    base1 = GRect(500, 800)
    base1.filled = True
    base1.fill_color = "#C0BDC1"
    base1.color = "#C0BDC1"
    window.add(base1)


def beard():
    line1 = GLine(315.5, 398.5, 361, 392)
    line2 = GLine(314.5, 405.5, 354, 405.5)
    line3 = GLine(313, 412, 355, 422)
    line4 = GLine(238, 390, 189.5, 383.5)
    line5 = GLine(238, 398.5, 201.5, 398.5)
    line6 = GLine(238.5, 405, 191.5, 415)
    window.add(line1)
    window.add(line2)
    window.add(line3)
    window.add(line4)
    window.add(line5)
    window.add(line6)


def title2():
    title = GLabel('Doraemon Jerry', x=60, y=150)
    title.font = "-60"
    title.color = "black"
    window.add(title)


def title1():
    title = GLabel('This is', x=20, y=80)
    title.font = "-60"
    title.color = "black"
    window.add(title)


def stan_code():
    stan = GLabel('stanCode', x=105, y=700)
    stan.font = "-80"
    stan.color = "white"
    window.add(stan)


def weight():
    weight1 = GLabel('weight', x=44, y=465)
    weight1.font = "-40"
    weight1.color = "#499083"
    window.add(weight1)


def self():
    self1 = GLabel('Self', x=190, y=800)
    self1.font = "-65"
    self1.color = "#4A4A7B"
    window.add(self1)


def lines():
    line1 = GLine(15, 539.5, 44, 500.5)
    line2 = GLine(44, 500.5, 83.5, 489)
    line3 = GLine(33.5, 552, 53.5, 525.5)
    line4 = GLine(53.5, 525.5, 73.5, 517.5)
    line5 = GLine(73.5, 517.5, 95, 513.5)
    line6 = GLine(49.5, 573.5, 69.5, 545)
    line7 = GLine(69.5, 545, 84.5, 536.5)
    line8 = GLine(68.5, 569.5, 84.5, 560)
    line9 = GLine(84.5, 560, 99, 546.5)
    line10 = GLine(99, 546.5, 103.5, 537.5)
    line11 = GLine(79.5, 586, 98, 574)
    window.add(line1)
    window.add(line2)
    window.add(line3)
    window.add(line4)
    window.add(line5)
    window.add(line6)
    window.add(line7)
    window.add(line8)
    window.add(line9)
    window.add(line10)
    window.add(line11)


def card():
    card1 = GPolygon()
    card1.add_vertex((187, 412.5))
    card1.add_vertex((188, 465.5))
    card1.add_vertex((23, 479))
    card1.add_vertex((18, 413.5))
    card1.filled = True
    card1.fill_color = "#F2F2F1"
    window.add(card1)


def fist():
    fist1 = GPolygon()
    fist1.add_vertex((82.5, 467))
    fist1.add_vertex((89.5, 474))
    fist1.add_vertex((86.5, 487))
    fist1.add_vertex((76.5, 490))
    fist1.add_vertex((86.5, 493))
    fist1.add_vertex((96.5, 508))
    fist1.add_vertex((94.5, 515.5))
    fist1.add_vertex((102.5, 519))
    fist1.add_vertex((82.5, 538.5))
    fist1.add_vertex((96.5, 548))
    fist1.add_vertex((102.5, 538.5))
    fist1.add_vertex((110.5, 559.5))
    fist1.add_vertex((99, 575))
    fist1.add_vertex((100.5, 597))
    fist1.add_vertex((78.5, 618.5))
    fist1.add_vertex((59.5, 607))
    fist1.add_vertex((47.5, 602))
    fist1.add_vertex((34.3373, 597))
    fist1.add_vertex((24, 584.5))
    fist1.add_vertex((14.5, 568))
    fist1.add_vertex((2.5, 555.5))
    fist1.add_vertex((0, 514))
    fist1.add_vertex((20.5, 487))
    fist1.add_vertex((47.5, 474))
    fist1.filled = True
    fist1.fill_color = "#B09285"
    fist1.color = "#B09285"
    window.add(fist1)


def arm():
    arm1 = GPolygon()
    arm1.add_vertex((28, 579))
    arm1.add_vertex((88.5, 606.5))
    arm1.add_vertex((22.1833, 800))
    arm1.add_vertex((0, 800))
    arm1.add_vertex((0, 623))
    arm1.add_vertex((28, 579))
    arm1.filled = True
    arm1.fill_color = "#9A8271"
    arm1.color = "#9A8271"
    window.add(arm1)


def hide1():
    rectangle = GRect(265, 129)
    rectangle.filled = True
    rectangle.fill_color = "#9D2448"
    rectangle.color = "#9D2448"
    window.add(rectangle, 127, 568)


def bag():
    bag1 = GOval(107 * 2, 138 * 2)
    bag1.filled = True
    bag1.fill_color = "#D9D9D9"
    # bag1.color = "#D9D9D9"
    window.add(bag1, 253 - 107, 706 - 138)


def lip():
    lips1 = GPolygon()
    lips1.add_vertex((268.5, 421.5))
    lips1.add_vertex((276, 421.5))
    lips1.add_vertex((286, 419.5))
    lips1.add_vertex((308, 427))
    lips1.add_vertex((289, 430))
    lips1.add_vertex((276, 432))
    lips1.add_vertex((264.5, 432))
    lips1.add_vertex((248.5, 427))
    lips1.add_vertex((236, 424.5))
    lips1.add_vertex((258, 417.5))
    lips1.add_vertex((268.5, 421.5))
    lips1.filled = True
    lips1.fill_color = "#8D616A"
    lips1.color = "#8D616A"
    window.add(lips1)
    lips2 = GPolygon()
    lips2.add_vertex((264.5, 432))
    lips2.add_vertex((276, 432))
    lips2.add_vertex((289, 430))
    lips2.add_vertex((308, 427))
    lips2.add_vertex((289, 441.5))
    lips2.add_vertex((279, 443.5))
    lips2.add_vertex((263, 443.5))
    lips2.add_vertex((252, 438.5))
    lips2.add_vertex((236, 424.5))
    lips2.add_vertex((248.5, 427))
    lips2.add_vertex((264.5, 432))
    lips2.filled = True
    lips2.fill_color = "#A3707D"
    lips2.color = "#A3707D"
    window.add(lips2)


def glass_frame():
    line1 = GLine(199.842, 340.474, 187.842, 336.474)
    window.add(line1)
    line2 = GLine(364.967, 346.499, 349.967, 345.499)
    window.add(line2)
    line3 = GLine(287, 341.5, 263, 341.5)
    window.add(line3)


def glass():
    glass1 = GPolygon()
    glass1.add_vertex((214.5, 327))
    glass1.add_vertex((242.5, 327))
    glass1.add_vertex((263.5, 341))
    glass1.add_vertex((259.5, 359.5))
    glass1.add_vertex((249, 369.5))
    glass1.add_vertex((242.5, 374.5))
    glass1.add_vertex((217.5, 374.5))
    glass1.add_vertex((203.5, 359.5))
    glass1.add_vertex((200, 338.5))
    glass1.add_vertex((214.5, 327))
    glass1.filled = True
    glass1.fill_color = "#9D817D"
    window.add(glass1)
    glass2 = GPolygon()
    glass2.add_vertex((308.5, 331))
    glass2.add_vertex((334, 331))
    glass2.add_vertex((350, 344))
    glass2.add_vertex((350, 357))
    glass2.add_vertex((342.5, 369.5))
    glass2.add_vertex((330.5, 379.5))
    glass2.add_vertex((308.5, 379.5))
    glass2.add_vertex((293, 369.5))
    glass2.add_vertex((286.5, 341))
    glass2.add_vertex((308.5, 331))
    glass2.filled = True
    glass2.fill_color = "#9D817D"
    window.add(glass2)


def nostril():
    nose1 = GOval(3.5 * 2, 2 * 2)
    nose1.filled = True
    nose1.fill_color = "#040000"
    nose1.color = "#040000"
    window.add(nose1, 260.5 - 3.5, 394 - 2)
    nose2 = GOval(3.5 * 2, 2 * 2)
    nose2.filled = True
    nose2.fill_color = "#040000"
    nose2.color = "#040000"
    window.add(nose2, 285.5 - 3.5, 395 - 2)


def nose():
    nose1 = GPolygon()
    nose1.add_vertex((262.5, 341.5))
    nose1.add_vertex((275, 341.5))
    nose1.add_vertex((271.5, 392.5))
    nose1.add_vertex((271.5, 399.5))
    nose1.add_vertex((264, 397.5))
    nose1.add_vertex((256, 395.5))
    nose1.add_vertex((250.5, 397.5))
    nose1.add_vertex((245, 391.5))
    nose1.add_vertex((246.5, 384.5))
    nose1.add_vertex((250.5, 378.5))
    nose1.add_vertex((262.5, 341.5))
    nose1.filled = True
    nose1.fill_color = '#A67879'
    nose1.color = "#A67879"
    window.add(nose1)
    nose2 = GPolygon()
    nose2.add_vertex((275, 341.5))
    nose2.add_vertex((287, 341.5))
    nose2.add_vertex((295, 381))
    nose2.add_vertex((297.5, 391.5))
    nose2.add_vertex((296.5, 396.5))
    nose2.add_vertex((291.5, 397.5))
    nose2.add_vertex((285.725, 396.5))
    nose2.add_vertex((278.5, 397.5))
    nose2.add_vertex((271.5, 399.5))
    nose2.add_vertex((271.5, 392.5))
    nose2.add_vertex((275, 341.5))
    nose2.filled = True
    nose2.fill_color = '#B18988'
    nose2.color = "#B18988"
    window.add(nose2)


def eye():
    eye1 = GOval(14.5 * 2, 7.5 * 2)
    eye1.filled = True
    eye1.fill_color = "#C7B8BE"
    eye1.color = "#C7B8BE"
    window.add(eye1, 235.5 - 14.5, 338.5 - 7.5)
    eye2 = GOval(14.5 * 2, 7.5 * 2)
    eye2.filled = True
    eye2.fill_color = "#C7B8BE"
    eye2.color = "#C7B8BE"
    window.add(eye2, 314.5 - 14.5, 343.5 - 7.5)
    pupil1 = GOval(6.5 * 2, 6.5 * 2)
    pupil1.filled = True
    pupil1.fill_color = "black"
    pupil1.color = "black"
    window.add(pupil1, 234.5 - 6.5, 337.5 - 6.5)
    pupil2 = GOval(6.5 * 2, 6.5 * 2)
    pupil2.filled = True
    pupil2.fill_color = "#060000"
    pupil2.color = "#060000"
    window.add(pupil2, 314.5 - 6.5, 342.5 - 6.5)


def eyebrow1():
    eyebrow = GPolygon()
    eyebrow.add_vertex((252, 309))
    eyebrow.add_vertex((254, 316.5))
    eyebrow.add_vertex((241.25, 311.75))
    eyebrow.add_vertex((228.5, 307))
    eyebrow.add_vertex((215.5, 311))
    eyebrow.add_vertex((212, 309))
    eyebrow.add_vertex((228.5, 298))
    eyebrow.add_vertex((240.25, 303.5))
    eyebrow.add_vertex((252, 309))
    eyebrow.filled = True
    eyebrow.fill_color = "black"
    window.add(eyebrow)


def eyebrow2():
    eyebrow = GPolygon()
    eyebrow.add_vertex((345, 316))
    eyebrow.add_vertex((332.5, 311.5))
    eyebrow.add_vertex((319.5, 316))
    eyebrow.add_vertex((298.5, 322))
    eyebrow.add_vertex((295.5, 316))
    eyebrow.add_vertex((330, 305.5))
    eyebrow.add_vertex((342, 311.5))
    eyebrow.add_vertex((345, 316))
    eyebrow.filled = True
    eyebrow.fill_color = "black"
    window.add(eyebrow)


def hair():
    hair1 = GPolygon()
    hair1.add_vertex((269.787, 156))
    hair1.add_vertex((312.046, 167.95))
    hair1.add_vertex((338.528, 185.022))
    hair1.add_vertex((365.01, 192.42))
    hair1.add_vertex((396, 240.221))
    hair1.add_vertex((382.109, 317.613))
    hair1.add_vertex((363.32, 362))
    hair1.add_vertex((355.431, 290.298))
    hair1.add_vertex((342.472, 244.773))
    hair1.add_vertex((306.975, 244.773))
    hair1.add_vertex((275.421, 233.961))
    hair1.add_vertex((252.883, 242.497))
    hair1.add_vertex((225.274, 240.221))
    hair1.add_vertex((204.99, 282.331))
    hair1.add_vertex((196.538, 296.558))
    hair1.add_vertex((188.086, 338.669))
    hair1.add_vertex((177.381, 305.663))
    hair1.add_vertex((174, 251.602))
    hair1.add_vertex((182.452, 214.044))
    hair1.add_vertex((216.822, 178.762))
    hair1.add_vertex((269.787, 156))
    hair1.filled = True
    hair1.fill_color = "black"
    window.add(hair1)


def ear1():
    ears = GPolygon()
    ears.add_vertex((383.025, 314))
    ears.add_vertex((392, 317.405))
    ears.add_vertex((392, 333.865))
    ears.add_vertex((386.764, 349.189))
    ears.add_vertex((379.782, 356.568))
    ears.add_vertex((368.145, 377))
    ears.add_vertex((360, 377))
    ears.add_vertex((363.491, 356.568))
    ears.add_vertex((372.8, 332.162))
    ears.add_vertex((383.025, 314))
    ears.filled = True
    ears.fill_color = "#A77173"
    window.add(ears)


def ear2():
    ears = GPolygon()
    ears.add_vertex((177.583, 308))
    ears.add_vertex((188.083, 337.138))
    ears.add_vertex((191, 373))
    ears.add_vertex((184.583, 371.319))
    ears.add_vertex((180.5, 362.196))
    ears.add_vertex((170, 344.422))
    ears.add_vertex((163, 327.612))
    ears.add_vertex((164.75, 308))
    ears.filled = True
    ears.fill_color = "#A77173"
    window.add(ears)


def cloth():
    cloth1 = GPolygon()
    cloth1.add_vertex((243.5, 520))
    cloth1.add_vertex((290.5, 525))
    cloth1.add_vertex((324.011, 520))
    cloth1.add_vertex((344.5, 503.5))
    cloth1.add_vertex((355.5, 474))
    cloth1.add_vertex((446.5, 511.5))
    cloth1.add_vertex((499.5, 565))
    cloth1.add_vertex((499.5, 674.988))
    cloth1.add_vertex((499.5, 798.5))
    cloth1.add_vertex((442, 798.5))
    cloth1.add_vertex((434.5, 789))
    cloth1.add_vertex((460, 657))
    cloth1.add_vertex((434.5, 798.5))
    cloth1.add_vertex((51.5, 798.5))
    cloth1.add_vertex((60.5, 762.5))
    cloth1.add_vertex((51.5, 712))
    cloth1.add_vertex((0, 620))
    cloth1.add_vertex((0, 520))
    cloth1.add_vertex((93, 477))
    cloth1.add_vertex((138, 469.5))
    cloth1.add_vertex((161.5, 467.5))
    cloth1.add_vertex((174.5, 469.5))
    cloth1.add_vertex((185, 458.5))
    cloth1.add_vertex((219.5, 510))
    cloth1.add_vertex((243.5, 520))
    cloth1.filled = True
    cloth1.fill_color = "#9D2448"
    window.add(cloth1)


def face():
    face1 = GPolygon()
    face1.add_vertex((302.961, 244.274))
    face1.add_vertex((341.029, 244.274))
    face1.add_vertex((355.934, 261.396))
    face1.add_vertex((355.934, 287.08))
    face1.add_vertex((362, 300.208))
    face1.add_vertex((362, 325.321))
    face1.add_vertex((362, 337.804))
    face1.add_vertex((362, 351.575))
    face1.add_vertex((362, 370.41))
    face1.add_vertex((337.629, 436.618))
    face1.add_vertex((293.42, 476))
    face1.add_vertex((245.811, 472.575))
    face1.add_vertex((219.739, 452.028))
    face1.add_vertex((193.668, 412.646))
    face1.add_vertex((188, 337.804))
    face1.add_vertex((193.668, 295.071))
    face1.add_vertex((202.736, 282.514))
    face1.add_vertex((223.14, 238.566))
    face1.add_vertex((248.645, 239.708))
    face1.add_vertex((273.583, 234))
    face1.add_vertex((302.961, 244.274))
    face1.filled = True
    face1.fill_color = "#B09088"
    face1.color = "#B09088"
    window.add(face1)


def neck():
    neck_1 = GPolygon()
    neck_1.add_vertex((197, 417.5))
    neck_1.add_vertex((220.5, 449))
    neck_1.add_vertex((246.5, 471))
    neck_1.add_vertex((293.5, 474.5))
    neck_1.add_vertex((322.4, 449))
    neck_1.add_vertex((322.5, 458.5))
    neck_1.add_vertex((355.5, 474.5))
    neck_1.add_vertex((346.5, 504))
    neck_1.add_vertex((322.5, 522))
    neck_1.add_vertex((290.5, 531))
    neck_1.add_vertex((253.5, 526))
    neck_1.add_vertex((220.5, 510.5))
    neck_1.add_vertex((183.5, 458.5))
    neck_1.filled = True
    neck_1.fill_color = "#8B706A"
    window.add(neck_1)


if __name__ == '__main__':
    main()
