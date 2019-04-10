import React, { Component } from 'react';

import Classrooms from './Classrooms';
import SearchBar from './SearchBar';
import '../App.css';

export default class Dashboard extends Component {
  render() {
    return (
      <div className="App">
        <h1 className="App-title">Room of Requirement</h1>
        <SearchBar updateClassrooms={this.updateClassrooms} />
        <div className="Classrooms-list">
          <Classrooms />
        </div>
      </div>
    );
  }
}
