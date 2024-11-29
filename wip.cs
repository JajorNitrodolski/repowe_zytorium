using System;
class Node
{
    public int data;
    public Node left;
    public Node right;

    public Node(int data)
    {
        this.data = data;
    }
}
class BST
{
    Node root;
    public void insert(Node node)
    {
        node = insertHelper(root, node);
    }
    private Node insertHelper(Node root, Node node)
    {
        int data = node.data;
        if(root == null)
        {
            root = node;
            return root;
        }
        else if(data < root.data)
        {
            root.left = insertHelper(root.left, node);
        }
        else
        {
            root.right = insertHelper(root.right, node);
        }
        return root;
    }
    public void display()
    {
        displayHelper(root);
    }
    private void displayHelper(Node root)
    {
        if(root != null)
        {
            displayHelper(root.left);
            Console.WriteLine(root.data);
            displayHelper(root.right);
        }
    }
    public bool search(int data)
    {
        if (root == null)
        {
            return false;
        }
        else if (root.data == data)
        {
            return true;
        }
        else if (root.data > data)
        {
            return searchHelper(root.left, data);
        }
        else
        {
            return searchHelper(root.right, data);
        }
    }
    private bool searchHelper(Node root, int data)
    {
        return false;
    }
    public void remove(int data)
    {

    }
    private Node removeHelper(Node root, int data)
    {
        return null;
    }
    private int successor(Node root)
    {
        return 0;
    }
    private int predecessor(Node root)
    {
        return 0;
    }
    public BST()
    {
        this.root = null;
    }
}
class Program
{
    static void Main(string[] args)
    {
        BST drzewo = new BST();
        drzewo.insert(new Node(5));
        drzewo.insert(new Node(1));
        drzewo.insert(new Node(3));
        drzewo.insert(new Node(4));
        drzewo.insert(new Node(2));
        drzewo.display();
    }
}