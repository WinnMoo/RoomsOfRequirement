import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';

// eslint-disable-next-line react/prefer-stateless-function
class ClassDetails extends Component {
  static propTypes = {
    currentClass: PropTypes.shape({
      classroom: PropTypes.string,
      times: PropTypes.arrayOf(
        PropTypes.shape({
          start_time: PropTypes.string,
          end_time: PropTypes.string,
        }),
      ),
    }).isRequired,
  }

  render() {
    const { currentClass } = this.props;
    const { classroom } = currentClass;
    return (
      <h1 className="App-title">{classroom}</h1>
    );
  }
}

const mapStateToProps = state => ({
  currentClass: state.classroomReducer.currentClass,
});

export default connect(mapStateToProps)(ClassDetails);
