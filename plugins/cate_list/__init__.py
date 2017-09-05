from siteasy import BasePlugin
class Plugin(BasePlugin):
    def apply(self,view):
        context = super(Plugin,self).apply(view)
        if view.classname == 'CateView':
            if len(view.mainviews) == 0:
                return {}
            else:
                article_list = view.article_list
        for area in self.areas:
            context[area]['context'].update({'article_list':article_list})
        return context
