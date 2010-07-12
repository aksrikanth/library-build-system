import sys
import getopt
from BeautifulSoup import BeautifulSoup, Tag, NavigableString

class Toc:

  def __init__(self, title, options):
    # defaults
    self.infile = sys.stdin
    self.outfile = sys.stdout
    self.tag_names = ['h2', 'h3', 'h4']
    self.toc_id = 'auto_toc'
    self.name_prefix = 'section'
    self.title = title

    # options
    for option, value in options:
      if option in ('-h', '--help'):
        usage()
        sys.exit()
      elif option in ('-t', '--tags'):
        self.tag_names = value.split(',')
      elif option in ('-i', '--infile'):
        self.infile = open(value, 'r')
      elif option in ('-o', '--outfile'):
        self.outfile = open(value, 'w')

    # process the html, create toc and print
    self.get_tags()
    self.id_tags()
    self.create_toc()
    self.output()

    # clean up
    self.infile.close()
    self.outfile.close()

  def get_tags(self):
    self.soup = BeautifulSoup(self.infile.read())

    # check if there is an existing toc
    toc = self.soup.findAll(id=self.toc_id)
    for tag in toc:
      tag.extract()

    # check which of the mentioned tags are present
    tag_names = []
    for tag_name in self.tag_names:
      tag_list = self.soup.findAll(tag_name)
      if len(tag_list) != 0 and len(tag_names) < 2:
        tag_names.append(tag_name)
    self.tag_names = tag_names

    # get tags
    self.tag_list = self.soup.findAll(self.tag_names)

  def id_tags(self):
    counts = []
    self.toc_list = []
    for item in self.tag_names:
      counts.append(0)
    for tag in self.tag_list:
      reset = False
      for index, tag_name in enumerate(self.tag_names):
        if reset == True:
          counts[index] = 0
        if tag.name == tag_name:
          depth = index
          counts[index] += 1
          reset = True

      name = self.name_prefix
      for count in counts:
        if count == 0:
          break
        name = '%s_%i' % (name, count)

      tag['id'] = name
      self.toc_list.append({ 'depth': depth, 'id': name, 'title': tag.text })

  def create_toc(self):
    # lists will hold the last ol/ul elements at each depth
    lists = []

    # setup the toc container
    toc = Tag(self.soup, 'div')
    toc['id'] = self.toc_id
    last_li = toc
    header = Tag(self.soup, 'h2')
    header_title = NavigableString('Contents')
    header.append(header_title)
    toc.append(header)

    for toc_item in self.toc_list:
      depth = toc_item['depth']
      if len(lists) ==  depth: # this is the first time we're at this depth
        list_el = Tag(self.soup, 'ol')
        lists.append(list_el)
        last_li.append(list_el)

      elif depth > old_depth: # this is a new sub-tree
        list_el = Tag(self.soup, 'ol')
        lists[depth] = list_el
        last_li.append(list_el)

      old_depth = depth

      # set up the new item
      li = Tag(self.soup, 'li')
      a = Tag(self.soup, 'a')
      title = NavigableString(toc_item['title'])
      a.append(title)
      a['href'] = '#%s' % (toc_item['id'])
      li.append(a)
      lists[depth].append(li)
      last_li = li

    # insert the toc at the top of the html
    self.soup.insert(0, toc)

  def output(self):
    prefix = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
	<title>%s</title>
</head>
<body>
    """ % (self.title)
    suffix = """
    </body>
    </html>
    """
    self.outfile.write(prefix)
    self.outfile.write(self.soup.prettify())
    self.outfile.write(suffix)

def parse_opts(args):
  try:
    opts, args = getopt.getopt(args, 'ht:i:o:', ['help', 'tags', 'infile', 'outfile'])
  except getopt.GetoptError, err:
    sys.stderr.write(str(err))
    usage()
    sys.exit(2)
  return ' '.join(args), opts

def usage():
  name = sys.argv[0]
  print ''
  print 'usage: ',name,' [options]'
  print 'options:'
  print '  -h, --help ::'
  print '    show this help message'
  print '  -t, --tags ::'
  print '    comma separated list of tags to put in the table of contents'
  print '    e.g. h2,h3'
  print '  -i, --infile ::'
  print '    (X)HTML file input to generate TOC for (default is stdin).'
  print '  -o, --outfile ::'
  print '    file to send output to (default is stdout)'

if __name__ == '__main__':
  title, options = parse_opts(sys.argv[1:])
  toc = Toc(title, options)
