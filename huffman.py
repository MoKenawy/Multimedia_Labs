# huffman encoding
# Input (symbols, freq | prob)
# Steps:
# 1. Sort symbols Ascendingly based on frequency
# 2. Build a binary tree from left to right
#    2.1 . take first two symbols and assign them a parent with a sum of their frequencies
#    2.2. insert parent into the list keeping the order.
#    2.3. if list is not empty go back to (2.1)
# 3. label left branches with zeros and right branches with 1
# 4. construct codes for each symbol
# output encoded symbols

# data-structures:  input => dict{symbol, freq}
# heapq of () 

import heapq
#import graphviz
import os
import sys
sys.path.append("C:\\Python312\\Lib\\site-packages\\graphviz")


class Symbol:
    def __init__(self,content, freq):
        self.content = content
        self.freq = freq
        self.left_child = None
        self.right_child = None
        self.code = None
    def display(self):
        print(f"{self.content} \t\t {self.freq} \t\t {self.code}")
    
    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanTree:
    symbols_list = []
    def __init__(self,symbols_list):
        self.symbols_list = symbols_list
        self.count = 1

    def sort_symbols(self):
        self.symbols_list.sort(key= lambda x: x.freq)
    
    def show_list(self):
        root = self.symbols_list[0]
        def _show(node):
            if node != None:
                node.display()
                _show(node.left_child)
                _show(node.right_child)
        _show(root)
    def construct_tree(self):
        list = symbols_list
        while len(list) > 1:
            left_child = list.pop(0)
            right_child = list.pop(0)
            parent = Symbol(content= f"P{self.count}", freq= (left_child.freq + right_child.freq))
            parent.left_child = left_child
            parent.right_child = right_child
            list.append(parent)
            list.sort(key= lambda x: x.freq)
            self.count +=1

    def code_tree(self):
        root = symbols_list[0]
        root.code = ""
        table = self.code_symbols(root,'')
        return root, table
        
    def code_symbols(self,root,code, table = []):
        if root != None:
            # root.left_child.code = root.code + "0"
            # root.right_child.code = root.code + "1"
            root.code = code
            table.append((root.content , root.code))
            
            self.code_symbols(root.left_child, code + "0", table)
            self.code_symbols(root.right_child, code + "1",table)
        return table
    def _display_tree(self,root):
        if root:
            # First print the data of node
            root.display()

            # Then recur on left child
            self._display_tree(root.left_child)

            # Finally recur on right child
            self._display_tree(root.right_child)

    def encode_with_table(self, symbols, table):
        encoded = []
        for symbol in symbols:
            for s, code in table:
                if symbol == s:
                    encoded.append(code)

        return encoded

    def encode(self,tree):
        root = tree[0]
        def _encode(node, symbol):
            if node != None:
                if symbol == node.content:
                    return  node.code
                _encode(node.left_child, symbol)
                
    # def display_tree(self):
    #     root = symbols_list[0]
    #     self._display_tree(root)

    # def visualize_binary_tree(self,root):
    #     dot = graphviz.Digraph()
    #     dot.node(str(root.content))

    #     def add_nodes_edges(node):
    #         if node.left_child:
    #             dot.node(str(node.left_child.content))
    #             dot.edge(str(node.content), str(node.left_child.content))
    #             add_nodes_edges(node.left_child)
    #         if node.right_child:
    #             dot.node(str(node.right_child.content))
    #             dot.edge(str(node.content), str(node.right_child.content))
    #             add_nodes_edges(node.right_child)

    #     add_nodes_edges(root)
    #     dot.render('binary_tree', view=True, format='png')


    # def init_heap(self):
    #     h= []
    #     heapq.heapify(h)
    #     for symbol in self.symbols_list:
    #         heapq.heappush(h, symbol)

    #     print("------------------- in heap ---------------")            
    #     for symbol in h :
    #         symbol.display()
    #     return h

if __name__ == "__main__":
    symbols = ['m','p','s','t']
    # symbols = ['10','20',
    #         '25',
    #         '180',
    #         '200',
    #         '220',
    #         ]
    freq = [1,2,4,4]
    #freq = [20,20,200,500,200,20,20,20]

    data = "mppstmt"
    symbols_list = []
    for i in range(len(symbols)) :
        symbols_list.append(Symbol(content=symbols[i], freq=freq[i]))
    

    huffman = HuffmanTree(symbols_list)
    
    huffman.sort_symbols()
    huffman.construct_tree()
    root , table= huffman.code_tree()
    #print(f"encoding table : {table}")
    
    huffman.show_list()
    encoded = huffman.encode(data, table)
    print(f"data: {data}")
    print(f"encoded data: {encoded}")

