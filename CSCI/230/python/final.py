""" 
This program is dependent on the PIL module HIGHLY.
The rest is included with Tkinter and a normal Python Setup.

This Labor of Love was Writen by Uladzimir Kasacheuski.
Finished 6/23/15

nappa300@gmail.com
3173313503

Contact me with any questions please.

"""

import Tkinter
from Tkinter import *
import tkMessageBox
import tkFileDialog
from tkFileDialog import askopenfilename    
import PIL
from PIL import Image, ImageTk 
import os.path
import base64
import cStringIO

#img = Image.open("/home/vladk/Desktop/33.png")

def resizeImageTo(base,filename):
    global premultiply;
    global unmultiply;
    basesize = base;
    img = Image.open(filename);
    
    
    fileName, fileExtension = os.path.splitext(filename);
    print fileName;
    print fileExtension;
    
    if not(float(img.size[0]) > basesize) and not(float(img.size[1]) > basesize):
        print "already less than " + str(basesize);
        return img, fileName, fileExtension;
    
    if(float(img.size[0]) > float(img.size[1])):
        # Width > Height
        percent = (basesize / float(img.size[0]))
        width = basesize
        height = int((float(img.size[1])*float(percent)));
        print str(width) + " " + str(height);
    else:
        percent = (basesize / float(img.size[1]))
        height = basesize
        width = int((float(img.size[0])*float(percent)));
        print str(width) + " " + str(height) + "\n Here";
        
    img = img.resize((width,height), PIL.Image.ANTIALIAS)
    return img, fileName, fileExtension;
#resizeImageTo(100, "/home/vladk/Desktop/12_44.gif"); 


#Tk().withdraw()
#Select a file
#filename = askopenfilename()
#print(filename)

