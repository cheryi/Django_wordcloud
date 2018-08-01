# Django_wordcloud
This repo is to produce wordcloud from news in remote database with Django.

install requirement :　python 3.6.5 , pymysql 0.9.2 , jieba 0.39 , Django 2.0.7

notice : variable 'ip' in connect_sql/views.py needs to be change.

If you want to load web template(.js/.css) , put them into 'static' directory.
.CSS → fix the 'href' in 'link' in 'web.html' like {% static 'yourcss.css' %}.
.js → fix the 'src' in <scrpit> in 'web.html' like src=<scrpit src="{% static 'yourjs.js' %}"></script>
