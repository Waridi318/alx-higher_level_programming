#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - inserts a number into a
 * sorted singly linked list
 * @head: ptr->head
 * @number: int n
 * Return: address of new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	while (current->next != 0)
	{
		if (current->n <= number && current->next->n >= number && current->next != 0)
		{
			new->next = current->next;
			current->next = new;
			break;
		}
		if (current->next == 0 && current->n < number)
		{
			current->next = new;
		}
		current = current->next;
	}
	return (new);
}
