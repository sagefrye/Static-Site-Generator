import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_link(self):
        node = TextNode("This is a link", TextType.LINK, "https://google.com")
        node2 = TextNode("This is a link", TextType.LINK, "https://google.com")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is node", TextType.ITALIC)
        node2 = TextNode("This is node2", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.LINK, "https://google.com")
        self.assertEqual("TextNode(This is a text node, link, https://google.com)", repr(node))

if __name__ == "__main__":
    unittest.main()