import sqlite3
import sys
from dbfunctions import create_player_record, update_player_record, display_record, delete_player_record


def main():
    print("****" * 4)
    print("Dota 2 Team Comp Tracker")
    print("****" * 4)

    while True:
        print("\nMain Menu\n")
        print("[C]reate Player Record(s)")
        print("[U]pdate Player Record")
        print("[D]isplay Player Record(s)")
        print("[R]emove Player Record\n")

        cmd = input("Enter command [C,U,D,R] or [Q]uit: ")
        if cmd.upper() == 'C':
            create_player_record()
        elif cmd.upper() == 'U':
            player = input("Enter player to update: ")
            update_player_record(player)
        elif cmd.upper() == 'D':
            d_player = input("Press ENTER to display all, or enter player name: ")
            if cmd.strip == '':
                display_record()
            else:
                display_record(d_player)
        elif cmd.upper() == 'R':
            r_player = input("Enter player to remove: ")
            delete_player_record(r_player)
        elif cmd.upper() == 'Q':
            sys.exit()
        else:
            print("Invalid command!")


if __name__ == '__main__':
    main()
