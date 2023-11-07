#include "Python.h"
#include <stdio.h>

/**
 * print_python_list_info - python list information in the back
 *
 * @p: python object type
 *
 * Return nothing
 *
*/


void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *) p;
	int i;

	printf("[*] Size of the Python List = %lu\n", list->ob_base.ob_size);
	printf("[*] Allocated = %lu\n", list->allocated);
	for (i = 0; i < list->ob_base.ob_size; i++)
	{
		printf("Element %d: %s\n", i, list->ob_item[i]->ob_type->tp_name);
	}
}
