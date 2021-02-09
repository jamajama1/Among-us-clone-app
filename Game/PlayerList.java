package Game;

import java.util.ArrayList;


public class PlayerList {

    //ArrayList to keep track of the list of players
    public static ArrayList<Player> player_list = new ArrayList<Player>();

    //adds a player to player_list
    public static void add_player (Player player){
        player_list.add(player);


    }


}
