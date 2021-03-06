#!/usr/bin/python

import sys
sys.path.append('/home/jumblesale/Code/roster/markdown')

import markdown
import os

header = open('html/header.html').read()
footer = open('html/footer.html').read()
index  = open('episodes/index.html', 'w')

index.write(header)
index.write('<h1>~jumblesale plays ksp</h1>')
index.write('<ul>')

discoveredFiles = []

for root, dirs, files in os.walk("text"):
    for i, thefile in enumerate(files):
        if(not thefile.endswith('.md')):
            continue
        print(thefile)
        discoveredFiles.append(thefile)

discoveredFiles.sort()

for i, thefile in enumerate(discoveredFiles):
    with open("text/%s" % thefile) as entry:
        title = thefile.replace('.md', '.html')
        html  = markdown.markdown(entry.read())
        with open("episodes/%d.html" % (i + 1), 'w') as htmlFile:
            htmlFile.write(header)
            htmlFile.write(html)
            htmlFile.write(footer)

            index.write('<li><a href="%d.html">%s</a></li>' % (i + 1, title))

index.write('</ul></body></html>')
