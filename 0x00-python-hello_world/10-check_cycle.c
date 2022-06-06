#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to singly linked list to check
 *
 * Return: 0 if there is no cycle, 1 if otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *temp, *tempNext;


	if (!list || !list->next)
		return (0);

	temp = list->next;
	tempNext = list->next->next;

	while (temp && tempNext && tempNext->next)
	{
		if (temp == tempNext)
			return (1);

		temp = temp->next;
		tempNext = tempNext->next->next;
	}

	return (0);
}
