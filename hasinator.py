"""
Python file hashing utility

Scoring
=====================
  Required (100)
  -------------
    * Recurses files from path given on commandline
    * Hashes file contents to md5
    * Gives intuitive output linking filename to hash
    * Git commit history shows at least one commit from each team member

  Bonus
  --------------
    * (5) File/folder exclusion support
    * (5) File/folder exclusion by wildcards
    * (10) Support configurable hash algorithms
    * (5) Support multiple output encodings (base64, hex, etc.)
    * (5) Support output types (stdout, file, xml, etc.)
    * (5) Output other file information (file-size, modify-time, etc.)
    * (5) Show progress in console
    * (5) Verify single file with known hash
    * (10) Write a generator function
    * (10) Pass a function as an argument

  Next-step
  --------------
    * (50) Reading from output file to compare against files on disk
    * (10) Read from a standard hash file, autodetect hashtype (.md5sum)
  
"""
import os, optparse

class Program(object):

    def go(self):
        "Main entry of the software"
        # TODO: Parse command-line arguments
        #       Configure hashing and output algorithms
        #       Recurse through the filesystem, honoring exclusions
        #       Output the resulting hash

    def walk(self, path):
        """
        Walk through the filesystem and hash each of the files. Python
        includes a function to recurse through a filesystem folder
        structure. You can read about os.walk at
        http://docs.python.org/library/os.html#os.walk
        """
        for root, dirs, files in os.walk(path):
            # Remove items from dirs you don't want to recurse into
            pass

    def output(self, path, hash):
        "Write the file hash data to the output"

class Options(object):

    def __init__(self):
        """
        Parse the options from the command line. Raise and error or call
        sys.exit() upon failure. Python has full support for command-line
        options parsing built in. You can find a write-up about it at
        http://docs.python.org/library/optparse.html
        """
        parser = optparse.OptionParser()
        # Add options to the parser here

        self.options, self.args = parser.parse_args()

    def is_excluded(self, path):
        "Determine if the path was excluded from the commandline"

    def initial_path(self):
        "Return the initial path for the hashing"

    def recurse(self):
        "True if the software should recurse through folders"

    def hash_type(self):
        "Return hash function option"

    def output_type(self):
        "Return the output format type"

class Hasher(object):

    def __init__(self, func, output):
        """
        Initialize the hashing function here. Python has built-in hashing
        functions that are oulined at
        http://docs.python.org/library/hashlib.html, and built-in
        encoding functions that are outlined at
        http://docs.python.org/library/codecs.html. Strings can be
        directly encoded using the ::encode() method. An example of this
        technique is outlined at
        http://www.tutorialspoint.com/python/string_encode.htm
        """

    def hash_for(self, filename):
        "Hashes the file referenced by filename and formats the result"

if __name__ == '__main__':
    Program().go()
