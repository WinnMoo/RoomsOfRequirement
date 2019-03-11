import React, { Component, Fragment } from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import Classrooms from './layout/Classrooms';
import SearchBar from './layout/SearchBar';
import store from '../store';
import './App.css';

// Later i'd like to call the python script to help populate this list.
const classroomList = [
  {
    class_id: 1,
    classroom: 'VEC-202',
    start_time: '12:30',
    end_time: '13:45',
  },
  {
    class_id: 2,
    classroom: 'ECS-403',
    start_time: '14:00',
    end_time: '14:45',
  },
  {
    class_id: 3,
    classroom: 'EN1-109',
    start_time: '16:00',
    end_time: '17:45',
  },
];

export default class App extends Component {
  state = {
    classrooms: classroomList,
  };

  updateClassrooms = (building) => {
    let temp = classroomList;
    if (building !== '') {
      temp = classroomList.filter(classroom => classroom.classroom.includes(building));
    }
    this.setState({ classrooms: temp });
  };

  render() {
    const { classrooms } = this.state;
    return (
      <Provider store={store}>
        <Fragment>
          <div className="App">
            <header className="App-header">
              <h1 className="App-title">Room of Requirement</h1>
            </header>
            <SearchBar updateClassrooms={this.updateClassrooms} />
            <div className="Classrooms-list">
              <Classrooms classrooms={classrooms} />
            </div>
          </div>
        </Fragment>
      </Provider>
    );
  }
}

ReactDOM.render(<App />, document.getElementById('app'));
