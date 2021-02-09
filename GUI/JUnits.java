package GUI;

import Game.Game;
import org.junit.jupiter.api.Test;


import static Game.PlayerList.player_list;
import static org.junit.jupiter.api.Assertions.assertEquals;


public class JUnits {

    //tests to make sure players are added to the game by new_player
    @Test
    public void playersAddedToGame() {
        Main tester = new Main();

        tester.new_player("playerone");
        tester.new_player("playertwo");
        tester.new_player("playerthree");
        tester.new_player("playerfour");
        tester.new_player("playerfive");
        tester.new_player("playersix");
        tester.new_player("playerseven");
        tester.new_player("playereight");
        tester.new_player("playernine");
        tester.new_player("playerten");

        assertEquals("playerone", player_list.get(0).username);
        assertEquals("playertwo", player_list.get(1).username);
        assertEquals("playerseven", player_list.get(6).username);
        assertEquals("playerten", player_list.get(9).username);
        player_list.clear();
    }

    //tests to ensure that there is only one impostor chosen and every other player is a crewmate
    @Test
    public void OneImpostorChosen(){
        Main tester = new Main();

        tester.new_player("playerone");
        tester.new_player("playertwo");
        tester.new_player("playerthree");
        tester.new_player("playerfour");
        tester.new_player("playerfive");
        tester.new_player("playersix");
        tester.new_player("playerseven");
        tester.new_player("playereight");
        tester.new_player("playernine");
        tester.new_player("playerten");
        tester.newGame();
        int impostorCount = 0;
        int crewmateCount = 0;
        for (int i = 0; i < player_list.size(); i++){
            if (player_list.get(i).role == "crewmate"){
                crewmateCount = crewmateCount + 1;
            }
            else if (player_list.get(i).role == "impostor") {
                impostorCount = impostorCount + 1;
            }
        }
        assertEquals(9, crewmateCount);
        assertEquals(1, impostorCount);
        player_list.clear();
    }

    //tests playerDead method to make sure only the player used in the argument dies
    @Test
    public void playerWillDie(){
        Main tester = new Main();

        tester.new_player("playerone");
        tester.new_player("playertwo");
        tester.new_player("playerthree");
        tester.new_player("playerfour");
        tester.new_player("playerfive");
        tester.new_player("playersix");
        tester.new_player("playerseven");
        tester.new_player("playereight");
        tester.new_player("playernine");
        tester.new_player("playerten");
        tester.newGame();
        Game.playerDead(player_list.get(0).username);
        Game.playerDead(player_list.get(3).username);
        Game.playerDead(player_list.get(7).username);
        Game.playerDead(player_list.get(9).username);
        assertEquals("dead", player_list.get(0).status);
        assertEquals("dead", player_list.get(3).status);
        assertEquals("dead", player_list.get(7).status);
        assertEquals("dead", player_list.get(9).status);
        assertEquals("alive", player_list.get(2).status);
        assertEquals("alive", player_list.get(8).status);
        player_list.clear();
    }

    //makes sure all players are alive at the start of a game
    @Test
    public void playersAliveAtStart(){
        Main tester = new Main();

        tester.new_player("playerone");
        tester.new_player("playertwo");
        tester.new_player("playerthree");
        tester.new_player("playerfour");
        tester.new_player("playerfive");
        tester.new_player("playersix");
        tester.new_player("playerseven");
        tester.new_player("playereight");
        tester.new_player("playernine");
        tester.new_player("playerten");
        tester.newGame();
        for (int i = 0; i < player_list.size(); i++){
            assertEquals("alive", player_list.get(i).status);
        }
        player_list.clear();
    }


    //tests to make sure that crewmates win if impostor dies
    @Test
    public void crewmatesWinIfImpostorDies() {
        Main tester = new Main();

        tester.new_player("playerone");
        tester.new_player("playertwo");
        tester.new_player("playerthree");
        tester.new_player("playerfour");
        tester.new_player("playerfive");
        tester.new_player("playersix");
        tester.new_player("playerseven");
        tester.new_player("playereight");
        tester.new_player("playernine");
        tester.new_player("playerten");
        tester.newGame();
        for (int i = 0; i < player_list.size(); i++){
            if (player_list.get(i).role == "impostor"){
                Game.playerDead(player_list.get(i).username);
            }
        }
        assertEquals("Crewmates win", Game.winner);

        player_list.clear();
    }

