```
 ____   ____ ____ 
|  _ \ / ___/ ___|
| | | | |  | |    
| |_| | |__| |___ 
|____/ \____\____|
                  
```
<div align="center">

[![GitHub Issues](https://img.shields.io/github/issues/53jk1/distributed-cipher-cracking.svg)](https://github.com/53jk1/distributed-cipher-cracking/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/53jk1/distributed-cipher-cracking.svg)](https://github.com/53jk1/distributed-cipher-cracking/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center">
Preparation of a laboratory station for analysing the effectiveness of selected methods of cracking cipher algorithms with the use of the Python language. In the article I will present the technique of breaking ciphers with brute force, I will analyse the frequency of breaking passwords depending on their difficulty level.
    <br> 
</p>

## 🧐 About <a name = "about"></a>

Preparation of a laboratory station for analysing the effectiveness of selected methods of cracking cipher algorithms with the use of the Python language. In the article I will present the technique of breaking ciphers with brute force, I will analyse the frequency of breaking passwords depending on their difficulty level. 

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them.

```
Python 3.8
python3-pip
```

### Installing

A step by step series of examples that tell you how to get a development env running.

Firstly check if you have installed Python, and pip.
The names may vary slightly.
```
~$ which pip3
/usr/bin/pip3
~$ which python3
/usr/bin/python3
```
If you are sure you have Python and pip, `cd` in the folder with the script, then use this command to install all the dependencies. You can skip this step if you are sure you have all the libraries needed to run the project.
```
~/distributed-cipher-cracking$ pip3 install -r requirements.txt
```


## 🔧 Benchmarks <a name = "benchmarks"></a>

```
python3 main.py "test" "test" 130 90
```

## ⛏️ Built Using <a name = "built_using"></a>

- [pycrypto](https://pypi.org/project/pycrypto/)
- [PyCryptodome](https://pycryptodome.readthedocs.io/en/latest/) 
- [Rich 11.2.0](https://rich.readthedocs.io/en/stable/introduction.html)
- [psutil](https://psutil.readthedocs.io/en/latest/)

## ✍️ Authors <a name = "authors"></a>

- [@53jk1](https://github.com/53jk1)
- [@Desukiteru](https://github.com/Desukiteru)
