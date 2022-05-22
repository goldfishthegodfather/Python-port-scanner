![Badge tracking project size](https://img.shields.io/github/repo-size/Preffet/Python-port-scanner?color=%23611487)![Badge tracking code size](https://img.shields.io/github/languages/code-size/Preffet/Python-port-scanner?color=%23361487)![Badge tracking last commit](https://img.shields.io/github/last-commit/Preffet/Python-port-scanner?color=%23142d87)
-----------------------------------------------------------------------------

![banner](https://user-images.githubusercontent.com/84241003/161392493-8540fc6d-930c-458f-a33a-4fce3da2f3a7.png)

-----------------------------------------------------------------------------

### Description

This is a port scanner project written in Python. It was created for freecodecamp "Information Security" course "Port Scanner" assignment.

-----------------------------------------------------------------------------

### get_open_ports function

In the `port_scanner.py` file, a function called `get_open_ports` takes a `target` argument and a `port_range` argument. `target` can be a URL or IP address. `port_range` is a list of two numbers indicating the first and last numbers of the range of ports to check. Then this function returns a list of open ports in the given range.

Here are examples of how the function may be called:

```
get_open_ports("209.216.230.240", [440, 445])
get_open_ports("www.stackoverflow.com", [79, 82])
```

The `get_open_ports` function also takes an optional third argument of `True` to indicate "Verbose" mode. If this is set to true, it returns a descriptive string instead of a list of ports.

Here is the format of the string that is returned in verbose mode:

```
Open ports for {URL} ({IP address})
PORT     SERVICE
{port}   {service name}
{port}   {service name}
```

-----------------------------------------------------------------------------

### Errors

If the URL passed into the `get_open_ports` function is invalid, the function returns the string: "Error: Invalid hostname".

If the IP address passed into the `get_open_ports` function is invalid, the function returns the string: "Error:  Invalid IP address".

-----------------------------------------------------------------------------

### Testing

The unit tests for this project are in `test_module.py`. They are imported from `test_module.py` to `main.py` and will run automatically when you run the project.
