import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_eq_link(self):
        node = TextNode("This is a link", TextType.LINK, "https://google.com")
        node2 = TextNode("This is a link", TextType.LINK, "https://google.com")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is node", TextType.ITALIC_TEXT)
        node2 = TextNode("This is node2", TextType.ITALIC_TEXT)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()