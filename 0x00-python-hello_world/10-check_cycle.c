#include "lists.h"

/**
 *
 * 
 * 
 * 
 */

int check_cycle(listint_t *list)
{
        listint_t *slow, *fast;

        if (list == NULL)
        return (0);

        slow = list;
        fast = list;

        while (fast != NULL)
        {
                if (fast == slow)
                return (1);

                slow = slow->next;
                fast = fast->next;
        }
        return (0);
}
