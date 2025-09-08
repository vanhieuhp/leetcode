from typing import List

from utils.trie_utils import build_trie


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = build_trie(products)
        res = []
        node = trie.root
        for ch in searchWord:
            if ch in node.children:
                node = node.children[ch]
                res.append(node.suggestions)
            else:
                res.extend([[]] * (len(searchWord) - len(res)))
                break
        return res

products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchWord = "mouse"

res = Solution().suggestedProducts(products, searchWord)
print(res)
