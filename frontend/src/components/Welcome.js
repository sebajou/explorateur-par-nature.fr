import React, { useState } from 'react';
// import ReactDOM from 'react-dom';
import Login from './Login';
import Hello from './Hello';
// import Essai from './Essai';

function Welcome() {
    // const [open, setOpen] = useState(false);
    const [openp, setOpenP] = useState(false);

    return (
        <div className="container">
          <div className="button-container">
            <button className="button" onClick={() => setOpenP(true)}>
              Open Portal Modal
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
