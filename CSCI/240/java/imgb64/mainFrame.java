
package imgb64;

// Filename = cFrame.java
import javax.swing.*;
import javax.swing.event.*;
import javax.swing.text.*;
//import javax.swing.JFrame;
//import javax.swing.JScrollPane;
//import javax.swing.JTextArea;
//import javax.swing.SwingUtilities;
import java.awt.*;
import java.awt.Insets;
import java.awt.event.*;
import java.awt.FileDialog;
import java.io.File;
import java.io.FilenameFilter;


public class mainFrame extends JFrame {
    protected JLabel panelStatus;
    protected JButton encodeButton;
    protected JButton decodeButton;
    protected JButton helpButton;
    protected static imgb64 controlClass;
    
	public static void main(String args[]) {
        System.out.println("You've ran mainFrame.java. It is not ment to be run individually.");
        //mainFrame theFrame = new mainFrame(); // Create the Frame with Defaults
		//theFrame.setVisible(true);
	}
    
    public mainFrame(imgb64 sentClass){
        System.out.println("Creating a mainFrame class object.");
        controlClass = sentClass;
        
        /////////////////////////////////////////
        // Set the basics of the frame
        /////////////////////////////////////////
        //JFrame thisFrame = new JFrame("My Awesome Frame");
        mainFrame thisFrame = this;
        thisFrame.setTitle("Image Base64 Transcoder");
        thisFrame.setLayout(null);
		thisFrame.setSize(500, 260);
		thisFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        thisFrame.setLocationRelativeTo(null); 
        
        
        /////////////////////////////////////////
        // Set the Panel Position and Status Label
        /////////////////////////////////////////
        panelStatus = new JLabel();
        panelStatus.setText("Welcome to Image-Base64 Transcoder.");
        panelStatus.setBounds(100,25,300,30);
        thisFrame.add(panelStatus);
        
        
        /////////////////////////////////////////
        // Set the load and save buttons 
        /////////////////////////////////////////
        encodeButton = new JButton();
        encodeButton.setBounds(100,75,300,50);
        encodeButton.setText("Encode Image into Base64");
        encodeButton.addActionListener(new aChangeDisplay("Encode"));
        thisFrame.add(encodeButton);
        
        decodeButton = new JButton();
        decodeButton.setBounds(100,150,300,50);
        decodeButton.setText("Decode Base64 into Image");
        decodeButton.addActionListener(new aChangeDisplay("Decode"));
        thisFrame.add(decodeButton);
        
        ////////
        // setVisible only after all elements are added
        ////////
        // 
		
        //thisFrame.setVisible(true);
    }
    
    
    /////////////////////////////////////////////////////////////////////////////
    // Set Button Actions ///////////////////////////////////////////////////////
    /////////////////////////////////////////////////////////////////////////////
    private static class aChangeDisplay implements ActionListener{
        protected String doWhat;
        public aChangeDisplay(String toWhat){
            doWhat = toWhat;   
        }
        public void actionPerformed(ActionEvent obj1){
            controlClass.changeDisplayTo(doWhat);
        } 
    } 
    
    
}
