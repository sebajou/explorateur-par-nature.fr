import React, { Component } from 'react';
import Login from './Login';
import Signup from './Signup';
import Logout from './Logout';


class Welcome extends Component {
  constructor(props) {
      super(props);

      this.state = {openp: false, opens: false, openl: false};

      this.handleToggleLoginClick = this.handleToggleLoginClick.bind(this);
      this.handleToggleSignupClick = this.handleToggleSignupClick.bind(this);
      this.handleToggleLogoutClick = this.handleToggleLogoutClick.bind(this);
  }

  handleToggleLoginClick(event) {
    this.setState({openp: !this.state.openp});
  }

  handleToggleLogoutClick(event) {
    this.setState({openl: !this.state.openl});
  }

  handleToggleSignupClick(event) {
    this.setState({opens: !this.state.opens});
  }

  render() {
    const { openp, opens, openl } = this.state

    return (
        <div className="container">
          <div className="button-container">
            <button className="button" onClick={this.handleToggleLoginClick}>
              Open Portal Modal
            </button>
          </div>
          <div className="button-container">
            <button className="button" onClick={this.handleToggleLogoutClick}>
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
            <Logout
              message="Voulez vous vous déconnecter ? "
              isOpen={openl}
              onClose={this.handleToggleLogoutClick}
            />
            <Signup
              message="Création d'un profil de tuteur"
              isOpen={opens}
              onClose={this.handleToggleSignupClick}
            />
        </div>
    </div>
    );
  }
};

export default Welcome