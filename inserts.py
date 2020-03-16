from utils.database import Users, Albums, Images, Tags, Tag_Types, Image_Tags
from utils.base import session_factory, engine, Base

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# populate database
amy = Users(net_id='jyxu')
lrrh = Albums(name='little red', user=amy)
aiwl = Albums(name='alice wonderland', user=amy)

sentiment = Tag_Types(name='sentiment')
object = Tag_Types(name='object')

truck = Tags(name='truck', confidence=50, type=object)
happy = Tags(name='happy', confidence=70, type=sentiment)

img1 = Images(album=aiwl)
img2 = Images(album=lrrh)

img1.tags.append(truck)
img1.tags.append(happy)
img2.tags.append(truck)

sess = session_factory()
sess.add(amy)
sess.add(lrrh)
sess.add(aiwl)
sess.add(sentiment)
sess.add(object)
sess.add(truck)
sess.add(happy)
sess.add(img1)
sess.add(img2)

sess.commit()
sess.close()
