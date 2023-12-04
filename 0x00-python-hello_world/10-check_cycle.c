#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the list
 * Return: 0 if no cycle, 1 if cycle
 */
int check_cycle(listint_t *list)
{
    listint_t *tortoise, *hare; /* declare two pointers */

    if (list == NULL) /* check if list is empty */
        return (0);

    tortoise = list; /* initialize tortoise to head of list */
    hare = list->next; /* initialize hare to second node of list */

    while (hare != NULL) /* loop until hare reaches end of list */
    {
        if (hare->next == NULL) /* check if hare has enough space to move */
            return (0);

        hare = hare->next->next; /* move hare two nodes ahead */
        tortoise = tortoise->next; /* move tortoise one node ahead */

        if (hare == tortoise) /* check if hare and tortoise meet */
            return (1); /* cycle found */
    }

    return (0); /* loop exit means no cycle */
}

