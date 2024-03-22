import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Switch, Redirect } from 'react-router-dom';
import axios from 'axios';

// Components
import Signup from './Signup';
import Login from './Login';
import Dashboard from './Dashboard';

function App() {
  const [loggedIn, setLoggedIn] = useState(false);

  // Function to handle login
  const handleLogin = async (credentials) => {
    try {
      const response = await axios.post('http://localhost:5000/login', credentials);
      const token = response.data.token;
      localStorage.setItem('token', token);
      setLoggedIn(true);
    } catch (error) {
      console.error('Login failed:', error);
    }
  };

  // Function to handle logout
  const handleLogout = () => {
    localStorage.removeItem('token');
    setLoggedIn(false);
  };

  return (
    <Router>
      <Switch>
        <Route path="/signup" component={Signup} />
        <Route path="/login">
          <Login handleLogin={handleLogin} />
        </Route>
        <PrivateRoute path="/dashboard" component={Dashboard} loggedIn={loggedIn} handleLogout={handleLogout} />
        <Route exact path="/">
          <Redirect to="/login" />
        </Route>
      </Switch>
    </Router>
  );
}

// PrivateRoute component to handle authorization
const PrivateRoute = ({ component: Component, loggedIn, handleLogout, ...rest }) => (
  <Route {...rest} render={(props) => (
    loggedIn ? (
      <Component {...props} handleLogout={handleLogout} />
    ) : (
      <Redirect to="/login" />
    )
  )} />
);

export default App;

Sure, I'll break down the code into separate components and provide the names for each component:
App Component (App.js)

This is the main component that handles routing and manages the authentication state.

javascript

// App.js

import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Switch, Redirect } from 'react-router-dom';
import axios from 'axios';

// Components
import Signup from './Signup';
import Login from './Login';
import Dashboard from './Dashboard';

function App() {
  const [loggedIn, setLoggedIn] = useState(false);

  // Function to handle login
  const handleLogin = async (credentials) => {
    try {
      const response = await axios.post('http://localhost:5000/login', credentials);
      const token = response.data.token;
      localStorage.setItem('token', token);
      setLoggedIn(true);
    } catch (error) {
      console.error('Login failed:', error);
    }
  };

  // Function to handle logout
  const handleLogout = () => {
    localStorage.removeItem('token');
    setLoggedIn(false);
  };

  return (
    <Router>
      <Switch>
        <Route path="/signup" component={Signup} />
        <Route path="/login">
          <Login handleLogin={handleLogin} />
        </Route>
        <PrivateRoute path="/dashboard" component={Dashboard} loggedIn={loggedIn} handleLogout={handleLogout} />
        <Route exact path="/">
          <Redirect to="/login" />
        </Route>
      </Switch>
    </Router>
  );
}

// PrivateRoute component to handle authorization
const PrivateRoute = ({ component: Component, loggedIn, handleLogout, ...rest }) => (
  <Route {...rest} render={(props) => (
    loggedIn ? (
      <Component {...props} handleLogout={handleLogout} />
    ) : (
      <Redirect to="/login" />
    )
  )} />
);

export default App;

//Login Component (Login.js)

// This component renders the login form and handles login functionality.

// Login.js

import React, { useState } from 'react';

function Login({ handleLogin }) {
  const [credentials, setCredentials] = useState({
    username: '',
    password: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setCredentials({
      ...credentials,
      [name]: value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    handleLogin(credentials);
  };

  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Username:</label>
          <input type="text" name="username" value={credentials.username} onChange={handleChange} />
        </div>
        <div>
          <label>Password:</label>
          <input type="password" name="password" value={credentials.password} onChange={handleChange} />
        </div>
        <button type="submit">Login</button>
      </form>
    </div>
  );
}

export default Login;

// Dashboard Component (Dashboard.js)

// This component represents the authenticated dashboard page.


// Dashboard.js

import React from 'react';

function Dashboard({ handleLogout }) {
  return (
    <div>
      <h2>Dashboard</h2>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
}

export default Dashboard;

// Signup Component (Signup.js)

// You would need to create this component to handle user signup. It's not provided in the initial code.

// Signup.js

import React from 'react';

function Signup() {
  // Implementation for signup form and functionality goes here
  return (
    <div>
      <h2>Signup</h2>
      {/* Signup form */}
    </div>
  );
}

export default Signup;
