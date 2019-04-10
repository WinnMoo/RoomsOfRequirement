import React, { Component, Fragment } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import Classroom from './Classroom';
import { getClassrooms } from '../../Store/Actions/Classrooms';

class Classrooms extends Component {
  static propTypes = {
    filteredClassrooms: PropTypes.arrayOf(PropTypes.object).isRequired,
    getClassrooms: PropTypes.func.isRequired,
  };

  componentDidMount() {
    // eslint-disable-next-line react/destructuring-assignment
    this.props.getClassrooms();
  }

  render() {
    const { filteredClassrooms } = this.props;
    return (
      <Fragment>
        {filteredClassrooms.map(room => (
          <Classroom key={room.class_id} room={room} />
        ))}
      </Fragment>
    );
  }
}
// export 'default' (imported as 'connect') was not found in 'react-redux
const mapStateToProps = state => ({
  filteredClassrooms: state.classroomReducer.filteredClassrooms,
});

export default connect(
  mapStateToProps,
  { getClassrooms },
)(Classrooms);
