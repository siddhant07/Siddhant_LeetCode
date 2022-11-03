/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry=0;
        ListNode BackHead=new ListNode(0);
        ListNode runner=BackHead;
        int a,b;
        
        while(l1!=null || l2!=null){
            a=(l1!=null)?l1.val:0;
            b=(l2!=null)?l2.val:0;
            runner.next=new ListNode((a+b+carry)%10);
            runner=runner.next;
            carry=(a+b+carry)/10;
            if(l1!=null)
                l1=l1.next;
            if(l2!=null)
                l2=l2.next;
        }
        if(carry>0)
            runner.next=new ListNode(1);
        
        return BackHead.next;
        
        /*while(l1!= null){
            n1+=l1.val*digitizer;
            digitizer=digitizer*10;
            l1=l1.next;
        }
        
        digitizer=1;
        while(l2!= null){
            n2+=l2.val*digitizer;
            digitizer=digitizer*10;
            l2=l2.next;
        }
        ListNode answer=new ListNode(n1+n2);
        return answer;*/
        
        
        
    }
}