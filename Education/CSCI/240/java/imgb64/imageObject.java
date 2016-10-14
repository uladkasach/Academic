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

public class imageObject {
    
    protected encodeFrame masterClass;
    protected decodeFrame masterClass2;
    protected File theFile;
    protected BufferedImage buffImage;
    protected String theDir;
    
	public static void main(String args[]) {
        System.out.println("You've ran imageObject.java. It is not meant to be run individually.");
	}
    public imageObject(){
        System.out.println("Who is the Master Class?");   
    }
   
    public imageObject(encodeFrame sentClass){
        System.out.println("Creating an imageObject class object.");   
        masterClass = sentClass;
    }
    public imageObject(decodeFrame sentClass){
        System.out.println("Creating an imageObject class object.");   
        masterClass2 = sentClass;
    }
   
    
    public void pickAFile(){
        JFileChooser chooser = new JFileChooser();
        chooser.setCurrentDirectory(new java.io.File(".")); 
        chooser.setAcceptAllFileFilterUsed(false);
        FileFilter filter = new FileNameExtensionFilter("JPEG or PNG file", "jpg", "jpeg", "png");
        chooser.addChoosableFileFilter(filter);
        chooser.setDialogTitle("Select a JPEG or PNG File");
        if (chooser.showOpenDialog(null) == JFileChooser.APPROVE_OPTION) {
            theFile = chooser.getSelectedFile();
            theDir = theFile.getParent();
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
    
    public String getTheDir(){
        return theDir;   
    }
    
    public String getTheFilePath(){
        return theFile.getAbsolutePath();   
    }
    
    public BufferedImage getImageBuffSizedAt(int width, int height){
        return resize(buffImage, width, height);
    }
    
    public void saveTheImageAs(BufferedImage buffToWrite, String filePath, String theExt){
       
            try {
                 File outputfile = new File(filePath);
                ImageIO.write(buffToWrite, theExt, outputfile);   
            } catch(IOException ex){
                System.out.println (ex.toString());
                System.out.println("Could not create image file ");
                return;
            }
    }
    
    
    public void returnTheImageToMaster(){
        System.out.println("Returning this ImageIcon to MasterClass");
        ImageIcon iconToSend = new ImageIcon(resize(buffImage,300,200)); 
        masterClass.displayImage(iconToSend);
        //icon;
    }
    
    public void setThisImageFromMaster(BufferedImage sentBuffImage){
        buffImage = sentBuffImage;
        System.out.println("The image has been set");
        
        ImageIcon iconToSend = new ImageIcon(resize(buffImage,300,200)); 
        masterClass2.displayImage(iconToSend);
        
    }
    
    public BufferedImage getBuffImage(){
        return buffImage;
    }
    
    public static BufferedImage resize(BufferedImage image, int width, int height) {
        BufferedImage bi = new BufferedImage(width, height, BufferedImage.TRANSLUCENT);
        Graphics2D g2d = (Graphics2D) bi.createGraphics();
        g2d.addRenderingHints(new RenderingHints(RenderingHints.KEY_RENDERING, RenderingHints.VALUE_RENDER_QUALITY));
        g2d.drawImage(image, 0, 0, width, height, null);
        g2d.dispose();
        return bi;
    }
    
    //
    
}