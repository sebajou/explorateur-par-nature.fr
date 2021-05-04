import React, { useState } from 'react';
// import ReactDOM from 'react-dom';
import Login from './Login';
import Hello from './Hello';
// import Essai from './Essai';
import axiosInstance from "./AxiosAPI";


function Welcome() {
    // const [open, setOpen] = useState(false);
    const [openp, setOpenP] = useState(false);

    async function handleLogout() {
      try {
          const response = await axiosInstance.post('/blacklist/', {
              "refresh_token": localStorage.getItem("refresh_token")
          });
          localStorage.removeItem('access_token');
          localStorage.removeItem('refresh_token');
          axiosInstance.defaults.headers['Authorization'] = null;
          return response;
      }
      catch (e) {
          console.log(e);
      }
    }

    return (
        <div className="container">
          <div className="button-container">
            <button className="button" onClick={() => setOpenP(true)}>
              Open Portal Modal
            </button>
          </div>
          <div className="button-container">
            <button className="button" onClick={() => handleLogout()}>
              Logout
            </button>
          </div>
          

        <div>
            <Login
              message="Connexion Tuteur"
              isOpen={openp}
              onClose={() => setOpenP(false)}
            />
            <Hello />
        </div>
    </div>
    );
}

export default Welcome
