class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if not l1:
            return l2

        if not l2:
            return l1

        merged_head = l1 if l1.val <= l2.val else l2
        curr_l1 = l1.next if l1.val <= l2.val else l1
        curr_l2 = l2.next if l2.val < l1.val else l2
        merged_last = merged_head

        while curr_l1 is not None and curr_l2 is not None:

            next_l1 = curr_l1.next
            next_l2 = curr_l2.next

            if curr_l1.val <= curr_l2.val:
                merged_last.next = curr_l1
                merged_last = merged_last.next
                curr_l1 = next_l1
            else:
                merged_last.next = curr_l2
                merged_last = merged_last.next
                curr_l2 = next_l2

        if curr_l1 is None:
            merged_last.next = curr_l2

            while curr_l2 is not None:
                merged_last = merged_last.next
                curr_l2 = curr_l2.next

        if curr_l2 is None:
            merged_last.next = curr_l1

            while curr_l1 is not None:
                merged_last = merged_last.next
                curr_l1 = curr_l1.next

        return merged_head
