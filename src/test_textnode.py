import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    split_nodes_delimiter,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_text)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_text)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("Ahis is a text node", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode(
            "This is a text node", text_type_bold, "https://me.com"
        )
        node2 = TextNode(
            "This is a text node", text_type_bold, "https://me.com"
        )
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", text_type_bold, "https://me.com")
        self.assertEqual(
            repr(node), "TextNode(This is a text node, bold, https://me.com)"
        )

    def test_delimiter_code(self):
        node1 = TextNode("This is a text with a `code block` word", text_type_text)
        # node2 = TextNode("This is a text with a **bold** word", text_type_bold)
        # node3 = TextNode("This is a text with a normal word", text_type_italic)
        nodes = split_nodes_delimiter([node1], '`', text_type_code)
        self.assertEqual(nodes, [
            TextNode("This is a text with a ", "text", None),
            TextNode("code block", "code", None),
            TextNode(" word", "text", None),
        ])

    def test_delimiter_bold(self):
        node = TextNode("This is a text with a **bolded** word", text_type_text)
        nodes = split_nodes_delimiter([node], '**', text_type_bold)
        self.assertEqual(nodes, [
            TextNode("This is a text with a ", "text", None),
            TextNode("bolded", "bold", None),
            TextNode(" word", "text", None),
        ])

    def test_delimiter_bold_double(self):
        node = TextNode("This is a **bolded** text with a **second bolded** word", text_type_text)
        nodes = split_nodes_delimiter([node], '**', text_type_bold)
        self.assertEqual(nodes, [
            TextNode("This is a ", "text", None),
            TextNode("bolded", "bold", None),
            TextNode(" text with a ", "text", None),
            TextNode("second bolded", "bold", None),
            TextNode(" word", "text", None),
        ])

    def test_delimiter_italic(self):
        node = TextNode("This is a text with an *italicized* word", text_type_text)
        nodes = split_nodes_delimiter([node], '*', text_type_italic)
        self.assertEqual(nodes, [
            TextNode("This is a text with an ", "text", None),
            TextNode("italicized", "italic", None),
            TextNode(" word", "text", None),
        ])


if __name__ == "__main__":
    unittest.main()
