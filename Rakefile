require 'rake/clean'
require 'yaml'

TXTFILES = FileList['mkd/*.mkd']
HTMLFILES = TXTFILES.gsub(/^mkd/, 'html').gsub(/mkd$/, 'html')
PDFFILES = TXTFILES.gsub(/^mkd/, 'pdf').gsub(/mkd$/, 'pdf')
PLUCKERFILES = TXTFILES.gsub(/^mkd/, 'plucker').gsub(/mkd$/, 'pdb')
MOBIFILES = TXTFILES.gsub(/^mkd/, 'mobi').gsub(/mkd$/, 'mobi')
EPUBFILES = TXTFILES.gsub(/^mkd/, 'epub').gsub(/mkd$/, 'epub')
LITFILES = TXTFILES.gsub(/^mkd/, 'lit').gsub(/mkd$/, 'lit')
PDBFILES = TXTFILES.gsub(/^mkd/, 'pdb').gsub(/mkd$/, 'pdb')
FB2FILES = TXTFILES.gsub(/^mkd/, 'fb2').gsub(/mkd$/, 'fb2')

CLOBBER.include(HTMLFILES)
CLOBBER.exclude('html/0-Readme.html')
CLOBBER.include(PDFFILES)
CLOBBER.exclude('pdf/0-Readme.pdf')
CLOBBER.include(PLUCKERFILES)
CLOBBER.exclude('plucker/0-Readme.pdb')
CLOBBER.include(MOBIFILES)
CLOBBER.exclude('mobi/0-Readme.mobi')
CLOBBER.include(EPUBFILES)
CLOBBER.exclude('epub/0-Readme.epub')
CLOBBER.include(LITFILES)
CLOBBER.exclude('lit/0-Readme.lit')
CLOBBER.include(PDBFILES)
CLOBBER.exclude('pdb/0-Readme.pdb')
CLOBBER.include(FB2FILES)
CLOBBER.exclude('fb2/0-Readme.fb2')

desc "Create html files only by default"
task :default => :html

desc "Create all formats from text"
task :all => [:html, :pdf, :plucker, :mobi, :epub, :lit, :pdb, :fb2]

desc "Create html ebooks from text"
task :html => HTMLFILES do
end

desc "Create pdf ebooks from html"
task :pdf => PDFFILES do
end

desc "Create plucker ebooks from html"
task :plucker => PLUCKERFILES do
end

desc "Create mobipocket ebooks from html"
task :mobi => MOBIFILES do
end

desc "Create ePub ebooks from html"
task :epub => EPUBFILES do
end

desc "Create MS LIT ebooks from html"
task :lit => LITFILES do
end

desc "Create e-reader ebooks from html"
task :pdb => PDBFILES do
end

desc "Create fb2 ebooks from html"
task :fb2 => FB2FILES do
end

def command(string, execute = true)
  puts string
  sh string if execute
end

def metadata(filename)
  metadata = YAML.load(`tail -n 1 "#{filename}"`)
end

rule('.html' => [
                proc do |name|
                  name.gsub(/^html/, 'mkd').gsub(/html$/, 'mkd')
                end
                ]) do |t|
  meta = metadata(t.source)
  command "sed '$d' \"#{t.source}\" | python scripts/markdown2.py | python scripts/toc.py \"#{meta[:title]}\" > \"#{t.name}\""
end

rule('.pdf' =>  [
                proc do |name|
                  name.gsub(/^pdf/, 'html').gsub(/pdf$/, 'html')
                end
                ]) do |t|
  command "html2ps \"#{t.source}\" | ps2pdf - > \"#{t.name}\""
end

rule('.pdb' =>  [
                proc do |name|
                  name.gsub(/^plucker/, 'html').gsub(/pdb$/, 'html')
                end
                ]) do |t|

  name = t.source.gsub(/^html\//, '').gsub(/\.html$/, '')
  command "plucker-build -P ./plucker -f \"#{name}\" \"#{t.source}\""
end

rule('.mobi' =>  [
                proc do |name|
                  name.gsub(/^mobi/, 'html').gsub(/mobi$/, 'html')
                end
                ]) do |t|
  meta = metadata(t.source.gsub(/^html/, 'mkd').gsub(/html$/, 'mkd'))
  command "ebook-convert \"#{t.source}\" \"#{t.name}\" --chapter '/' --max-toc-links 0 --level1-toc '//h2' --level2-toc '//h3' --title \"#{meta[:title]}\" --authors \"#{meta[:authors]}\" --cover \"#{t.source.gsub(/^html/, 'covers').gsub(/html$/, 'jpg')}\""
end

rule('.epub' =>  [
                proc do |name|
                  name.gsub(/^epub/, 'html').gsub(/epub$/, 'html')
                end
                ]) do |t|
  meta = metadata(t.source.gsub(/^html/, 'mkd').gsub(/html$/, 'mkd'))
  command "ebook-convert \"#{t.source}\" \"#{t.name}\" --chapter '/' --max-toc-links 0 --level1-toc '//h2' --level2-toc '//h3' --title \"#{meta[:title]}\" --authors \"#{meta[:authors]}\" --cover \"#{t.source.gsub(/^html/, 'covers').gsub(/html$/, 'jpg')}\""
end

rule('.lit' =>  [
                proc do |name|
                  name.gsub(/^lit/, 'html').gsub(/lit$/, 'html')
                end
                ]) do |t|
  meta = metadata(t.source.gsub(/^html/, 'mkd').gsub(/html$/, 'mkd'))
  command "ebook-convert \"#{t.source}\" \"#{t.name}\" --chapter '/' --max-toc-links 0 --level1-toc '//h2' --level2-toc '//h3' --title \"#{meta[:title]}\" --authors \"#{meta[:authors]}\" --cover \"#{t.source.gsub(/^html/, 'covers').gsub(/html$/, 'jpg')}\""
end

rule('.pdb' =>  [
                proc do |name|
                  name.gsub(/^pdb/, 'html').gsub(/pdb$/, 'html')
                end
                ]) do |t|
  meta = metadata(t.source.gsub(/^html/, 'mkd').gsub(/html$/, 'mkd'))
  command "ebook-convert \"#{t.source}\" \"#{t.name}\" --chapter '/' --max-toc-links 0 --level1-toc '//h2' --level2-toc '//h3' --title \"#{meta[:title]}\" --authors \"#{meta[:authors]}\" --cover \"#{t.source.gsub(/^html/, 'covers').gsub(/html$/, 'jpg')}\""
end

rule('.fb2' =>  [
                proc do |name|
                  name.gsub(/^fb2/, 'html').gsub(/fb2$/, 'html')
                end
                ]) do |t|
  meta = metadata(t.source.gsub(/^html/, 'mkd').gsub(/html$/, 'mkd'))
  command "ebook-convert \"#{t.source}\" \"#{t.name}\" --chapter '/' --max-toc-links 0 --level1-toc '//h2' --level2-toc '//h3' --title \"#{meta[:title]}\" --authors \"#{meta[:authors]}\" --cover \"#{t.source.gsub(/^html/, 'covers').gsub(/html$/, 'jpg')}\""
end
