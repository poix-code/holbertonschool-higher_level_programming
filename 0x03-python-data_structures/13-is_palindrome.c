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
	listint_t *tmp = *head;
	int arr[5000];
	int idx, count;

	idx = count = 0;
	if (!*head)
		return (1);
	for (; tmp; tmp = tmp->next, idx++)
		arr[idx] = tmp->n;
	for (; idx > count; idx--, count++)
	{
		if (arr[idx - 1] != arr[count])
			return (0);
	}
	return (1);
}
