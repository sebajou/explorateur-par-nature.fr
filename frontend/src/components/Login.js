import React, { Component } from "react";
import ReactDOM from 'react-dom';
import axiosInstance from "./AxiosAPI";
import '../styles/Login.css';
import '../styles/styles.css';

class Login extends Component {
    constructor(props) {
        super(props);
        this.state = {username: "", password: ""};

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
            Connexion Tuteur
            <form onSubmit={this.handleSubmit}>
              <label>
                  Username:
                  <input name="username" type="text" value={this.state.username} onChange={this.handleChange}/>
              </label>
              <label>
                  Password:
                  <input name="password" type="password" value={this.state.password} onChange={this.handleChange}/>
              </label>
              <input type="submit" value="Submit"/>
            </form>
            <h2>{message}</h2>
            <button className="close" onClick={onClose}>
                Close
            </button>
        </div>,
        document.body
      );
  }
};

export default Login;