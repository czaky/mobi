"""Cmd shell for the reservation system."""

import cmd
import sys
import db

class ReservationShell(cmd.Cmd):
    """Cmd shell for the reservation system."""
    intro = 'Welcome to the reservation shell.\nType help or ? to list commands.'
    prompt = 'res> '

    def __init__(self, data_database: db.ReservationDB):
        cmd.Cmd.__init__(self)
        self.data = data_database
        self.flight = None

    def do_flight(self, flight):
        'Set the current flight number:  FLIGHT AA311'
        self.flight = self.data.lookup_flight(flight)
        if self.flight:
            print('OK')
        else:
            print(f'ERROR: flight "{flight}" not found in the database.')

    def do_scan(self, pnr):
        'Scan a boarding pass reservation code:  SCAN ACIWMY'
        if not self.flight:
            print('ERROR: please select the flight using the `FLIGHT XXXX` command.')
        elif self.flight.scan_passenger(pnr):
            print('ALLOW')
        else:
            print('DENY')

    def do_exit(self, _):
        'Exit the shell:  EXIT'
        print('Thank you for using Mobi reservation system.')
        return True

    def precmd(self, line):
        "Make prompt case insensitive."
        parts = line.split()
        parts[0] = parts[0].lower()
        return ' '.join(parts)


DEFAULT_DATA = "test_reservation_data.json"

def main(argv):
    "main"
    data_file_name = DEFAULT_DATA
    if len(argv) > 1:
        data_file_name = argv[1]
    database = db.ReservationDB()
    database.load_data(data_file_name)
    res = ReservationShell(database)
    res.cmdloop()

if __name__ == '__main__':
    main(sys.argv)
