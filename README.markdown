# E-Book Library Build System

## PART I

### Introduction

This system is designed to store e-books in #plain text format# and to
generate readable html, pdf and other formats from it automatically. In
order to accomplish this, the text files need to be formatted appropriately.
The aim of this system is to ensure that the text is readable by itself and
that other formats build on the text document and add appropriate features.

Since the books are stored in plain text, this is suitable only for _ASCII
prose_. There is no provision for anything more than the most *simple*
formatting. It is possible, therefore that some books might require
preprocessing and might lose some formatting. Accented characters are not
supported at this time.

### Requirements

The following programs and libraries must be installed for proper
functioning of this system:

 1. txt2html
 2. ruby
 3. rubygems
 4. hpricot gem
 5. builder gem
 6. rake gem
 6. html2ps
 7. ps2pdf (may be packaged with the ghostscript package)
 8. plucker

On Ubuntu these may be installed by running

        # Run this on the command line
        $ sudo apt-get install txt2html ruby html2ps ghostscript plucker

I recommend installing the latest version of rubygems from it's source by
following the instructions here : http://rubygems.org/read/chapter/3

Then the gems can be installed by running

        # Run this on the command line
        $ sudo gem install hpricot builder rake

## PART II

### Usage

{ :authors: "Srikanth K Agaram", :title: "E-Book Library Build System" }
