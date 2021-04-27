import sqlite3


def create_player_record():
    while True:
        info = []
        heroes = []
        pl_name = input("Player name: ")
        pl_pos = input(f"{pl_name}'s position: ")
        hero_1 = input(f"{pl_name} - Hero 1: ")
        hero_2 = input(f"{pl_name} - Hero 2: ")
        hero_3 = input(f"{pl_name} - Hero 3: ")

        for i in (pl_name, pl_pos):
            info.append(i)

        for h in (hero_1, hero_2, hero_3):
            heroes.append(h)

        with sqlite3.connect("teamcommcomp.db") as conn:
            c = conn.cursor()
            c.execute("INSERT INTO Players VALUES(?, ?, ?, ?, ?)", info + heroes)
            print('Data inserted into database.')

        display_record(pl_name)

        stop = input("Hit Q to quit.\n")
        if stop.upper() == 'Q':
            break
        else:
            continue


def update_player_record(player):
    while True:
        print(f"Updating record for {player.upper()}")
        print("Current record: \n")

        display_record(player)
        print()

        info = []
        heroes = []
        print(f"{player}'s data:")
        pl_pos = input(f"{player}'s position(s): ")
        hero_1 = input(f"{player} - Hero 1: ")
        hero_2 = input(f"{player} - Hero 2: ")
        hero_3 = input(f"{player} - Hero 3: ")

        info.append(pl_pos)
        for h in (hero_1, hero_2, hero_3):
            heroes.append(h)

        with sqlite3.connect("teamcommcomp.db") as conn:
            c = conn.cursor()
            c.execute("""UPDATE Players
            SET position=:pos, 
                hero_1=:hero1, 
                hero_2=:hero2, 
                hero_3=:hero3
            WHERE name=:player""",
                      {'pos': pl_pos,
                       'hero1': hero_1,
                       'hero2': hero_2,
                       'hero3': hero_3,
                       'player': player})
        print(f'Record updated for {player}.')

        display_record(player)

        stop = input("Hit Q to quit.\n")
        if stop.upper() == 'Q':
            break
        else:
            continue


def display_record(player=None):
    with sqlite3.connect('teamcommcomp.db') as conn:
        c = conn.cursor()
        if player:
            c.execute("SELECT * from Players WHERE name=:pl_name", {'pl_name': player})
        else:
            c.execute("SELECT * from Players")

        rows = c.fetchall()

        for row in rows:
            print(row)
