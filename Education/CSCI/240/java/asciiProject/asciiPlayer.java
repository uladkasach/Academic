
import javax.swing.*;


public class asciiPlayer {
    
    
	public static void main(String args[]) {
       
        JFrame theFrame = createThisFrame(); // Create the Frame with Defaults
        
        JButton jb=new JButton();
        jb.setBounds(50,10,100,50);
        jb.setText("Leech");
        theFrame.add(jb);
        
        JButton jb2=new JButton();
        jb2.setBounds(350,10,100,50);
        jb2.setText("Leech");
        theFrame.add(jb2);
        
        
        
        
	}
    
    
    public static JFrame createThisFrame(){
        JFrame thisFrame = new JFrame("My Awesome Frame");
        thisFrame.setLayout(null);
		thisFrame.setVisible(true);
		thisFrame.setSize(500, 500);
		thisFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        thisFrame.setLocationRelativeTo(null); 
        return thisFrame;
    }
    
    
    
}