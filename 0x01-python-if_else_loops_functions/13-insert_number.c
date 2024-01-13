#include "lists.h"

/**
 * insert_node -  inserts a number into a sorted singly linked list.
 * @head: a pointer the head of the list
 * @number: the value to insert in the node
 * Return:  the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (current == NULL || new->n < current->n)
	{
		new->next = current;
		*head = new;
		return (*head);
	}

	while (current)
	{
		if (new->n < current->next->n || current->next == NULL)
		{
			new->next = current->next;
			current->next = new;
			return (current);
		}
		current = current->next;
	}
	return (NULL);
}
