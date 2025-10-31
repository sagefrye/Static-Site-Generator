import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    
    def test_props2html(self):
        props = {"href": "https://google.com", "target": "_blank"}
        node = HTMLNode("a", "Link to google", None, props)
        self.assertEqual('href="https://google.com" target="_blank" ', node.props_to_html())

    def test_repr(self):
        props = {"href": "https://google.com", "target": "_blank"}
        node = HTMLNode("a", "Link to google", None, props)
        self.assertEqual("HTMLNode(a, Link to google, None, {'href': 'https://google.com', 'target': '_blank'})", repr(node))

if __name__ == "__main__":
    unittest.main()