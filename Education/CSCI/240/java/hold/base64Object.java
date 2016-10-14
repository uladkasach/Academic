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
import java.io.OutputStream;
import java.io.ByteArrayOutputStream;

//import org.apache.commons.codec.binary.Base64;


public class base64Object {
    
    protected static encodeFrame masterClass;
    protected File theFile;
    protected BufferedImage theBuffImage;
    
	public static void main(String args[]) {
        System.out.println("You've ran base64Object.java. It is not meant to be run individually.");
	}
    public base64Object(){
        System.out.println("Who is the Master Class?");   
    }
   
    public base64Object(encodeFrame sentClass){
        System.out.println("Creating an base64Object class object.");   
        masterClass = sentClass;
    }
   
    
    public static File getSaveLocation() {
       JFileChooser chooser = new JFileChooser();
       chooser.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);  
       int result = chooser.showSaveDialog(masterClass);

       if (result == chooser.APPROVE_OPTION) { 
          return chooser.getSelectedFile();
       } else {
          return null;
       }
    }
    
    public String EncodeBuffImageToUri(BufferedImage sentBuffImage){
        theBuffImage = sentBuffImage;
        ByteArrayOutputStream os = new ByteArrayOutputStream();
        OutputStream b64 = new Base64.OutputStream(os);
        ImageIO.write(theBuffImage, "png", b64);
        String result = os.toString("UTF-8");
        
        return result;
    }
    
    /*
    public void pickAFile(){
        JFileChooser chooser = new JFileChooser();
        chooser.setCurrentDirectory(new java.io.File(".")); 
        chooser.setAcceptAllFileFilterUsed(false);
        FileFilter filter = new FileNameExtensionFilter("JPEG or PNG file", "jpg", "jpeg", "png");
        chooser.addChoosableFileFilter(filter);
        chooser.setDialogTitle("Select a JPEG or PNG File");
        if (chooser.showOpenDialog(null) == JFileChooser.APPROVE_OPTION) {
            theFile = chooser.getSelectedFile();
            try {
                System.out.println("Bufering output");
                buffImage = ImageIO.read(theFile);
                returnTheImageToMaster();
            } catch(IOException ex){
                System.out.println (ex.toString());
                System.out.println("Could not turn file into buffered image ");
                return;
            }
        } else {
          System.out.println("No Selection ");
        }
    }
    */
    
    
    
    //
    
}