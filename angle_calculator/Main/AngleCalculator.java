/**
 * Author: Robert W. Rallison
 * Last Modified: 6/24/2003
 * Dependentcies: Java Swing, Java Awt, java run-time 1.2 or later
 * Description: This is where all graphics or arranged and all calculations
 * are made.
 *
 * Notes: The print job setup can be found in the last function.
 */

import java.io.*;
import java.awt.*;
import java.awt.print.*;
import java.awt.font.*;
import java.awt.geom.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.*;
import java.lang.*;
import java.text.AttributedString;

public class AngleCalculator extends JFrame implements ActionListener {
	JTextField waveLength; // wavelength input from angle calculator
	JTextField spatFreq; // spatial frequency input from angle calculator
	JTextField halfAngle; // half angle output from angle calculator
	JTextField fullAngle; // full angle output from angle calculator
	JTextField DMSHalf; // half angle output in deg min sec from angle calculator
	JTextField DMSFull; // full angle output in deg min sec from angle calculator
	// add this
	JTextField reconWaveLength; // reconstruction wavelength from angle calculator
	JTextField reconHalf; // reconstruction half angle output from angle calc
	JTextField DMSReconHalf; // recon half angle output in deg min sec
	// add this
	JTextField waveLength2; // wavelength input from spatial freq. calculator
	JTextField spatFreq2; // spatial frequency output from spat. freq. calc.
	JTextField halfAngle2; // half angle input from spatial freq. calculator
	JTextField DMSHalf2; // half angle deg min sec output from spat. freq. calc.
	JTextField sizeAngle; // half angle input from size calculator
	JTextField minSize; // size output from size calculator
	JTextField beamSize; // beam size input from size calculator
	JPanel anglePanel; // angle calculator pane
	JPanel freqPanel; // spatial frequency calculator pane 
	JPanel sizePanel; // geometry calculator pane
	JPanel imagePanel; // the panel to display graphics
	JTabbedPane tabbedPane; // my tabbed pane
		
	public AngleCalculator () {
		addWindowListener(new WindowAdapter() {
			public void windowClosing(WindowEvent e) {
				System.exit(0);
			}
		});
		
		Container contentPane = getContentPane();
		
		// Creating a menu bar
        JMenuBar menuBar = new JMenuBar();
        setJMenuBar(menuBar);
        JMenuItem menuItem;
        JSeparator separator;
        
        // setting up File menu
        JMenu fileMenu = new JMenu("File");
        
        menuItem = new JMenuItem("Print Tab");
        fileMenu.add(menuItem);
        menuItem.setActionCommand("print");
		menuItem.addActionListener(this);
		separator = new JSeparator();
        fileMenu.add(separator);
        
        menuItem = new JMenuItem("Exit");
        fileMenu.add(menuItem);
        menuItem.setActionCommand("exit");
		menuItem.addActionListener(this);
		
		// setting up Help menu
        JMenu helpMenu = new JMenu("Help");
        menuItem = new JMenuItem("Angle Calculator Help");
        helpMenu.add(menuItem);
        menuItem.setActionCommand("help");
		menuItem.addActionListener(this);
        separator = new JSeparator();
        helpMenu.add(separator);
        
        menuItem = new JMenuItem("About Angle Calculator");
        helpMenu.add(menuItem);
        menuItem.setActionCommand("about");
		menuItem.addActionListener(this);
		
		// adding menues to the main menu bar
        menuBar.add(fileMenu);
        menuBar.add(helpMenu);
        
        // creating a tabbed pane
        tabbedPane = new JTabbedPane();
        
        // creating angle calculator tab
        anglePanel = AnglePanel();
        anglePanel.setAlignmentX(CENTER_ALIGNMENT);
        anglePanel.setAlignmentY(CENTER_ALIGNMENT);
        anglePanel.setLayout(new BoxLayout(anglePanel, BoxLayout.Y_AXIS));
        
        // creating spatial frequency tab
        freqPanel = SpatFreqPanel();
        freqPanel.setAlignmentX(CENTER_ALIGNMENT);
        freqPanel.setAlignmentY(CENTER_ALIGNMENT);
        freqPanel.setLayout(new BoxLayout(freqPanel, BoxLayout.Y_AXIS));
        
        // creating grating geometry calculator tab
        sizePanel = MinSizePanel();
        sizePanel.setAlignmentX(CENTER_ALIGNMENT);
        sizePanel.setAlignmentY(CENTER_ALIGNMENT);
        sizePanel.setLayout(new BoxLayout(sizePanel, BoxLayout.Y_AXIS));
        
        // creating a graphics panel
        imagePanel = ImagePane();
        imagePanel.setAlignmentX(CENTER_ALIGNMENT);
        imagePanel.setAlignmentY(CENTER_ALIGNMENT);
        imagePanel.setLayout(new BoxLayout(imagePanel, BoxLayout.Y_AXIS));
        
        
        // add all tabs to the tabbe pane
        tabbedPane.addTab("Angle", null, anglePanel, "Calculate angles for symetric gratings");
        tabbedPane.addTab("Spat Freq", null, freqPanel, "Calculate spacial frequency");
        tabbedPane.addTab("Size Calc", null, sizePanel, "Calcualte min working area");
        tabbedPane.addTab("Graphics", null, imagePanel, "Displays image from tab");

        //Add the tabbed pane to this panel.
        contentPane.add(tabbedPane);
        
	}
	
