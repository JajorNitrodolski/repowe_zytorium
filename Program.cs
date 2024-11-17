using System;
public class Node
{
    public int Data;
    public Node Next;
    public Node Prev;

    public Node(int data)
    {
        Data = data;
        Next = null;
        Prev = null;
    }
}

public class LinkedList
{
    private Node head;
    private Node tail;

    public void AddFirst(int data)
    {
        Node newNode = new Node(data);
        if (head == null)
        {
            head = tail = newNode;
        }
        else
        {
            newNode.Next = head;
            head.Prev = newNode;
            head = newNode;
        }
    }

    public void AddLast(int data)
    {
        Node newNode = new Node(data);
        if (tail == null)
        {
            head = tail = newNode;
        }
        else
        {
            tail.Next = newNode;
            newNode.Prev = tail;
            tail = newNode;
        }
    }

    public bool Pop(int data)
    {
        Node current = head;

        while (current != null)
        {
            if (current.Data.Equals(data))
            {
                if (current.Prev != null) current.Prev.Next = current.Next;
                else head = current.Next;

                if (current.Next != null) current.Next.Prev = current.Prev;
                else tail = current.Prev;

                return true;
            }
            current = current.Next;
        }

        return false;
    }

    public void PrintForward()
    {
        Node current = head;
        while (current != null)
        {
            Console.Write(current.Data + " ");
            current = current.Next;
        }
        Console.WriteLine();
    }

    public void PrintBackward()
    {
        Node current = tail;
        while (current != null)
        {
            Console.Write(current.Data + " ");
            current = current.Prev;
        }
        Console.WriteLine();
    }
}
class Program
{
    static void Main(string[] args)
    {
        LinkedList list = new LinkedList();

        list.AddFirst(2);
        list.AddFirst(1);
        list.AddLast(3);
        list.AddLast(4);

        list.PrintForward();
        list.PrintBackward();

        list.Pop(3);
        list.PrintForward();
    }
}