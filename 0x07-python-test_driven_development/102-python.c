#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

void print_python_string(PyObject *p)
{

    printf("[.] string object info\n");
    if (!PyUnicode_Check(p))
    {
        fprintf(stderr, "  [ERROR] Invalid String Object\n");
        return;
    }
    PyUnicodeObject* unicodeObject = (PyUnicodeObject*)p;
    const char* typeName;
    if (PyUnicode_IS_COMPACT_ASCII(unicodeObject))
    {
        typeName = "compact ascii";
    }
    else
    {
        typeName = "compact unicode object";
    }
    printf("  Type: %s\n", typeName);

    Py_ssize_t length = PyUnicode_GET_LENGTH(p);
    printf("  Length: %zd\n", length);

    const char* value = PyUnicode_AsUTF8(p);
    printf("  Value: %s\n", value);
}