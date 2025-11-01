import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestTextNode(unittest.TestCase):

    # HTMLNode Tests
    
    def test_props2html(self):
        props = {"href": "https://google.com", "target": "_blank"}
        node = HTMLNode("a", "Link to google", [], props)
        self.assertEqual(' href="https://google.com" target="_blank"', node.props_to_html())

    def test_repr(self):
        props = {"href": "https://google.com", "target": "_blank"}
        node = HTMLNode("a", "Link to google", [], props)
        self.assertEqual("HTMLNode(a, Link to google, [], {'href': 'https://google.com', 'target': '_blank'})", repr(node))

    # LeafNode Tests
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_link(self):
        props = {"href": "https://google.com", "target": "_blank"}
        node = LeafNode("a", "Click me!", props)
        self.assertEqual(node.to_html(), '<a href="https://google.com" target="_blank">Click me!</a>')

    def test_leaf_to_html_raw(self):
        node = LeafNode(None, "Here is some raw text")
        self.assertEqual(node.to_html(), "Here is some raw text")

    def test_leaf_value_error(self):
        node = LeafNode(None, None)
        self.assertRaises(ValueError, node.to_html)

    def test_leaf_to_html_emptyprop(self):
        props = {}
        node = LeafNode("p", "Empty prop", props)
        self.assertEqual(node.to_html(), "<p>Empty prop</p>")

    # ParentNode Tests

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()