import orm
from models import User, Blog, Comment
import asyncio

loop = asyncio.get_event_loop()
@asyncio.coroutine
def test():
    yield from orm.create_pool(loop=loop, user='www-data', password='www-data', db='aaa')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()

loop.run_until_complete(test())