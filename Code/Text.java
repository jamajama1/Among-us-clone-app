// This file contains code that displays the mission prompts and chat messages.
package Code;

import javax.swing.*;
import java.awt.*;
import Code.Prompt;
public class Text {
    // Initializing J objects
    JFrame textFrame;
    JLabel promptLabel;
    JLabel chatLabel;
    JPanel promptPanel;
    JPanel chatPanel;


    Text() {
        //code for creating frames, panels, and Labels
        textFrame = new JFrame("Text");
        promptPanel = new JPanel();
        promptLabel = new JLabel();
        chatLabel = new JLabel();

        promptPanel.setLayout(new BoxLayout(promptPanel, BoxLayout.PAGE_AXIS));
        promptPanel.add(promptLabel);
        promptPanel.add(Box.createVerticalGlue()); // Vertical format for prompt over text
        promptPanel.add(chatLabel);

        textFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // Close the text Frame
        textFrame.setSize(400, 300);

        // Display the prompt
        Prompt prompt = new Prompt();
        String mission = prompt.mess(prompt.getNum());
        System.out.println(mission); // debug
        promptLabel.setText(mission + "\n");
        promptLabel.setVerticalTextPosition(SwingConstants.TOP);
        //textFrame.add(promptLabel);
        textFrame.add(promptPanel);
        textFrame.setVisible(true);

        // Get text input
        String chat = JOptionPane.showInputDialog(null, "Enter message");
        chatLabel.setText(chat);
        chatLabel.setVerticalTextPosition(chatLabel.BOTTOM);
        // textFrame.add(chatLabel);
        textFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        textFrame.pack();
    }
}
