from browser import RelationshipBrowser


class Research:
    """Research class that finds relationships using the RelationshipBrowser abstraction"""
    
    def __init__(self, browser):
        """
        Initialize Research with a RelationshipBrowser object.
        
        Args:
            browser: An object implementing RelationshipBrowser interface
        
        Note: Research depends on the abstraction (RelationshipBrowser), not on 
        concrete implementation details. It doesn't know or care how the data is stored.
        """
        self.browser = browser
        self._find_johns_children()
    
    def _find_johns_children(self):
        """Find and print all of John's children"""
        for child in self.browser.find_all_children_of("John"):
            print(f"John has a child called {child.name}")
