import colorama
colorama.init()

from argparse import ArgumentParser
from codecs import open
from subprocess import call
import os
import glob
import socket
import sys


# Handle argument parsing
def get_args():
    parser = ArgumentParser(
        prog='i3-config-builder',
        description='Command line i3 config file builder'
    )
    parser.add_argument('-r', '--restart', action='store_true', help='Make i3 restart to load config')
    parser.add_argument('-c', '--reload', action='store_true', help='Make i3 to reload config')
    parser.add_argument('-b', '--base-dir', default=os.path.expanduser('~/.i3/config.d'), help='Directory containing input configuration files')
    parser.add_argument('-d', '--output-dir', default=os.path.expanduser('~/.i3'), help='Directory to output built config')
    args, unknown = parser.parse_known_args()

    bad_input = False

    if not os.path.isdir(os.path.realpath(args.base_dir)):
        sys.stderr.write('Base directory does not exist\n')
        bad_input = True

    if not os.path.isdir(os.path.realpath(args.output_dir)):
        sys.stderr.write('Output directory does not exist\n')
        bad_input = True

    if bad_input:
        sys.stderr.write('Cannot continue\n')
        sys.exit(1)

    return args


# Main function that gets called on execution
def main():
    pass
    args = get_args()
    debug = False

    hostname = socket.gethostname()

    base_dir = os.path.realpath(args.base_dir) + '/'
    output_file = os.path.realpath(args.output_dir) + '/config'
    extension = 'i3conf'

    print("Building i3 configuration file for host: {hostname}".format(hostname=hostname))

    # Find file names of input files
    file_names = [f for f in glob.glob("{}*[0-9]-*-*.{}".format(base_dir, extension)) if '-all-' in f or '-' + hostname + '-' in f]
    file_names.sort()

    print('Found configuration files:')
    for f in file_names:
        print(f)

    # Read config files
    config_files = []
    for f in file_names:
        try:
            with open(f, encoding='utf-8') as open_file:
                config_files.append({
                    'name': f,
                    'contents': open_file.read()
                })
        except Exception as e:
            print("Exception: {}".format(e))
            print("Failed to read input file: {}".format(f))
            sys.exit(1)

    # Backup existing output file if it exists
    if os.path.exists(output_file):
        os.rename(output_file, output_file + '.bak')

    # Write all the config files to a single file
    with open(output_file, 'w', 'utf-8-sig') as config:
        for config_part in config_files:
            config.write(
                "#################\n# Part file: {} #\n{}\n##############\n\n"
                .format(config_part['name'], config_part['contents'])
            )

    if args.restart:
        print('Restarting i3')
        call(['i3', 'restart'])

    if args.reload:
        print('Reloading i3')
        call(['i3', 'reload'])

    print("New config created at: {}".format(output_file))


if __name__ == '__main__':
    main()
