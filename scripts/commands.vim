" Use the command to convert from PDF to text
" pdftotext -layout -nopgbrk "$f"
"
" prepend all indented lines with a newline
g/^\s\s*\S/norm O
" collapse multiple blank lines
%s/\n\{3,}/\r\r/e
" remove leading whitespace
%s/^\s*//g
" make lowercase sentence into title case
" '<,'>s/\w*/\u&/g
"
" join chapter number and name into one line and underline. Transform upper
" case to title case.
" e.g.
" > CHAPTER ONE
" >
" > THE OTHER MINISTER'S SON
"
" is converted to
" > Chapter One : The Other Minister'S Son
" > --------------------------------------
"
" note that the letter following the apostrophe is (erroneously) upper case
map t A :JJVuyypVr-kV:s/\w*/\u&/g
" apply above mapping to all lines that start with CHAP
g/^CHAP/norm t
" replace some unicode characters with ascii equivalents -- see utf8.vim
" After cleaning up text file use
" txt2html -tf --xhtml --nomake_links --noanchors <txt-file> | ./toc.rb > <html-file>
