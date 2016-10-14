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

public class decodeFrame extends JFrame {
    
    
    protected static imgb64 controlClass;
    
    protected static decodeFrame thisFrame;
    
    protected JLabel panelStatus;
    protected static JButton chooseButton;
    protected static JButton saveButton;
    protected static JButton helpButton;
    protected static JButton returnButton;
    
    protected static imageObject theImage;
    protected static JLabel imageLabel;
    protected static JPanel imagePanel;
    
    protected static base64Object theBase64;
    
    protected static chooseNameFrameDecode theNameFrame;
    
    protected static JLabel finalSizeLabel;
    protected static JLabel newWidthLabel; 
    protected static JTextField newWidth;
    protected static JLabel newHeightLabel; 
    protected static JTextField newHeight;
    
    protected static String digitsOnlyString;
    
    protected static String theExt;
    
	public static void main(String args[]) {
        System.out.println("You've ran decodeFrame.java. It is not meant to be run individually.");
	}
    
    public decodeFrame(imgb64 sentClass){
        System.out.println("Creating a decodeFrame class object.");
        controlClass = sentClass;
        
        thisFrame = this;
        theImage = new imageObject(thisFrame);
        theBase64 = new base64Object(thisFrame);
        theNameFrame = new chooseNameFrameDecode(thisFrame, "/var/www/CSCi/jaera", "base64uri");
        //theImage.setMasterClass(thisFrame);
        
        
        /////////////////////////////////////////
        // Set the basics of the frame
        /////////////////////////////////////////
        //JFrame thisFrame = new JFrame("My Awesome Frame");
        //encodeFrame thisFrame = this; --- Already set to pass this class reference to the image object
        thisFrame.setTitle("Decode a Base64 Uri into an Image");
        thisFrame.setLayout(null);
		thisFrame.setSize(500, 320);
		thisFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        thisFrame.setLocationRelativeTo(null); 
        
        
        /////////////////////////////////////////
        // Set the Panel Position and Status Label
        /////////////////////////////////////////
        panelStatus = new JLabel();
        panelStatus.setText("Decode a Base64 Uri into an Image");
        panelStatus.setBounds(100,25,300,30);
        thisFrame.add(panelStatus);
        
        
        /////////////////////////////////////////
        // Set the load and save buttons 
        /////////////////////////////////////////
       
        chooseButton = new JButton();
        chooseButton.setBounds(100,75,300,50);
        chooseButton.setText("Pick a .base64uri File");
        chooseButton.addActionListener(new aChooseButton());
        thisFrame.add(chooseButton);
        
        saveButton = new JButton();
        saveButton.setBounds(100,150,300,50);
        saveButton.setText("Save as an Image");
        saveButton.addActionListener(new aSaveButton());
        saveButton.setEnabled(false);
        thisFrame.add(saveButton);

        returnButton = new JButton();
        returnButton.setBounds(300,250,100,30);
        returnButton.setText("Return");
        returnButton.addActionListener(new aChangeDisplay2("Main"));
        thisFrame.add(returnButton);
        
        
        /////////////////////////////////////////
        // Set the image display GUI parts
        /////////////////////////////////////////
        
        imagePanel = new JPanel(); 
        imagePanel.setBounds(100,280,300,200);
        imageLabel = new JLabel(); 
        imagePanel.add(imageLabel);
        thisFrame.add(imagePanel);
        imagePanel.setVisible(false);
        
        
        /////////////////////////////////////////
        // Set the final size parts of GUI
        /////////////////////////////////////////
        
        finalSizeLabel = new JLabel(); 
        finalSizeLabel.setBounds(100,210,300,30);
        thisFrame.add(finalSizeLabel);
        finalSizeLabel.setVisible(false);
        
        newWidthLabel = new JLabel(); 
        newWidthLabel.setText("New Width");
        newWidthLabel.setBounds(100,240,80,30);
        thisFrame.add(newWidthLabel);
        newWidthLabel.setVisible(false);
        
        newWidth = new JTextField();
        newWidth.setBounds(190,240,50,30);
        newWidth.getDocument().addDocumentListener(new lNumsOnlyCheckHeight());
        thisFrame.add(newWidth);
        newWidth.setVisible(false);
        
        newHeightLabel = new JLabel(); 
        newHeightLabel.setText("New Height");
        newHeightLabel.setBounds(250,240,100,30);
        thisFrame.add(newHeightLabel);
        newHeightLabel.setVisible(false);
        
        newHeight = new JTextField();
        newHeight.setBounds(340,240,50,30);
        newHeight.getDocument().addDocumentListener(new lNumsOnlyCheckHeight());
        thisFrame.add(newHeight);
        newHeight.setVisible(false);
        
    }
    
    
    /////////////////////////////////////////////////////////////////////////////
    // Set Main Functions ///////////////////////////////////////////////////////
    /////////////////////////////////////////////////////////////////////////////
    public static void displayImage(ImageIcon theIcon){
        System.out.println("Displaying the Image"); 
        imageLabel.setIcon(theIcon); 
        finalSizeLabel.setText("Max Width : " + theImage.getBuffImage().getWidth() + "px. Max Height : " + theImage.getBuffImage().getHeight() + "px."  );
        thisFrame.adjustFrameToMode("Image");
        newWidth.setText(String.valueOf(theImage.getBuffImage().getWidth())); 
        newHeight.setText(String.valueOf(theImage.getBuffImage().getHeight())); 
    }
    
