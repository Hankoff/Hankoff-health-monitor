from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder


main_screen = ("""
#:import utils kivy.utils
Page:
<Page@PageLayout>:
    border: 20
    swipe_threshold: .2
    InputArea1:
    InputArea2:
    InputArea3:
<InputArea1@GridLayout>:
    canvas.before:
        Color:
            rgba: (9/255.0,31/255.0,94/255.0,1)
        Rectangle:
            size: self.size
            pos: self.pos
    cols: 1
    rows: 7
    spacing: "20dp", "20dp"
    padding: ("20dp", "20dp", "20dp", "20dp")
    Label:
        size_hint: None, None
        width: "200dp"
        height:"50dp"
        text: "Weight(Kg): "
        color: (1, 1, 1, 1)
    TextInput:
        font_size: 20
        id: _a
    Label:
        color: (1, 1, 1, 1)
        size_hint: None, None
        width: "200dp"
        height:"50dp"
        text: "Height(Cm): "
    TextInput:
        font_size: 20
        id: _b
    Button:
        text: "result"
        on_release: root.calculation()
        background_normal: ""
        # background_color: (50/255.0,118/255.0,227/255.0,1)
        background_color: (50/255.0,118/255.0,227/255.0,1)
    Label:
        background_color: (9/255.0,31/255.0,94/255.0,1)
        halign: 'center'
        font_size: 20
        spacing: "40dp", "50dp"
        canvas.before: 
            Color:
                rgba: self.background_color
            Rectangle:
                size: self.size
                pos: self.pos
        color: (50/255.0,118/255.0,227/255.0,1)
        bold: True
        italic: True
        outline_color: (0,0,0,1)
        outline_width: 2
        id: _result
<InputArea2@GridLayout>:
    canvas.before:
        Color:
            rgba: (9/255.0,31/255.0,94/255.0,1)
        Rectangle:
            size: self.size
            pos: self.pos
    cols: 1
    rows: 7
    spacing: "20dp", "20dp"
    padding: ("20dp", "20dp", "20dp", "20dp")
    Label:
        size_hint: None, None
        text: "Age: "
        color: (1, 1, 1, 1)
    TextInput:
        font_size: 20
        id: _c
    Label:
        color: (1, 1, 1, 1)
        text: "Rest Heart Rate: "
    TextInput:
        size_hint: None, None
        width: "200dp"
        height:"50dp"
        font_size: 20
        id: _d
    Button:
        text: "result"
        on_release: root.calculation1()
        background_normal: ""
        # background_color: (50/255.0,118/255.0,227/255.0,1)
        background_color: (50/255.0,118/255.0,227/255.0,1)
    Label:
        background_color: (9/255.0,31/255.0,94/255.0,1)
        halign: 'center'
        font_size: 20
        spacing: "40dp", "50dp"
        canvas.before: 
            Color:
                rgba: self.background_color
            Rectangle:
                size: self.size
                pos: self.pos
        color: (50/255.0,118/255.0,227/255.0,1)
        bold: True
        italic: True
        outline_color: (0,0,0,1)
        outline_width: 2
        id: _result2
<InputArea3@GridLayout>:
    canvas.before:
        Color:
            rgba: (9/255.0,31/255.0,94/255.0,1)
        Rectangle:
            size: self.size
            pos: self.pos
    cols: 1
    rows: 12
    spacing: "20dp", "20dp"
    padding: ("20dp", "20dp", "20dp", "20dp")
    Label:
        text: 'Training Zone'
        font_size: 32   
    Label:
        text: 'Very Light'
    CheckBox:
        group: 'difficulty'
        on_active: root.training_zone(self, self.active)
    Label:
        text: 'Light'
    CheckBox:
        group: 'difficulty'
        on_active: root.training_zone1(self, self.active)
    Label:
        text: 'moderate'
    CheckBox:
        group: 'difficulty'
        on_active: root.training_zone2(self, self.active)
    Label:
        text: 'hard'
    CheckBox:
        group: 'difficulty'
        on_active: root.training_zone3(self, self.active)
    Label:
        text: 'maximum'
    CheckBox:
        group: 'difficulty'
        on_active: root.training_zone4(self, self.active)
    Label:
        id: _output
        text: 'please select your preference'
    """)



class InputArea1(GridLayout):

    def calculation(self):
        res = int(self.ids._a.text) / ((int(self.ids._b.text) / 100) * (int(self.ids._b.text) / 100))
        res2 = round(res, 2)
        if res2 < 18.5:
            self.ids._result.text = \
                f'your ibm is {str(res2)}  \nyou are Underweight\n'
        elif 18.5 <= res2 <= 24.9:
            self.ids._result.text = \
                f'your ibm is {str(res2)}  \nyou are normal\n'
        elif 25 <= res2 <= 29.9:
            self.ids._result.text = \
                f'your ibm is {str(res2)} \nyou are overweight\n'
        elif 29.9 <= res2 <= 34.9:
            self.ids._result.text = \
                f'your ibm is {str(res2)}  \nyou are Obese\n'
        elif res2 > 34.9:
            self.ids._result.text = \
                f'your ibm is {str(res2)}  \nyou are Extremely obese\n'


class InputArea2(GridLayout):

    def calculation1(self):
        global hrm
        hrm = \
            205.8 - (0.685 * int(self.ids._c.text))
        vo2max = \
            15 * (hrm / int(self.ids._d.text))
        resa = round(vo2max, 2)
        self.ids._result2.text = str(resa)


class InputArea3(GridLayout):
    def training_zone(self, instance, value):
        verylightmin = hrm * 0.50
        verylightmax = hrm * 0.59
        if value == True:
            self.ids._output.text = f" Minimal BPM is {round(verylightmin)}\
             Maximal BPM is {round(verylightmax)}"

    def training_zone1(self, instance, value):
        lightmin = hrm * 0.60
        lightmax = hrm * 0.69
        if value == True:
            self.ids._output.text = f" Minimal BPM is {round(lightmin)}\
             Maximal BPM is {round(lightmax)}"

    def training_zone2(self, instance, value):
        moderatemin = hrm * 0.70
        moderatemax = hrm * 0.79
        if value == True:
            self.ids._output.text = f" Minimal BPM is {round(moderatemin)}\
             Maximal BPM is {round(moderatemax)}"

    def training_zone3(self, instance, value):
        hardmin = hrm * 0.80
        hardmax = hrm * 0.89
        if value == True:
            self.ids._output.text = f" Minimal BPM is {round(hardmin)}\
             Maximal BPM is {round(hardmax)}"

    def training_zone4(self, instance, value):
        maximummin = hrm * 0.90
        maximumax = hrm * 1
        if value == True:
            self.ids._output.text = f" Minimal BPM is {round(maximummin)}\
             Maximal BPM is {round(maximumax)}"

class CalculatorBmiApp(App):
    def build(self):
        return Builder.load_string(main_screen)


CalculatorBmiApp().run()
