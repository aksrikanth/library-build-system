#!/usr/bin/env ruby

# == Synopsis
# toc : Generate a table of contents for an html file and append it to the top of the file.
#
# == Usage
#
# toc [OPTIONS]
#
# -h, --help ::
#   show this help message
# -t, --tags ::
#   comma separated list of tags to put in the table of contents
#   e.g. h2,h3
# -i, --infile ::
#   (X)HTML file input to generate TOC for (default is stdin).
# -o, --outfile ::
#   file to send output to (default is stdout)
#
# == Author
#
# Srikanth K Agaram (code at srikanthak dot name)
#
# == Copyright
#
# Copyright (c) 2009 Srikanth Agaram. Licensed under GNU GPLv3

require 'rdoc/usage'
require 'getoptlong'

require 'rubygems'
require 'builder'
require 'hpricot'

# Tree implementation to store the table of contents {{{
class TreeNode
  attr_accessor :parent, :depth, :data, :children

  def initialize(data)
    @data = data
    @parent = nil
    @children = []
  end

  def append(child)
    child.parent = self
    children.push child
  end

  def prefix_traverse(depth, &block)
    yield self
    children.each { |child| child.prefix_traverse(depth + 1, &block) }
  end

  def index
    @parent.children.index(self) + 1
  end

  def position
    if @parent.nil?
      []
    else
      @parent.position.push index
    end
  end

  def path
    position.join('_')
  end

  def depth
    if @parent.nil?
      0
    else
      @parent.depth + 1
    end
  end
end

class Tree
  attr_accessor :root

  def initialize(node)
    @root = node
  end

  def prefix_traverse(&block)
    @root.prefix_traverse(0, &block)
  end
end

# Example of building and traversing a tree {{{
# root = TreeNode.new('root')
# a = TreeNode.new('a')
# b = TreeNode.new('b')
# c = TreeNode.new('c')
# d = TreeNode.new('d')
# e = TreeNode.new('e')
# f = TreeNode.new('f')
# g = TreeNode.new('g')
# h = TreeNode.new('h')
# i = TreeNode.new('i')
# j = TreeNode.new('j')
# k = TreeNode.new('k')

# root.append(a)
# root.append(b)
# root.append(c)
# a.append(d)
# a.append(e)
# b.append(f)
# c.append(g)
# c.append(h)
# d.append(i)
# d.append(j)
# d.append(k)

# tree = Tree.new(root)

# tree.prefix_traverse do |depth, data|
#   depth.times do
#     print '.'
#   end
#   puts data
# end
# }}}

# }}}

# Table of contents extractor {{{
class Toc
  def initialize(options)
    default_options = {
      :tags => ['h2', 'h3'],
    }

    options = default_options.merge(options)

    if options[:infile].nil?
      @document = Hpricot $stdin
    else
      @document = Hpricot open(options[:infile])
    end

    @tags_list = options[:tags]
    @parent = gen_parent_hash

    @prefix = 'section_'

    output = gen_html
    if options[:outfile].nil?
      puts output
    else
      File.open(options[:outfile], 'w') do |file|
        file.write html
      end
    end
  end

  private

  # Helper functions {{{
  def gen_html
    # remove the old TOC if present
    @document.search('#toc-toc').remove

    # generate the TOC tree
    toc_tree = gen_toc_tree

    # add anchors to the TOC tree nodes
    add_toc_anchors(toc_tree)

    # generate the TOC html
    x = Builder::XmlMarkup.new(:indent => 2)
    x.div(:id => 'toc-toc') do
      x.h2 "Table of Contents"
      gen_toc_html(x, toc_tree.root)
    end

    # insert the TOC into the html
    @document.search('body').prepend(x.target!)

    # return the modified html
    @document.to_html
  end

  def gen_toc_tree
    elements = find_tags
    current_node = {}
    @tags_list.each { |tag| current_node[tag] = nil }

    toc_tree = Tree.new(TreeNode.new('root'))
    elements.each do |element|
      name = element.name.downcase
      new_node = TreeNode.new(element)
      current_node[name] = new_node

      if @parent[name].nil?
        toc_tree.root.append(new_node)
      else
        current_node[@parent[name]].append(new_node)
      end
    end

    toc_tree
  end

  def find_tags
    elements = @document.search("body//*").select do |e|
      result = false
      if e.methods.include? "name"
        result = @tags_list.include? e.name
      end
      result
    end

    elements
  end

  def add_toc_anchors(toc_tree)
    toc_tree.prefix_traverse do |node|
      unless node.parent.nil?
        # save the contents of the element
        html = node.data.inner_html

        # create the anchor element that will be linked to in the TOC
        anchor = Builder::XmlMarkup.new(:indent => 2)
        anchor.a(html, :name => @prefix + node.path)

        # insert the anchor into the element
        node.data.inner_html = anchor.target!
      end
    end
  end

  def gen_toc_html(builder, node)
    unless node.children.empty?
      builder.ul do
        node.children.each do |child|
          builder.li do
            builder.a(child.data.inner_text, :href => "##{@prefix}#{child.path}")
            gen_toc_html(builder, child)
          end
        end
      end
    end
  end

  def gen_parent_hash
    current = nil
    parent = {}
    @tags_list.each do |tag|
      parent[tag] = current unless current.nil?
      current = tag
    end

    parent
  end
  # }}}

end
# }}}

# Extract command line options {{{
options = {}

opts = GetoptLong.new(
        ['--help', '-h', GetoptLong::OPTIONAL_ARGUMENT],
        ['--tags', '-t', GetoptLong::OPTIONAL_ARGUMENT],
        ['--infile', '-i', GetoptLong::OPTIONAL_ARGUMENT],
        ['--outfile', '-o', GetoptLong::OPTIONAL_ARGUMENT]
                     )

opts.each do |opt, arg|
  case opt
  when '--help'
    case arg
    when /^u/i
      RDoc::usage('Usage')
    when /^a/i
      RDoc::usage('Author')
    when /l|c/i
      RDoc::usage('Copyright')
    else
      RDoc::usage
    end

  when '--tags'
    options[:tags] = arg.split(',')

  when '--infile'
    options[:infile] = arg

  when '--outfile'
    options[:outile] = arg
  end
end
# }}}

toc = Toc.new(options)
