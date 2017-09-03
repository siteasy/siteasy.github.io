from models import BasePlugin,MainView
class Plugin(BasePlugin):
    def apply(self,view):
        context = super(Plugin,self).apply(view)
        #print("inst:",MainView.instances)
        #print("all_list instance:",self.all_articles)
        mainview_list = sorted(self.all_articles, key=lambda k : k.date)
        article_list = [{'url':'/'+view.cateview.text+'/'+view.text+'.html','text':view.text,'short_md_content':view.short_md_content} for view in mainview_list]
        for area in self.areas:
            context[area]['context'].update({'article_list':article_list})
        return context
