'''
create obj
'''

data = {'user': 1}
serializer = StatusSerializer(data=data)
serializer.is_valid()
'''
Update obj
'''

obj = Status.objects.first()

data = {'content': 'some new content', "user": 1}
up_ser = StatusSerializer(obj, data=data)
up_ser.is_valid()
# True
up_ser.save()
# <Status: some new content>