	/**
	 * This functions creates and returns a pane for the angle calculator tab
	 */
	public JPanel AnglePanel() {
    	JPanel pane = new JPanel();
    	JPanel anglePane = new JPanel();
    	JPanel inputPane = new JPanel();
    	
    	Dimension size = new Dimension(90,20);
    	Dimension angleSize = new Dimension(110,20);
    	
    	JLabel waveLengthLabel = new JLabel("Wavelength (nm)");
    	waveLength = new JTextField(15);
    	waveLength.setAlignmentX(LEFT_ALIGNMENT);
    	waveLength.setMaximumSize(size);
    	waveLength.setText("488");
    	JLabel reconWaveLengthLabel = new JLabel("Playback (nm)");
    	reconWaveLength = new JTextField(15);
    	reconWaveLength.setAlignmentX(LEFT_ALIGNMENT);
    	reconWaveLength.setMaximumSize(size);
    	reconWaveLength.setText("633");
    	JLabel spatFreqLabel = new JLabel("Spat Freq (l/mm)");
    	spatFreq = new JTextField(15);
    	spatFreq.setAlignmentX(LEFT_ALIGNMENT);
    	spatFreq.setMaximumSize(size);
    	spatFreq.setText("1000");
    	
    	JButton calcButton = new JButton("Calculate");
    	calcButton.setActionCommand("calcAngle");
		calcButton.addActionListener(this);
		JButton resetButton = new JButton("Reset");
    	resetButton.setActionCommand("resetAngle");
		resetButton.addActionListener(this);
		
		JLabel halfAngleLabel = new JLabel("Half Angle (deg)");
    	halfAngle = new JTextField(15);
    	halfAngle.setAlignmentX(LEFT_ALIGNMENT);
    	halfAngle.setMaximumSize(angleSize);
    	
    	JLabel DMSLabel = new JLabel("DMS");
    	DMSHalf = new JTextField(15);
    	DMSHalf.setAlignmentX(LEFT_ALIGNMENT);
    	DMSHalf.setMaximumSize(angleSize);
    	
    	JLabel fullLabel = new JLabel("Full Angle (deg)");
    	fullAngle = new JTextField(15);
    	fullAngle.setAlignmentX(LEFT_ALIGNMENT);
    	fullAngle.setMaximumSize(angleSize);
    	
    	JLabel DMSLabelFull = new JLabel("DMS");
    	DMSFull = new JTextField(15);
    	DMSFull.setAlignmentX(LEFT_ALIGNMENT);
    	DMSFull.setMaximumSize(angleSize);
    	
    	JLabel reconHalfAngleLabel = new JLabel("Playback Angle");
    	reconHalf = new JTextField(15);
    	reconHalf.setAlignmentX(LEFT_ALIGNMENT);
    	reconHalf.setMaximumSize(angleSize);
		
		inputPane.setLayout(new BoxLayout(inputPane, BoxLayout.Y_AXIS));
		inputPane.setBorder(BorderFactory.createEmptyBorder(10,10,10,10));
		anglePane.setLayout(new BoxLayout(anglePane, BoxLayout.Y_AXIS));
		anglePane.setBorder(BorderFactory.createEmptyBorder(10,10,10,10));
		inputPane.add(waveLengthLabel);
		inputPane.add(waveLength);
		inputPane.add(Box.createRigidArea(new Dimension(0,5)));
		inputPane.add(reconWaveLengthLabel);
		inputPane.add(reconWaveLength);
		inputPane.add(Box.createRigidArea(new Dimension(0,5)));
		inputPane.add(spatFreqLabel);
		inputPane.add(spatFreq);
		inputPane.add(Box.createRigidArea(new Dimension(0,10)));
		inputPane.add(calcButton);
		inputPane.add(Box.createRigidArea(new Dimension(0,5)));
		inputPane.add(resetButton);
		anglePane.add(halfAngleLabel);
		anglePane.add(halfAngle);
		anglePane.add(DMSLabel);
		anglePane.add(DMSHalf);
		anglePane.add(fullLabel);
		anglePane.add(fullAngle);
		anglePane.add(DMSLabelFull);
		anglePane.add(DMSFull);
		anglePane.add(Box.createRigidArea(new Dimension(0,5)));
		anglePane.add(reconHalfAngleLabel);
		anglePane.add(reconHalf);
    	
    	JSplitPane splitPane = new JSplitPane(JSplitPane.HORIZONTAL_SPLIT, true,
							   inputPane, anglePane);
					
		splitPane.setOneTouchExpandable(false);
		splitPane.setDividerSize(5);
		pane.add(splitPane);
    	return pane;
    }
    
