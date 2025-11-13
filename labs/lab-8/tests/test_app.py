# TODO: add five more unit test cases

def test_home_page(client):
    """Test that home page loads"""
    response = client.get('/')
    assert response.status_code == 200

def test_login_page(client):
    """Test that home page loads"""
    response = client.get('/login')
    assert response.status_code == 200

def test_users_page(client):
    """Test that users page loads"""
    response = client.get('/users')
    assert response.status_code == 200

def test_invalid_first_name(client):
    """Test signup validation for invalid first name"""
    response = client.post('/signup', data={
        'FirstName': '123',  # invalid - contains numbers
        'LastName': 'Doe',
        'Email': 'test@test.com',
        'PhoneNumber': '1234567890',
        'Password': 'password123'
    })
    assert b'First name can only contain letters' in response.data

def test_invalid_phone_number(client):
    """Test signup validation for invalid phone number"""
    response = client.post('/signup', data={
        'FirstName': 'John',
        'LastName': 'Doe',
        'Email': 'test@test.com',
        'PhoneNumber': '123',  # invalid - not 10 digits
        'Password': 'password123'
    })
    assert b'Phone number must be exactly 10 digits' in response.data

def test_invalid_password(client):
    response = client.post('/signup', data={
        'FirstName': 'John',
        'LastName': 'Doe',
        'Email': 'test', #Email must have a proper web-based mailing provider
        'PhoneNumber': '1234567890',
        'Password': 'password123' 
    })
    assert b'Invalid Email must incude an @ and a web-based email provider ex.(@gmail.com, @aol.com, @yahoo.com)'

def test_error_page(client):
    response = client.get('/error')
    assert response.status_code == 200
    #See if the error page comes up if an error were to occur

def test_success_page(client):
    response = client.get('/success')
    assert response.status_code == 200
    #Sees when a success page when a login occurs if credentials are correct

def test_valid_email_login(client):
    #Testing if the email provider is valid when logining in
    Email = "John.Doe@yahoo.com"
    Password ="Hello90"
    client.post('/signup', data={
        'FirstName': 'John',
        'LastName': 'Doe',
        'Email': Email,
        'PhoneNumber': '1234567890',
        'Password': Password 
    })

    response = client.post('/login', data={
        'Email': Email,
        'Password': Password
    })

    assert b'Succesful Login'

def test_wrong_password_login(client):
    email = 'John.Doe@gmail.com'
    correct_pw = 'Hello900'
    incorrect_pw = 'Byeee800'

    client.post('/signup', data={
        'FirstName': 'John',
        'LastName': 'Doe',
        'Email': email,
        'PhoneNumber': '1234567890',
        'Password': correct_pw 
    })

    response = client.post('/login', data={
        'Email': email,
        'Password': incorrect_pw
    })

    assert b'Incorrect Login Credentials try again'
