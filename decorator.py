def simple_decorator(decorator):
       def new_decorator(f):
           g = decorator(f)
           g.__name__ = f.__name__
           g.__doc__ = f.__doc__
           g.__dict__.update(f.__dict__)
           return g
       # Now a few lines needed to make simple_decorator itself
       # be a well-behaved decorator.
       new_decorator.__name__ = decorator.__name__
       new_decorator.__doc__ = decorator.__doc__
       new_decorator.__dict__.update(decorator.__dict__)
       return new_decorator
   
   #
   # Sample Use:
   #
@simple_decorator
def my_simple_logging_decorator(func):
    def you_will_never_see_this_name(*args, **kwargs):
        print 'calling {}'.format(func.__name__)
        return func(*args, **kwargs)
    return you_will_never_see_this_name
   
@my_simple_logging_decorator
def double(x):
   'Doubles a number.'
   return 2 * x
   
assert double.__name__ == 'double'
assert double.__doc__ == 'Doubles a number.'
print double(155)
