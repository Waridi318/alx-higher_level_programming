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
	listint_t *current, *new, *r;

	r = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	if (head == NULL)
	{
		return (NULL);
	}
	new->n = number;
	new->next = NULL;

	current = *head;
	while (current->next != NULL)
	{
		if (current->n <= number && current->next->n >= number)
		{
			new->next = current->next;
			current->next = new;
			break;
		}
		current = current->next;
	}
	if (current->next == 0 && current->n <= number)
	{
		current->next = new;
	}
	if (r->next == NULL || r->n >= number)
	{
		new->next = *head;
		*head = new;
	}
	return (new);
}
