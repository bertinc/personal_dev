/**
 * Author: Robert W. Rallison
 * Last Modified: 6/24/2003
 * Dependentcies: Java Swing, Java Awt, java run-time 1.2 or later
 * Description: This is the main driver for the grating calculator.  In here
 * I create an instance of the calculator for a main frame and make it visible
 *
 * Notes: This is only a prototype.  It is not a finished product by any means.
 * Also, I do not claim that calculations will be error free.  I still need to
 * include a lot of error protection for limits.  This is only my third
 * attempt at graphical applications in Java Swing, so the code may look a
 * little ugly.
 */

import javax.swing.*;
import java.awt.*;

class Main {
	public static void main(String[] args) {
		// setting up the look and feel
		try {
        	UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
    	} catch (Exception e) { }
        
        // creating the main frame and making it visible
		AngleCalculator mainFrame = new AngleCalculator();
		mainFrame.setSize(260, 290);
		mainFrame.setTitle("Grating Calculator");
		mainFrame.setVisible(true);
    } // end of main driver
}