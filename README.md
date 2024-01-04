# Web testing w/ Selenium + Python
 
Web Apps automation using Selenium + Python + Behave 

---
## Setup  

### Sauce Labs setup
1. Free [Sauce account](https://saucelabs.com/sign-up)
2. Make sure you know how to find your Sauce Labs Username and Access Key by going to the [Sauce Labs user settings page](https://app.saucelabs.com/user-settings)

---
### Selenium setup
1. We will run our automated tests on Sauce Labs Virtual devices (VMs); therefore, there is no need to install Selenium Grid or browsers drivers.

---
### Python and Behave setup
1. Install the Python packages:
2. pip install selenium==4.15.2
3. pip install behave

---

## Run your behave tests

Run the tests on the Sauce EU DC:

```java
        behave -c

```

## Run your tests without behave

Run the tests on the Sauce EU DC:

```java
         python3 ./testcases/myTest.py

```

## Extra resources

- [Selenium on Sauce Labs](https://docs.saucelabs.com/web-apps/automated-testing/selenium/)
