#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *current = *head;

	new->n = number;

	while (current != NULL)
	{
		if (current->next->n > number)
		{
			new->next = current->next;
			current->next = new;
			break;
		}

		current = current->next;
	}

	return (new);
}
