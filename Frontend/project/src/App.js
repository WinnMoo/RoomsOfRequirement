import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {

    invalidInput(){

        console.log("Room searched for was invalid, please search again");
    }

    checkBuildingExists(searchedRoom){
        const rooms = ["VEC", 'ECS', "EN2", "EN3"]
        for(let i = 0; i < rooms.length; i++) {
            if(searchedRoom === rooms[i]){
                return true;
            }
        }
        return false;
    }

    validInput(searchedRoom){
        if(this.checkBuildingExists(searchedRoom)){
          /*
            <table>
                <tr>
                    <th>Room Number</th>
                    <th>Available</th>
                    <th>Remaining Time Until Occupied</th>
                </tr>
            </table>
            */
        }

    }

    handleSubmit(){
        if(document.getElementById("searchedRoom") != null){
            const searchedRoom = document.getElementById("searchedRoom").value;
            console.log(document.getElementById("searchedRoom").value);
            searchedRoom.trim();
            document.getElementById("searchedRoom").innerHTML = `You wrote: ${searchedRoom}`;
            /*
            if(searchedRoom.includes('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '.', '?')){
                this.invalidInput();
            } else {
                this.validInput(searchedRoom);
            }
            */
        } else {
            console.log("nothing is there");
            /*
            <table>
                <tr>
                    <th>Room Number</th>
                    <th>Available</th>
                    <th>Remaining Time Until Occupied</th>
                </tr>
            </table>
            */
        }
    }


    render() {
        return (
            <div className="App">
                <header className="App-header">
                    <img src={logo} className="App-logo" alt="logo"/>
                    <h1 className="App-title">Room of Requirement</h1>
                    <form className="input">
                        <input type="text" name="search" placeholder="Building Name.." autoComplete="off" id="searchedRoom" onChange={this.handleSubmit()}/>
                    </form>
                </header>
            </div>
        );
    }
}

export default App;
