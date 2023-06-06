#ifndef LIST_H
#define LIST_H

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/**
 * struct ListNode - Node structure for a singly linked list
 * @data: Data stored in the node
 * @next: Pointer to the next node
 */
typedef struct ListNode
{
	int data;
	struct ListNode *next;
} ListNode;

int check_cycle(ListNode *head);

#endif /* LIST_H */

