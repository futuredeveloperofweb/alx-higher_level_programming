#include <Python.h>

/**
 * python_info - display the basics of the python lists
 * @p: PyObject list
 */
void python_info(PyObject *p)
{
	int size, a, i;
	PyObject *obj;

	size = Py_SIZE(p);
	a = ((PyListObject *)p)->allocated;

	printf("[*] Size of python list = %d\n", size);
	printf("[*] Allocated = %d\n", a);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
