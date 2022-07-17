import argparse
import pathlib
import os
import json

from datetime import datetime
from dateutil import relativedelta


parser = argparse.ArgumentParser(description='Timecop, Target Script')
parser.add_argument('--db-dir',
                    type=pathlib.Path,
                    default=pathlib.Path.cwd(),
                    help='Storage directory')
parser.add_argument('--projects',
                    type=str,
                    default='default',
                    help='Project labels, eg. "world-domination-project", comma separated')
parser.add_argument('--target',
                    type=int,
                    default=10,
                    help='Number of hours intended to spend')
args = parser.parse_args()

projects = args.projects.split(',')

def main():
    # current timerange
    _now = datetime.now()
    _nextmonth = _now + relativedelta.relativedelta(months=1)
    _start = _now.replace(day=10, hour=0, minute=0, second=0)
    _stop = _nextmonth.replace(day=9, hour=23, minute=59, second=59)
    print('from')
    print(datetime.strftime(_start, '%Y-%m-%d %H-%M-%S'))
    print('until')
    print(datetime.strftime(_stop, '%Y-%m-%d %H-%M-%S'))
    print('projects')
    print(projects)
    # load data
    _format_file = '%Y-%m-%d--%H-%M-%S'
    dir_list = os.listdir(args.db_dir)
    # filter the time range
    selected = []
    for filename in dir_list:
        for project in projects:
            if filename.startswith(project):
                rem = filename.split(project + '-')[1]
                rst = rem.split('.json')[0]
                dt = datetime.strptime(rst, _format_file)
                if _start < dt < _stop:
                    selected.append(filename)
    # compute data
    total_seconds = 0
    for filename in selected:
        with open(str(args.db_dir) + '/' + filename, 'r') as f:
            result = json.load(f)
            if result['project'] in projects:
                total_seconds += result['time']['duration']
    print(total_seconds)
    total_hours = total_seconds / 3600
    print('total hours')
    print(round(total_hours, 2))
    print('target hours')
    print(args.target)
    print('target met')
    print(str(round((total_hours / args.target)*100, 2)) + '%')
