using System;
using System.ComponentModel.Design.Serialization;

namespace bst
{
    class Program
    {
        class NodeT
        {
            public NodeT parent;
            public NodeT left;
            public NodeT right;
            public int data;
            public NodeT(int data)
            {
                this.data = data;
                this.parent = null;
                this.left = null;
                this.right = null;
            }
        }
        class BST
        {
            private NodeT root;
            public NodeT findParent(NodeT child)
            {
                while(1==1)
                {
                    var parent = this.root;
                    if (child.data < parent.data)
                    {
                        if (parent.left == null) return parent;
                        else parent = parent.left;
                    }
                    else if (child.data >= parent.data)
                    {
                        if (parent.right == null) return parent;
                        else parent = parent.right;
                    }
                }
            }
            public NodeT Add(int data)
            {
                var child = new NodeT(data);
                if (this.root == null) this.root = child;
                else
                {
                    var parent = this.findParent(child);
                    if (child.data < parent.data) parent.left = child;
                    else parent.right = child;
                }
                return child;
            }
            public void Pop()
            {

            }
        }
        static void Main(string[] args)
        {

        }
    }
}