    /**
     * This function creates and returns a pane for the spatial frequency
     * calculator tab
     */
    public JPanel SpatFreqPanel () {
    	JPanel pane = new JPanel();
    	JPanel freqPane = new JPanel();
    	JPanel inputPane = new JPanel();
    	
    	Dimension size = new Dimension(90,20);
    	Dimension freqSize = new Dimension(110,20);
    	
    	JLabel halfAngleLabel = new JLabel("Half Angle (deg)");
    	halfAngle2 = new JTextField(15);
    	halfAngle2.setAlignmentX(LEFT_ALIGNMENT);
    	halfAngle2.setMaximumSize(size);
    	halfAngle2.setText("45");
       	JLabel waveLengthLabel = new JLabel("Wavelength (nm)");
    	waveLength2 = new JTextField(15);
    	waveLength2.setAlignmentX(LEFT_ALIGNMENT);
    	waveLength2.setMaximumSize(size);
    	waveLength2.setText("632.8");
    	JButton calcButton = new JButton("Calculate");
    	calcButton.setActionCommand("calcFreq");
		calcButton.addActionListener(this);
		JButton resetButton = new JButton("Reset");
    	resetButton.setActionCommand("resetFreq");
		resetButton.addActionListener(this);
    	
    	JLabel spatFreqLabel = new JLabel("Spat Freq (l/mm)");
    	spatFreq2 = new JTextField(15);
    	spatFreq2.setAlignmentX(LEFT_ALIGNMENT);
    	spatFreq2.setMaximumSize(freqSize);
    	JLabel DMSHalf2Label = new JLabel("Half Angle DMS");
    	DMSHalf2 = new JTextField(15);
    	DMSHalf2.setAlignmentX(LEFT_ALIGNMENT);
    	DMSHalf2.setMaximumSize(freqSize);
    	
    	inputPane.setLayout(new BoxLayout(inputPane, BoxLayout.Y_AXIS));
		inputPane.setBorder(BorderFactory.createEmptyBorder(10,10,10,10));
		freqPane.setLayout(new BoxLayout(freqPane, BoxLayout.Y_AXIS));
		freqPane.setBorder(BorderFactory.createEmptyBorder(10,10,10,10));
		
		inputPane.add(halfAngleLabel);
		inputPane.add(halfAngle2);
		inputPane.add(Box.createRigidArea(new Dimension(0,5)));
		inputPane.add(waveLengthLabel);
		inputPane.add(waveLength2);
		inputPane.add(Box.createRigidArea(new Dimension(0,10)));
		inputPane.add(calcButton);
		inputPane.add(Box.createRigidArea(new Dimension(0,5)));
		inputPane.add(resetButton);
		freqPane.add(spatFreqLabel);
		freqPane.add(spatFreq2);
		freqPane.add(Box.createRigidArea(new Dimension(0,10)));
		freqPane.add(DMSHalf2Label);
		freqPane.add(DMSHalf2);
		
		JSplitPane splitPane = new JSplitPane(JSplitPane.HORIZONTAL_SPLIT, true,
							   inputPane, freqPane);
					
		splitPane.setOneTouchExpandable(false);
		splitPane.setDividerSize(5);
		pane.add(splitPane);
    	
    	return pane;
    }
    
