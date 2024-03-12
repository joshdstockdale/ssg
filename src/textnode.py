from htmlnode import (
    LeafNode,
)

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return (
                self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url
            )

        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text)
    if text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text)
    if text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text)
    if text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)
    if text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == text_type_image:
        return LeafNode("img", "",
                        {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"Invalid type given: {text_node.text_type}")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    if len(old_nodes) <= 0:
        return new_nodes

    current_node = old_nodes[0]
    if current_node.text_type == text_type_text:
        if current_node.text.count(delimiter) == 1:
            raise ValueError(f"No closing {delimiter} found")
        split = current_node.text.split(delimiter)
        for i in range(len(split)):
            if split[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(split[i], text_type_text))
            else:
                new_nodes.append(TextNode(split[i], text_type))
        new_nodes.extend(
            split_nodes_delimiter(old_nodes[1:], delimiter, text_type)
        )
    return new_nodes
