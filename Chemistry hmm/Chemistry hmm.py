import pynecone as pc
import random
import time

easy_question = {
    0:["What is the reagent used for flame test",["Con.HCl","Con.H₂SO₄","dil.HCl","BaCl₂"],"Con.HCl"],
    1:["What is the reagent used in ash test",["Con.HNO₃","Con.H₂SO₄","dil.HCl","MnO₂"],"Con.HNO₃"],
    2:["Green tinted ash indicates",["Zn²⁺","Al³⁺","Mg²⁺","Sr²⁺"],"Zn²⁺"]
    }

class State(pc.State):
    question:str
    options:list
    answer:int
    index:int
    def easy(self):
        return pc.redirect("/levels/easy")
    def getQuestion(self):
        self.question = easy_question[1][0]
        self.options = easy_question[1][1]
        self.answer = easy_question[1][2]
        return self.question
    def randomize(self):
        return random.randint(0,len(easy_question)-1)

Style = {
    "textAlign":"centre",
    "margin":"auto",
    "margin_top":"3em",
    "font_size":"42px",
    "font_weight":"10000",
    "font_family":"power red and blue",
    }
ButtonsStyle = {
    "margin":"auto",
    "postion":"relative",
    "top":"50px",
    "font_size":"32px",
    "font_weight":"10000",
    "font_family":"power red and blue",
}
Buttonsstyle = {
    "margin":"auto",
    "postion":"relative",
    "top":"50px",
    "font_size":"32px",
    "font_weight":"10000",
    "font_family":"power red and blue",
}
CreditsStyle = {
    "margin":"auto",
    "margin_top":"100em",
    "font_size":"16px",
    "font_weight":"10000",
    "font_family":"power red and blue",
}
Arial ={
    "textAlign":"centre",
    "margin":"auto",
    "margin_top":"3em",
    "font_size":"42px",
    "font_weight":"10000",
    "font_family":"arial",
}
Option1 ={
    "align-self":"left",
    "font_size":"32px",
    "padding":"30px",
    "top":"5em",
    "margin_left":"450",
}

def index():
    return pc.vstack(
        pc.box(
            "🧪Chemistry Praticals🧪",style = Style
        ),
        pc.button(
            "Easy",style =  ButtonsStyle,on_click = State.easy,
        ),
        pc.button(
            "Medium",style =  Buttonsstyle,
        ),
        pc.button(
            "Hard",style =  Buttonsstyle,
        ),
    )
def easy():
    i = 1
    question = easy_question[i][0]
    options = easy_question[i][1]
    answer = easy_question[i][2]
    return pc.stack(pc.vstack(
        pc.box(question,style = Arial),
    ),pc.hstack(
        pc.button(options[0],style = Option1),
        pc.button(options[1],style = Option1),
        pc.button(options[2],style = Option1),
        pc.button(options[3],style = Option1),
    ))



app = pc.App(state=State)
app.add_page(index)
app.add_page(easy,route="/levels/easy")
app.compile()