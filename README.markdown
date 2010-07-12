# E-Book Library Build System

## PART I

### Introduction

This system is designed to store e-books in **plain text format** and to
generate readable html, pdf and other formats from it automatically. In
order to accomplish this, the text files need to be formatted appropriately.
The aim of this system is to ensure that the text is readable by itself and
that other formats build on the text document and add appropriate features.

Since the books are stored in plain text, this is suitable only for _ASCII
prose_. There is no provision for anything more than the most *simple*
formatting. It is possible, therefore that some books might require
preprocessing and might lose some formatting.

### Requirements

The following programs and libraries must be installed for proper
functioning of this system:

 1. python
 2. ruby
 3. rubygems
 4. rake gem
 5. html2ps (needed for pdf)
 6. ps2pdf (needed for pdf. may be packaged with the ghostscript package)
 7. plucker (needed for plucker)
 8. calibre (needed for mobibook and ePub)

On Ubuntu these may be installed by running

    # Run this on the command line
    $ sudo apt-get install python ruby html2ps ghostscript plucker calibre

I recommend installing the latest version of rubygems from it's source by
following the instructions [here](http://rubygems.org/read/chapter/3).

Then the gems can be installed by running

    # Run this on the command line
    $ sudo gem install rake

## PART II

### Books

All books to be built must be in plain text format and placed in the `txt/`
folder. The books may be formatted in [markdown](http://daringfireball.net/projects/markdown/).
See [their syntax page](http://daringfireball.net/projects/markdown/syntax) to see how to format
your books. You can also follow the example `0-Readme.txt` in the `txt` folder.

### Usage

Use the following `rake` command to see what formats can be built.

    # Run this on the command line
    $ rake -T

For example to build kindle compatible '.mobi' files do

    # Run this on the command line
    $ rake mobi

{ :authors: "Srikanth Agaram", :title: "E-Book Library Build System" }
