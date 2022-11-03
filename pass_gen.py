import tkinter as tk
import random
import rsa
from  tkinter import Frame, filedialog
from tkinter import messagebox


root = tk.Tk()

root.geometry("300x350")
root.title("Engine Code")
root.resizable(False, False)
frame = Frame(root, width=300, height=350)
output_text = tk.StringVar()
output = tk.Text(root,height=5, width=50, font = ('Arial', 18))
output = tk.Entry(root, textvariable= output_text)
output.place(x=100,y=15)

eng_label = tk.Label(root, width = 10, height = 2, text="Engine Code:")
eng_label.place(x=10,y=7)


eng_ky_text = tk.StringVar()
eng_ky = tk.Text(root,height=5, width=50, font = ('Arial', 18))
eng_ky = tk.Entry(root, textvariable= eng_ky_text)
eng_ky.place(x=100,y=50)


key_label = tk.Label(root, width = 10, height = 2, text="Engine Key:")
key_label.place(x=10,y=42)

var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()



sb1 = tk.IntVar(value=8)
sb1 = tk.Spinbox(root, from_= 8, to = 16, width = 4, increment = 1 )
sb1.place(x= 160, y = 90)

sb_label = tk.Label(root, width = 10, height = 2, text="No. of Code:")
sb_label.place(x=80,y=82)

c2 = tk.Checkbutton(root, text = "Caps",variable = var2, onvalue= 1, offvalue= 0 )
c2.place(x=40, y = 130)
c3 = tk.Checkbutton(root, text = "Nums",variable = var3, onvalue= 1, offvalue= 0 )
c3.place(x=120, y = 130)
c4 = tk.Checkbutton(root, text = "Syms",variable = var4, onvalue= 1, offvalue= 0 )
c4.place(x=200, y = 130)

def gen_pass():
   global fvar
   lower = "abcdefghijklmnopqrstuvwxyz" 
   upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   numbers = "0123456789"
   symbols = "!@#$%^&*()."
   length = int(sb1.get())
   string = lower 
   if (var2.get()==1):
    string += upper
   if (var3.get()==1) :
    string += numbers 
   if (var4.get()==1) :
    string += symbols
   fvar = "".join(random.sample(string,length))
   output_text.set(fvar)

   



def en_code():
 try:
   public_key,private_key = rsa.newkeys(1024)

   with open("public.pem", "wb") as f:
    f.write(public_key.save_pkcs1("PEM"))

   with open("private.pem", "wb") as f:
    f.write(private_key.save_pkcs1("PEM"))


   with open("private.pem", mode = "rb") as f: 
    keydata = f.read()
    private_key = rsa.PrivateKey.load_pkcs1(keydata)

    eng_ky_text.set(private_key)
    
   with open("private.pem", "rb") as f:
      
      private_key = rsa.PrivateKey.load_pkcs1(f.read())
      encrypted_code = (rsa.encrypt(fvar.encode('utf-8'), private_key))
      
   with open("encrypted_code", "wb") as f:
     
      f = filedialog.asksaveasfile(mode = 'wb', defaultextension='.bin',
      filetypes=[
         ("Binary",".bin"),
         ("HTML file", ".html"),
         ("All files", ".*")
      ])
      f.write(encrypted_code)
      f.close()
 except:
  messagebox.showinfo("Save File", "File Not Saved")
   
     
   
gen_text=tk.StringVar()
gen_btn = tk.Button(root, textvariable=gen_text, command= gen_pass, font = "Arial", bg="gray", fg = "white", height = 1, width = 15)
gen_text.set("Extract")
gen_btn.place(x = 80, y=200)


save_text=tk.StringVar()
save_btn = tk.Button(root, textvariable=save_text, command= en_code, font = "Arial", bg="gray", fg = "white", height = 1, width = 15)
save_text.set("Encrypt")
save_btn.place(x = 80, y=250)




root.mainloop()

