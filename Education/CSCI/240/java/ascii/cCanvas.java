// Filename = cCanvas.java
package ascii;
import javax.swing.*;
import java.awt.Font;
import java.nio.charset.Charset;
import java.io.IOException;
import java.nio.file.*;
import java.util.Scanner;
import java.io.File;
import java.io.PrintWriter;
import java.io.FileNotFoundException;

public class cCanvas extends JTextArea {
    
    String[] panels = new String[20];
    int currentPanel;
    int totalPanels;
    cFrame theFrame;
    protected String content;
    
    public cCanvas(cFrame theFrameSent){  
        setFont(new Font("monospaced", Font.PLAIN, 12));
        setLineWrap(true);
        setWrapStyleWord(true);
        panels[0] = "";
        currentPanel = 0;
        totalPanels = 1;
        theFrame = theFrameSent;
        determineAbleButtons();
        displayPanelStatus();
        
        int total = 20;
        int count = 0;
        while(count < total){
            panels[count] = "Your Panel " + (count+1) + " is empty!";
            count+=1;   
        }
        
        displayPanel(currentPanel);
    }
    
    public static void main(String[] args){
        System.out.println("Running cCanvas.java");
    }
 
    
    public void displayPanel(int which){
        if(which < 20){
            setText(panels[which]);  
        } else {
            System.out.println("Cannot display panel above 10");   
        }
    }
    
    public void nextPanel(){
        saveCurrentPanel();
        currentPanel += 1;
        displayPanel(currentPanel);
        determineAbleButtons();
        displayPanelStatus();
    }
    public void backPanel(){
        saveCurrentPanel();
        currentPanel -= 1;
        displayPanel(currentPanel);
        determineAbleButtons();
        displayPanelStatus();
    }
    
    protected void addPanel(){
        totalPanels += 1;
        //System.out.println("Added a Panel - total = " + totalPanels);
        determineAbleButtons();
        displayPanelStatus();
    }
    
    protected void removePanel(){
        totalPanels -= 1;
        //System.out.println("Removed a Panel - total = " + totalPanels);
        determineAbleButtons();
        displayPanelStatus();
    }

    protected void saveCurrentPanel(){
        //System.out.println("Saving data to panel " + currentPanel);
        panels[currentPanel] = getText();
    }
    
    protected void displayPanelStatus(){
        theFrame.setStatus("Displaying Panel " + (currentPanel+1) + " / " + totalPanels);
    }
    
    protected void determineAbleButtons(){
            theFrame.enableButton("next");
            theFrame.enableButton("back");
        if(totalPanels < 2){
            theFrame.disableButton("next");
            theFrame.disableButton("back");
        } else if (currentPanel == 0) {
            theFrame.disableButton("back");
        } else if (currentPanel == totalPanels-1){
            theFrame.disableButton("next");
        }
        
        if(totalPanels < 2){
            theFrame.disableButton("remove");
        } else if(totalPanels == 2) {
            theFrame.enableButton("remove");
        }
        
        if(totalPanels > 19){
            theFrame.disableButton("add");
        } else if(totalPanels == 19){
            theFrame.enableButton("add");
        }
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
    
    protected void loadFromFile(String filename){
        try {
            System.out.println("Load from file " + filename);   
            content = readFile(filename);
            //System.out.println(content);
        } catch(IOException ex){
            System.out.println (ex.toString());
            System.out.println("Could not find file " + filename);
            return;
        }
        
        String[] panelsArrayLoad = content.split("PANELSEPERATORASCI9001");
        //System.out.println(panelsArrayLoad[1]);
        
        /////////////////////////////
        /////// Count Array Length
        int counter = 0;
        for (int i = 0; i < panelsArrayLoad.length; i ++)
            if (panelsArrayLoad[i] != null)
                counter ++;
        /////////////////////////////
        int total = counter;
        int count = 0;
        if(total > 20){
            total = 20;   
        }
        while(count < total){
            panels[count] = panelsArrayLoad[count];
            count+=1;   
        }
        currentPanel = 0;
        totalPanels = total;
        displayPanel(currentPanel);
        determineAbleButtons();
        displayPanelStatus();
    }
    
    protected void savePanelsToFile(){
        saveCurrentPanel();
        System.out.println("Saving this file biches");
        try {
            PrintWriter out = new PrintWriter("yourAnimation.ascii9001");
            int total = totalPanels;
            int count = 1;
            String text = panels[0];
            while(count < total){
                text = text + "PANELSEPERATORASCI9001" + panels[count];
                count += 1;   
            }
            out.println(text);
            out.close();
            theFrame.setStatus("Saved to yourAnimation.ascii9001");
        } catch(FileNotFoundException ex){
            System.out.println (ex.toString());
            System.out.println("Could not find file ");
            return;
        }
    }
}