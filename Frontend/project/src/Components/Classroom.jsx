import React, { Component } from 'react';
import PropTypes from 'prop-types';

// eslint-disable-next-line react/prefer-stateless-function
export default class Classroom extends Component {
  render() {
    const { classroom } = this.props;
    const {
      building,
      roomNumber,
      startTime,
      endTime,
    } = classroom;
    return (
      <div className="Classroom-box">
        <h2>
          {building}
          {'-'}
          {roomNumber}
        </h2>
        <p>{`${startTime}-${endTime}`}</p>
      </div>
    );
  }
}

Classroom.propTypes = {
  classroom: PropTypes.shape({
    building: PropTypes.string,
    roomNumber: PropTypes.number,
    startTime: PropTypes.string,
    endTime: PropTypes.string,
  }).isRequired,
};
