# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def linked_list_to_int(l: ListNode) -> int:
    list_int = 0
    multiplier = 1
    while l.next is not None:
        list_int += int(l.val) * multiplier
        l = l.next
        multiplier *= 10
    list_int += int(l.val) * multiplier
    return list_int


class AddTwoNumbers:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first_num = linked_list_to_int(l1)
        second_num = linked_list_to_int(l2)
        sum = first_num + second_num
        tmp = sum % 10
        sum //= 10
        res = ListNode(tmp)
        prev = res
        while sum != 0:
            tmp = sum % 10
            sum //= 10
            next = ListNode(tmp)
            prev.next = next
            prev = next
        return res
