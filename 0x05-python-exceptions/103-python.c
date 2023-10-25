#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <floatobject.h>

/**
 * print_python_float - print information about python float
 * @p: a pointer of pyobject struct
 */
void print_python_float(PyObject *p)
{
	double b;

	setbuf (stdout, P NULL)
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float"))
	{
		printf("[ERROR] Invalid Float Object\n");
		return;
	}

	b = ((PyFloatobject *)p)->ob_fval:
	printf(" value: $s\n"
	PyOs_double _to_string(d, 'r', 0, Py_DTSE_ ADD_DOT_0, NULL)):}
