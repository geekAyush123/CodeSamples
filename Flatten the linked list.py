using System;
using System.Collections.Generic;

public class Node
{
    public int data;
    public Node next;
    public Node bottom;

    public Node(int data)
    {
        this.data = data;
        this.next = null;
        this.bottom = null;
    }
}

public class Solution
{
    public Node Flatten(Node root)
    {
        // List to store all values
        List<int> values = new List<int>();

        Node current = root;

        // Traverse the 2D linked list
        while (current != null)
        {
            Node down = current;
            while (down != null)
            {
                values.Add(down.data);  // Add the value to the list
                down = down.bottom;
            }
            current = current.next;
        }

        // Sort the values
        values.Sort();

        // Create a new flattened list
        Node dummy = new Node(-1);  // Dummy node to simplify the list creation
        Node head = dummy;

        foreach (int val in values)
        {
            Node temp = new Node(val);
            dummy.bottom = temp;  // Link the bottom nodes
            dummy = dummy.bottom;
        }

        // Return the flattened list (head of the bottom-linked list)
        return head.bottom;
    }
}
