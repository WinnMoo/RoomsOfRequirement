import React, { Component, Fragment } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import Classroom from './Classroom';
import getClassrooms from '../../Actions/Classrooms';

class Classrooms extends Component {
  static propTypes = {
    classrooms: PropTypes.arrayOf(PropTypes.object).isRequired,
    getClassrooms: PropTypes.func.isRequired,
  };

  componentDidMount() {
    // eslint-disable-next-line react/destructuring-assignment
    this.props.getClassrooms();
  }

  render() {
    const { classrooms } = this.props;
    return (
      <Fragment>
        {classrooms.map(room => (
          <Classroom key={room.class_id} room={room} />
        ))}
      </Fragment>
    );
  }
}
// export 'default' (imported as 'connect') was not found in 'react-redux
const mapStateToProps = state => ({
  classrooms: state.classroomReducer.classrooms,
});

export default connect(
  mapStateToProps,
  { getClassrooms },
)(Classrooms);
