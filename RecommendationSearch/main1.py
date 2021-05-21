from flask import Flask, request, jsonify
app=Flask(__name__)
@app.route("/search/<string:key>")
def index(key):
    class TrieNode():
        def __init__(self):
            # Initialising
            self.children = {}
            self.last = False

    class Trie():
        def __init__(self):
            self.root = TrieNode()
            self.word_list = []

        def formTrie(self, keys):
            for key in keys:
                self.insert(key)

        def insert(self, key):

            node = self.root

            for a in list(key):
                if not node.children.get(a):
                    node.children[a] = TrieNode()

                node = node.children[a]

            node.last = True

        def search(self, key):
            node = self.root
            found = True

            for a in list(key):
                if not node.children.get(a):
                    found = False
                    break

                node = node.children[a]

            return node and node.last and found

        def suggestionsRec(self, node, word):
            if node.last:
                self.word_list.append(word)

            for a, n in node.children.items():
                self.suggestionsRec(n, word + a)

        def printAutoSuggestions(self, key):
            node = self.root
            not_found = False
            temp_word = ''

            for a in list(key):
                if not node.children.get(a):
                    not_found = True
                    break

                temp_word += a
                node = node.children[a]

            if not_found:
                return 0
            elif node.last and not node.children:
                return -1

            self.suggestionsRec(node, temp_word)
            result = []
            for s in self.word_list:
                result.append(s)
            return result

    keys = ["hello", "dog", "hell", "cat", "a",
            "hel", "help", "helps", "helping", 'comapny', 'chirag', 'what is engineering',
            'where can i find forms']  # keys to form the trie structure
    status = ["Not found", "Found"]
    t = Trie()
    t.formTrie(keys)
    comp = t.printAutoSuggestions(key)
    if comp == -1:
        print("No other strings found with this prefix\n")
    elif comp == 0:
        print("No string found with this prefix\n")
    return jsonify(comp)
if __name__=='__main__':
    app.run(debug=True)