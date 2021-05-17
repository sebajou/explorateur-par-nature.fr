import React, { Component } from "react";
import ReactDOM from 'react-dom';
import axiosInstance from "./AxiosAPI";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import { faTimes } from "@fortawesome/free-solid-svg-icons";

library.add(faTimes);

class Logout extends Component{
    constructor(props){
        super(props);
        this.state = {};

    this.handleChange = this.handleChange.bind(this);
    this.handleLogout = this.handleLogout.bind(this);
    }

    handleChange(event) {
        this.setState({[event.target.name]: event.target.value});
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
        <form onSubmit={this.handleLogout}>
            <div className="row center-block col-12">
                <input className="btn btn-outline-secondary" type="submit" value="Déconnexion"  variant="primary"/>
            </div>
        </form>
        </div>
        </div>,
        document.body
        );
    }
  };
  
  export default Logout
  