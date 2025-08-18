
class HTMLNode:
    
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        to_string = ""
        if self.props:
            for p in self.props:
                to_string += p +'="'+ self.props[p] + '" '
        return to_string
    
    def __repr__(self):
        return f"Tag:{self.tag} Value:{self.value} Children:{self.children} Props:{self.props}"

