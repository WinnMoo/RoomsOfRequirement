import React from 'react';
import Classrooms from './Components/Classrooms';
import SearchBar from './Components/SearchBar';
import './App.css';

// Later i'd like to call the python script to help populate this list.
const classroomList = [
  {
    id: 1,
    building: 'VEC',
    roomNumber: 202,
    startTime: '12:30PM',
    endTime: '1:45PM',
  },
  {
    id: 2,
    building: 'ECS',
    roomNumber: 403,
    startTime: '2:00PM',
    endTime: '2:45PM',
  },
  {
    id: 3,
    building: 'EN1',
    roomNumber: 109,
    startTime: '4:00PM',
    endTime: '5:45PM',
  },
];

export default class App extends React.Component {
  state = {
    classrooms: classroomList,
  };

  updateClassrooms = (building) => {
    let temp = classroomList;
    if (building !== '') {
      temp = classroomList.filter(classroom => classroom.building.includes(building));
    }
    this.setState({ classrooms: temp });
  }

  render() {
    const { classrooms } = this.state;
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Room of Requirement</h1>
        </header>
        <SearchBar updateClassrooms={this.updateClassrooms} />
        <div className="Classrooms-list">
          <Classrooms classrooms={classrooms} />
        </div>
      </div>
    );
  }
}
