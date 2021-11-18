import axios from 'axios';

class AuthService {
  login(user) {
    const data = new URLSearchParams({
      'email': user.email,
      'password': user.password
    });

    return axios
      .post(process.env.VUE_APP_API_URL + '/users/login', data, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      })
      .then(response => {
        if (response.data.access_token) {
          const user = {
            id: response.data.user.id,
            name: response.data.user.name,
            email: response.data.user.email,
            access_token: response.data.access_token,
          };
          localStorage.setItem('user', JSON.stringify(user));

          return user;
        }

        return null;
      });
  }

  logout() {
    localStorage.removeItem('user');
  }

  register(user) {
    return axios.post(process.env.VUE_APP_API_URL + '/users', {
      name: user.name,
      email: user.email,
      password: user.password
    });
  }
}

export default new AuthService();