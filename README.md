# Search_bar_using_flask_and_trie
I used the advance data structure to create a search bar , which will autocomplte the search sentence based on the prefix character.

**Trie DataStructure:**
Trie is an efficient information reTrieval data structure. Using Trie, search complexities can be brought to optimal limit (key length). If we store keys in binary search tree, a well balanced BST will need time proportional to M * log N, where M is maximum string length and N is number of keys in tree. Using Trie, we can search the key in O(M) time. However the penalty is on Trie storage requirements (Please refer Applications of Trie for more details)



Every node of Trie consists of multiple branches. Each branch represents a possible character of keys. We need to mark the last node of every key as end of word node. A Trie node field isEndOfWord is used to distinguish the node as end of word node. A simple structure to represent nodes of the English alphabet can be as following,


Sources:
geeksforgeeks.com
python and flask documentation

