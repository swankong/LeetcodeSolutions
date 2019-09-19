# Leetcode #23
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
# Example:
# Input:
# [
#  1->4->5,
#  1->3->4,
#  2->6
# ]
# Output: 1->1->2->3->4->4->5->6


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        n_lists = len(lists)

        if n_lists == 0:
            return None
        elif n_lists == 1:
            return lists[0]

        head_ptr = lists[0]
        for i_list in lists[1:]:  # merge with pairs
            head_ptr = self.merge2List(head_ptr, i_list)

        return head_ptr

    def merge2List(self, l_list, r_list):    # Solution 1
        if not r_list or r_list is None:  # do nothing for a empty list
            return l_list
        if not l_list or r_list is None:  # return 2nd if 1st is empty
            l_list = r_list
            return l_list

        # l_pptr is left prev pointer
        l_ptr, r_ptr, l_pptr = l_list, r_list, None
        while l_ptr is not None and r_ptr is not None:
            if r_ptr.val < l_ptr.val:
                tmp_ptr, r_ptr = r_ptr, r_ptr.next  # keep r_ptr in tmp, move r_ptr forward
                tmp_ptr.next = l_ptr
                if l_pptr is None:  # 插在最前
                    l_pptr = tmp_ptr
                    l_list = l_pptr
                else:
                    l_pptr.next = tmp_ptr
                    l_pptr = l_pptr.next  # move forward
            else:
                l_pptr = l_ptr  # move left forward
                l_ptr = l_ptr.next
        if l_ptr is None:
            l_pptr.next = r_ptr
        return l_list

    def mergeKLists2(self, lists):  # Solution 2
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        n_lists = len(lists)
        if n_lists == 0:
            return None
        elif n_lists == 1:
            return lists[0]

        i, index_ = 0, 0
        head_ptr = None
        while i < n_lists and n_lists > 0:
            if not lists[i]:
                lists.pop(i)
                n_lists -= 1
                continue
            if i == 0:
                head_ptr = lists[0]
            if lists[i].val < head_ptr.val:
                head_ptr = lists[i]
                index_ = i
            i += 1

        if lists and lists[index_]:
            lists[index_] = lists[index_].next
            p_ptr = head_ptr

        while True:
            i, index_ = 0, 0
            while i < n_lists:
                if lists[i] is None:
                    lists.pop(i)
                    n_lists -= 1
                if i == 0 and n_lists > 0:
                    tmp_val = lists[i].val
                if i < n_lists and n_lists > 0 and lists[i] is not None and lists[i].val <= tmp_val:
                    tmp_val = lists[i].val
                    index_ = i
                i += 1
            if n_lists <= 1:
                if lists and p_ptr:
                    p_ptr.next = lists[0]
                break
            tmp_ptr = lists[index_]  # point to insert node
            lists[index_] = lists[index_].next  # move next
            if p_ptr.next != tmp_ptr:
                tmp_ptr.next = p_ptr.next  # point to the link list
                p_ptr.next = tmp_ptr  # insert into the list
            p_ptr = p_ptr.next

        return head_ptr