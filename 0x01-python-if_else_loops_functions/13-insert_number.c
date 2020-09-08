#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Insert a node with a number a sorted linked list.
 * @head: head of the sorted linked list.
 * @number: number to be inserted in the linked list.
 *
 * Return: the added node.
 */
listint_t *insert_node(listint_t **head, int number)
{
  listint_t *new_node = NULL;
  listint_t *tmp = NULL;

  if (head == NULL)
    return (NULL);
  new_node = malloc(sizeof(listint_t));
  if (new_node == NULL)
    return (NULL);
  new_node->n = number;
  new_node->next = NULL;
  if (!*head)
    {
      *head = new_node;
      return (new_node);
    }
  tmp = *head;
  if (tmp->n > number)
    {
      new_node->next = tmp;
      *head = new_node;
      return (new_node);
    }
  else
    {
      while (tmp->next)
	{
	  if (tmp->n <= number && tmp->next->n >= number)
	    {
	      new_node->next = tmp->next;
	      tmp->next = new_node;
	      return (new_node);
	    }
	  tmp = tmp->next;
	}
      tmp->next = new_node;
    }
  return (new_node);
}
