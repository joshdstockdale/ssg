import unittest

from htmlnode import (
    HTMLNode,
    LeafNode,
    ParentNode,
)


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(
            "a",
            "Link Text",
            None,
            {"class": "me-class", "href": "https://me.com"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="me-class" href="https://me.com"'
        )

    def test_leaf(self):
        node = LeafNode(
            "a",
            "Link Text",
            {"class": "me-class", "href": "https://me.com"},
        )
        self.assertEqual(
            node.to_html(),
            '<a class="me-class" href="https://me.com">Link Text</a>'
        )
        node = LeafNode(
            None,
            "Link Text",
            {"class": "me-class", "href": "https://me.com"},
        )
        self.assertEqual(
            node.to_html(),
            'Link Text'
        )
        node = LeafNode(
            "a",
            "Link Text",
        )
        nodeValError = LeafNode(
            None,
            None,
        )
        self.assertEqual(
            node.to_html(),
            '<a>Link Text</a>'
        )
        with self.assertRaises(ValueError):
            nodeValError.to_html()

    def test_parent(self):
        node = ParentNode(
            "p", 
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        )


if __name__ == "__main__":
    unittest.main()
