"""
This will import all modules with name groupN.py (1 <= N <= 50)
and print the result of the corresponding tweet() function
implemented in groupN.py.
"""

for i in range(1, 51):
    module_name = "group{}".format(i)
    try:
        module = __import__(module_name)
        print("group {0} says: {1}".format(i, module.tweet()))
    except ImportError:
        pass
