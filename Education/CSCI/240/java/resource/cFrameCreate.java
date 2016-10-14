import javax.swing.*;
import java.awt.*;
import java.awt.FlowLayout;
import java.awt.event.*;
 

//http://www.javaprogrammingforums.com/java-swing-tutorials/15198-creating-simple-gui-jframe.html

public class cFrameCreate extends JFrame
{
    
    private void cFrameCreate()
    {
        setTitle("Frame Example");
        setSize(400, 200);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null); 
        setVisible(true);

        prepContent(); 
        
    } // End FrameCreate
 
    private void prepContent()
    {
        setLayout(new FlowLayout(FlowLayout.CENTER));

        JLabel theLabel = new JLabel("Yo Shawty, I'ts");
        add(theLabel);

        JButton theButton = new JButton("Sherbert Day");  
        add(theButton);
        theButton.addActionListener(new cPrintHello());
    } // END prepContent

    public class cPrintHello implements ActionListener{
        public void actionPerformed(ActionEvent obj1){
            System.out.println("Hello Buddy");
        } 
    } // END cPrintHello


    public static void main(String[] args)
    {
        cFrameCreate theFrame = new cFrameCreate();   
    } // END main
     
}