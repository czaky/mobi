# Mobi Code Assignment

Flight departure boarding pass scan tool with command line.

## Objective

Prevent passengers from boarding the wrong plane.
Prevent a boarding pass to be used twice.

## Components

### Database

Small implementation of an in memory database,
which reads data from a JSON file and stores it
in a hierarchy of hash tables keyed by: `flight_code` and `pnr`.

### Shell

Implementation of a command line shell to the database allowing
to select a `FLIGHT` and `SCAN` a boarding pass. The shell
is implemented using `cmd.Cmd` Python utility.
