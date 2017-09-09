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
import java.io.ByteArrayInputStream;

import javax.xml.bind.DatatypeConverter;
import java.io.UnsupportedEncodingException;

import java.io.File;
import java.io.PrintWriter;
import java.io.FileNotFoundException;

import java.util.Scanner;

//import org.apache.commons.codec.binary.Base64;


public class base64Object {
    
    protected static encodeFrame masterClass;
    protected static decodeFrame masterClass2;
    protected File theFile;
    protected BufferedImage theBuffImage;
    protected String theDir;
    
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
    public base64Object(decodeFrame sentClass){
        System.out.println("Creating an base64Object class object.");   
        masterClass2 = sentClass;
    }
   
    
    
    public String EncodeBuffImageToUri(BufferedImage sentBuffImage, String theExtension){
       theBuffImage = sentBuffImage;
        
       String uri = "data:image/" + theExtension + ";base64,";
       try{
            BufferedImage originalImage = theBuffImage;
            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            ImageIO.write( originalImage, "jpg", baos );
            baos.flush();
            byte[] imageInByte = baos.toByteArray();
            baos.close();	
            String encoded = uri + DatatypeConverter.printBase64Binary(imageInByte);
            return encoded;
        }catch(IOException e){
            System.out.println(e.getMessage());
            return "errored";
        }	
    }
    
    public void saveThisEncoding(String theEncoding, String filePath){
        System.out.println("Saving the txt encoding at " + filePath);   
        try {
            PrintWriter out = new PrintWriter(filePath);
            out.println(theEncoding);
            out.close();
        } catch(FileNotFoundException ex){
            System.out.println (ex.toString());
            System.out.println("Could not find file ");
            return;
        }
    }
    
    
    
   
    public void pickAFile(){
        JFileChooser chooser = new JFileChooser();
        chooser.setCurrentDirectory(new java.io.File(".")); 
        chooser.setAcceptAllFileFilterUsed(false);
        FileFilter filter = new FileNameExtensionFilter("A Base64 Text File", "base64uri");
        chooser.addChoosableFileFilter(filter);
        chooser.setDialogTitle("Select a .base64uri File");
        if (chooser.showOpenDialog(null) == JFileChooser.APPROVE_OPTION) {
            theFile = chooser.getSelectedFile();
            theDir = theFile.getParent();
            try {
                System.out.println("Load from file " + theFile.getAbsolutePath());   
                String theText = readFile(theFile.getAbsolutePath());
                //System.out.println(theText);
                
                turnItIntoBuffImage(theText);
                
            } catch(IOException ex){
                System.out.println (ex.toString());
                System.out.println("Could not find file ");
                return;
            }
            
            
        } else {
          System.out.println("No Selection ");
        }
    }
   
    
    public String getTheDir(){
        return theDir;   
    }
    
    public void turnItIntoBuffImage(String theBase64Code){
        String[] tokens = theBase64Code.split(";base64,");
        String[] tokens2 = tokens[0].split("image/");
        System.out.println("The extension is " + tokens2[1]);
        String theBase64String = tokens[1];
        
        byte[] decoded = DatatypeConverter.parseBase64Binary(theBase64String);
        BufferedImage theBufferedImage = createImageFromBytes(decoded);
        
        masterClass2.sendBuffImageToImageObject(theBufferedImage, tokens2[1]);
    }
    
    private String readFile(String pathname) throws IOException {
        File file = new File(pathname);
        StringBuilder fileContents = new StringBuilder((int)file.length());
        Scanner scanner = new Scanner(file);
        String lineSeparator = System.getProperty("line.separator");

        try {
            while(scanner.hasNextLine()) {        
                fileContents.append(scanner.nextLine() + lineSeparator);
            }
            return fileContents.toString();
        }  finally {
            scanner.close();
        }
    } 
    
    private BufferedImage createImageFromBytes(byte[] imageData) {
        ByteArrayInputStream bais = new ByteArrayInputStream(imageData);
        try {
            return ImageIO.read(bais);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
    
    //
    
}