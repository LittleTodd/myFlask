import nba_py

def get_games():
    scoreboard = nba_py.Scoreboard(month=12, day=24, year=2017)
    line_score = scoreboard.line_score()

    games = []
    current_game = {}

    current_game_sequence = 0
    game_sequence_counter = 0

    for team in line_score:
        if (team["GAME_SEQUENCE"] != current_game_sequence):
            current_game["TEAM_1_ABBREVIATION"] = team["TEAM_ABBREVIATION"]
            current_game["TEAM_1_WINS_LOSSES"] = team["TEAM_WINS_LOSSES"]
            current_game["TEAM_1_PTS"] = team["PTS"]
            current_game["TEAM_1_ID"] = team["TEAM_ID"]

            current_game_sequence = team["GAME_SEQUENCE"]
            game_sequence_counter += 1
        elif (game_sequence_counter == 1):
            current_game["TEAM_2_ABBREVIATION"] = team["TEAM_ABBREVIATION"]
            current_game["TEAM_2_WINS_LOSSES"] = team["TEAM_WINS_LOSSES"]
            current_game["TEAM_2_PTS"] = team["PTS"]
            current_game["TEAM_2_ID"] = team["TEAM_ID"]

            current_game["GAME_ID"] = team["GAME_ID"]

            games.append(current_game)

            current_game = {}
            game_sequence_counter = 0

    return games
