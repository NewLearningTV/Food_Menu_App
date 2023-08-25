from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# 각 식당 페이지에 대한 라우트 추가
@app.route('/restaurants/italian_a_1')
def italian_a():
    return render_template('restaurants/italian_a_1.html')

@app.route('/restaurants/italian_b_1')
def italian_b():
    return render_template('restaurants/italian_b_1.html')

@app.route('/restaurants/pizza_a_1')
def pizza_a():
    return render_template('restaurants/pizza_a_1.html')

@app.route('/restaurants/korean_a_1')
def korean_a():
    return render_template('restaurants/korean_a_1.html')

@app.route('/restaurants/chinese_a_1')
def chinese_a():
    return render_template('restaurants/chinese_a_1.html')

@app.route('/restaurants/burger_a_1')
def burger_a():
    return render_template('restaurants/burger_a_1.html')

@app.route('/restaurants/mexican_a_1')
def mexican_a():
    return render_template('restaurants/mexican_a_1.html')

@app.route('/restaurants/indian_a_1')
def indian_a():
    return render_template('restaurants/indian_a_1.html')

@app.route('/restaurants/japanese_a_1')
def japanese_a():
    return render_template('restaurants/japanese_a_1.html')

@app.route('/restaurants/french_a_1')
def french_a():
    return render_template('restaurants/french_a_1.html')

@app.route('/search', methods=['POST'])
def search():
    # 사용자로부터 데이터 받기
    food_type = request.json.get('food_type')
    location = request.json.get('location')
    
    # 예시 데이터
    all_restaurants = [
        {'name': 'Ristorante Mar', 'type': 'Italian', 'rating': 4.5, 'link': '/restaurants/italian_a_1', 'address': '123 Main St'},
        {'name': 'Ristorante Luna', 'type': 'Italian', 'rating': 4.7, 'link': '/restaurants/italian_b_1', 'address': '456 Johnson Blvd'},
        {'name': 'Lennys Detroit Style Pizza', 'type': 'Pizza', 'rating': 4.2, 'link': '/restaurants/pizza_a_1', 'address' : '789 E St'},
        {'name': 'Korean BBQ D', 'type': 'Korean', 'rating': 4.8, 'link': '/restaurants/korean_a_1', 'address':'11112 Riverlake Ln'},
        {'name': 'Chinese Takeout E', 'type': 'Chinese', 'rating': 4.6, 'link': '/restaurants/chinese_a_1', 'address':'2345 River St'},
        {'name': 'Burger Joint F', 'type': 'Burger', 'rating': 4.4, 'link': '/restaurants/burger_a_1', 'address':'2117 River St'},
        {'name': 'Taco Stand G', 'type': 'Mexican', 'rating': 4.3, 'link': '/restaurants/mexican_a_1', 'address':'78 Capital Blvd'},
        {'name': 'Indian Curry House H', 'type': 'Indian', 'rating': 4.9, 'link': '/restaurants/indian_a_1', 'address': '9900 Lincoln Blvd' },
        {'name': 'Japanese Sushi I', 'type': 'Japanese', 'rating': 4.0, 'link': '/restaurants/japanese_a_1', 'address': '1220 South Bend Ln'},
        {'name': 'French Bistro J', 'type': 'French', 'rating': 4.1, 'link': '/restaurants/french_a_1', 'address':'440 North Highway Blvd'}
    ]
    
    # 음식 종류와 주소로 결과 필터링
    filtered_restaurants = [
        restaurant for restaurant in all_restaurants 
        if food_type.lower() in restaurant['type'].lower() and location.lower() in restaurant['address'].lower()
    ]
    
    # 레이팅 순으로 정렬하고 최대 3개만 반환
    sorted_restaurants = sorted(filtered_restaurants, key=lambda x: x['rating'], reverse=True)[:3]
    
    return jsonify(sorted_restaurants)

@app.route('/all_restaurants')
def all_restaurants():
    restaurants = [
        {'name': 'Ristorante Mar', 'link': '/restaurants/italian_a_1'},
        {'name': 'Ristorante Luna', 'link': '/restaurants/italian_b_1'},
        {'name': "Lenny's Detroit Style Pizza", 'link': '/restaurants/pizza_a_1'},
        {'name': "Na Moo", 'link': '/restaurants/korean_a_1'},
        {'name': "Joyful Dim Sum House", 'link': '/restaurants/chinese_a_1'},
        {'name': "King of Burgers", 'link': '/restaurants/burger_a_1'},
        {'name': "Taco Feliz", 'link': '/restaurants/mexican_a_1'},
        {'name': "New Delhi Indian House", 'link': '/restaurants/indian_a_1'},
        {'name': "Sushi New", 'link': '/restaurants/japanese_a_1'},
        {'name': "Cafe Nice", 'link': '/restaurants/french_a_1'},
        # ... 필요에 따라 추가하세요
    ]

    return render_template('all_restaurants.html', restaurants=restaurants)


if __name__ == '__main__':
    app.run(debug=True, port=8001)
