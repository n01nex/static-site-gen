import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(
            tag="a",
            value="Click me!",
            props={"href": "https://www.google.com", "target": "_blank"},
        )
        node2 = HTMLNode(
            tag="a",
            value="Click me!",
            props={"href": "https://www.google.com", "target": "_blank"},
        )
        self.assertEqual(repr(node), repr(node2))
    
    def test_noneq(self):
        node3 = HTMLNode(
            tag="a",
            value="Click me!",
            props={"href": "https://www.google.com", "target": "_blank"},
        )
        # A node without props
        node4 = HTMLNode(
            tag="p",
            value="Some paragraph text.",
        )
        self.assertNotEqual(repr(node3), repr(node4))

        def test_props_to_html(self):
            node5 = HTMLNode(
                "a",
                "This is a link",
                None,
                {"href": "https://www.google.com", "target": "_blank"},
            )
            expected_output = ' href="https://www.google.com" target="_blank"'
            self.assertEqual(node5.props_to_html(), expected_output)




if __name__ == "__main__":
    unittest.main()