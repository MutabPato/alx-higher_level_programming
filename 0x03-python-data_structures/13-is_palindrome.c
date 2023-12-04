#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: first node
 * Return: reversed list.
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}

/**
 * compare_list - compares two lists
 * @list1: first list
 * @list2: second list
 * Return: NULL if list are similar 0 if different.
 */
int compare_list(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return (0);

	list1 = list1->next;
	list2 = list2->next;
	}
	return (1);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: first node
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	int result;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slow = *head;
	listint_t *fast = *head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	listint_t *reversed_second_half = reverse_list(slow);

	result = compare_list(*head, reversed_second_half);

	reverse_list(reversed_second_half);
	return (result);

}
