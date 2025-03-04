package GUI;

import Game.Game;
import Game.Player;
import Game.PlayerList;

import javax.swing.*;
import javax.swing.border.EmptyBorder;
import java.awt.*;
import java.awt.event.ActionEvent;


public class Main
{
	/*
	private JFrame frame;
	private JFrame gameFr;
	private JPanel mainPanel;
	private JPanel mainPanel2;
	private JButton b1;
	private JButton b2;
	private JLabel gameLabel;
	gameFrame f = new gameFrame();
	*/

	private JFrame frame;
//private static JFrame gameFr;
private JPanel mainPanel;
private JPanel mainPanel2;
private static JButton b1;
private JButton b2;
private JLabel gameLabel;



	public Main() {
		gui();
	}

	public void gui() {

		//Creating frame
		JFrame.setDefaultLookAndFeelDecorated(true);
		frame = new JFrame("Version 1.0");
		//gameFr = new JFrame("Version 1.0");
		frame.setVisible(true);
		//frame.setSize(600, 400);//setting size of frame 600 width and 400 height.
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);//Allows frame to exit, without it frame will not close

		//Creating Panel
		mainPanel = new JPanel();
		mainPanel.setBackground(Color.BLACK);//setting background of JPanel to be black
		BoxLayout boxlayout = new BoxLayout(mainPanel, BoxLayout.Y_AXIS);//Setting Boxlayout for Jpanel
		mainPanel.setLayout(boxlayout);//BoxLayout.Y_AXIS adds panel components from top to bottom
		mainPanel.setBorder(new EmptyBorder(new Insets(150, 200, 150, 200)));//Set border for the panel

		//Creating Label that will contain Game title and adding it to our JPanel
		gameLabel = new JLabel("AMONG US");
		gameLabel.setForeground(Color.RED);//setting color of label text to Red
		gameLabel.setFont(new Font("Phosphate", Font.BOLD, 42));//setting font type and size for label
		mainPanel.add(gameLabel);
		mainPanel.add(Box.createRigidArea(new Dimension(0, 40)));//(width,height); used to insert spacing between the 2 components of 40pixels

		//Creating Button components to be placed on JPanel
		b1 = new JButton("Online");
		b2 = new JButton("How To Play");
		mainPanel.add(b1);
		mainPanel.add(b2);



		//Creating Panel for game window
		//gameFr.add(f);
		//gameFr.setSize(800,600);
		//mainPanel2 = new JPanel();
		//mainPanel2.setBackground(Color.WHITE);//setting background of JPanel to be black
		//BoxLayout boxlayout2 = new BoxLayout(mainPanel2, BoxLayout.Y_AXIS);//Setting Boxlayout for Jpanel
		//mainPanel2.setLayout(boxlayout2);//BoxLayout.Y_AXIS adds panel components from top to bottom
		//Set border for the panel
		//mainPanel2.setBorder(new EmptyBorder(new Insets(150, 200, 150, 200)));
		//mainPanel.setBorder(new EmptyBorder(new Insets(50, 80, 50, 80)));
		//gameFr.add(mainPanel2);
		//gameFr.pack();


		//Implementing action listener for "Online" button

		//Implementing action listener for "How To Play" button
		b2.addActionListener(new java.awt.event.ActionListener(){
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				//pop up how to play frame
				JFrame howToPlay = new JFrame("How To Play");
				howToPlay.setVisible(true);
				howToPlay.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

				//creating jpanel
				JPanel howP = new JPanel();
				howP.setBackground(Color.BLACK);//setting background of JPanel to be black
				BoxLayout boxlayout = new BoxLayout(howP, BoxLayout.Y_AXIS);//Setting Boxlayout for Jpanel
				howP.setLayout(boxlayout);//BoxLayout.Y_AXIS adds panel components from top to bottom

				//Creating Labels containing rules and adding them to our JPanel
				/*Label*/
				JLabel label = new JLabel("RULES");
				label.setForeground(Color.RED);
				label.setFont(new Font("Comic Sans MS", Font.BOLD, 24));
				howP.add(label);//add to panel
				howP.add(Box.createRigidArea(new Dimension(0, 20)));
				/*rule1*/
				JLabel rule1 = new JLabel("1. This is a game of collbaration and deception. Players are either given the role of a crew member or imposter.");
				rule1.setForeground(Color.WHITE);
				howP.add(rule1);//add to panel
				/*rule2*/
				JLabel rule2 = new JLabel("2. The job of a crew member is to complete tasks given to them, while also trying to locate the imposter among them.");
				rule2.setForeground(Color.WHITE);
				howP.add(rule2);//add to panel
				/*rule3*/
				JLabel rule3 = new JLabel("3. Crew members can initiate the voting off sequence by reporting dead bodies or calling emergency meeting if they believe they found the imposter.");
				rule3.setForeground(Color.WHITE);
				howP.add(rule3);//add to panel
				/*rule4*/
				JLabel rule4 = new JLabel("4. The imposter's job is to sabotage and kill off the crewmates while avoiding getting spotted.");
				rule4.setForeground(Color.WHITE);
				howP.add(rule4);//add to panel
				/*rule5*/
				JLabel rule5 = new JLabel("5. As imposter, you must manipulate the crew members. Make them fight among themselves and elminate eachother.");
				rule5.setForeground(Color.WHITE);
				howP.add(rule5);//add to panel
				/*rule6*/
				JLabel rule6 = new JLabel("6. To move around use the W,A,S,D keys.");
				rule6.setForeground(Color.WHITE);
				howP.add(rule6);//add to panel
				/*rule7*/
				JLabel rule7 = new JLabel("7. The N key will be used as the action button. For imposters, it will allow them to kill crew members. For crew members, it will allow them to complete tasks.");
				rule7.setForeground(Color.WHITE);
				howP.add(rule7);//add to panel
				/*rule8*/
				JLabel rule8 = new JLabel("8. The M key will be used as the report button. Crew mates can use this button to report a dead body spotted or the imposter can self report a dead body to initiate voting");
				rule8.setForeground(Color.WHITE);
				howP.add(rule8);//add to panel
				/*rule9*/
				JLabel rule9 = new JLabel("9. If a player is killed by the imposter, they will not be allowed to speak until the game ends. Only players still alive can discuss on who the imposter may be.");
				rule9.setForeground(Color.WHITE);
				howP.add(rule9);//add to panel
				/*rule10*/
				JLabel rule10 = new JLabel("10. After discussions are over, players get chance to vote who they believe is the imposter or skip vote. Whoever gets majority votes will be removed off the ship, so vote intelligently!");
				rule10.setForeground(Color.WHITE);
				howP.add(rule10);//add to panel
				howP.add(Box.createRigidArea(new Dimension(0, 40)));//(width,height); used to insert spacing between the 2 components of 40pixels

				//Adding panel with components to frame
				howToPlay.add(howP);
				howToPlay.pack();
			}

		});


		//Adding panel with components to frame
		frame.add(mainPanel);
		frame.pack();//automatically sizes frame with all its contents to be at an appropriate size if frame.setSize is not used

	}

	//adds new player with the players username and adds the player to the player_list
	public static void new_player(String username){
		Player player = new Player();
		player.username = username;
		PlayerList.add_player(player);
	}



	//creates an instance of Game to start a new game
	public static void newGame(){
		new Game();
	}


	public static void main(String[] args) {
		new Main();


		b1.addActionListener(new java.awt.event.ActionListener(){
				@Override
				public void actionPerformed(ActionEvent e) {
					// TODO Auto-generated method stub
					gameFrame game = new gameFrame();
			}
		});

	}

}
