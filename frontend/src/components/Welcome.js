import React, { useState } from 'react';
// import ReactDOM from 'react-dom';
import Login from './Login';
import Hello from './Hello';

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
              message="Bienvenue sur Explorateur par Nature !"
              isOpen={openp}
              onClose={() => setOpenP(false)}
            />
            <Hello />
        </div>
    </div>
    );
}

export default Welcome