class App(Tk):
  def __init__(self):   
    Tk.__init__(self)

    
    self.headerFont = ("Helvetica", "14", "")
    self.buttonFont = ("Helvetica", "16", "bold")    
    self.miniFont = ("Helvetica", "11", "")

    self.title("Base64 Image Translator")
    #self.showMainPage()
    #self.img = ImageTk.PhotoImage(Image.open("True1.gif"))
    #self.panel = Label(self, image = self.img)
    
    Label(self, text = "", width = 35, font = self.buttonFont).grid(columnspan = 2)
    self.title = Label(self, text = "Base64 Image Translator",font = self.headerFont)
    self.title.grid(row = 1, columnspan = 2)
    Label(self, text = "", width = 35, height = 2).grid(columnspan = 2)
    
    self.btnEncode = Button(self, text = "Encode", font = self.buttonFont, width = 20)
    self.btnEncode.grid( columnspan = 2)
    self.btnEncode["command"] = self.showEncode
    
    Label(self, text = "", width = 35).grid(columnspan = 2)
    
    
    self.btnDecode = Button(self, text = "Decode", font = self.buttonFont, width = 20)
    self.btnDecode.grid( columnspan = 2)
    self.btnDecode["command"] = self.showDecode

    Label(self, text = "", width = 35).grid(columnspan = 2)
    
    self.panel = Label(self);
    self.panel.grid(columnspan = 2);
    
    Label(self, text = "", width = 35).grid(columnspan = 2)
        
    self.btnHelp = Button(self, text = "Help", font = self.miniFont, width = 10)
    self.btnHelp["command"] = self.helpAlert
    self.btnHelp.grid(columnspan = 2, row = 9)
    
    Label(self, text = "", width = 35).grid(columnspan = 2)
    
  def helpAlert(self):
    tkMessageBox.showinfo("Some Help and Info", "This program allows you to convert images into a base64 encoded dataURL which can be opened directly in the browser, and from a base64 encoded dataURL back into an image file. \n\nWhen you save a image as a base64 encoded dataURL - try it out and copy the text inside the .txt file into your browser url. Your image will apear. \n\n How? Magic Fairies.");
    
  def showMain(self):
    
    self.title["text"] = "Base64 Image Translator";
    self.btnEncode["text"] = "Encode";
    self.btnEncode["command"] = self.showEncode

    self.btnDecode["text"] = "Decode";
    self.btnDecode["command"] = self.showDecode

    self.btnBack.destroy();
    self.btnHelp.grid(columnspan = 2, row = 9, column = 0);
    
    self.panel["image"] = "";
    
  def showEncode(self):
        
    self.title["text"] = "Encode Image";

    self.btnEncode["text"] = "Pick an Image";
    self.btnEncode["command"] = self.fcnPickImage

    self.btnDecode["text"] = "Save as Base64";
    self.btnDecode["command"] = self.fcnPickImageFirst

    self.btnHelp.grid(columnspan = 1, column = 1, row = 9)


    self.btnBack = Button(self, text = "Back", font = self.miniFont, width = 10)
    self.btnBack["command"] = self.showMain
    self.btnBack.grid(columnspan = 1, column = 0, row = 9)
        
  def showDecode(self):
    self.title["text"] = "Decode a Base64 Image";

    self.btnEncode["text"] = "Pick an Encoding";
    self.btnEncode["command"] = self.fcnPickB64

    self.btnDecode["text"] = "Save as Image";
    self.btnDecode["command"] = self.fcnPickB64First

    self.btnHelp.grid(columnspan = 1, column = 1, row = 9)


    self.btnBack = Button(self, text = "Back", font = self.miniFont, width = 10)
    self.btnBack["command"] = self.showMain
    self.btnBack.grid(columnspan = 1, column = 0, row = 9)
        
        
  def fcnPickB64(self):
    print "Pick an Encoding";
    filetypes = [("Base64Encoding Txt", "*Base64Encoding.txt")]
    self.filename = tkFileDialog.askopenfilename(parent=self, title= "Select Attachment" , multiple=False, filetypes=filetypes);
    print self.filename;
    
    #self.filename = "/home/vladk/Desktop/num6Base64Encoding.txt"
    
    text_file = open(self.filename);
    text = text_file.read();
    #print text; 
    
    texter = text.split(",",1)
    text = texter[1];
    
    
    texter = texter[0].split("/",1);
    texter = texter[1].split(";",1);
    texter = texter[0];
    
    #print texter; # png or jpg 
    #print text; # the data
    
    imgdata = base64.b64decode(text);
    self.newFilePath = self.filename.split("Base64Encoding.txt")[0] + "ImageDecoded." + texter;
    #with open(filename, 'wb') as f:
    #    f.write(imgdata);
    #print filename;
    
    self.imageData = imgdata;
    
    buff = cStringIO.StringIO();
    buff.write(imgdata)
    buff.seek(0);
    buff = Image.open(buff);
    
    self.img = ImageTk.PhotoImage(buff)
    self.panel["image"] = self.img;
    
    
    self.btnDecode["command"] = self.fcnSaveB64AsImage
    
  def fcnSaveB64AsImage(self):
    text_file = open(self.newFilePath, "w");
    text_file.write(self.imageData);
    text_file.close();
    
    print self.newFilePath;
    tkMessageBox.showinfo("Sucessfully Saved", "Image has been successfully saved at location " + self.newFilePath);
    
    self.showMain();
        
    
  def fcnPickB64First(self):
    tkMessageBox.showinfo("Decode a Base64 Image", "Please pick a Base64 Encoding of an image before you save.")
    
    
  def fcnPickImage(self):
    print "Pick an Image";
    filetypes = [("Image Files", ("*.jpg", "*.png"))]
    self.filename = tkFileDialog.askopenfilename(parent=self, title= "Select Attachment" , multiple=False, filetypes=filetypes);
    print self.filename;
    
    #self.filename = "/home/vladk/Desktop/12_44.png";
    
    global resizeImageTo;
    img, fileName2, fileExtension  = resizeImageTo(700, self.filename);
    
    self.newFilePath = fileName2 + "Base64Encoding.txt";
    
    print fileExtension;
    if(fileExtension == ".png"):
        formatStr = "PNG";
        formatStr2 = "png";
    elif(fileExtension == ".jpg"):
        formatStr = "JPEG";
        formatStr2 = "jpg";
    else:
        tkMessageBox.showinfo("File Type", "That file type is unrecognized. Aborting.")
        print "Unrecognized File Type. Abort.";
        return;
    
    output = cStringIO.StringIO();
    img.save(output, format=formatStr);
    im_data = output.getvalue();
    
    self.img = ImageTk.PhotoImage(img)
    self.panel["image"] = self.img;
    
    
    #print "here";
    
    self.data_url = 'data:image/' + formatStr2 + ';base64,' + base64.b64encode(im_data);
    #print self.data_url;
    
    self.btnDecode["command"] = self.fcnSaveImageAsB64
        
  def fcnPickImageFirst(self):
    tkMessageBox.showinfo("Encode an Image", "Please pick an image to encode before you save.")
    
  def fcnSaveImageAsB64(self):
    #print "Yeeeeee";
    text_file = open(self.newFilePath, "w");
    text_file.write(self.data_url);
    text_file.close();
    
    print self.newFilePath;
    tkMessageBox.showinfo("Sucessfully Saved", "Image has been successfully saved at location " + self.newFilePath);
    
    self.showMain();
        
    
        
def main():
  app = App()
  app.mainloop()

if __name__ == "__main__":
  main()