    public static void adjustFrameToMode(String which){
        if(which == "Image"){
            
            imagePanel.setVisible(true);

            finalSizeLabel.setVisible(true);
            newWidthLabel.setVisible(true);
            newWidth.setVisible(true);
            newHeightLabel.setVisible(true);
            newHeight.setVisible(true);
            
            saveButton.setEnabled(true);

            thisFrame.setSize(500, 600);
            returnButton.setBounds(300,510,100,30);   
            thisFrame.setVisible(true);
            
        } else if (which == "Default") {
            
            imagePanel.setVisible(false);

            finalSizeLabel.setVisible(false);
            newWidthLabel.setVisible(false);
            newWidth.setVisible(false);
            newHeightLabel.setVisible(false);
            newHeight.setVisible(false);

            saveButton.setEnabled(false);
            
            thisFrame.setSize(500, 320);
            returnButton.setBounds(300,250,100,30);
            thisFrame.setVisible(true);
            
        } else {
            System.out.println("Which mode would you like this frame to be in?");   
        }
    }
    
    public static void sendBuffImageToImageObject(BufferedImage theBuffImage, String theExtension){
        System.out.println("Got the image");   
        theImage.setThisImageFromMaster(theBuffImage);
        theExt = theExtension;
    }
    
    public static void saveThisImageAsABase64(){
        theNameFrame.setDir(theBase64.getTheDir());
        theNameFrame.setExt(theExt);
        theNameFrame.setVisible(true);
    }
    
    public static void continueSavingIt(){
        theNameFrame.setVisible(false);
        String filePath = theNameFrame.getTheFilePath();
        System.out.println("Save it at " + filePath);   
        
        BufferedImage buffImageToEncode = theImage.getImageBuffSizedAt(Integer.parseInt(newWidth.getText()), Integer.parseInt(newHeight.getText()));
        System.out.println("Resized image returned");
        
        String fileName = filePath;
        String extension = "";
        int i = fileName.lastIndexOf('.');
        if (i > 0) {
            extension = fileName.substring(i+1);
        }
        
        System.out.println("Extension = "  + extension);
        
        theImage.saveTheImageAs(buffImageToEncode, filePath, extension);
        
        //String theUri = theBase64.EncodeBuffImageToUri(buffImageToEncode, extension);
        
        //theBase64.saveThisEncoding(theUri, filePath);

        JOptionPane.showMessageDialog(null,
          "Your file has been saved at " + filePath, "Success!",
          JOptionPane.ERROR_MESSAGE);
        
        thisFrame.adjustFrameToMode("Default");
        controlClass.changeDisplayTo("Main");
        
        
    }
    
    /////////////////////////////////////////////////////////////////////////////
    // Set Button Actions ///////////////////////////////////////////////////////
    /////////////////////////////////////////////////////////////////////////////
    private static class aChangeDisplay2 implements ActionListener{
        protected String doWhat;
        public aChangeDisplay2(String toWhat){
            doWhat = toWhat;   
        }
        public void actionPerformed(ActionEvent obj1){
            thisFrame.adjustFrameToMode("Default");
            controlClass.changeDisplayTo(doWhat);
        } 
    } 
    private static class aChooseButton implements ActionListener{
        public void actionPerformed(ActionEvent obj1){
            theBase64.pickAFile();
        } 
    }
    private static class aSaveButton implements ActionListener{
        public void actionPerformed(ActionEvent obj1){
            saveThisImageAsABase64();
            //System.out.println();
            //base64Object.getSaveLocation();
        } 
    }
    
   
    /////////////////////////////////////////////////////////////////////////////
    // Set Document Listeners ///////////////////////////////////////////////////
    /////////////////////////////////////////////////////////////////////////////
    private static class lNumsOnlyCheckHeight implements DocumentListener{
          public void changedUpdate(DocumentEvent e) {
            makeNumOnly();
          }
          public void removeUpdate(DocumentEvent e) {
            makeNumOnly();
          }
          public void insertUpdate(DocumentEvent e) {
            makeNumOnly();
          }
          public static void makeNumOnly() {
                  SwingUtilities.invokeLater(new Runnable(){
                    public void run() {
                        if(newWidth.getText().length() == 0){
                            newWidth.setText("0"); 
                        }
                        if(newHeight.getText().length() == 0){
                            newHeight.setText("0"); 
                        }
                         String theText = newWidth.getText();
                         String digits = theText.replaceAll("[^0-9]", "").replaceFirst("^0+(?!$)", "");
                         String theText2 = newHeight.getText();
                         String digits2 = theText2.replaceAll("[^0-9]", "").replaceFirst("^0+(?!$)", "");
                          if(theText != digits || theText2 != digits2){
                              newWidth.setText(digits); 
                              newHeight.setText(digits2); 
                          } else {
                              if(
                                Integer.parseInt(newWidth.getText()) > theImage.getBuffImage().getWidth()
                                    ||
                                Integer.parseInt(newHeight.getText()) > theImage.getBuffImage().getHeight()
                                    || 
                                Integer.parseInt(newWidth.getText()) < 2
                                    || 
                                Integer.parseInt(newHeight.getText()) < 2
                              ){
                                  finalSizeLabel.setForeground (Color.red);
                                  saveButton.setEnabled(false);
                              } else {
                                  finalSizeLabel.setForeground (Color.black);
                                  saveButton.setEnabled(true);
                              }   
                          }
                    }
                });
          }
    }
    
}


/*
JOptionPane.showMessageDialog(null,
  "Error: Please enter number bigger than 0", "Error Massage",
  JOptionPane.ERROR_MESSAGE);

  */