from requests import get, post, delete
#
print(get('http://localhost:8000/api/v2/news').json())
#
# print(get('http://localhost:8000/api/news/1').json())
#
# print(get('http://localhost:8000/api/news/999').json())
# # новости с id = 999 нет в базе
# print(get('http://localhost:8000/api/news/q').json())

# print(post('http://localhost:8000/api/news').json())
# print(post('http://localhost:8000/api/news',
#            json={'title': 'Заголовок'}).json())
print(post('http://localhost:8000/api/v2/news',
           json={'title': 'apishechka',
                 'content': 'super api conquest',
                 'user_id': 1,
                 'is_private': False}).json())

# print(delete('http://localhost:8000/api/news/999').json())
# # новости с id = 999 нет в базе
#
# print(delete('http://localhost:8000/api/news/1').json())