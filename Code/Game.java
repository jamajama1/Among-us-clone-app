package Code;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Container;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.border.Border;


public class Game extends JFrame{

	JFrame frame;
	JLabel charLabel;
	Action upA;
	Action downA;
	Action leftA;
	Action rightA;
	String[] arr = {"blue", "brown", "cyan", "green", "orange", "pink", "purple", "red", "white", "black"};
	int index = 0;
	static int max = 10;
	String background = "/Users/dylanschillaci/git/course-project-a5-ezpz/course-project-a5-ezpz/Code/stars.jpg";//change this string to whatever the file path is on ur pc
	JLabel playerAmount;
	
	JLabel list;
	String playerList;
	
	Game() { 
		//code for creating frame
		frame = new JFrame("Game");
		frame.setContentPane(new JLabel(new ImageIcon(background)));
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setSize(850,638);
		frame.setLayout(new BorderLayout());
		
		/*
		//Creating map design
		JLabel label = new JLabel();
		label.setBackground(Color.WHITE);
		label.setBounds(50,50,150,50);
		label.setOpaque(true);
		// create a line border with the specified color and width
        Border border= BorderFactory.createRaisedBevelBorder();
        label.setBorder(border);
   
		frame.add(label);
		label.setLocation(400, 300);
    */		
		//Creating JPanel with start button
		JPanel panel = new JPanel();
		panel.setBackground(Color.BLACK);
		JButton start = new JButton("Start");
	    panel.add(start);
		
		//creating player instance for first player 
		Character p1 = new Character(arr[index]);
		index++;
		charLabel = p1.getJLabel();
		
		//creating JLabel to be added to panel that keeps track of number of players
		playerAmount = new JLabel("("+ Integer.toString(index) + "/" + Integer.toString(max) + ")" );
		playerAmount.setForeground(Color.RED);//setting color of label text to Red
		playerAmount.setFont(new Font("Comic Sans MS", Font.PLAIN, 12));//setting font type and size for label
		panel.add(playerAmount);
		
		//creating list of players as Jlabel
		int x = index - 1;
	    playerList = "PLAYERS {"  + arr[x] + " }"; //creating string for player list
		list = new JLabel(playerList);
		list.setForeground(Color.GREEN);//setting color of label text to Red
		list.setFont(new Font("Comic Sans MS", Font.PLAIN, 12));//setting font type and size for label
		panel.add(list);
				
		
		//Adding panel with Start button and player amount to the bottom of frame.
		frame.add(panel, BorderLayout.SOUTH);
		
		
		
		//actions for up,down,left,right
		upA = new Up();
		downA = new Down();
		leftA = new Left();
		rightA = new Right();
		
		//making keybinds for each w,a,s,d. To movearound successfully now
		charLabel.getInputMap().put(KeyStroke.getKeyStroke('w'), "Move up");
		charLabel.getActionMap().put("Move up", upA);
		charLabel.getInputMap().put(KeyStroke.getKeyStroke('a'), "Move left");
		charLabel.getActionMap().put("Move left", leftA);
		charLabel.getInputMap().put(KeyStroke.getKeyStroke('s'), "Move down");
		charLabel.getActionMap().put("Move down", downA);
		charLabel.getInputMap().put(KeyStroke.getKeyStroke('d'), "Move right");
		charLabel.getActionMap().put("Move right", rightA);
		
		frame.add(charLabel);
		frame.setVisible(true);
	}
	
	public class Up extends AbstractAction {
		public void actionPerformed(ActionEvent e) {
			if(charLabel.getY() >= -250) {
			charLabel.setLocation(charLabel.getX(),charLabel.getY()-30);
			}
		}
	}
	public class Down extends AbstractAction {
		public void actionPerformed(ActionEvent e) {
			if(charLabel.getY() <= 250) {
			charLabel.setLocation(charLabel.getX(),charLabel.getY()+30);
			}
		}
	}
	public class Left extends AbstractAction {
		public void actionPerformed(ActionEvent e) {
			if(charLabel.getX() >= 10) {
			charLabel.setLocation(charLabel.getX()-30,charLabel.getY());
			}
		}
	}
	public class Right extends AbstractAction {
		public void actionPerformed(ActionEvent e) {
			if(charLabel.getX() <= 800) {
			charLabel.setLocation(charLabel.getX()+30,charLabel.getY());
			}
		}
	}
}