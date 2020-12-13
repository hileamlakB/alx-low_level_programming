#include "lists.h"

/**
 * add_dnodeint_end - adds node to end of doubly linked list
 * @head: pointer to head of list
 * @n: integer value of node
 * Return: pointer to node added
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *newNode = malloc(sizeof(dlistint_t)), *_head = *head;

	if (!newNode)
	{
		dprintf(2, "Error: Can't malloc\n");
		return (NULL);
	}
	newNode->n = n, newNode->next = NULL, newNode->prev = NULL;
	if (!_head)
	{
		_head = newNode;
		return (newNode)
	}

	while (_head->next)
		_head = _head->next;

	_head->next = newNode;
	newNode->prev = _head;

	return (newNode);
}
