i3-config-builder
=================

Python based configuration assembler. This project takes several separate configuration files and combines them together into the config to be used by i3.

This is to help with managing different i3 configurations for different computers. This project allows for separate config files for different hostnames.

This project can be found at https://github.com/brileb73/i3-config-builder and is based on the work done by simpss over at https://github.com/simpss/i3_config.


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

Here is an example call to i3cfgbuild::

    i3cfgbuild -b ~/i3-config-builder/examples -d ~/.i3 -c

This command uses the .i3conf files in ~/i3-config-builder/examples to create the config file ~/.i3/config and reloads i3 after the new config file is in place.


Input file name format
----------------------

All input files must start with a number followed by '-all-' or '-hostname-' to specify any computer or just a specific computer to add the config files. Make sure to make all input files have the .i3conf extension.

Examples:

- 1-all-mod-key.i3conf
- 12-chaos-raptor-workspaces.i3conf
- 12-ghost-workspaces.i3conf
- 2-chaos-raptor-laptop-keys.i3conf
- 3-all-restart-reload-i3.i3conf

In the above examples, the files that would be used for the hostname ghost are:

- 1-all-mod-key.i3conf
- 12-ghost-workspaces.i3conf
- 3-all-restart-reload-i3.i3conf


Output file format
------------------

The output file created is going to be called 'config' and placed in the output directory specified (default is ~/.i3). The contents of each input file is appended to the output file with a comment of what the input file name was.


Examples
--------

There are some example files in the examples directory of the repository which should generate a file that operates in the same way as the default i3 config file for using the super (Mod4) modifier.

