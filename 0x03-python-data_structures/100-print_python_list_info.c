#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints information about a Python list object
 * @p: Pointer to the Python list object
 *
 * Description: This function prints the size and allocation information of
 *              the given Python list object, as well as the type name of the
 *              first five elements in the list.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	PyTypeObject *type = Py_TYPE(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);
	printf("[*] Element 0: %s\n", Py_TYPE(PyList_GetItem(p, 0))->tp_name);
	printf("[*] Element 1: %s\n", Py_TYPE(PyList_GetItem(p, 1))->tp_name);
	printf("[*] Element 2: %s\n", Py_TYPE(PyList_GetItem(p, 2))->tp_name);
	printf("[*] Element 3: %s\n", Py_TYPE(PyList_GetItem(p, 3))->tp_name);
	printf("[*] Element 4: %s\n", Py_TYPE(PyList_GetItem(p, 4))->tp_name);
}

