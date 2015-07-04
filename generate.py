import markdown
import os

header = open('text/header.html').read()

for root, dirs, files in os.walk("text"):
    for thefile in files:
        if(not thefile.endswith('.md')):
            continue
        print(thefile)
        with open("text/%s" % thefile) as entry:
            html = markdown.markdown(entry.read())
            with open("text/%s" % thefile.replace('.md', '.html'), 'w') as htmlFile:
                htmlFile.write(header)
                htmlFile.write(html)