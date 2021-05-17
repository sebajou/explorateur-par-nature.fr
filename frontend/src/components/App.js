import React from 'react';
import '../styles/App.css';
// import Modal, {modal} from './Modal';
// import ReactDOM from 'react-dom';
import Welcome from './Welcome';
import Login from './Login';

function App() {
    return (
        <div>
            <Welcome>
                <Login />
            </Welcome>
        </div>
        )
};

export default App