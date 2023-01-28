from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
from tkinter import  messagebox
from tkinter import *
import PIL.ImageTk
import PIL.Image
import time

class Gera_qrcode():
    def __init__(self, root):
        
        self.root = root
        self.Label_texto = Label(root,text='Gera Qrcode Pix',foreground='white',background='SteelBlue', font=('Raleway',20))
        self.Label_texto.place(x=330,y=1)
        
        self.label_nome = Label(root,text='Nome completo',foreground='white',background='SteelBlue',font=('Raleway',15))
        self.label_nome.place(x=30,y=60)
        self.Entry_nome = Entry(root,highlightcolor="purple", background="white",font=("arial",15),width=28)
        self.Entry_nome.place(x=30,y=90)        
        
        self.label_cidade = Label(root,text='Cidade',foreground='white',background='SteelBlue',font=('Raleway',15))
        self.label_cidade.place(x=30,y=120)
        self.Entry_cidade = Entry(root,highlightcolor="purple", background="white",font=("arial",15),width=18)
        self.Entry_cidade.place(x=30,y=150) 
        
        self.label_identificador = Label(root,text='Identificador',foreground='white',background='SteelBlue',font=('Raleway',15))
        self.label_identificador.place(x=30,y=190)
        self.Entry_identificador = Entry(root,highlightcolor="purple", background="white",font=("arial",15),width=18)
        self.Entry_identificador.place(x=30,y=220) 
        
        self.label_valor = Label(root,text='Valor',foreground='white',background='SteelBlue',font=('Raleway',15))
        self.label_valor.place(x=30,y=260)
        self.Entry_valor= Entry(root,highlightcolor="purple", background="white",font=("arial",15),width=18)
        self.Entry_valor.place(x=30,y=290) 
        
        self.chave = StringVar()
        self.radiobt_email = Radiobutton(root,text='Email',value='Email',background='SteelBlue', variable=self.chave)
        self.radiobt_email.place(x=30,y=330)
        self.radiobt_numero = Radiobutton(root,text='Numero',value='Numero',background='SteelBlue', variable=self.chave)
        self.radiobt_numero.place(x=110,y=330)
        self.radiobt_cpf = Radiobutton(root,text='Cpf',value='Cpf',background='SteelBlue', variable=self.chave)
        self.radiobt_cpf.place(x=210,y=330)
        self.radiobt_aleatoria = Radiobutton(root,text='Aleatoria',value='Aleatoria',background='SteelBlue', variable=self.chave)
        self.radiobt_aleatoria.place(x=290,y=330)
        
        self.label_chave = Label(root,text='Chave',foreground='white',background='SteelBlue',font=('Raleway',15))
        self.label_chave.place(x=30,y=360)
        self.Entry_chave = Entry(root,highlightcolor="purple", background="white",font=("arial",15),width=28)
        self.Entry_chave.place(x=30,y=390)

        self.botao_gerar = Button(root,text='Gerar qrcode',command=self.Gerar_qrcode,foreground='white', background='DarkSlateBlue' ,activebackground="lightblue",font=("arial",15),width=10)
        self.botao_gerar.place(x=30,y=450)
        self.frame_qr = Frame(root,background='DarkSlateBlue',width=350,height=300)
        self.frame_qr.place(x=460,y=100)
        
        
    def Gerar_qrcode(self):
        if self.Entry_nome.get() == '' or self.Entry_cidade.get() == '' or self.Entry_identificador.get() == '' or self.Entry_valor.get() == '' or self.Entry_chave.get() == '':
            messagebox.showinfo('Error','alguns campos estão em branco')
        else:
            self.options = webdriver.ChromeOptions()
            self.options.add_argument("--headless")
            self.driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=self.options) #,chrome_options=options
            self.driver.get('https://gerarqrcodepix.com.br/')
        
            
            self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[1]/div[1]/input').send_keys(f'{self.Entry_nome.get()}')
          
            self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[1]/div[2]/input').send_keys(f'{self.Entry_cidade.get()}')
            
            self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[3]/div/input').send_keys(f'{self.Entry_identificador.get()}')
         
            self.driver.find_element(By.XPATH,'//*[@id="yes"]').click()
             
            self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[4]/div/input').send_keys(f'{self.Entry_valor.get()}')
          
            
            if self.chave.get()  == 'Email':
                self.driver.find_element(By.XPATH,'//*[@id="email"]').click() 
                self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[5]/div/div[1]/input').send_keys(f'{self.Entry_chave.get()}') 
            if self.chave.get()  == 'Numero':
                self.driver.find_element(By.XPATH,'//*[@id="phone"]').click()
                self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[5]/div/div[2]/input').send_keys(f'{self.Entry_chave.get()}')
            if self.chave.get() == 'Cpf':
                self.driver.find_element(By.XPATH,'//*[@id="document"]').click() 
                self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[5]/div/div[3]/input').send_keys(f'{self.Entry_chave.get()}') 
            if self.chave.get() == 'Aleatoria':
                self.driver.find_element(By.XPATH,'//*[@id="random"]').click() 
                self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[5]/div/div[4]/input').send_keys(f'{self.Entry_chave.get()}') 
           
            time.sleep(2.0)
            self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div').screenshot('qrcode.png')
            self.image_qrcode =  PIL.ImageTk.PhotoImage(PIL.Image.open("qrcode.png"))
            self.labelImage = Label(self.root,image=self.image_qrcode,height=400,width=400)
            self.labelImage.place(x=460,y=100)
            messagebox.showinfo('Sucess','Qrcode gerado com sucesso!')


if __name__ == '__main__':
    
   tela_qrcode = Tk()
   tela_qrcode.title('Gerador de Qrcode Pix')
   tela_qrcode.geometry('860x550+200+100')      
   tela_qrcode.config(background='SteelBlue')
   tela_qrcode.resizable(0,0)
   tela = Gera_qrcode(tela_qrcode)
   tela_qrcode.mainloop()
 