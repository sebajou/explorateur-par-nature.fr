import React, { Component } from "react";
import ReactDOM from 'react-dom';
import axiosInstance from "./AxiosAPI";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import { faTimes } from "@fortawesome/free-solid-svg-icons";

library.add(faTimes);

class Signup extends Component{
    constructor(props){
        super(props);
        this.state = {
            username: "",
            password: "",
            first_name: "",
            last_name: "",
            email:"",
            errors:{}
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({[event.target.name]: event.target.value});
    }

    async handleSubmit(event) {
        event.preventDefault();
        try {
            const response = await axiosInstance.post('/user/create/', {
                username: this.state.username,
                email: this.state.email,
                first_name: this.state.first_name,
                last_name: this.state.last_name,
                password: this.state.password
            });
            return response;
        } catch (error) {
            console.log(error.stack);
            this.setState({
                errors:error.response.data
            });
        }
    }

    render() {

        const { message, isOpen, onClose} = this.props;
  
        if (!isOpen) return null;
      
        return ReactDOM.createPortal (

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

                <div className="row">
                    Créer un profil : 
                    <form onSubmit={this.handleSubmit}>
                        <label>
                            Nom d'utilisateur : 
                            <input name="username" type="text" value={this.state.username} onChange={this.handleChange}/>
                        </label>
                        <label>
                            Courriel : 
                            <input name="email" type="email" value={this.state.email} onChange={this.handleChange}/>
                        </label>
                        <label>
                            Prenom : 
                            <input name="first_name" type="text" value={this.state.first_name} onChange={this.handleChange}/>
                        </label>
                        <label>
                            Nom de famille : 
                            <input name="last_name" type="text" value={this.state.last_name} onChange={this.handleChange}/>
                        </label>
                        <label>
                            Password: 
                            <input name="password" type="password" value={this.state.password} onChange={this.handleChange}/>
                        </label>
                        <input type="submit" value="Submit"/>
                    </form>
                </div>
            </div>
        </div>,
        document.body
        );
    }
};

export default Signup;