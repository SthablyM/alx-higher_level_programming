#include "lists.h"
/**
 *check_cycle - check if singly list has cycle in it
 *@list: pointer
 *Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *s, *f;
	s = list;
	f = list;

	while (s != NULL && f != NULL && f->next != NULL)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
		{
			return (1);
		}
	}
	return (0);

}
