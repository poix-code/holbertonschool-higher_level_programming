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
	int len = listint_len(tmp);
	int *arr, idx = 0;
	int c = 0;

	if (!*head)
		return (1);
	arr = malloc(sizeof(int) * len);
	for (; tmp; tmp = tmp->next, idx++)
	{
		arr[idx] = tmp->n;
	}
	while (c < len / 2)
	{
		if (arr[c] == arr[idx - 1])
		{
			c++;
			idx--;
			continue;
		}
		break;
	}
	if (c == len / 2)
	{
		free(arr);
		return (1);
	}
	free(arr);
	return (0);
}
/**
 *  listint_len - Calcuate the number of nodes in a linked list.
 * @h: head of the linked list.
 *
 * Return: number of nodes of the linked list.
 */
int listint_len(listint_t *h)
{
	int count = 0;

	if (h == NULL)
		return (count);
	for (; h != NULL; h = h->next, count++)
	{}
	return (count);
}
