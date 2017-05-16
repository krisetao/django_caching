# django_caching

本项目由[九章算法](www.jiuzhang.com)开发维护并开源，[九章算法](www.jiuzhang.com)——硅谷顶尖IT企业工程师实时在线授课为您传授面试技巧, 帮助更多中国人找到好工作。

django_caching是一个十分易于使用的针对model的缓存插件。原理是缓存下所有用过的sql，这样下次执行同一条sql的时候就不需要真正进行db query了。并且django_caching会自动进行cache的invalidation（save或者delete的时候），不需要人工干预。

### 使用方法：

在项目的`settings.py`里面的`INSTALLED_APPS`里加入`cache`:

```Python
INSTALLED_APPS = (
    ...,
    'cache',
)
```

然后在`CACHES`里面加入`cache_manager`和`test`：

```Python
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

然后执行：

```Sh
python manage.py migrate
```

这样配置就完成了。

然后在所有需要使用的models中进行修改：

```Python
from django.db import models
from cache.manager import CacheManager

class DemoModel(models.Model):
    title = models.CharField('Demo', max_length=255)
    ...
    
    # for cache
    objects = models.Manager()
    cached_objects = CacheManager()
```

之后将代码中所有用到`DemoModel.objects`的地方改成`DemoModel.cached_objects`，在所有用到`get_object_or_404`的地方改成：

```Python
from cache.shortcuts import get_cached_object_or_404
from demo.models import DemoModel

...
demo = get_cached_object_or_404(DemoModel, title='demo')
```

__一定要用cached_objects和get_cached_object_or_404，否则如果进行了更改，save或者delete之后不会自动invalidate cache！ __

__一定要用cached_objects和get_cached_object_or_404，否则如果进行了更改，save或者delete之后不会自动invalidate cache！ __

__一定要用cached_objects和get_cached_object_or_404，否则如果进行了更改，save或者delete之后不会自动invalidate cache！ __



本项目由[九章算法](www.jiuzhang.com)开发维护并开源，[九章算法](www.jiuzhang.com)——硅谷顶尖IT企业工程师实时在线授课为您传授面试技巧, 帮助更多中国人找到好工作。

文档编辑：[Pure White](https://purewhite.io)
