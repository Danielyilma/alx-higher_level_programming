#include "lists.h"

/**
 * insert_node - insert node in sorted list
 *
 * @head: head of the node
 * @number: the number
 *
 * Return: the new node
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode = malloc(sizeof(listint_t)), *temp = *head;

	if (!newnode)
	return (NULL);

	newnode->n = number;
	newnode->next = NULL;

	if (*head == NULL)
	{
		*head = newnode;
	}

	while (temp != NULL)
	{
		if (temp->next->n > number)
		{
			newnode->next = temp->next;
			temp->next = newnode;
			break;
		}
		temp = temp->next;
	}
	return (newnode);
}
