import requests
import json

def get_randomuser_full_data():
    url = 'https://randomuser.me/api/'

    response = requests.get(url)
    data = response.json()
    return data['results'][0]
    


def get_user_data(user: dict):
    full_name = user['name']['first'] + ' ' + user['name']['last']

    phone = user['phone']
    email = user['email']
    age = user['dob']['age']
    nat = user['nat']
    gender = user['gender']
    country = user['location']['country']

    data = {
        'full_name': full_name,
        'phone': phone,
        'email': email,
        'age': age,
        'nat':nat,
        'gender':gender,
        'country':country
    }
    return data



    


def main() -> None:
    females = []
    males = []
    while len(females) < 10 or len(males) < 10:
        user = get_randomuser_full_data()
        user_data = get_user_data(user)
        if user_data['gender'] == 'female' and len(females) < 10:
            females.append(user_data)
        if user_data['gender'] == 'male' and len(males) < 10:
            males.append(user_data)
        all_users = {
        'female': females,
        'male': males
    }

        

    with open('users.json', 'w') as f:
        json.dump(all_users, f, indent=4)


main()