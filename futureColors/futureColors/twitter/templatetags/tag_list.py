from django.template import Library, Node     
register = Library()

class timeline(Node):
    def __init__(self, parser, token):
        bits = token.contents.split()
        self.timelineName = bits[1]

    def render(self, context):
        render = self.printTimeline(context[self.timelineName])
        return render
    
    def printTimeline(self, timeline):
        result = ''
        tmp = ''
        for status in timeline:
            if len(status) == 0:
                return ''
            if len(status) > 1:
                tmp = self.printTimeline(status[1])
            result += ('<div class=twit>%s: %s %s</div>' % (status[0].author.screen_name,status[0].text, tmp))
        return result
    
    
    
timeline = register.tag('timeline', timeline)
