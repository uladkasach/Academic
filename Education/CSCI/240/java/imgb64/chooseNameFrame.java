package imgb64;

import javax.swing.*;
import javax.swing.event.*;
import javax.swing.text.*;

import java.awt.*;
import java.awt.event.*;


public class chooseNameFrame extends JFrame {
    
    protected encodeFrame masterClass;
    protected String theDir;
    protected String theExt;
    protected static chooseNameFrame thisFrame;
    protected JTextField newName;
    
    protected JLabel theDirLabel;
    protected JLabel theExtLabel;
    
	public static void main(String args[]) {
        System.out.println("You've ran chooseNameFrame.java. It is not meant to be run individually.");
	}
    
    public chooseNameFrame(encodeFrame sentClass, String sentDir, String sentExt){
        System.out.println("Creating a chooseNameFrame class object.");   
        masterClass = sentClass;
        theDir = sentDir;
        theExt = sentExt;
        
        thisFrame = this;
        
        thisFrame.setTitle("Choose a Name to Save File As");
        thisFrame.setLayout(null);
		thisFrame.setSize(400, 220);
		//thisFrame.setDefaultCloseOperation();
        thisFrame.setLocationRelativeTo(null); 
        
        
        /////////////////////////////////////////
        // Set the Main Label
        /////////////////////////////////////////
        JLabel panelStatus2 = new JLabel();
        panelStatus2.setText("Directory will be");
        panelStatus2.setBounds(50,05,300,30);
        thisFrame.add(panelStatus2);
        
        theDirLabel = new JLabel();
        theDirLabel.setText( theDir);
        theDirLabel.setBounds(75,23,275,30);
        thisFrame.add(theDirLabel);
        
        
        JLabel panelStatus5 = new JLabel();
        panelStatus5.setText("File Name will be ");
        panelStatus5.setBounds(50,55,300,30);
        thisFrame.add(panelStatus5);
        
        
        newName = new JTextField();
        newName.setBounds(70,85,180,30);
        newName.setText("myAwesomeEncodedImage");
        //newName.getDocument().addDocumentListener(new AlphaOnlyMakeSure());
        thisFrame.add(newName);
        
        
        theExtLabel = new JLabel();
        theExtLabel.setText("."+theExt);
        theExtLabel.setBounds(255,85,100,30);
        thisFrame.add(theExtLabel);
        
        JButton chooseButton = new JButton();
        chooseButton.setBounds(50,130,300,50);
        chooseButton.setText("Use This File Name");
        chooseButton.addActionListener(new aChooseButton());
        thisFrame.add(chooseButton);
        
        //thisFrame.setVisible(true);
    }
    
    /////////////////////////////////////////////////////////////////////////////
    // Set Main Functions ///////////////////////////////////////////////////////
    /////////////////////////////////////////////////////////////////////////////
    public void tryAndChooseIt(){
        //System.out.println("Choosing it baws");   
        if(newName.getText().length() < 1){
            JOptionPane.showMessageDialog(null, "Error: Name can not be blank!", "Error Massage", JOptionPane.ERROR_MESSAGE);
        } else {
            masterClass.continueSavingIt();
        }
    }
    
    public void setDir(String sentDir){
        theDir = sentDir;   
        theDirLabel.setText( theDir);
    }
    public void setExt(String sentExt){
        theExt = sentExt;   
        theExtLabel.setText("."+theExt);
    }
    
    public String getTheName(){
        return newName.getText();   
    }
    
    public String getTheFilePath(){
        return theDir +"/"+ newName.getText() + "." + theExt;   
    }
    
    /////////////////////////////////////////////////////////////////////////////
    // Set Button Actions ///////////////////////////////////////////////////////
    /////////////////////////////////////////////////////////////////////////////
    private static class aChooseButton implements ActionListener{
        public void actionPerformed(ActionEvent obj1){
            thisFrame.tryAndChooseIt();
        } 
    }
    
    
    
}