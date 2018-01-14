from settings import global_config,env
import re
import json
import time
import os
from collections import OrderedDict
import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter 
from dateutil import parser

#class HighlightRenderer(mistune.Renderer):
#    def block_code(self, code, lang):
#        if not lang:
#            return '\n<pre><code>%s</code></pre>\n' % \
#                mistune.escape(code)
#        lexer = get_lexer_by_name(lang, stripall=True)
#        print(lang,lexer)
#        formatter = html.HtmlFormatter(noclasses=inlinestyles, linenos=linenos)
#        return highlight(code, lexer, formatter)

def block_code(text, lang, inlinestyles=False, linenos=False):
    if not lang:
        text = text.strip()
        return u'<pre><code>%s</code></pre>\n' % mistune.escape(text)

    try:
        lexer = get_lexer_by_name(lang, stripall=True)
        #print(lexer)
        formatter = HtmlFormatter(
            noclasses=inlinestyles, linenos=linenos
        )
        #print(formatter)
        code = highlight(text, lexer, formatter)
        #print(code)
        if linenos:
            return '<div class="highlight-wrapper">%s</div>\n' % code
        return code
    except:
        return '<pre class="%s"><code>%s</code></pre>\n' % (
            lang, mistune.escape(text)
        )


class HighlightRender(mistune.Renderer):
    def block_code(self, text, lang):
        # renderer has an options
        #inlinestyles = self.options.get('inlinestyles', True)
        #linenos = self.options.get('linenos', True)
        return block_code(text, lang, True, True)

def renderMD(md_in):
    renderer = HighlightRender()
    markdown = mistune.Markdown(renderer=renderer)
    return markdown(md_in)

def loadjson(fn,ordered_dict = True):
    f = open(fn)
    c = json.loads(f.read(),object_pairs_hook=OrderedDict)
    f.close()
    return c

def render(tpl,context):
    #print(env.loader.list_templates())
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
        date = parser.parse(head_dict['date'])
        content = s.replace(head,'')
        if global_config['add_date']:
            content += "\n---\n %s"%date
        title = head_dict['title']
    else:
        date = time.ctime(os.stat(md_path).st_ctime)
        m = re.search(r'#(.+)',s)
        if m:
            title = re.search(r'#(.+)',s).group(1)
        else:
            title = ""
        if global_config['add_date'] and os.path.splitext(md_path)[0][-5:] != 'index':
            content = s + "\n %s"%date
        else:
            content = s
    f.close()
    return content,short_content,title,date

def select_link_one_layer(site_map,id):
    for k,v in site_map.items():
        pass


