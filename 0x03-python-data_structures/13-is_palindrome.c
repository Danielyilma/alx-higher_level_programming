#include "lists.h"


/**
 * is_palindrome - checking if the numbers
 *  in the list is palindrome
 *
 * @head: head node
 *
 * Return: 0 if not or 1 if it is palindrome
 *
*/

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int number[1024];
	int i = 0, j;

	while (current != NULL)
	{
		number[i] = current->n;
		current = current->next;
		i++;
	}
	i--;

	for (j = 0; i > j; j++)
	{
		if (number[i] != number[j])
		return (0);
		i--;
	}
	return (1);
}