    //tests to make sure the impostor wins if there is only one crewmate alive
    @Test
    public void impostorWinsIfThereIsOneCremateLeft() {
        Main tester = new Main();

        tester.new_player("playerone");
        tester.new_player("playertwo");
        tester.new_player("playerthree");
        tester.new_player("playerfour");
        tester.new_player("playerfive");
        tester.new_player("playersix");
        tester.new_player("playerseven");
        tester.new_player("playereight");
        tester.new_player("playernine");
        tester.new_player("playerten");
        tester.newGame();
        for (int i = 0; i < player_list.size(); i++){
            if (player_list.get(i).role != "impostor"){
                Game.playerDead(player_list.get(i).username);
            }
        }
        assertEquals("Impostor wins", Game.winner);

        player_list.clear();
    }

    //tests to make sure no one dies if no votes are cast
    @Test
    public void nooneDiesIfNooneVotes() {
        Main tester = new Main();

        tester.new_player("playerone");
        tester.new_player("playertwo");
        tester.new_player("playerthree");
        tester.new_player("playerfour");
        tester.new_player("playerfive");
        tester.new_player("playersix");
        tester.new_player("playerseven");
        tester.new_player("playereight");
        tester.new_player("playernine");
        tester.new_player("playerten");
        tester.newGame();
        Game.applyVotes();
        Game.tallyVotes();
        for (int i = 0; i < player_list.size(); i++) {
            assertEquals("alive", player_list.get(i).status);
        }
        player_list.clear();
    }

    //tests to make sure no one dies if skip receives the most votes
    @Test
    public void noOneDiesIfSkipsReceivesMostVotes() {
        Main tester = new Main();

        tester.new_player("playerone");
        tester.new_player("playertwo");
        tester.new_player("playerthree");
        tester.new_player("playerfour");
        tester.new_player("playerfive");
        tester.new_player("playersix");
        tester.new_player("playerseven");
        tester.new_player("playereight");
        tester.new_player("playernine");
        tester.new_player("playerten");
        tester.newGame();
        player_list.get(1).voted = player_list.get(0).username;
        player_list.get(0).voted = "skip";
        player_list.get(2).voted = "skip";
        player_list.get(3).voted = "skip";
        Game.applyVotes();
        Game.tallyVotes();
        for (int i = 0; i < player_list.size(); i++) {
            assertEquals("alive", player_list.get(i).status);
        }
        player_list.clear();
    }

    //tests to make sure a player dies if they receive the most votes
    @Test
    public void playerDiesIfTheyReceiveTheMostVotes() {
        Main tester = new Main();

        tester.new_player("playerone");
        tester.new_player("playertwo");
        tester.new_player("playerthree");
        tester.new_player("playerfour");
        tester.new_player("playerfive");
        tester.new_player("playersix");
        tester.new_player("playerseven");
        tester.new_player("playereight");
        tester.new_player("playernine");
        tester.new_player("playerten");
        tester.newGame();
        player_list.get(1).voted = player_list.get(7).username;
        player_list.get(4).voted = player_list.get(7).username;
        player_list.get(2).voted = player_list.get(7).username;
        player_list.get(3).voted = "skip";
        Game.applyVotes();
        Game.tallyVotes();
        int ind = Game.getPlayerIndex(player_list.get(7).username);
        for (int i = 0; i < player_list.size(); i++) {
            if (i == ind){
                assertEquals("dead", player_list.get(i).status);
            } else {
                assertEquals("alive", player_list.get(i).status);
            }
        }
        player_list.clear();
    }

    //tests to make sure crewmates win if the impostor is voted out
    @Test
    public void crewmatesWinIfImpostorVotedOut() {
        Main tester = new Main();

        tester.new_player("playerone");
        tester.new_player("playertwo");
        tester.new_player("playerthree");
        tester.new_player("playerfour");
        tester.new_player("playerfive");
        tester.new_player("playersix");
        tester.new_player("playerseven");
        tester.new_player("playereight");
        tester.new_player("playernine");
        tester.new_player("playerten");
        tester.newGame();
        player_list.get(1).voted = player_list.get(0).username;
        player_list.get(4).voted = player_list.get(0).username;
        player_list.get(2).voted = player_list.get(0).username;
        player_list.get(3).voted = "skip";
        Game.applyVotes();
        Game.tallyVotes();
        int ind = Game.getPlayerIndex(player_list.get(0).username);
        assertEquals("Crewmates win", Game.winner);
        player_list.clear();
        }

