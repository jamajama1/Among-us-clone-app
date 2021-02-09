package GUI;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.awt.geom.*;


public class gameFrame extends JFrame{

	JFrame frame;
	JLabel label;
	Action upA;
	Action downA;
	Action leftA;
	Action rightA;
	gameFrame() {
		//code for creating frame
		frame = new JFrame("Game");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setSize(1000,1000);
		frame.setLayout(null);
		label = new JLabel();
		label.setBackground(Color.blue);
		label.setBounds(50,50,50,50);
		label.setOpaque(true);

		//actions for up,down,left,right
		upA = new Up();
		downA = new Down();
		leftA = new Left();
		rightA = new Right();

		//making keybinds for each w,a,s,d. To movearound successfully now
		label.getInputMap().put(KeyStroke.getKeyStroke('w'), "Move up");
		label.getActionMap().put("Move up", upA);
		label.getInputMap().put(KeyStroke.getKeyStroke('a'), "Move left");
		label.getActionMap().put("Move left", leftA);
		label.getInputMap().put(KeyStroke.getKeyStroke('s'), "Move down");
		label.getActionMap().put("Move down", downA);
		label.getInputMap().put(KeyStroke.getKeyStroke('d'), "Move right");
		label.getActionMap().put("Move right", rightA);

		frame.add(label);
		frame.setVisible(true);
	}

	public class Up extends AbstractAction {
		public void actionPerformed(ActionEvent e) {
			label.setLocation(label.getX(),label.getY()-30);
		}
	}
	public class Down extends AbstractAction {
		public void actionPerformed(ActionEvent e) {
			label.setLocation(label.getX(),label.getY()+30);
		}
	}
	public class Left extends AbstractAction {
		public void actionPerformed(ActionEvent e) {
			label.setLocation(label.getX()-30,label.getY());
		}
	}
	public class Right extends AbstractAction {
		public void actionPerformed(ActionEvent e) {
			label.setLocation(label.getX()+30,label.getY());
		}
	}
}
