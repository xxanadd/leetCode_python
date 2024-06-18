import unittest
from AddTwoNumbers import AddTwoNumbers, ListNode


def parse_linked_list(head: ListNode) -> list:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        test = AddTwoNumbers()

        test_cases = [
            (
                ListNode(2, ListNode(4, ListNode(3))),
                ListNode(5, ListNode(6, ListNode(4))),
                [7, 0, 8]
            ),
            (
                ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))),
                ListNode(9,  ListNode(9, ListNode(9, ListNode(9,)))),
                [8, 9, 9, 9, 0, 0, 0, 1]
            ),
            (
                ListNode(0),
                ListNode(0),
                [0]
            ),
        ]

        for l1, l2, expected in test_cases:
            with self.subTest(l1=l1, l2=l2, expected=expected):
                result = test.addTwoNumbers(l1, l2)
                parsed_result = parse_linked_list(result)
                self.assertListEqual(expected, parsed_result)


if __name__ == '__main__':
    unittest.main()
