# E-Book Library Build System #

## PART I ##

### Introduction ###

This system is designed to store e-books in **plain text format** and to
generate readable html, pdf and other formats from it automatically. In
order to accomplish this, the text files need to be formatted appropriately.
The aim of this system is to ensure that the text is readable by itself and
that other formats build on the text document and add appropriate features.

Since the books are stored in plain text, this is suitable only for _ASCII
prose_. There is no provision for anything more than the most *simple*
formatting. It is possible, therefore that some books might require
preprocessing and might lose some formatting.

### Requirements ###

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

## PART II ##

### Books ###

All books to be built must be in plain text format and placed in the `mkd/`
folder. The books may be formatted in [markdown](http://daringfireball.net/projects/markdown/).
See [their syntax page](http://daringfireball.net/projects/markdown/syntax) to see how to format
your books. You can also follow the example `0-Readme.mkd` in the `mkd` folder.

### Usage ###

Use the following `rake` command to see what formats can be built.

    # Run this on the command line
    $ rake -T

For example to build kindle compatible '.mobi' files do

    # Run this on the command line
    $ rake mobi

{ "author-sort": "Srikanth Agaram", "authors": "Srikanth Agaram", "book-producer": "Srikanth Agaram", "comments": "Manual for the e-book build system used ot generate this ebook", "isbn": "unknown", "pubdate": "draft", "title": "E-Book Library Build System" }
#    --publisher
#    Set the ebook publisher.
#    --rating
#    Set the rating. Should be a number between 1 and 5.
#    --series
#    Set the series this ebook belongs to.
#    --series-index
#    Set the index of the book in this series.
#    --tags
#    Set the tags for the book. Should be a comma separated list.
#    --title
#    Set the title.
#    --title-sort
#    The version of the title to be used for sorting.
#    --no-svg-cover
#    Do not use SVG for the book cover. Use this option if your EPUB is going to be used on a device that does not support SVG, like the iPhone or the JetBook Lite. Without this option, such devices will display the cover as a blank page.
#    --preserve-cover-aspect-ratio
#    When using an SVG cover, this option will cause the cover to scale to cover the available screen area, but still preserve its aspect ratio (ratio of width to height). That means there may be white borders at the sides or top and bottom of the image, but the image will never be distorted. Without this option the image may be slightly distorted, but there will be no borders.
