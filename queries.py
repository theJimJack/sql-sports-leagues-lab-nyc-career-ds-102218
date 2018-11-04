def select_name_of_player_with_shortest_name():
    return '''SELECT p.name, length(p.name) AS name_length FROM players p
            GROUP BY p.name
            HAVING max(name_length);'''


def select_all_new_york_players_names():
    return '''SELECT p.name FROM teams t
            JOIN players p
            ON t.id = p.team_id
            WHERE t.name LIKE "%New York%"
            ;'''

def select_team_name_and_total_goals_scored_for_new_york_rangers():
    return '''SELECT t.name, sum(tg.score) FROM teams t
            JOIN team_games tg
            ON t.id = tg.team_id
            WHERE t.name = "New York Rangers"
            ;'''

def select_all_games_date_and_info_teams_name_and_score_for_teams_in_nhl():
    return '''SELECT g.*,tg.* FROM games g
            JOIN team_games tg
            ON g.id = tg.game_id
            JOIN teams t
            ON tg.team_id = t.id
            JOIN leagues l
            ON t.league_id = l.id
            WHERE l.name = "NHL"
            ;'''

def select_date_info_and_total_points_for_highest_scoring_nba_game():
    return '''SELECT g.date,g.info, tg_home.score+tg_away.score FROM games g
            JOIN team_games tg_home
            ON g.id = tg_home.game_id
            JOIN team_games tg_away
            ON tg.away.game_id = tg_home.game_id
            WHERE max(tg_home.score+tg_away.score)
            ;'''
