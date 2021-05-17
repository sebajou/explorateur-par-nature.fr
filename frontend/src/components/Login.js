import React, { Component } from "react";
import ReactDOM from 'react-dom';
import axiosInstance from "./AxiosAPI";
import '../styles/Login.css';
import '../styles/styles.css';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import { faTimes } from "@fortawesome/free-solid-svg-icons";

library.add(faTimes);

class Login extends Component {
    constructor(props) {
        super(props);
        this.state = {username: "", password: "", connected: false};
        // this.state = { message: "Connexion Tuteur"}

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleSubmitWThen = this.handleSubmitWThen.bind(this);
    }

    handleChange(event) {
        this.setState({[event.target.name]: event.target.value});
    }

    handleSubmitWThen(event){
        event.preventDefault();
        axiosInstance.post('/token/obtain/', {
                username: this.state.username,
                password: this.state.password
            }).then(
                result => {
                    axiosInstance.defaults.headers['Authorization'] = "JWT " + result.data.access;
                    localStorage.setItem('access_token', result.data.access);
                    localStorage.setItem('refresh_token', result.data.refresh);
                    this.setState({connected: true});
                    console.log(this.state.connected)
                }
            ).catch (error => {
                throw error;
            })
    }

    async handleSubmit(event) {
        event.preventDefault();
        try {
            const response = await axiosInstance.post('/token/obtain/', {
                username: this.state.username,
                password: this.state.password
            });
            axiosInstance.defaults.headers['Authorization'] = "JWT " + response.data.access;
            localStorage.setItem('access_token', response.data.access);
            localStorage.setItem('refresh_token', response.data.refresh);
            this.setState({connected: true});
            console.log(this.state.connected)
            return response;
        } catch (error) {
            throw error;
        }
    }

  render() {

  const { message, isOpen, onClose} = this.props;
  
  if (!isOpen) return null;

  return ReactDOM.createPortal(
      
    <div className="modal">
    <div className="container">
        <div className="row">
            <div className="col-12">
                <button className="close" onClick={onClose}>
                    <FontAwesomeIcon icon={["fas", "times"]} />
                </button>
            </div>
        </div>
        <div className="row">
            <div className="col-10 center-block">
                <h2>{message}</h2>
            </div>
        </div>
        <form onSubmit={this.handleSubmit}>
          <div className="row col-12 center-block">
              <label>
                  <input name="username" type="text" value={this.state.username} onChange={this.handleChange}
                  placeholder="nom d'utilisateur"/>
              </label>
          </div>
          <div className="row center-block col-12">
              <label>
                  <input name="password" type="password" value={this.state.password} onChange={this.handleChange}
                  placeholder="mot de passe"/>
              </label>
          </div>
          <div className="row center-block col-12">
                <input className="btn btn-outline-secondary" type="submit" value="Connexion"  variant="primary"/>
          </div>
        </form>
    </div>
    </div>,
        document.body
      );
  }
};

export default Login;