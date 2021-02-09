package Game;

import GUI.Main;

import java.util.ArrayList;
import java.util.Collections;

import static Game.PlayerList.player_list;

public class Game {
    public static String winner = null;
    public static ArrayList<Integer> vote_tracker = new ArrayList<Integer>();
    public static Boolean vote_state = false;
    public static Boolean has_vote_state_been_true = false;

    public Game(){
        chooseRoles();
        setVote_tracker();
        has_vote_state_been_true = false;
    }



    //clears the player_list
    public static void clear_player_list (){
        player_list.clear();
    }

    //clears vote_tracker and then adds a spot in vote_tracker for every player + option to skip
    public static void setVote_tracker(){
        if (!vote_tracker.isEmpty()) {
            vote_tracker.clear();
        }
            for (int i = 0; i < player_list.size() + 1; i++) {
                vote_tracker.add(0);
            }


    }


    //assigns impostor randomly to one player and makes every other player a crewmate
    void chooseRoles (){
        int number_of_players = player_list.size();
        Collections.shuffle(player_list);
        for (int i = 0; i < number_of_players; i++){
            if (i == 0){
                player_list.get(i).role = "impostor";
            }
            else{
                player_list.get(i).role = "crewmate";
            }
        }
    }

    //checks how many crewmates are alive and if there is only one, impostor wins
    private static void checkDeathWin() {
        int number_of_players = player_list.size();
        int alive_crewmates = 0;
        for (int i = 0; i < number_of_players; i++){
            if(player_list.get(i).status == "alive" && player_list.get(i).role == "crewmate"){
                alive_crewmates = alive_crewmates + 1;
            }
        }

        if (alive_crewmates == 1){
            impostor_win();
        }
    }

    //changes the status of an alive player to dead and checks to see if that death made impostor or crewmates win
    public static void playerDead(String username){
        int number_of_players = player_list.size();
        for (int i = 0; i < number_of_players; i++){
            if(player_list.get(i).username == username){
                player_list.get(i).status = "dead";

                if(player_list.get(i).role == "impostor"){
                    crewmate_win();

                }
                i = number_of_players;

            }
        }
        checkDeathWin();

    }

    //takes a username and returns the index of that player within player_list
    public static int getPlayerIndex (String username){
        for (int i = 0; i < player_list.size(); i++){
            if (player_list.get(i).username == username){
                return i;
            }
        }
        return -1;
    }


    //takes Player and applies their vote to the vote_tracker
    public static void vote(Player voter){
        if (voter.voted == "skip"){
            vote_tracker.set(player_list.size(), vote_tracker.get(player_list.size()) + 1);
            voter.voted = "no vote";
        }
        if (voter.voted == "no vote"){

        }
        else{
            vote_tracker.set(getPlayerIndex(voter.voted), vote_tracker.get(player_list.size()) + 1);
            voter.voted = "no vote";
        }
    }

    //iterates through player_list and calls the vote method on every alive player
    public static void applyVotes(){
        for (int i = 0; i < player_list.size(); i++){
            if (player_list.get(i).status == "alive") {
                vote(player_list.get(i));
            }
        }
    }

    //tallies votes and kills a player if they receive the most votes
    public static void tallyVotes(){
        boolean tied = true;
        int current_champ = 0;
        int current_champ_votes = 0;
        for (int i = 0; i < vote_tracker.size(); i++){
            if (vote_tracker.get(i) > current_champ_votes){
                current_champ = i;
                current_champ_votes = vote_tracker.get(i);
                tied = false;
            }
            else if (vote_tracker.get(i) == current_champ_votes){
                tied = true;
            }
        }
        if (!tied && current_champ != player_list.size()){
            playerDead(player_list.get(current_champ).username);
        }
        setVote_tracker();
    }

    public static Boolean hasEveryPlayerVoted(){
        for (int i = 0; i < player_list.size(); i++){
            if (player_list.get(i).status == "alive"){
                if (player_list.get(i).voted == "no vote"){
                    return false;
                }
            }

        }
        return true;
    }

    //enter the voting state and stays until all players have voted or a timer expires (timer will be added later)
    public static void enterVoting(){
        while (vote_state){
            /*while (!hasEveryPlayerVoted()  && timer still going ){
                timer goes down
            }*/

            vote_state = false;

        }
        applyVotes();
        tallyVotes();

    }

    //if a body is reported, the game will enter the voting state
    public static void reportBody(){
        vote_state = true;
        has_vote_state_been_true = true;
        enterVoting();
    }

    public static Boolean doesPlayerHaveEmergencyButton(Player player){
        if (player.button_presses > 0){
            return true;
        }
        return false;
    }

    public static void emergencyButton(Player player){
        if (doesPlayerHaveEmergencyButton(player)){
            player.button_presses = player.button_presses - 1;
            vote_state = true;
            has_vote_state_been_true = true;
            enterVoting();
        }
        else{
            System.out.println("no emergency buttons");
        }
    }



    //sets winner to "Impostor wins" and prints
    public static void impostor_win() {
        winner = "Impostor wins";
        System.out.println(winner);

    }

    //sets winner to "Crewmates win" and prints
    public static void crewmate_win(){
        winner = "Crewmates win";
        System.out.println(winner);

    }




}
