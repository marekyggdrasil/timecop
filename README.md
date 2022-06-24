# Timecop

## Installation

```sh
pip install timecop-tracker
```

## Usage

Whenever you work on something, you may run the the dead-man to keep idle and collect the time data

```sh
dead-man --db-dir /home/drevil/timecop-data/ --project world-domination --task "Supervolcano base"
```

when you are done you can simply stop it with CTR-C key combination. You may generate time sheet reports

```sh
timecop --db-dir /home/drevil/timecop-data/ --project world-domination --start 2022-06-02 --stop 2022-06-25 --out out.csv
```

simple as that!
