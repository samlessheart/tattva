from .models import Daily_thought
import redis
from tatva.settings import CELERY_BROKER_URL


def get_daily_thought():
    try:
        r = redis.Redis.from_url(  url = CELERY_BROKER_URL,  decode_responses=True )
        suvichar = r.get('daily_thought')
        if suvichar:
            
            return suvichar 
    
        else:
            suvichar = Daily_thought.objects.all().order_by('last_used')[0]

            r.set('daily_thought', suvichar.suvichar, ex=60*60*24)
            suvichar = suvichar

        return suvichar
    except:
        pass 

    


if __name__ == '__main__':
    get_daily_thought()




