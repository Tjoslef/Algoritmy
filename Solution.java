
import java.util.ArrayList;
import java.util.Collections;

public class Solution {
    class ListNode {
        int val;
      ListNode next;
      ListNode() {}
      ListNode(int val) { this.val = val; }
      ListNode(int val, ListNode next) { this.val = val; this.next = next; 
      }   
    }
    public ListNode reverseKGroup(ListNode head, int k) {
        ArrayList<Integer> values = new ArrayList<>();
        ListNode current = head;
        while (current != null) {
            values.add(current.val);
            current = current.next;
        }

        ListNode dummy = new ListNode(0);
        ListNode prevTail = dummy;

        for (int i = 0; i < values.size(); i += k) {
            ListNode currentTail = prevTail;
            for (int j = Math.min(i + k - 1, values.size() - 1); j >= i; j--) {
                currentTail.next = new ListNode(values.get(j));
                currentTail = currentTail.next;
            }
            prevTail = currentTail;
        }

        return dummy.next;
    }  
    
    public static void print2DArrayList(ArrayList<ArrayList<Integer>> arrayList2D) {
        for (ArrayList<Integer> row : arrayList2D) {
            for (Integer val : row) {
                System.out.print(val + " ");
            }
            System.out.println();
        }}
    public static void main(String[] args) {
        Solution solution = new Solution();
        Solution.ListNode node5 = solution.new ListNode(5);
        Solution.ListNode node4 = solution.new ListNode(4, node5);
        Solution.ListNode node3 = solution.new ListNode(3, node4);
        Solution.ListNode node2 = solution.new ListNode(2, node3);
        Solution.ListNode node1 = solution.new ListNode(1, node2);
        Solution.ListNode result = solution.reverseKGroup(node1, 2);
        while (result != null) {
            System.out.print(result.val + " ");
            result = result.next;
        }

    }
}