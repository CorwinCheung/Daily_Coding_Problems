#Brute force solution, O(n) check all strings
def autocomplete(q_string,set):
    completed = []
    for s in set:
        if s[:len(q_string)] == q_string:
            completed.append(s)
    return completed

#Preprocess the set of strings into a trie(prefix tree) by each letter to get strings in O(log n), if balanced
class TrieNode():
    def __init__(self):
        self.children = {}
        self.end_word = False
class Trie():
    def __init__(self): 
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end_word=True

    def search_prefix(self,node,prefix):
        results = []
        if node.end_word:
            results.append(prefix)
        for char, next_node in node.children.items():
            results.extend(self.search_prefix(next_node, prefix + char))
        return results
        
    def preprocess_autocomplete(self,q_string,set):
        for e in set:
            self.insert(e)
        
        node = self.root
        for c in q_string:
            if c not in node.children:
                return []
            node = node.children[c]
        return self.search_prefix(node,q_string)



def main():
    query = "de"
    strings = ["dog,","deer","deal"]
    print(autocomplete(query, strings))

    trie = Trie()
    print(trie.preprocess_autocomplete(query,strings))
main()
