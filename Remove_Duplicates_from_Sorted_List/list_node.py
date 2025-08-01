class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next

    def create_linked_list(self, l: list):
        p_n = None
        for i, entity in enumerate(l):
            c_n = type(self)(val=entity)
            if i == 0:
                head = c_n
            if p_n:
                p_n.next = c_n
            p_n = c_n
        
        return head

    def dump_to_list(self, head):
        cur_node = head
        l = []
        while True:
            l.append(cur_node.val)
            cur_node = cur_node.next
            
            if cur_node is None: break
        return l

if __name__ == "__main__":
    test = ListNode().create_linked_list([1, 2, 3, 4, 5, 5, 6])
    print(ListNode().dump_to_list(test))

