/* eslint-disable camelcase */
import React, { Component } from 'react';
import PropTypes from 'prop-types';

// eslint-disable-next-line react/prefer-stateless-function
export default class Classroom extends Component {
  static propTypes = {
    room: PropTypes.shape({
      classroom: PropTypes.string,
      start_time: PropTypes.string,
      end_time: PropTypes.string,
    }).isRequired,
  };

  render() {
    const { room } = this.props;
    const { classroom, start_time, end_time } = room;
    return (
      <div className="Classroom-box">
        <h2>{classroom}</h2>
        <p>{`${start_time}-${end_time}`}</p>
      </div>
    );
  }
}
