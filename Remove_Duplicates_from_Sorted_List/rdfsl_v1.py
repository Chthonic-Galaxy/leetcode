from list_node import ListNode

def delete_duplicates(head: ListNode) -> ListNode:
    node = head
    _next = node.next

    while True:
        if node.val != _next.val:
            node = _next
            _next = node.next
        else:
            while node.val == _next.val:
                _next = _next.next
                if _next is None: break
            node.next = _next
        if _next is None: break

    return head

if __name__ == "__main__":
    linked_list = ListNode().create_linked_list([1, 2, 3])
    print(ListNode().dump_to_list(delete_duplicates(linked_list)))
    linked_list = ListNode().create_linked_list([1, 1, 3])
    print(ListNode().dump_to_list(delete_duplicates(linked_list)))
    linked_list = ListNode().create_linked_list([1, 1, 1, 2])
    print(ListNode().dump_to_list(delete_duplicates(linked_list)))
    linked_list = ListNode().create_linked_list([1,1,2,3,3])
    print(ListNode().dump_to_list(delete_duplicates(linked_list)))

