'''
File: huffman.py
Name: Liam Staudinger
Course: CSC 120, Spring 2024
Purpose: This program reads in a file containing a preorder traversal of a 
binary tree, an inorder traversal of a binary tree, and a string of bits. The 
program then constructs the binary tree from the traversals and decodes the 
string of bits using the binary tree. The program then prints the postorder 
traversal of the binary tree and the decoded values.
'''

class BinaryTree:
    '''
    This class represents a binary tree with methods to insert and retrieve 
    values. The class defines methods for inserting values to the left and 
    right of the tree, and for retrieving the left, right, and value of the 
    tree. It also defines a method for returning a string representation of the 
    tree.
    '''
    def __init__(self, value):
        '''
        Constructor for the BinaryTree class. Initializes the value of the tree 
        and sets the left and right children to None.

        Parameters:
            value (int): The value of the tree.
        Returns:
            None
        '''
        self._value =  value
        self._left = None
        self._right = None

    def value(self):
        '''
        Returns the value stored in the BinaryTree node.
        '''
        return self._value
    
    def left(self):
        '''
        Returns the left child of the BinaryTree node.
        '''
        return self._left
    
    def right(self):
        '''
        Returns the right child of the BinaryTree node.
        '''
        return self._right
    
    def insert_left(self, tree):
        '''
        Inserts a tree to the left of the current tree. If a left child already 
        exists, the existing child is moved down the tree.

        Parameters:
            tree (BinaryTree): The tree to insert to the left of the current 
            tree.
        Returns:
            None
        '''
        # Assign the new tree as the left child if none exists
        if self._left == None:
            self._left = tree
        else:
            t = tree
            # Move the existing left child down the tree
            t._left = self._left
            # Assign the new tree as the left child
            self._left = t

    def insert_right(self, tree):
        '''
        Inserts a tree to the right of the current tree. If a right child 
        already exists, the existing child is moved down the tree.

        Parameters:
            tree (BinaryTree): The tree to insert to the right of the current 
            tree.
        Returns:
            None
        '''
        # Assign the new tree as the right child if none exists
        if self._right == None:
            self._right = tree
        else:
            t = tree
            # Move the existing right child down the tree
            t._right = self._right
            # Assign the new tree as the right child
            self._right = t

    def __str__(self):
        '''
        Returns a string representation of the BinaryTree node and its
        children.
        '''
        if self._left is None and self._right is None:
            return str(self._value)
        return f"{str(self._value)} [{str(self._left)}, {str(self._right)}]"
            
def open_file():
    '''
    Prompts the user for a file name and reads the file. The function returns
    a list containing the preorder traversal, contained in a list, the inorder 
    traversal, contained in a list, and bit string from the file.

    Parameters:
        None
    Returns:
        list: A list containing the preorder traversal, inorder traversal, and 
        bit string from the file.
    '''
    file_name = input('Input file: ')
    file = open(file_name, 'r')
    preorder = []
    inorder = []
    bit_string = ''
    i = 0
    for line in file:
        # If it's the first line
        if i == 0:
            line = line.strip().split()
            for j in range(len(line)):
                preorder.append(int(line[j]))
            i += 1
        # If it's the second line
        elif i == 1:
            line = line.strip().split()
            for j in range(len(line)):
                inorder.append(int(line[j]))
            i += 1
        # If it's the third line
        else:
            line = line.strip().split()
            for j in range(len(line)):
                bit_string += line[j]
    file.close()
    return [preorder, inorder, bit_string]
    
def build_tree(preorder, inorder):
    '''
    This function constructs a binary tree from the preorder and inorder
    traversals of the tree. The function returns the root of the tree.

    Parameters:
        preorder (list): A list containing the preorder traversal of the tree.
        inorder (list): A list containing the inorder traversal of the tree.
    Returns:
        root (BinaryTree): The binary tree constructed from the traversals.
    '''
    if inorder == []:
        return None
    else:
        root_value = preorder.pop(0)
        root = BinaryTree(root_value)
        # Find the index of the root value in the inorder list
        inorder_root = inorder.index(root_value)
        # If the left subtree in the inorder list is not empty, recursively 
        # build the left subtree
        if inorder[:inorder_root] != []:
            root.insert_left(build_tree(preorder, inorder[:inorder_root]))
        # If the right subtree in the inorder list is not empty, recursively
        # build the right subtree
        if inorder[inorder_root+1:] != []:
            root.insert_right(build_tree(preorder, inorder[inorder_root+1:]))
        return root
    
def decode_tree(tree, bit_string):
    '''
    This function decodes a string of bits using a binary tree. The function
    returns the decoded values.

    Parameters:
        tree (BinaryTree): The binary tree used to decode the bit string.
        bit_string (str): The string of bits to decode.
    Returns:
        decoded_values (str): The decoded values from the bit string.
    '''
    decoded_values = ''
    node = tree
    for bit in bit_string:
        if bit == '0':
            node = node.left()
        else:
            node = node.right()
        if node is not None:
            # Node is a leaf
            if node.left() is None and node.right() is None:  
                decoded_values += str(node.value())
                # Return to the root
                node = tree  
    return decoded_values

def postorder(tree):
    '''
    This function returns the postorder traversal of a binary tree as a string.
    
    Parameters:
        tree (BinaryTree): The binary tree to traverse.
    Returns:
        str: The postorder traversal of the binary tree.
    '''
    if tree is None:
        return ''
    return postorder(tree.left()) + postorder(tree.right()) + \
           (str(tree.value()) + ' ')
    
def main():
    '''
    Main function to drive the program. The function reads in a file containing
    the preorder traversal, inorder traversal, and bit string of a binary tree.
    The function constructs the binary tree from the traversals and decodes the
    bit string using the binary tree. The function then prints the postorder
    traversal of the binary tree and the decoded values.

    Parameters:
        None
    Returns:
        None
    '''
    tree_info = open_file()
    preorder = tree_info[0]
    inorder = tree_info[1]
    bit_string = tree_info[2]
    tree = build_tree(preorder, inorder)
    decoded_values = decode_tree(tree, bit_string)
    postorder_str = postorder(tree)
    print(postorder_str[:-1])
    print(decoded_values)
main()