#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
    Py_ssize_t i, size;
    PyObject *obj;

    if (!PyList_Check(p))
    {
        printf("[*] Python list info\n  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Python list info\n  [*] Size of the Python List = %ld\n  [*] Allocated = %ld\n", size, ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        obj = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
    }
}

void print_python_bytes(PyObject *p)
{
    Py_ssize_t i, size;
    char *buffer;

    if (!PyBytes_Check(p))
    {
        printf("[*] Python bytes info\n  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    printf("[*] Python bytes info\n  [*] Size of the Python Bytes = %ld\n", size);

    buffer = PyBytes_AsString(p);
    printf("  [*] Bytes: ");
    for (i = 0; i < size && i < 10; i++)
        printf("%02x ", buffer[i] & 0xff);
    printf("\n");
}

void print_python_float(PyObject *p)
{
    if (!PyFloat_Check(p))
    {
        printf("[*] Python float info\n  [ERROR] Invalid Float Object\n");
        return;
    }

    printf("[*] Python float info\n  [*] value: %f\n", ((PyFloatObject *)p)->ob_fval);
}
