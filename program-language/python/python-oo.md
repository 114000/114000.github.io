---
title: Python OO
date: 2018-08-18
tag:
- python
- oo
---

## class

```python
class Man:
  def __init__ (self, name):
    self.name = name
  
  def hello (self):
    print('Hello ' + self.name + '!')


m = Man('David')
m.hello() # Hello David!
```