import csv


# Get the unique characters in the label file.
def get_unique_labels(filename):
    char_set = set()

    with open(filename, 'r') as datafile:
        csv_reader = csv.reader(datafile, delimiter=',', quotechar='|')
        for r in csv_reader:
            char_set.add(r[3])

    return char_set


def generate_psb():
    char_set = get_unique_labels('labels3.csv')
    for char in char_set:
        if char == '\n':
            continue

        filename = './pbs/rsh-' + char + '.pbs'
        with open(filename, 'w') as pbs_file:
            pbs_file.write('#!/bin/bash\n')
            pbs_file.write('# PBS -l nodes=1:ppn=2\n')
            pbs_file.write('# PBS -l walltime=24:00:00\n')
            pbs_file.write('source /home/rcf-proj/tt3/tianxiat/workspace/rsh - trans/VE3/bin/activate\n')
            pbs_file.write('cd /home/rcf-proj/tt3/tianxiat/workspace/rsh-trans\n')
            pbs_file.write('python main_gbc.py' + char)


if __name__ == '__main__':
    generate_psb()