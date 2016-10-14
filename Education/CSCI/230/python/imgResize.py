import PIL
from PIL import Image
import os.path
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
        return;
    
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
    
    img.save(fileName + "-baseSize" + str(basesize) + fileExtension);
    


resizeImageTo(100, "/home/vladk/Desktop/12_44.gif"); 

