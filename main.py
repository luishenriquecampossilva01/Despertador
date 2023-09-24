from tkinter.ttk import *
from tkinter import*
from PIL import Image,ImageTk

#cores
co0 = "#f0f3f5"
co1 = "#feffff"
co2 = "#d6872d"
co3 = "#fc766d"
co4 = "#403d3d"
co5 = "#4a88e8"




#criando janela

janela = Tk()
janela.title("")
janela.geometry("350x150")
janela.configure(background=co1)
janela.resizable(width=FALSE,height=FALSE)

#dividindo a janela em 2 frames
frame_logo = Frame(janela,width=400,height=10,bg=co1)
frame_logo.grid(row=0,column=0,pady=1,padx=0)

frame_corpo = Frame(janela,width=400,height=290,bg=co1)
frame_corpo.grid(row=1,column=0,pady=1,padx=0)

#configurando o frame logo
l_linha = Label(frame_logo,width=400,height=1,bg=co2,anchor=NW,font=('Ivy 1'))
l_linha.place(x=0,y=0)

#configurando o frame corpo
imagem = Image.open('icons8-alarm.png')
imagem = imagem.resize((100,100))
imagem = ImageTk.PhotoImage(imagem)

#configurando o frame logo
l_imagem = Label(frame_corpo,image=imagem,compound=LEFT,padx=10,height=100,bg=co1,anchor=NW,font=('Ivy 16 bold'),fg=co3)
l_imagem.place(x=10,y=10)

l_nome = Label(frame_corpo,text='Alarme',height=1,bg=co1,anchor=NE,font=('Ivy 10'),fg=co4)
l_nome.place(x=110,y=10)
janela.mainloop()