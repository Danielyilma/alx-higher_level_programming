#include "Python.h"

/**
 * print_python_list - python list
 *
 * @p: python object
 *
 * Return: nothing
*/

void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	int i = 0;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %lu\n", list->ob_base.ob_size);
	printf("[*] Allocated = %lu\n", list->allocated);

	for (i = 0; i < list->ob_base.ob_size; i++)
	{
		printf("Element %d: %s\n", i, list->ob_item[i]->ob_type->tp_name);
	}
}

/**
 * print_python_bytes - print python byte information
 *
 * @p: python object
 *
 * Return: nothing
*/

void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	int i = 0;
	char *byt = bytes->ob_sval;
	ssize_t len = bytes->ob_base.ob_size;

	printf("[.] bytes object info\n");
	printf("  size: %lu\n", bytes->ob_base.ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	i = len > 10 ? 10 : len + 1;

	printf("  first %d bytes: ", i);
	i = 0;

	for (i = 0; i <= len && i < 10; i++)
	{
		printf("%02x ", (unsigned char)byt[i]);
	}

	printf("\n");
}
