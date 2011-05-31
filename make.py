import glob
import json
import os.path
import subprocess
import sys
import re

class color:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'

  def disable(self):
    self.HEADER = ''
    self.OKBLUE = ''
    self.OKGREEN = ''
    self.WARNING = ''
    self.FAIL = ''
    self.ENDC = ''

def execute_command(command, logfile, debug):
  print '%(color_start)s%(command)s%(color_end)s\n\n' % {
      'color_start': color.OKBLUE, 'command': command, 'color_end': color.ENDC}
  if not debug:
    logfile.write('%(command)s\n' % {'command': command})
    logfile.write('\n*** start:\n')
    proc = subprocess.Popen(command, shell=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
    while (proc.poll() is None):
      logfile.write(proc.stdout.read())
      logfile.flush()
    logfile.write('\n*** end\n\n')
    logfile.flush()
    if proc.returncode != 0:
      print proc.returncode
      print '%(color_start)s%(message)s%(color_end)s\n' % {
          'color_start': color.FAIL, 'message': '**Error**',
          'color_end': color.ENDC}

def get_metadata(basename, formats):
  filename = get_filename_from_basename(basename, 'mkd', formats)
  proc = subprocess.Popen(
      ['tail', '-1', filename],
      stdout=subprocess.PIPE)
  data = proc.communicate()[0]
  pattern = re.compile(r'(^<!--|-->$)')
  data = pattern.sub('', data)
  return json.loads(data)

def get_filename_from_basename(basename, format, formats):
  format_data = formats.get(format, None)
  if format_data is None:
    raise Exception('Unknown format: %(format)s' % {'format': format})
  return '%(format)s/%(basename)s.%(extension)s' % {'format': format,
      'extension': format_data['extension'], 'basename': basename }

def get_basename_from_filename(filename):
  pattern = re.compile(r'(^.*/|\..*$)')
  return pattern.sub('', filename)

def get_modified_basenames(source_format, target_format, formats):
  source_data = formats.get(source_format, None)
  if source_data is None:
    raise Exception('Unknown format: %(format)s' % {'format': source_format})
  source_files = glob.glob('%(format)s/*.%(extension)s' % {
      'format': source_format, 'extension': source_data['extension']})
  source_files.sort()
  target_files = [
      get_filename_from_basename(
        get_basename_from_filename(fn), target_format, formats)
      for fn in source_files ]

  modified_basenames = []

  for (source, target) in zip(source_files, target_files):
    if os.path.isfile(target):
      if os.path.getmtime(source) > os.path.getmtime(target):
        modified_basenames.append(get_basename_from_filename(source))
    else:
      modified_basenames.append(get_basename_from_filename(source))

  return modified_basenames

def markdown_command(source, target, metadata, defaults):
  return '''python scripts/markdown2.py --encoding="UTF-8" -x smarty-pants "%(source)s" | \
      python scripts/toc.py "%(title)s" > "%(target)s" ''' % {
          'source': source,
          'target': target,
          'title': metadata['title']}

def calibre_command(source, target, metadata, defaults):
  copy = defaults.copy()
  copy.update(metadata)
  metadata = copy
  command_list = ['ebook-convert',
      '"%(source)s"' % {'source': source},
      '"%(target)s"' % {'target': target}]

  for option, value in metadata.items():
    if value is None:
      del metadata[option]
    else:
      command_list.append(
          '--%(option)s="%(value)s"' % {'option': option, 'value': value})

  return ' '.join(command_list)

def build_commands(formats, target_formats, defaults, logfilename):
  logfile = open(logfilename, 'a')
  for target_format in target_formats:
    format_data = formats.get(target_format, None)
    if format_data is None:
      raise Exception('Unknown format: %(format)s' % {'format': target_format})

    source_format = format_data['source']
    target_basenames = get_modified_basenames(source_format, target_format, formats)
    for target_basename in target_basenames:
      source = get_filename_from_basename(target_basename, source_format, formats)
      target = get_filename_from_basename(target_basename, target_format, formats)
      metadata = get_metadata(target_basename, formats)
      command = format_data['generator'](source, target, metadata, defaults)
      execute_command(command, logfile, False)
  logfile.close()

ebook_formats = {
    'mkd':   {'extension': 'mkd'},
    'cover': {'extension': 'jpg'},
    'html':  {'extension': 'html', 'source': 'mkd',  'generator': markdown_command},
    'epub':  {'extension': 'epub', 'source': 'html', 'generator': calibre_command},
    'fb2':   {'extension': 'fb2',  'source': 'html', 'generator': calibre_command},
    'lit':   {'extension': 'lit',  'source': 'html', 'generator': calibre_command},
    'mobi':  {'extension': 'mobi', 'source': 'html', 'generator': calibre_command},
    'pdb':   {'extension': 'pdb',  'source': 'html', 'generator': calibre_command},
    'pdf':   {'extension': 'pdf',  'source': 'html', 'generator': calibre_command},
    }

ebook_targets = ['html', 'epub', 'fb2', 'lit', 'mobi', 'pdb', 'pdf']

default_metadata = {
  'extra-css': 'scripts/ebooks.css',
  'smarten-punctuation': None,
  'language': 'english',
  'no-svg-cover': None,
  'preserve-cover-aspect-ratio': None,
  'chapter': '/', # Disable chapter detection
  'max-toc-links': 0,
  'level1-toc': '//h2',
  'level2-toc': '//h3',
}

build_commands(ebook_formats, ebook_targets, default_metadata, 'output.log')
