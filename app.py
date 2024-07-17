from flask import Flask, request, jsonify
#import boto3
import uuid
app = Flask(__name__)

# Initialize DynamoDB resource
#dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
#table = dynamodb.Table('users')  # Replace 'Users' with your DynamoDB table name

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    user_ID=str(uuid.uuid4())
    data['id']=user_ID
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    dateofbirth=data.get('dateofbirth')
    gender=data.get('gender')

    # Add more fields as needed
    
    # Check if required fields are present
    if  not username or not email   or not dateofbirth :
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Put user information into DynamoDB
#    table.put_item(Item={
 #       'user_id': user_ID,
  #      'username': username,
   #     'email': email,
    #    'password': password,
     #   'dateofbirth':dateofbirth,
        
        # Add more fields as needed
    #})
    
    return jsonify({'message': 'User information submitted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)





    @app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    try:
        response = user_table.get_item(Key={'username': data['username']})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    if 'Item' not in response:
        return jsonify({"error": "User not found"}), 404
    
    user = response['Item']
    
    if not check_password_hash(user['password'], data['password']):
        return jsonify({"error": "Invalid password"}), 401
    
    return jsonify({"message": "Login successful"}), 200