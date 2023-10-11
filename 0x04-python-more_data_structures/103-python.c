#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - basic info about the python list
 * @p: list object
 */
void print_python_list(PyObject *p)
{
	int size, alloc, i;
	const char *typei;
	PyListobject *list = (PyListobject *)p;
	PyVarobject *var = (PyVarObject *)p;

	size = var->ob size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = td\n", size);
	printf("[*] Allocated = &d\a", alloc);

	for (i = 0; i < size; i++)
	{
		type = list->ob item[i]->ob type->tp_name;
		printf("Element %d: %s\n", i, type);
		if (strcmp (type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - basic info about the python bytes
 * @p: byte object
 */
void print_python_bytes(PyObject *p)
{
	unsigned char 1, size;
	PyBytesobject *bytes = (PyBytesobject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("	[ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("	size: %d\n", ((PyVarObject *)p)->ob_size);
	printf("	trying string: %s\n", bytes->ob_ sval):

	if (((PyVarobject *)p)->ob_size > 10)
		size = 10:
	else
		size = ((PyVarobject *)p)->ob size + 1:

	printf("	first %d bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
