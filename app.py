from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from selenium import webdriver

from pymongo import MongoClient
client = MongoClient('mongodb+srv://minji:0819@Cluster0.vdsdj.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('lang=ko_KR')
# chromedriver_path = "chromedriver"
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3)
# driver = webdriver.Chrome(os.path.join(os.getcwd(), chromedriver_path), options=options)

driver.get(url='https://map.kakao.com/')
driver.find_element_by_xpath('//*[@id="search.keyword.query"]').send_keys('신도저리')


# driver.find_element_by_xpath()


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/restaurant", methods=["POST"])
def restaurant_post():
    url_receive = request.form['url_give']
    star_receive = request.form['star_give']
    writer_receive = request.form['writer_give']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    # 여기에 코딩을 해서 meta tag를 먼저 가져와보겠습니다.
    name = soup.select('')
    # image = soup.select_one('# ibu_1')
    # address = soup.select_one('# app-root > div > div > div > div:nth-child(5) > div > div.place_section.no_margin._18vYz > div > ul > li._1M_Iz._1aj6- > div > a > span._2yqUQ')

    print(name)
    # doc = {
    #     'name': name,
    #     'image': image,
    #     'address': address,
    #     'star': star_receive,
    #     'writer': writer_receive,
    # }
    #
    # db.restaurants.insert_one(doc)

    return jsonify({'msg':'저장 완료!'})

@app.route("/movie", methods=["GET"])
def movie_get():
    movie_list = list(db.movies.find({}, {'_id': False}))
    return jsonify({'movies': movie_list})

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/sign_up')
def sign_up():
    return render_template('signUp.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)