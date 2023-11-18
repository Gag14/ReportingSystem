function login() {
    // Get form data
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // TODO: Implement login logic and API call
    console.log('Login clicked');
    console.log('Username:', username);
    console.log('Password:', password);
     fetch('http://127.0.0.1:5000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
}
