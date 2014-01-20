# db2rst - Convert DocBook to reStructuredText

This script was originally written by <wojdyr@gmail.com>.

*This version* was forked from <https://github.com/kurtmckee/db2rst>, which was forked from the original Google Code
sources at <https://code.google.com/p/db2rst/>.

There is also another fork of the original script by wojdyr here: <https://github.com/gerv/bzdocs/blob/master/db2rst.py>

## Installing the script

There are two ways to install db2rst:

* Use `pip` or `easy_install`. For example:

        pip install db2rst

* Download the source, unpack it, and run the setup script:

        python setup.py install

**Note**: depending on your system setup, you may need to run these commands as the *super-user*. If you're on Linux or
Mac OS X, add `sudo` before the install command. If you are installing via `pip`, for example, use:

    sudo pip install db2rst

## Using the script

The basic syntax for using the script is:

    db2rst *file1.xml* > *file1.rst*

Where *file1.xml* is the name of the DocBook file that you want to convert, and *file2* is the name of the file you want
to save the ReStructuredText in. If you leave off the `> file1.rst` bit, it'll just send the output to stdout, which may
be what you want...

