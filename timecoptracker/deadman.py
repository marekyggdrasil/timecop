import time
import sys
import argparse
import pathlib
import json

from datetime import datetime

parser = argparse.ArgumentParser(description='Timecop, Dead Man Script')
parser.add_argument('--db-dir',
                    type=pathlib.Path,
                    default=pathlib.Path.cwd(),
                    help='Storage directory')
parser.add_argument('--project',
                    type=str,
                    default='default',
                    help='Project label, eg. "world-domination-project"')
parser.add_argument('--activity',
                    type=str,
                    default='work',
                    help='Project task description, eg. "Building super volcano"')
args = parser.parse_args()

def backline():
    print('\r', end='')

def main():
    print(args.db_dir)
    print('{0:8}: {1}'.format('Project', args.project))
    print('{0:8}: {1}'.format('Activity', args.activity))
    print()
    _format = '%Y-%m-%d %H:%M:%S'
    _format_file = '%Y-%m-%d--%H-%M-%S'
    start = datetime.now()
    try:
        while True:
            now = datetime.now()
            duration = now - start
            text = 'timecop ' + str(duration)
            print(text, end='', flush=True)
            time.sleep(1)
            backline()
    except KeyboardInterrupt:
        print()
        print('Work session over.')
    stop = datetime.now()
    duration = stop - start
    text = 'final ' + str(duration)
    print(text, end='', flush=True)
    print()
    result = {
        'project': args.project,
        'activity': args.activity,
        'time': {
            'start': start.strftime(_format),
            'stop': stop.strftime(_format),
            'duration': duration.total_seconds()
        }
    }
    filename = args.project + '-' + start.strftime(_format_file) + '.json'
    with open(str(args.db_dir) + '/' + filename, 'w') as f:
        json.dump(result, f)


