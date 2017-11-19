# Author: Xavier Ashe
from cStringIO import StringIO
from htmllib import HTMLParser, HTMLParseError
from formatter import AbstractFormatter, DumbWriter
import sys, re, splunk.Intersplunk as si

def html2text(html):
    f = StringIO()
    parser = HTMLParser(AbstractFormatter(DumbWriter(f)))
    try:
        parser.feed(html)
    except HTMLParseError:
        return ''
    else:
        parser.close()
        return f.getvalue()

try:
    #keywords,options = si.getKeywordsAndOptions()
    #selectedField = options.get('field', None)
    del sys.argv[0]
    results,dummyresults,settings = si.getOrganizedResults()
    for result in results:
        for field, value in result.iteritems():
            if len(sys.argv) == 0:
                result[field] = html2text(value)
            elif field in sys.argv:
                result[field] = html2text(value)
except:
    import traceback
    stack =  traceback.format_exc()
    results = si.generateErrorResults("Error '%s'. %s" % (e, stack))
si.outputResults(results)