    //tests to make sure no one dies if a vote is tied
    @Test
    public void noOneDiesInTiedVote() {
        Main tester = new Main();

        tester.new_player("playerone");
        tester.new_player("playertwo");
        tester.new_player("playerthree");
        tester.new_player("playerfour");
        tester.new_player("playerfive");
        tester.new_player("playersix");
        tester.new_player("playerseven");
        tester.new_player("playereight");
        tester.new_player("playernine");
        tester.new_player("playerten");
        tester.newGame();
        player_list.get(1).voted = player_list.get(6).username;
        player_list.get(0).voted = player_list.get(6).username;
        player_list.get(2).voted = player_list.get(7).username;
        player_list.get(3).voted = player_list.get(7).username;
        player_list.get(4).voted = player_list.get(8).username;
        Game.applyVotes();
        Game.tallyVotes();
        for (int i = 0; i < player_list.size(); i++) {
            assertEquals("alive", player_list.get(i).status);
        }
        player_list.clear();
    }

    //tests to make sure reporting a dead body will cause the game to enter the vote state
    @Test
    public void reportBodyCausesVote() {
        Main tester = new Main();

        tester.new_player("playerone");
        tester.new_player("playertwo");
        tester.new_player("playerthree");
        tester.new_player("playerfour");
        tester.new_player("playerfive");
        tester.new_player("playersix");
        tester.new_player("playerseven");
        tester.new_player("playereight");
        tester.new_player("playernine");
        tester.new_player("playerten");
        tester.newGame();
        assertEquals(false, Game.has_vote_state_been_true);
        Game.reportBody();
        assertEquals(true, Game.has_vote_state_been_true);
        player_list.clear();
    }

    //tests to make sure reporting a dead body will cause the game to enter the vote state
    @Test
    public void emergencyButtonCauseVote() {
        Main tester = new Main();

        tester.new_player("playerone");
        tester.new_player("playertwo");
        tester.new_player("playerthree");
        tester.new_player("playerfour");
        tester.new_player("playerfive");
        tester.new_player("playersix");
        tester.new_player("playerseven");
        tester.new_player("playereight");
        tester.new_player("playernine");
        tester.new_player("playerten");
        tester.newGame();
        assertEquals(false, Game.has_vote_state_been_true);
        Game.emergencyButton(player_list.get(0));
        assertEquals(true, Game.has_vote_state_been_true);
        player_list.clear();
    }

    //tests to see if player has an emergency button before and after pressing button, should print"no emergency buttons" when the player has no button
    @Test
    public void onlyOneEmergencyButton() {
        Main tester = new Main();

        tester.new_player("playerone");
        tester.new_player("playertwo");
        tester.new_player("playerthree");
        tester.new_player("playerfour");
        tester.new_player("playerfive");
        tester.new_player("playersix");
        tester.new_player("playerseven");
        tester.new_player("playereight");
        tester.new_player("playernine");
        tester.new_player("playerten");
        tester.newGame();
        assertEquals(true, Game.doesPlayerHaveEmergencyButton(player_list.get(0)));
        Game.emergencyButton(player_list.get(0));
        assertEquals(false, Game.doesPlayerHaveEmergencyButton(player_list.get(0)));
        Game.emergencyButton(player_list.get(0));

        player_list.clear();
    }
    //tests to make sure prompt mess handles inputs correctly
    @Test
    public void num_is_1() { // Input is 1 for message 1
        Prompt tester = new Prompt(); // Prompt is tested
            assertEquals("Use the movement keys to do a dance party", tester.mess(1));
    }
    //tests to make sure prompt mess handles invalid inputs correctly
    @Test
    public void num_is_9() { // Input is 1 for message 9
        Prompt tester = new Prompt(); // Prompt is tested

        assertEquals("o to the left of the screen and race to the right of the screen", tester.mess(9));

    }
    //tests to make sure prompt mess handles inputs correctly

}

