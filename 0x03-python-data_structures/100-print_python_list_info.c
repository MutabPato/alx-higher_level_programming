#define _POSIX_C_SOURCE 200809L
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to python object
 * Return: nothing.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "Object is not a Python List\n");
		return;
	}

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; ++i)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
