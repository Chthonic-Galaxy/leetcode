from list_node import ListNode

def delete_duplicates(head: ListNode) -> ListNode:
    node = head

    while node and node.next:
        if node.val != node.next.val:
            node = node.next
        else:
            node.next = node.next.next

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