    /**
     * This function creates and returns a pane for the minimum working area
     * calculator tab
     */
    public JPanel MinSizePanel() {
    	JPanel pane = new JPanel();
    	JPanel inputPane = new JPanel();
    	JPanel outputPane = new JPanel();
    	
    	Dimension max = new Dimension(110,20);
    	Dimension min = new Dimension(82,20);
    	
    	JLabel sizeAngleLabel = new JLabel("Half Angle (deg)");
    	sizeAngle = new JTextField(15);
    	sizeAngle.setAlignmentX(LEFT_ALIGNMENT);
    	sizeAngle.setMaximumSize(max);
    	sizeAngle.setMinimumSize(min);
    	sizeAngle.setText("40");
    	JLabel minSizeLabel = new JLabel("Min Length (mm)");
    	minSize = new JTextField(15);
    	minSize.setAlignmentX(LEFT_ALIGNMENT);
    	minSize.setMaximumSize(max);
    	minSize.setText(" ");
    	JLabel beamSizeLabel = new JLabel("Beam Size (mm)");
    	beamSize = new JTextField(15);
		beamSize.setAlignmentX(LEFT_ALIGNMENT);
    	beamSize.setMaximumSize(max);
    	beamSize.setMinimumSize(min);
    	beamSize.setText("190");
    	
    	JButton calcButton = new JButton("Calculate");
    	calcButton.setActionCommand("calcSize");
		calcButton.addActionListener(this);
		JButton resetButton = new JButton("Reset");
    	resetButton.setActionCommand("resetSize");
		resetButton.addActionListener(this);
    	
    	inputPane.setLayout(new BoxLayout(inputPane, BoxLayout.Y_AXIS));
		inputPane.setBorder(BorderFactory.createEmptyBorder(10,10,10,10));
		outputPane.setLayout(new BoxLayout(outputPane, BoxLayout.Y_AXIS));
		outputPane.setBorder(BorderFactory.createEmptyBorder(10,10,10,10));
		
		inputPane.add(sizeAngleLabel);
		inputPane.add(sizeAngle);
		inputPane.add(Box.createRigidArea(new Dimension(0,5)));
		inputPane.add(beamSizeLabel);
		inputPane.add(beamSize);
		inputPane.add(Box.createRigidArea(new Dimension(0,10)));
		inputPane.add(calcButton);
		inputPane.add(Box.createRigidArea(new Dimension(0,5)));
		inputPane.add(resetButton);
		outputPane.add(minSizeLabel);
		outputPane.add(minSize);
		
		JSplitPane splitPane = new JSplitPane(JSplitPane.HORIZONTAL_SPLIT, true,
							   inputPane, outputPane);
					
		splitPane.setOneTouchExpandable(false);
		splitPane.setDividerSize(5);
		pane.add(splitPane);
    	
    	return pane;
    }
    
