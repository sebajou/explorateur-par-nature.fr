import React, { Component } from 'react';
// import ReactDOM from 'react-dom';
import Login from './Login';
import Hello from './Hello';
// import Essai from './Essai';
import axiosInstance from "./AxiosAPI";
import Signup from './Signup';


class Welcome extends Component {
  constructor(props) {
      super(props);

      this.state = {openp: false, opens: false};

      this.handleLogout = this.handleLogout.bind(this);
      this.handleToggleLoginClick = this.handleToggleLoginClick.bind(this);
      this.handleToggleSignupClick = this.handleToggleSignupClick.bind(this);
  }


  async handleLogout() {
    try {
        const response = await axiosInstance.post('/blacklist/', {
            "refresh_token": localStorage.getItem("refresh_token")
        });
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        axiosInstance.defaults.headers['Authorization'] = null;
        this.setState({connected: false});
        console.log(this.state.connected)
        return response;
    }
    catch (e) {
        console.log(e);
    }
  };

  handleToggleLoginClick(event) {
    this.setState({openp: !this.state.openp});
  }

  handleToggleSignupClick(event) {
    this.setState({opens: !this.state.opens});
  }

  render() {
    const { openp, opens } = this.state

    return (
        <div className="container">
          <div className="button-container">
            <button className="button" onClick={this.handleToggleLoginClick}>
              Open Portal Modal
            </button>
          </div>
          <div className="button-container">
            <button className="button" onClick={this.handleLogout}>
              Logout
            </button>
          </div>
          <div className="button-container">
            <button className="button" onClick={this.handleToggleSignupClick}>
              Créer un profil
            </button>
          </div>
          

        <div>
            <Login
              message="Connexion Tuteur"
              isOpen={openp}
              onClose={this.handleToggleLoginClick}
            />
            <Signup
              message="Création d'un profil de tuteur"
              isOpen={opens}
              onClose={this.handleToggleSignupClick}
            />
            <Hello />
        </div>
    </div>
    );
  }
};

export default Welcome
