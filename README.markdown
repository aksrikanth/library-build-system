# E-Book Library Build System #

## PART I ##

### Introduction ###

This system is designed to store e-books in **plain text format** and to
generate readable html, pdf and other formats from it automatically. In
order to accomplish this, the text files need to be formatted appropriately.
The aim of this system is to ensure that the text is readable by itself and
that other formats build on the text document and add appropriate features.

Since the books are stored in UTF-8 encoded text, this is suitable only for
straight text. There is no provision for anything more than the most *simple*
formatting. It is possible, therefore that some books might require
preprocessing and might lose some formatting.

### Requirements ###

The following programs and libraries must be installed for proper
functioning of this system:

 1. python
 2. calibre (needed for mobibook and ePub)

On Ubuntu these may be installed by running

    # Run this on the command line
    $ sudo apt-get install python calibre

## PART II ##

### Books ###

All books to be built must be in UTF-8 encoded text and placed in the `mkd/`
folder. The books should be formatted in
[markdown](http://daringfireball.net/projects/markdown/).
See [their syntax page](http://daringfireball.net/projects/markdown/syntax)
to see how to format your books. You can also follow the example `0-Readme.mkd`
in the `mkd` folder.

Each book must contain on it's last line some metadata about the book in JSON
format. The minimum metadata required is `title` and `author`. In order to
prevent the metadata from appearing in the ebooks, it should be placed in an
html comment.

The possible metadata tags are:

 * `author-sort` :: String to be used when sorting by author.
 * `authors` :: Ampersand separated list of authors.
 * `comments` :: Comments about the books contents.
 * `isbn` :: ISBN of the published book.
 * `pubdate` :: Date of original publication.
 * `publisher` :: Publisher of the book.
 * `rating` :: Critical rating of the book (between 1 and 5).
 * `series` :: The name of the series to which the book belongs.
 * `series-index` :: The position of the book in the series.
 * `tags` :: Tags that describe the book (possibly for searching in the future).
 * `title` :: The title of the book.
 * `title-sort` :: The title of the book to be used for sorting.

For example, the last line of "The Adventures of Sherlock Holmes" would look
like:

    <!--{ "author-sort": "Arthur Conan Doyle", "authors": "Sir Arthur Conan +
    Doyle", "isbn": "987-0140621006", "pubdate": "1994-07-28", "publisher": +
    "Penguin Popular Classics", "series": "Sherlock Holmes Short Stories",  +
    "series-index": "1", "title": "The Adventures of Sherlock Holmes" }-->

### Usage ###

Run the python script `make.py` to generate all the formats from the markdown source.

    # Run this on the command line
    $ python make.py

<!--{ "authors": "Srikanth Agaram", "comments": "Manual for the e-book build system used to generate this ebook.", "title": "E-Book Library Build System" }-->