    public JPanel ImagePane(){
    	JPanel pane = new JPanel();
    	
    	JLabel temp = new JLabel("Coming soon!");
    	temp.setAlignmentX(CENTER_ALIGNMENT);
    	
    	pane.setLayout(new BoxLayout(pane, BoxLayout.Y_AXIS));
    	pane.add(Box.createRigidArea(new Dimension(0,60)));
    	pane.add(temp);
    	return pane;
    }
	
	/**
	 * This function is the action listener.  If a button is pressed or a menu
	 * item is selected, this function is where execution of actions start and
	 * end.
	 */
	public void actionPerformed(ActionEvent e) {
		
		// creates a print job to be sent to the printer
        if ("print".equals(e.getActionCommand())) {
        	Book book = new Book();
        	book.append(new PrintCalculations(), new PageFormat());
        	PrinterJob printerJob = PrinterJob.getPrinterJob();
        	printerJob.setPageable(book);
        	
        	boolean doPrint = printerJob.printDialog();
        	
			if (doPrint) { // The user confirmed that printing should proceed.
				try {
					printerJob.print();
				} catch (PrinterException exception) {
					System.err.println("Printing error: " + exception);
				}
			}
        }
		
		// calculates angles and converts everything into DMS format
		if ("calcAngle".equals(e.getActionCommand())) {
			double wave = Double.parseDouble(waveLength.getText());
			double reconWave = Double.parseDouble(reconWaveLength.getText());
			double freq = Double.parseDouble(spatFreq.getText());
			double angle;
			double reconAngle;
			String DMS;
			String FullDMS;
			
			angle = findHalfAngle(freq, wave);
			Double Angle = new Double(angle);
			
			reconAngle = findHalfAngle(freq, reconWave);
			Double ReconAngle = new Double(reconAngle);
			
			Double degs = new Double(Math.floor(angle));
			Integer intDegs = new Integer(degs.intValue());
			
			Double mins = new Double((angle % 1)*60);
			Integer intMins = new Integer(mins.intValue());
			
			Double secs = new Double((mins.doubleValue() % 1)*60);
			Integer intSecs = new Integer(secs.intValue());
			
			DMS = intDegs.toString() + " deg,  "
				 + intMins.toString() + "\',  "
			     + intSecs.toString() + "\"";
			DMSHalf.setText(DMS);
			
			Float floatAngle = new Float(Angle.floatValue());
			halfAngle.setText(floatAngle.toString());
			
			Float floatReconAngle = new Float(ReconAngle.floatValue());
			reconHalf.setText(floatReconAngle.toString());
			
			Float full = new Float(Angle.floatValue()*2);
			fullAngle.setText(full.toString());
			
			angle = angle*2;
			
			degs = new Double(Math.floor(angle));
			intDegs = new Integer(degs.intValue());
			
			mins = new Double((angle % 1)*60);
			intMins = new Integer(mins.intValue());
			
			secs = new Double((mins.doubleValue() % 1)*60);
			intSecs = new Integer(secs.intValue());
			
			FullDMS = intDegs.toString() + " deg,  "
				 + intMins.toString() + "\',  "
			     + intSecs.toString() + "\"";
			DMSFull.setText(FullDMS);
		}
		
		// calculates spatial frequency based on a measured angle
		if ("calcFreq".equals(e.getActionCommand())) {
			double wave = Double.parseDouble(waveLength2.getText());
			double angle = Double.parseDouble(halfAngle2.getText());
			
			Double SF = new Double(findSpatialFrequency(wave, angle));
			Float floatSF = new Float(SF.floatValue()*1000);
			
			spatFreq2.setText(floatSF.toString());
			
			Double degs = new Double(Math.floor(angle));
			Integer intDegs = new Integer(degs.intValue());
			
			Double mins = new Double((angle % 1)*60);
			Integer intMins = new Integer(mins.intValue());
			
			Double secs = new Double((mins.doubleValue() % 1)*60);
			Integer intSecs = new Integer(secs.intValue());
			
			String DMS = intDegs.toString() + " deg,  "
						+ intMins.toString() + "\',  "
						+ intSecs.toString() + "\"";
			DMSHalf2.setText(DMS);
		}
		
		// calculates the minimum required size of the grating working area
		// based on the half angle and beam size
		if ("calcSize".equals(e.getActionCommand())) {
			double bs = Double.parseDouble(beamSize.getText());
			double angle = Double.parseDouble(sizeAngle.getText());
			
			double ms = bs / (double)Math.cos(Math.toRadians(angle));
			
			Float MS = new Float(ms);
			
			minSize.setText(MS.toString());
		}
		
		// resets the angle calculator to defaults
		if ("resetAngle".equals(e.getActionCommand())) {
			waveLength.setText("488");
			spatFreq.setText("1000");
			halfAngle.setText(" ");
			DMSHalf.setText(" ");
			DMSFull.setText(" ");
			fullAngle.setText(" ");
			reconHalf.setText(" ");
		}
			
		// resets the frequency calculator to defaults
		if ("resetFreq".equals(e.getActionCommand())) {
			waveLength2.setText("632.8");
			spatFreq2.setText(" ");
			halfAngle2.setText("45");
			DMSHalf2.setText(" ");
		}
		
		// resets the geometry calculator the defaults
		if ("resetSize".equals(e.getActionCommand())) {
			sizeAngle.setText("40");
			minSize.setText(" ");
			beamSize.setText("190");
		}
		
		// display a message window about the application
		if ("about".equals(e.getActionCommand())) {
			String message = "Symetric Grating Calculator\n"
						   + "-----------------------------------"
					     + "\n\nCreated by: Robert W. Rallison"
						 + "\n\nLast Modified: 06/11/03"
						 + "\nVersion 0.9.9";
			JOptionPane.showMessageDialog(null, message,
				"About Calculator", JOptionPane.INFORMATION_MESSAGE);
		}
		
		// not finished with this one yet
		if ("help".equals(e.getActionCommand())) {
			String message = "Coming soon :)";
			JOptionPane.showMessageDialog(null, message,
				"Calculator Help", JOptionPane.INFORMATION_MESSAGE);
		}
		
		// exits the program
		if ("exit".equals(e.getActionCommand())) {
			System.exit(0);
		}
	}
	
