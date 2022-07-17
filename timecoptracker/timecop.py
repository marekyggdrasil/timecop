import argparse
import pathlib
import json
import os
import time
import math
import csv

from datetime import datetime

_from = datetime.now().replace(hour=0, minute=0, second=1)
_until = datetime.now().replace(hour=23, minute=59, second=59)

parser = argparse.ArgumentParser(description='Timecop, Reports Script')
parser.add_argument('--db-dir',
                    type=pathlib.Path,
                    default=pathlib.Path.cwd(),
                    help='Storage directory')
parser.add_argument('--projects',
                    type=str,
                    default='default',
                    help='Project labels, eg. "world-domination-project", comma separated')
parser.add_argument('--start',
                    type=lambda s: datetime.strptime(s, '%Y-%m-%d'),
                    default=_from,
                    help='Starting date, YYYY-MM-DD format.')
parser.add_argument('--stop',
                    type=lambda s: datetime.strptime(s, '%Y-%m-%d'),
                    default=_until,
                    help='Ending date, YYYY-MM-DD format.')
parser.add_argument('--out',
                    type=str,
                    help='Output file')
args = parser.parse_args()

projects = args.projects.split(',')
print('{0:8}: {1}'.format('Projects', projects))
print('{0:8}: {1}'.format('From', args.start))
print('{0:8}: {1}'.format('Until', args.stop))

def main():
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
                if args.start < dt < args.stop:
                    selected.append(filename)
    # filter the project
    data = {}
    for filename in selected:
        with open(str(args.db_dir) + '/' + filename, 'r') as f:
            result = json.load(f)
            if result['project'] in projects:
                if result['project'] not in data.keys():
                    data[result['project']] = []
                data[result['project']].append(result)
    # prepare the CSV report
    tot = 0
    rows = [['Project', 'Activity', 'Start', 'Stop', 'Time']]
    for project, results in data.items():
        first = True
        for result in results:
            project_name = ''
            if first:
                project_name = project
                first = False
            val = math.ceil(result['time']['duration'])
            tot += val
            row = [
                project_name,
                result['activity'],
                result['time']['start'],
                result['time']['stop'],
                time.strftime('%H:%M:%S', time.gmtime(val))]
            rows.append(row)
    row = [
        'Total',
        '',
        '',
        '',
        time.strftime('%H:%M:%S', time.gmtime(math.ceil(tot)))]
    rows.append(row)
    with open(args.out, 'w', newline = '') as csvfile:
        my_writer = csv.writer(csvfile, delimiter=',')
        for row in rows:
            my_writer.writerow(row)
