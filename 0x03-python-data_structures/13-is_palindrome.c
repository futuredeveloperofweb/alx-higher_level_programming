#include "lists.h"

/**
 * is_palindrom - checks if a singly linked list is a palindrome.
 * @head: a pointer to the beginning of linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (comp(head, *head));
}

/**
 * comp - check if palidrom
 * @head: a pointer to the beginning of linked list
 * @end: a pointer to the end of linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int comp(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (comp(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
