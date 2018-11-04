INSERT INTO leagues (name) VALUES ("NHL"), ("NBA");

INSERT INTO teams (name, league_id) VALUES
       ("New York Rangers", 1),
       ("Vancouver Canucks", 1),
       ("New York Knicks", 2),
       ("Houston Rockets", 2);

INSERT INTO players (name, team_id) VALUES
        ("Wayne Gretsky", 1),
        ("Jim Jacisin", 2),
        ("Starbury", 3),
        ("Dikembe Mutumbo", 4);

INSERT INTO games (date, location) VALUES
        (2018-10-22, "New York, NY"),
        (2018-01-01, "Vancouver, Canada"),
        (2017-11-07, "Washington, DC");

INSERT INTO team_games (team_id, game_id, score) VALUES
        (2,1,20),
        (1,1,10),
        (3,2,30),
        (4,2,40),
        (1,3,50),
        (4,3,60);
