"""
File: add2.py
Name: Jay
------------------------
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    1. put l1 in list, and then reverse, separate in order to count(s1)
    2. put l2 in list, and then reverse, separate in order to count(s2)
    3. ans is l1 + l2, put back to a list
    4. use dummy node, put back to ListNode
    """
    # l1_list = [2, 4, 3]
    l1_list = []
    cur1 = l1
    # put every number of ListNode in l1_list
    while cur1:
        l1_list.append(cur1.val)
        cur1 = cur1.next
    # reverse -> l1_list = [3, 4, 2]
    l1_list.reverse()
    # in order to count at last
    s1 = ''
    for num in l1_list:
        s1 += str(num)

    # l2_list = [5, 6, 4]
    l2_list = []
    cur2 = l2
    # put every number of ListNode in l2_list
    while cur2:
        l2_list.append(cur2.val)
        cur2 = cur2.next
    # reverse -> l2_list = [4, 6, 5]
    l2_list.reverse()
    # in order to count at last
    s2 = ''
    for num in l2_list:
        s2 += str(num)

    # ans = 807
    ans = int(s1) + int(s2)
    # ans_list = [8, 0, 7]
    ans_list = [int(digit) for digit in str(ans)]
    # ans_list = [7, 0, 8] (reverse)
    ans_list.reverse()

    # create a dummy node to put ans_list inside
    dummy = ListNode()
    cur = dummy
    for num in ans_list:
        cur.next = ListNode(num)
        cur = cur.next

    return dummy.next

####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
