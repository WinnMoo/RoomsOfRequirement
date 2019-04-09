import React, { Component } from 'react';
import { Provider } from 'react-redux';

import Classrooms from './layout/Classrooms';
import SearchBar from './layout/SearchBar';
import store from '../store';
import './App.css';

export default class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <div className="App">
          <h1 className="App-title">Room of Requirement</h1>
          <SearchBar updateClassrooms={this.updateClassrooms} />
          <div className="Classrooms-list">
            <Classrooms />
          </div>
        </div>
      </Provider>
    );
  }
}
