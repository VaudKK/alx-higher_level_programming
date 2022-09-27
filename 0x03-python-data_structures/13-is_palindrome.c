#include "lists.h"
#include <stdlib.h>

/**
* is_palindrome - checks if palidnorme
* @head: the single linked list
*
* Return: 1 if linked list 0 otherwise
*/
int is_palindrome(listint_t **head)
{
	int list_size = 0;
	int i = 0, j = 0;
	int left, right;
	int *numbers = malloc(sizeof(int));
	listint_t *my_list = malloc(sizeof(listint_t));

	if (head == NULL)
		return (1);

	my_list = *head;
	while (my_list != NULL)
	{
		*(numbers + list_size) = my_list->n;
		list_size += 1;
                my_list = my_list->next; 
	}

	free(my_list);

	for (i = list_size - 1; i >= 0; i--)
	{
		left = *(numbers + j);
		right = *(numbers + i);
		
		if (i == j)
		{
			return (1);
		}

		if (left != right)
		{
			return (0);
		}

		j++;
	}
	
	return (1);
}
