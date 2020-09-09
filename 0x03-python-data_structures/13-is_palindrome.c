#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - check if a singly linked list of integer is palindrome
 * @head: pointer first element of the linked list.
 *
 * Return: 1 if the singly linked list is palidrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp;
	int i, index, buffer[5000];

	*tmp = *head;
	if (!*head)
		return (1);
	for (index = 0; tmp; index++)
	{
		buffer[index] = tmp->n;
		tmp = tmp->next;
	}
	for (i = 0; idx > i; index--, i++)
	{
		if (buffer[index - 1] != buffer[i])
			return (0);
	}
	return (1);
}