	/**
	 * Given the spatial frequency and the wavelength, this function returns
	 * the half angle.
	 */
	public double findHalfAngle(double freq, double wave) {
		double halfAngle;
		
		wave = (wave/1000);
		freq = (freq/1000);
		
		halfAngle = Math.toDegrees((double)Math.asin((freq*wave)/2));
		
		return halfAngle;
	}
	
	/**
	 * Given a wavelength and an angle, this function calculates the
	 * spatial frequency.
	 */
	public double findSpatialFrequency (double wave, double angle) {
		double spatialFrequency;
		
		wave = (wave/1000);
		spatialFrequency = Math.sin(Math.toRadians(angle))*2;
		spatialFrequency = spatialFrequency/wave;
		
		return spatialFrequency;
	}
	
	/**
	 * This function creates and returns a Printable graphic depending on the
	 * active tab.
	 */
	private class PrintCalculations implements Printable {
		
		public int print (Graphics g, PageFormat pageFormat, int page) {
			int POINTS_PER_INCH = 72;
			
			// creating a graphic
			Graphics2D g2d = (Graphics2D) g;
			g2d.translate (pageFormat.getImageableX (), pageFormat.getImageableY ());
			g2d.setPaint (Color.black);
			
			// drawing a border around the page
			//g2d.setStroke (new BasicStroke (12));
			Rectangle2D.Double border = new Rectangle2D.Double (0, 0,
				pageFormat.getImageableWidth (), pageFormat.getImageableHeight ());
			//g2d.draw (border);
			
			// setting up the font and size
			Font titleFont = new Font ("helvetica", Font.BOLD, 36);
			//g2d.setFont (titleFont);
			
			// Compute the horizontal center of the page
			FontMetrics fontMetrics = g2d.getFontMetrics ();
			double titleX = (pageFormat.getImageableWidth () / 2) - (fontMetrics.stringWidth ("Place String Here") / 2);
			double titleY = 3 * POINTS_PER_INCH;
			//g2d.drawString (titleText, (int) titleX, (int) titleY);
			
			if (tabbedPane.getSelectedIndex() == 0) {
				String Wavelength = "Wavelength: " + waveLength.getText() + "nm";
				String ReconWavelength = "Playback Wavelength: " + reconWaveLength.getText() + "nm";
				String SpatialFrequency = "Spatial Frequency: " + spatFreq.getText() + " l/mm";
				String HalfAngle = "Half Angle: " + halfAngle.getText() + " deg";
				String DMSHalfAngle = "DMS: " + DMSHalf.getText();
				String FullAngle = "Full Angle: " + fullAngle.getText() + " deg";
				String DMSFullAngle = "DMS: " + DMSFull.getText();
				String ReconAngle = "Playback Angle: " + reconHalf.getText() + " deg";
				
				// drawing the text to the graphic
				g2d.drawString ("Angle Calculator Output", 72, 72);
				g2d.drawString ("-------------------------------------", 72, 82);
				g2d.drawString (Wavelength, 72, 112);
				g2d.drawString (SpatialFrequency, 72, 132);
				g2d.drawString (HalfAngle, 72, 162);
				g2d.drawString (DMSHalfAngle, 72, 177);
				g2d.drawString (FullAngle, 72, 207);
				g2d.drawString (DMSFullAngle, 72, 222);
				g2d.drawString (ReconWavelength, 72, 252);
				g2d.drawString (ReconAngle, 72, 272);
			}
			
			else if (tabbedPane.getSelectedIndex() == 1) {
				String Wavelength = "Wavelength: " + waveLength2.getText() + "nm";
				String SpatialFrequency = "Spatial Frequency: " + spatFreq2.getText() + " l/mm";
				String HalfAngle = "Half Angle: " + halfAngle2.getText() + " deg";
				String DMSHalfAngle = "DMS: " + DMSHalf2.getText();
				
				// drawing the text to the graphic
				g2d.drawString ("Spatial Frequency Output", 72, 72);
				g2d.drawString ("-------------------------------------", 72, 82);
				g2d.drawString (Wavelength, 72, 112);
				g2d.drawString (SpatialFrequency, 72, 132);
				g2d.drawString (HalfAngle, 72, 162);
				g2d.drawString (DMSHalfAngle, 72, 177);
			}
			
			else {
				String HalfAngle = "Half Angle: " + sizeAngle.getText() + " deg";
				String BeamSize = "Beam Size: " + beamSize.getText() + " mm";
				String MinSize = "Min Working Length: " + minSize.getText() + " mm";
				
				// drawing the text to the graphic
				g2d.drawString ("Size Calculator Output", 72, 72);
				g2d.drawString ("-------------------------------------", 72, 82);
				g2d.drawString (HalfAngle, 72, 112);
				g2d.drawString (BeamSize, 72, 142);
				g2d.drawString (MinSize, 72, 172);
			}
			
			// validating that the page does exist
			return (PAGE_EXISTS);
		}
	}
}