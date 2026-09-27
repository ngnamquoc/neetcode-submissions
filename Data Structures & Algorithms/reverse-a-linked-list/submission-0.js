/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

//1->0->null

class Solution {
    /**
     * @param {ListNode} head
     * @return {ListNode}
     */
    reverseList(head) {
        if(!head|| !head.next){
            return head
        }

        let prev=null
        let curr=head

        while(curr!==null){
            // save next
            const next=curr.next;
            //reverse
            curr.next=prev;

            // advance
            prev=curr;
            curr=next;

        }
        return prev

     

        
    }
}
