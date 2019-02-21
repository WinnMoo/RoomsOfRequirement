import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Classroom from './Classroom';

export default class Classrooms extends Component {
  render() {
    const { classrooms } = this.props;
    return classrooms.map(room => (
      <Classroom key={room.id} classroom={room} />
    ));
  }
}

Classrooms.propTypes = {
  classrooms: PropTypes.arrayOf(PropTypes.object).isRequired,
};
