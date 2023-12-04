#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 *add_nodeint - adds a new node at the end of a listint_t list
 *@head: pointer to pointer of first node of listint_t list
 *@n: integer to be included in new node
 *Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}
/**
 *is_palindrome - identify if single linked list is palindrome
 *@head: head of listint_t
 *Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *aux = NULL, *aux2 = NULL;

	if (*head == NULL || slow->next == NULL)
		return (1);
	while (slow != NULL)
	{
		add_nodeint(&aux, slow->n);
		slow = slow->next;
	}
	aux2 = aux;
	while (*head !=  NULL)
	{
		if ((*head)->n != aux2->n)
		{
			free_listint(aux);
			return (0);
		}
		*head = (*head)->next;
		aux2 = aux2->next;
	}
	free_listint(aux);
	return (1);
}
