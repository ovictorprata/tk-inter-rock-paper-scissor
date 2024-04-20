from tkinter import *

root = Tk()
root.minsize(500, 800)

def jogar():
    radio_pedra.pack_forget()
    radio_papel.pack_forget()
    radio_tesoura.pack_forget()

def configura_radiobutton(radio_button, opcao, valor, imagem):
  radio_button.config(variable=opcao, value=valor, image=imagem, compound='left', indicatoron=False, bg='white', borderwidth=0, highlightthickness=0)


root.config(bg='white')
font_button = ('Open Sans', 12,'bold')

imagem_pedra = PhotoImage(file='rock_100.png')
imagem_papel = PhotoImage(file='paper_100.png')
imagem_tesoura = PhotoImage(file='scissor_100.png')

opcao = StringVar()

radio_pedra = Radiobutton(root, image=imagem_pedra)
radio_papel = Radiobutton(root, image=imagem_papel)
radio_tesoura = Radiobutton(root, image=imagem_tesoura)
configura_radiobutton(radio_pedra, opcao, 'pedra', imagem_pedra)
configura_radiobutton(radio_papel, opcao, 'papel', imagem_papel)
configura_radiobutton(radio_tesoura, opcao, 'tesoura', imagem_tesoura)





button_instruction = Button(root, text='Instruções', font=font_button, width=59, height=3, bg='orange', fg='white')
button_jogar = Button(
    root
    , text='Jogar'
    , font=font_button
    , bg='orange'
    , command=jogar
)

button_jogar.place(x=0,y=0)
radio_pedra.place(x=60, y=400)
radio_papel.place(x=210, y=400)
radio_tesoura.place(x=360, y=400)
button_instruction.place(x=0, y=735)


root.mainloop()