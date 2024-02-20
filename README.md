# Mobi Code Assignment

Flight departure boarding pass scan tool with command line.

## Objective

Prevent passengers from boarding the wrong plane.
Prevent a boarding pass to be used twice.

## Design

The code has been split into the UI (`shell.py`) and the
database implementation (`database.py`).
Arguably everything could have been implemented in a single file
with the database objects replaced by hash-tables.
We wanted to separate logic and interaction into two files
and encapsulate data manipulation in this design.

One assumption made for simplicity was that there is only
a single flight and a single boarding gate at the moment,
so there are no provisions to deal with race conditions.

Another assumption made is that the data is loaded once and
does not change through the boarding process due to external
input.

There has also been no provisions made to persist the state of
the database or provide for any failure compensation should
the "simulator" process crash due to various reasons.

## Components

### Database

Small implementation of an in memory database,
which reads data from a JSON file and stores it
in a hierarchy of hash tables keyed by: `flight_code` and `pnr`.

### Shell

Implementation of a command line shell to the database allowing
to select a `FLIGHT` and `SCAN` a boarding pass. The shell
is implemented using `cmd.Cmd` Python utility.

## Running

The reservation shell can be invoked with the following command:
```bash
python3 shell.py [reservation_data_file.jsonl]
```
from the repository directory.

The database reads `.jsonl` files as records separated by newline.
It also reads `.json` files with records as array stored
in the `records` attribute of the top-level object.
See the two `test_reservation_data.json(l)` files.

There is also a `notebook.ipynb` file that contains a simple session.

## Testing

Testing can be done using following command:

```bash
python3 -m unittest -v
```
