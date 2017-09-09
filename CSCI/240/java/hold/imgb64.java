package imgb64;

import javax.swing.*;
import javax.swing.event.*;
import javax.swing.text.*;
import javax.swing.filechooser.*;
import javax.imageio.ImageIO;

import java.awt.*;
import java.awt.Insets;
import java.awt.event.*;
import java.awt.FileDialog;
import java.awt.image.BufferedImage;
import java.awt.Image;

import java.io.File;
import java.io.FilenameFilter;
import java.io.IOException;

////https://dzone.com/articles/htmlcssjavascript-gui-java-0


public class imgb64 {
    
    protected static imgb64 thisImgb64;
    protected static mainFrame mainFrameObj;
    protected static encodeFrame encodeFrameObj;
    
	public static void main(String args[]) {
        thisImgb64 = new imgb64();
        
        mainFrameObj = new mainFrame(thisImgb64); // Create the Frame with Defaults
        encodeFrameObj = new encodeFrame(thisImgb64);
        
        thisImgb64.changeDisplayTo("Main");
	}
    public imgb64(){}
    public static void changeDisplayTo(String what){
        System.out.println("Change this display to " + what);   
        if(what == "Main"){
            mainFrameObj.setVisible(true);
		    encodeFrameObj.setVisible(false);
        } else if(what == "Encode"){
            mainFrameObj.setVisible(false);
		    encodeFrameObj.setVisible(true);
        } else if (what == "Decode"){
            mainFrameObj.setVisible(false);
		    encodeFrameObj.setVisible(false);
        }
    }
    
}