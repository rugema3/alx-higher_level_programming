#include "list.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle
 * @head: Pointer to the head of the linked list
 *
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(ListNode *head)
{
	ListNode *slow = head, *fast = head;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		/* If the fast pointer meets the slow pointer, there is a cycle */
		if (slow == fast)
			return (1);
	}

	/* If the fast pointer reaches the end of the list, there is no cycle */
	return (0);
}

