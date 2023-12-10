#define _POSIX_C_SOURCE 200809L
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list - prints some basic info about Python lists
 * @p: pointer to python object
 * Return: nothing.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i;
	PyObject *item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", ((PyVarObject *)p)->ob_size);

	for (i = 0; i < ((PyVarObject *)p)->ob_size; ++i)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes -  prints some basic info about Python bytes objects
 * @p: pointer to python object
 * Return: nothing.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf(" Size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf(" trying string: %s\n", PyBytes_AsString(p));

	printf(" first 10 bytes: ");
	size = ((PyVarObject *)p)->ob_size;
	for (i = 0; i < 10 && i < size; ++i)
		printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);

	printf("\n");
}
