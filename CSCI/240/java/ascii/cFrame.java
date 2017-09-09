

package ascii;
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

public class cFrame extends JFrame {
    
    protected static cCanvas canvasObj;
    protected static JButton backButton;
    protected static JButton nextButton;
    protected static JButton addButton;
    protected static JButton removeButton;
    protected static JLabel panelStatus;
        
	public static void main(String args[]) {
        cFrame theFrame = new cFrame(); // Create the Frame with Defaults
	}
    
    public cFrame(){
        /////////////////////////////////////////
        // Set the basics of the frame
        /////////////////////////////////////////
        //JFrame thisFrame = new JFrame("My Awesome Frame");
        cFrame thisFrame = this;
        thisFrame.setTitle("Ascii Animatrix 9001");
        thisFrame.setLayout(null);
		thisFrame.setSize(500, 450);
		thisFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        thisFrame.setLocationRelativeTo(null); 
        
        
        /////////////////////////////////////////
        // Set the load and save buttons 
        /////////////////////////////////////////
        JButton jb=new JButton();
        jb.setBounds(50,10,100,30);
        jb.setText("Load");
        jb.addActionListener(new cLoad());
        thisFrame.add(jb);
        
        JButton jb2=new JButton();
        jb2.setBounds(350,10,100,30);
        jb2.setText("Save");
        jb2.addActionListener(new cSave());
        thisFrame.add(jb2);
        
        /////////////////////////////////////////
        // Set the Next and Back buttons 
        /////////////////////////////////////////
        nextButton = new JButton();
        nextButton.setBounds(425,125,50,70);
        nextButton.setText("Next");
        nextButton.setMargin(new Insets(0, 0, 0, 0));
        nextButton.addActionListener(new cNextPanel());
        thisFrame.add(nextButton);
        
        backButton = new JButton();
        backButton.setBounds(25,125,50,70);
        backButton.setText("Back");
        backButton.setMargin(new Insets(0, 0, 0, 0));
        backButton.addActionListener(new cBackPanel());
        thisFrame.add(backButton);

        
        /////////////////////////////////////////
        // Set the Add and Remove buttons 
        /////////////////////////////////////////
        addButton = new JButton();
        addButton.setBounds(50,360,150,30);
        addButton.setText("Add Panel");
        addButton.setMargin(new Insets(0, 0, 0, 0));
        addButton.addActionListener(new cAddPanel());
        thisFrame.add(addButton);
        
        removeButton = new JButton();
        removeButton.setBounds(300,360,150,30);
        removeButton.setText("Remove Panel");
        removeButton.setMargin(new Insets(0, 0, 0, 0));
        removeButton.addActionListener(new cRemovePanel());
        thisFrame.add(removeButton);
        
        
        /////////////////////////////////////////
        // Set the Panel Position and Status Label
        /////////////////////////////////////////
        panelStatus = new JLabel("Test");
        panelStatus.setText("Displaying Panel 1  - Out of 5");
        panelStatus.setBounds(100,300,300,30);
        thisFrame.add(panelStatus);
        
        
        /////////////////////////////////////////
        // Set the canvasObj 
        /////////////////////////////////////////
        canvasObj = new cCanvas(thisFrame);
        canvasObj.setBounds(100,70,300,200);
        thisFrame.add(canvasObj);
        
        ////////
        // setVisible only after all elements are added
        ////////
		thisFrame.setVisible(true);
        
    }
    
    
    /////////////////////////////////////////////////////////////////////////////
    // Set Essential Methods ////////////////////////////////////////////////////
    /////////////////////////////////////////////////////////////////////////////
    public void disableButton(String who){
        if(who == "next"){
            nextButton.setEnabled(false);
        } else if (who == "back"){
            backButton.setEnabled(false);
        } else if (who == "add"){
            addButton.setEnabled(false);
        } else if (who == "remove"){
            removeButton.setEnabled(false);
        } else {
            System.out.println("Dont know who you want to disable.");
        }
    }
    public void enableButton(String who){
        if(who == "next"){
            nextButton.setEnabled(true);
        } else if (who == "back"){
            backButton.setEnabled(true);
        } else if (who == "add"){
            addButton.setEnabled(true);
        } else if (who == "remove"){
            removeButton.setEnabled(true);
        } else {
            System.out.println("Dont know who you want to disable.");
        }
    }
    public void setStatus(String sayWhat){
        panelStatus.setText(sayWhat);
    }
    public void pickAFile(){
        FileDialog fd = new FileDialog(this, "Choose a ascii9001 file", FileDialog.LOAD);
        fd.setDirectory("C:\\");
        fd.setFilenameFilter(new FilenameFilter() {
            @Override
            public boolean accept(File dir, String name) {
                return name.endsWith(".ascii9001");
            }
        });
        fd.setVisible(true);
        String filename = fd.getFile();
        if (filename == null){
          System.out.println("You cancelled the choice");
        } else {
          System.out.println("You chose " + filename);   
          canvasObj.loadFromFile(filename);
        }
    }
    /////////////////////////////////////////////////////////////////////////////
    // Set Button Actions ///////////////////////////////////////////////////////
    /////////////////////////////////////////////////////////////////////////////
    public static class cNextPanel implements ActionListener{
        public void actionPerformed(ActionEvent obj1){
            canvasObj.nextPanel();
        } 
    } 
    public static class cBackPanel implements ActionListener{
        public void actionPerformed(ActionEvent obj1){
            canvasObj.backPanel();
        } 
    } 
    public static class cAddPanel implements ActionListener{
        public void actionPerformed(ActionEvent obj1){
            canvasObj.addPanel();
        } 
    } 
    public static class cRemovePanel implements ActionListener{
        public void actionPerformed(ActionEvent obj1){
            canvasObj.removePanel();
        } 
    } 
    public class cLoad implements ActionListener{
        public void actionPerformed(ActionEvent obj1){
            pickAFile();
        } 
    } 
    public class cSave implements ActionListener{
        public void actionPerformed(ActionEvent obj1){
            canvasObj.savePanelsToFile();
        } 
    } 
        
    
}