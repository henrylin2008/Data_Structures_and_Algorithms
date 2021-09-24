# HTTPRouter using a Trie

# For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the
# Trie data structure we learned previously.
#
# There are many different implementations of HTTP Routers such as regular expressions or simple string matching,
# but the Trie is an excellent and very efficient data structure for this purpose.
#
# The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post"
# and figure out what content to return. In a dynamic web server, the content will often come from a block of code
# called a handler.
#
# First we need to implement a slightly different Trie than the one we used for autocomplete. Instead of simple words
# the Trie will contain a part of the http path at each node, building from the root node /
#
# In addition to a path though, we need to know which function will handle the http request. In a real router we
# would probably pass an instance of a class like Python's SimpleHTTPRequestHandler which would be responsible for
# handling requests to that path. For the sake of simplicity we will just use a string that we can print out to
# ensure we got the right handler
#
# We could split the path into letters similar to how we did the autocomplete Trie, but this would result in a Trie
# with a very large number of nodes and lengthy traversals if we have a lot of pages on our site. A more sensible way
# to split things would be on the parts of the path that are separated by slashes ("/"). A Trie with a single path
# entry of: "/about/me" would look like:
#
# (root, None) -> ("about", None) -> ("me", "About Me handler")
#
# We can also simplify our RouteTrie a bit by excluding the suffixes method and the endOfWord property on
# RouteTrieNodes. We really just need to insert and find nodes, and if a RouteTrieNode is not a leaf node,
# it won't have a handler which is fine.

# A RouteTrie will store our routes and their associated handlers
from collections import defaultdict

class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.handler = root_handler

    def insert(self):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

    def find(self):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = defaultdict(RouteTrieNode)
        self.handler = handler

    def insert(self, path):
        # Insert the node as before
        if path not in self.children:
            self.children[path] = RouteTrieNode()

