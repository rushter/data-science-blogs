import re
import html

xmlbody = """<?xml version="1.0" encoding="UTF-8"?>
<!-- Created by generate_opml.py, please don't edit manually. -->
<opml version="1.0">
    <head>
        <title>Data science blogs</title>
    </head>
    <body>
        <outline text="Data science blogs" title="Data science blogs">
{items}
        </outline>
    </body>
</opml>
    """
xmlitem = '<outline type="rss" text="{title}" title="{title}" ' \
          'xmlUrl="{rssfeed}" htmlUrl="{httpfeed}"/>'

readme = open('README.md').read()
blogs = re.findall('\* (.*?) http([s]{0,1})\:\/\/(.*?) \[\(RSS\)\] \((.*?)\)', readme)

items = ''
for blog in blogs:
    item = xmlitem.format(title=html.escape(blog[0].strip()),
                          httpfeed='http{0}://{1}'.format(blog[1].strip(), blog[2].strip()),
                          rssfeed=blog[3].strip())
    items += '\t\t\t{}\r\n'.format(item)

open('data-science.opml', 'w').write(xmlbody.format(items=items[0:-2]))
