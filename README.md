# db2rst - Convert Docbook to ReStructuredText


This script was originally written by <wojdyr@gmail.com>.

*This version* is forked from <https://github.com/kurtmckee/db2rst>, which was forked from the original Google Code
sources at <https://code.google.com/p/db2rst/>.

## Using the Script

To use it, you must first have `lxml` installed. The easiest way to get it, in my opinion, is to use `pip`:

    pip install lxml

Once you've done that, you should be able to run the script by running it with Python:

    python *file1.xml* > *file1.rst*

Where *file1.xml* is the name of the DocBook file that you want to convert, and *file2* is the name of the file you want
to save the ReStructuredText in. If you leave off the `> file1.rst` bit, it'll just send the output to stdout, which may
be what you want...

