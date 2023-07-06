#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # dedup ranked (using set?)
    ranked = sorted(set(ranked), reverse=True)

    # go through the player scores and find out where they belong in the ranked list
    player_rankings = []
    len_ranked = len(ranked)
    rank_index = len_ranked - 1
    len_player = len(player)   
    player_index = 0

    while (rank_index >=0) and (player_index < len_player):
    
        # if the rank score is better than the player score write this rank and move to the next player score
        if ranked[rank_index] > player[player_index]:
            player_rankings.append(rank_index + 2)
            player_index += 1
        # if the rank score is not better than the player score move in rank
        else:
            rank_index -= 1

    for i in range(len_player - player_index):
        player_rankings.append(1)
        
    return player_rankings

if __name__ == '__main__':

    #7
    ranked=[100, 100, 50, 40, 40, 20, 10]
    #4
    player=[5, 25, 50, 120]

    result = climbingLeaderboard(ranked, player)

    print(result)

    #6
    ranked=[100, 90, 90, 80, 75, 60]
    #5
    player=[50, 65, 77, 90, 102]

    result = climbingLeaderboard(ranked, player)

    print(result)