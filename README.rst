i3-config-builder
=================

Python based configuration assembler. This project takes several separate configuration files and combines them together into the config to be used by i3.

This is to help with managing different i3 configurations for different computers. This project allows for separate config files for different hostnames.

This project is based on the work done by simpss over at https://github.com/simpss/i3_config.

To install from source, run the following in the root of the repo::

    pip install -e .


Usage
-----

Command line arguments::

    usage: i3-config-builder [-h] [-r] [-c] [-b BASE_DIR] [-d OUTPUT_DIR]

    Command line i3 config file builder

    optional arguments:
      -h, --help            show this help message and exit
      -r, --restart         Make i3 restart to load config
      -c, --reload          Make i3 to reload config
      -b BASE_DIR, --base-dir BASE_DIR
                            Directory containing input configuration files
      -d OUTPUT_DIR, --output-dir OUTPUT_DIR
                            Directory to output built config

Input file name format
----------------------

All input files must start with a number followed by '-all-' or '-hostname-' to specify any computer or just a specific computer to add the config files. Make sure to make all input files have the .i3conf extension.

Examples:

- 1-all-mod-key.i3conf
- 12-chaos-raptor-workspaces.i3conf
- 12-ghost-workspaces.i3conf
- 2-chaos-raptor-laptop-keys.i3conf
- 3-all-restart-reload-i3.i3conf

