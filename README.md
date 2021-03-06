# Copulae

Copulae is a package used to model complex dependency structures. Copulae implements common and
popular copula structures to bind multiple univariate streams of data together. All copula 
implemented are multivariate by default. 

###### Continuous Integration

[![Build Status](https://travis-ci.com/DanielBok/copulae.svg?branch=master)](https://travis-ci.com/DanielBok/copulae)

###### Documentation

[![Documentation Status](https://readthedocs.org/projects/copulae/badge/?version=latest)](https://copulae.readthedocs.io/en/latest/?badge=latest)

###### Coverage

[![Coverage Status](https://coveralls.io/repos/github/DanielBok/copulae/badge.svg?branch=master)](https://coveralls.io/github/DanielBok/copulae?branch=master)

## Installing

Install and update using [pip](https://pip.pypa.io/en/stable/quickstart/)

```bash
pip install -U copulae
```

Still working on the conda build. Please wait a while more!!  

## Documentation

The documentation is located at https://copulae.readthedocs.io/en/latest/. Please check it out. :)


## Simple Usage

```python
from copulae import NormalCopula
import numpy as np

np.random.seed(8)
data = np.random.normal(size=(300, 8))
cop = NormalCopula(8)
cop.fit(data)

cop.random(10)  # simulate random number

# getting parameters
print(cop.params)  

# overriding parameters
cop[:] = np.eye(8)  # in this case,  setting to independent Gaussian Copula
```

I'll work on the docs and other copulas as soon as I can!


## Acknowledgements

Most of the code has been implemented by learning from others. Copulas are not the easiest
beasts to understand but here are some items that helped me along the way. I would recommend
all the works listed below.

#### [Elements of Copula Modeling with R](https://www.amazon.com/Elements-Copula-Modeling-Marius-Hofert/dp/3319896342/)

I referred quite a lot to the textbook when first learning. The authors give a pretty thorough explanation 
of copula from ground up. They go from describing when you can use copulas for modeling to the different 
classes of copulas to how to fit them and more.

#### [Blogpost from Thomas Wiecki](https://twiecki.io/blog/2018/05/03/copulas/) 

This blogpost gives a very gentle introduction to copulas. Before diving into all the complex math you'd 
find in textbooks, this is probably the best place to start. 


## Motivations

I started working on the copulae package because I couldn't find a good existing package that does
multivariate copula modeling. Presently, I'm building up the package according to my needs at work.
If you feel that you'll need some features, you can drop me a message. I'll see how I can schedule it. 😊
## TODOS

- [ ] Set up package for pip and conda installation
- [ ] More documentation on usage and post docs on rtd
- [ ] Elliptical Copulas
    - [x] Gaussian (Normal)
    - [x] Student (T)
- [ ] Implement in Archmedeans copulas
    - [x] Clayton
    - [x] Gumbel
    - [ ] Frank
    - [ ] Joe
    - [ ] AMH 
- [ ] Implement goodness of fit
- [ ] Implement mixed copulas
- [ ] Implement more solvers
- [ ] Implement convenient graphing functions
