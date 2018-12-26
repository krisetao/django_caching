# django_caching

**django_caching** is an easy-to-use cache plugin for models in Django.

## How does it work?

**django_caching** caches all SQL queries called when cached objects requested. When the same SQL queries being excuted, there's no real database IO anymore.

**django_caching** automatically invalidates cache item when `save` or `delete`. 

## Compatibility

**django_caching** works well with Django 1.8 - 1.11 .

## Installation

You can install `django_caching` by `pip`

```shell
pip install django_caching
pip install python-memcached
```

It's also okay to install by clone this repository.

## Usage

### Step 1

Add `cache` in `INSTALLED_APPS` of your settings.

```python
INSTALLED_APPS = (
  ...,
  'cache',
)
```

### Step 2

Add `cache_manager` and `test` in `CACHES` of your settings.

```python
TESTING = {}
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'PREFIX': 'default',
    },
    'cache_manager': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'PREFIX': 'default::cache_manager',
    },
    'test': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'PREFIX': 'default::test',
    },
}
```

### Step 3

You should run `migrate` to apply the changes above.

```sh
python manage.py makemigrations
python manage.py migrate
```

### Step 4

Modify the models which you need to cache like this:

```python
from django.db import models
from cache.manager import CacheManager
from cache.constants import ONE_WEEK
# We have pre-define some constants for the duration time.
# You can also use number directly in denomination of second.

class DemoModel(models.Model):
    title = models.CharField('Demo', max_length=255)
    ……

    objects = models.Manager() # Use native Manager when 'objects' called 
    cached_objects = CacheManager(timeout=ONE_WEEK)
    # Use CacheManage when 'cached_objects' called.
    # timeout is defaultly set to ONE_DAY
```

Be careful ! `django_caching` wouldn't work properly if you give `CacheManager` another name instead of `cached_objects`.

### Step 5

Replace `DemoModel.objects` with `DemoModel.cached_objects` wherever you need cache.

We also provide a `get_cached_object_or_404` method to replace native `get_object_or_404` method.

```python
from cache.shortcuts import get_cached_object_or_404
from demo.models import DemoModel

……

demo = get_cached_object_or_404(DemoModel, title='demo')
demo2 = DemoModel.cached_objects.get(title='demo')
demos = DemoModel.cached_objects.all()
demos2 = DemoModel.cached_objects.filter(title__icontains='demo')
```

### Step 6

Have a coffee and enjoy the easy cache for your Django project!



## Watch Out!

**Cache can ONLY be invalidated automatically** when called by `cached_objects` or `get_cached_object_or_404` .



## Contributing

This package is maintained by [Jiuzhang](http://www.jiuzhang.com).

If you find a bug, you can open an issue and we will reply ASAP.

You can contribute to this repository by opening a pull request. We are glad to accept contribution from community.



