from django.shortcuts import render

#for connect to db
import pymysql
#jieba
import jieba
import jieba.analyse
#to load file
import os
#dump output to json
import json

#tag_1=topics [科技,財經,運動,娛樂,政治,健康]
#title=title
#detailed_info=news article

def connect_sql(topic):
	#connect to db, return list of articles
	ip='database ip'
	user = 'iir'
	passwd = 'iir_5757'
	db = 'computex2018'
	conn = pymysql.connect(host=ip,user=user,passwd=passwd,db=db,charset="utf8")
	cur = conn.cursor()
	
	#cur.execute('SELECT COUNT(*)title FROM news WHERE title LIKE "%iphone%";')
	articles=[]
	cur.execute('SELECT detailed_info FROM news WHERE tag_1="政治";')
	#cur.execute('SELECT detailed_info FROM news WHERE tag_1=topic;')
	
	for row in cur:#row's type is tuple
		articles.append(row[0])
	
	cur.close()
	conn.commit()
	conn.close()

	return articles
	
	
def tokenization(articles):
	

	#tokenization and tf-idf
	vocabulary=[]
	final_tf={}

	module_dir = os.path.dirname(__file__)  # get current directory
	#file_path = os.path.join(module_dir, 'baz.txt')

	jieba.load_userdict(os.path.join(module_dir,"userdict.txt"))
	jieba.analyse.set_stop_words(os.path.join(module_dir,"stop_words.txt"))
	for each in articles:
		tags=jieba.analyse.extract_tags(each, topK=10, withWeight=False, allowPOS=('n','ns','nz'))
		for t in tags:
			if t not in vocabulary:
				vocabulary.append(t)
				final_tf[t]=1
			else:
				final_tf[t]+=1
	sort_final_tf=sorted(final_tf.items(), key=lambda kv: kv[1],reverse=True)#list of tuple

	result_list=[]
	for each in sort_final_tf:
		#{text: "Lorem", weight: 13},
		result_list.append({'text':each[0],'weight':each[1]})
	
	return result_list


def connect_to_sql(request):
	
	#articles=connect_to_sql("政治")
	#connect to db, return list of articles
	
	ip='140.116.247.169'
	user = 'iir'
	passwd = 'iir_5757'
	db = 'computex2018'
	conn = pymysql.connect(host=ip,user=user,passwd=passwd,db=db,charset="utf8")
	
	cur = conn.cursor()
	cur.execute('SELECT detailed_info FROM news WHERE tag_1="政治"')
	particles=[]	
	for row in cur:#row's type is tuple
		particles.append(row[0])
	cur.close()

	cur = conn.cursor()
	cur.execute('SELECT detailed_info FROM news WHERE tag_1="運動"')
	sarticles=[]	
	for row in cur:#row's type is tuple
		sarticles.append(row[0])
	cur.close()

	cur = conn.cursor()
	cur.execute('SELECT detailed_info FROM news WHERE tag_1="財經"')
	earticles=[]	
	for row in cur:#row's type is tuple
		earticles.append(row[0])
	cur.close()

	cur = conn.cursor()
	cur.execute('SELECT detailed_info FROM news WHERE tag_1="娛樂"')
	aarticles=[]	
	for row in cur:#row's type is tuple
		aarticles.append(row[0])
	cur.close()

	cur = conn.cursor()
	cur.execute('SELECT detailed_info FROM news WHERE tag_1="科技"')
	tarticles=[]	
	for row in cur:#row's type is tuple
		tarticles.append(row[0])
	cur.close()

	cur = conn.cursor()
	cur.execute('SELECT detailed_info FROM news WHERE tag_1="健康"')
	harticles=[]	
	for row in cur:#row's type is tuple
		harticles.append(row[0])
	
	#cur.execute('SELECT COUNT(*)title FROM news WHERE title LIKE "%iphone%";')

	cur.close()
	conn.commit()
	conn.close()

	politics_titles=tokenization(particles)
	tech_titles=tokenization(tarticles)
	sport_titles=tokenization(sarticles)
	art_titles=tokenization(aarticles)
	health_titles=tokenization(harticles)
	econ_titles=tokenization(earticles)

	#data to web
	parameters = {'politics_titles':politics_titles,'tech_titles':tech_titles,'sport_titles':sport_titles,'econ_titles':econ_titles,'art_titles':art_titles,'health_titles':health_titles}
	#parameters = {'politics_titles':politics_titles,'tech_titles':tech_titles}
	return render(request, 'sql_web.html', parameters)

