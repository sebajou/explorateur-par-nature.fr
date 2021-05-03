import React, { Component, Modal } from "react";
// import ReactDOM from 'react-dom';
import Login from './Login';
// import Hello from './Hello';

class Welcome extends Component {
    constructor(props) {
        super(props);
        this.state = {setOpen: false, openp: false};

        this.handleShow = this.handleShow.bind(this);
        this.handleHide = this.handleHide.bind(this);
    }

    handleShow () {
        this.setState({setOpen: true});
    }

    handleHide () {
        this.setState({setOpen: false});
    }

    render() {
        // const [open, setOpen] = useState(false);
        // const [openp, setOpenP] = useState(false);
        const { openp, setOpenP } = this.state;
        const modal = this.state.showModal ? (
        <Modal>
            <Login
              message="Bienvenue sur Explorateur par Nature !"
              isOpen={openp}
              onClose={() => setOpenP(false)}
            />
            <button onClick={this.handleHide}>Hide modal</button>
        </Modal>

        ) : null;

        return (
            <div className="container">
              <div className="button-container">
                <button onClick={this.handleShow}>Show modal</button>
                {modal}
              </div>
            </div>
        );
    }
}

export default Welcome