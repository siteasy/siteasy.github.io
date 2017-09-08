from siteasy import BasePlugin
class Plugin(BasePlugin):
    def apply(self,view):
        context = super(Plugin,self).apply(view)
        article_list = view.site_map['sub']
        for area in self.areas:
            context[area]['context'].update({'article_list':article_list})
        return context
