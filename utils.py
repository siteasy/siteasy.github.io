from settings import global_config,env
import re
import json
import time
import os
from collections import OrderedDict
import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html

class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)

def renderMD(md_in):
    renderer = HighlightRenderer()
    markdown = mistune.Markdown(renderer=renderer)
    return markdown(md_in)

def loadjson(fn,ordered_dict = True):
    f = open(fn)
    c = json.loads(f.read(),object_pairs_hook=OrderedDict)
    f.close()
    return c

def render(tpl,context):
    t = env.get_template(tpl) 
    return t.render(context)

def get_md_content(md_path):
    #print("md_file=%s"%md_path)
    f = open(md_path)
    lines = f.readlines()
    s = ''.join(lines)
    short_content = ''.join(lines[:10])
    p = r'\{[^}]*\}'
    m = re.search(p,s)
    if m:
        head = m.group(0)
        head_dict = json.loads(head)
        date = head_dict['date']
        content = s.replace(head,'')
        if global_config['add_date']:
            content += "\n %s"%date
        title = head_dict['title']
    else:
        date = time.ctime(os.stat(md_path).st_ctime)
        m = re.search(r'#(.+)',s)
        if m:
            title = re.search(r'#(.+)',s).group(1)
        else:
            title = ""
        if global_config['add_date']:
            content = s + "\n %s"%date
        else:
            content = s
    f.close()
    return content,short_content,title,date

