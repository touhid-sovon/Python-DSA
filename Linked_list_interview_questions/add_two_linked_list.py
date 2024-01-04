from base_structure import *

def addtwoNumbers(ll1,ll2):
    ll = LinkedList()
    n1 = ll1.head
    n2 = ll2.head
    rem = 0

    while n1 or n2:
        result = rem
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next

        ll.add(result%10)
        rem = result // 10
    return ll

ll1 = LinkedList()
ll1.add(7)
ll1.add(1)
ll1.add(6)

ll2 = LinkedList()
ll2.add(5)
ll2.add(9)
ll2.add(2)

print(ll1)
print(ll2)

print(addtwoNumbers(ll1,ll2))
