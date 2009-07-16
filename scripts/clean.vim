" replace utf-8 characters with ascii substitutes
%s/’/'/ge
%s/“/"/ge
%s/”/"/ge
%s/–/--/ge
%s/—/---/ge
%s/…/. . ./ge
%s/‘/'/ge
%s/Ç/C/ge
%s/ü/u/ge
%s/é/e/ge
%s/â/a/ge
%s/ä/a/ge
%s/à/a/ge
%s/ç/c/ge
%s/ê/e/ge
%s/ë/e/ge
%s/è/e/ge
%s/ï/i/ge
%s/î/i/ge
%s/ì/i/ge
%s/Ä/A/ge
%s/Å/A/ge
%s/É/E/ge
%s/æ/ae/ge
%s/Æ/fe/ge
%s/ô/o/ge
%s/ö/o/ge
%s/ò/o/ge
%s/û/u/ge
%s/ù/u/ge
%s/ÿ/y/ge
%s/Ö/O/ge
%s/Ü/U/ge
%s/á/a/ge
%s/í/i/ge
%s/ó/o/ge
%s/ú/u/ge
%s/ñ/n/ge
%s/Ñ/N/ge
%s/¿/?/ge
%s/Ó/O/ge

" remove leading spaces
%s/^\s\+//ge

" replace ellipses with ' . . . '
%s/\.\.\./ . . . /ge
%s/[ .]\{4,}/ . . . /ge

" ensure that -- and --- have surrounding spaces
%s/\([^-]\)\s*\(-\{2,3}\)\s*\([^-]\)/\1 \2 \3/ge
%s/\([^-]\)\s*\(-\{2,3}\)\s*$/\1 \2/ge
