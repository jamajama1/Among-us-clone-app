package Code;

import java.awt.Dimension;

import javax.swing.ImageIcon;
import javax.swing.JLabel;

//Player class to create player objects
public class Character {
	
	protected String colors; //player color
	protected int number = 0; //player number, starts from 0
	private JLabel label;
	
	public Character(String color) {
		number++;
		colors = color;
		label=new JLabel();
		setJLabel(color);
	}
	
	
    //Getters returns color, player number, and jlabel
	public String getColor() {
		return colors;
	}

	public int getPlayerNumber() { 
		return number;
	}

	public JLabel getJLabel()
	{
		return label;
	}
	
	//Setters
	public void setJLabel(String color)
	{
		/*
		java.net.URL imgURL = this.getClass().getResource(fileName);
	    if (imgURL == null) {
	      throw new IllegalArgumentException("Couldn't find file: "+fileName );
	    }
	    */
		String filePath = "/Users/husseinatwa/eclipse-workspace/AmongUs_CSE442/src/characters/"+color+".png";
	    ImageIcon cardImage = new ImageIcon(filePath);    
	    label.setIcon(cardImage);
	    Dimension d = new Dimension(cardImage.getIconWidth() , cardImage.getIconHeight() );
	    label.setSize(d);
	    label.setPreferredSize(d);
	    label.setMaximumSize(d);
	    label.setMinimumSize(d);
	}
}
