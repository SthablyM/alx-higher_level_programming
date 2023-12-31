#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
/**
 *insert_node - inserts a number into a sorted singly linked list
 *@head:a pointer
 *@number: the number to insert
 *Return: NULL or pointer
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *prev;
	
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	current = *head;
	prev = NULL;
	while (current != NULL && current->n < number)
	{
		prev = current;
		current = current->next;
	}
	prev->next = new_node;
	new_node->next = current;
	return (new_node);

}
