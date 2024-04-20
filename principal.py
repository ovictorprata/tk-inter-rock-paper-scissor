from tkinter import *
from tkinter import ttk
from random import choice
from funcoes_jogo import *

def iniciar_jogo():
    label_x.config(text='X')
    root.after(1000, altera_label_pc)
    root.after(2000, sortear_escolha_pc)

def altera_label_pc():
    label_o_pc_vai_escolher.config(text='O PC vai escolher...')

def jogar():
    if usuario.get():
        
        iniciar_jogo()
    else:    
        label_o_pc_vai_escolher.config(text='Selecione uma opção para jogar.')



def sortear_escolha_pc(count=0):
    if count < 30:
        escolha_pc = choice(['pedra','papel','tesoura'])
        label_pc.config(text=escolha_pc)
        label_pc.after(50, lambda: sortear_escolha_pc(count + 1))
    else:
        label_o_pc_vai_escolher.config(text='O PC escolheu:')
        escolha_pc = choice(['pedra','papel','tesoura'])
        label_pc.config(text=escolha_pc)
        conferir_resultado(usuario.get(), escolha_pc, resultado_jogo)
        button.config(text='Jogar novamente')

root = Tk()
root.configure(bg='white')  # Cor de fundo branca
font_h1 = ('Arial', 32, 'bold')
font_text=('Arial', 14)
font_h2 = ('Arial', 28, 'bold')
frame_container = Frame(root, bg='white')
pontuacao_pc = 0
pontuacao_usuario = 0
label_titulo = Label(frame_container, text='JOKENPO GAME', font=font_h1, bg='white', fg='blue') 
usuario = StringVar()

label_instrucao = Label(frame_container, text='Escolha uma opção:', font=font_text, bg='white', fg='blue')  
radio_pedra = Radiobutton(frame_container, text='Pedra', value='pedra', variable=usuario, font=font_text, bg='white')
radio_papel = Radiobutton(frame_container, text='Papel', value='papel', variable=usuario, font=font_text, bg='white')
radio_tesoura = Radiobutton(frame_container, text='Tesoura', value='tesoura', variable=usuario, font=font_text, bg='white')

label_x = Label(frame_container, font=font_text, bg='white')

pc = StringVar(value='')
pc = ''

label_o_pc_vai_escolher = Label(frame_container, font=font_text, bg='white')
label_pc = Label(frame_container, text=pc, font=font_text, bg='white')
divider = ttk.Separator(frame_container, orient='horizontal')
resultado_jogo = Label(frame_container, text='', font=font_h2, bg='white') 
button = Button(frame_container, text='Jogar', command=jogar, font=font_text, bg='green', fg='white', relief='raised', padx=10, pady=5)   

frame_container.grid(row=0, column=0, padx=20, pady=20)
label_titulo.grid(row=0, column=0, columnspan=3, pady=20)
label_instrucao.grid(row=1, column=0, columnspan=3, sticky='w', padx=(10,0), pady=(0, 10))
radio_pedra.grid(row=2, column=0, padx=(0, 5))
radio_papel.grid(row=2, column=1)
radio_tesoura.grid(row=2, column=2, padx=(5, 0))
button.grid(row=3, column=0, columnspan=3, pady=20)   
label_x.grid(row=4, column=0, columnspan=3)
label_o_pc_vai_escolher.grid(row=5, column=0, columnspan=3, sticky='w')
label_pc.grid(row=6, column=0, columnspan=3)
divider.grid(row=7, column=0, columnspan=3, sticky='ew', pady=10)
resultado_jogo.grid(row=8, column=0, columnspan=3)
root.mainloop()
