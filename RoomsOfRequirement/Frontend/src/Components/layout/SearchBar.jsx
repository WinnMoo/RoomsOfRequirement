import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import TextField from '@material-ui/core/TextField';

import { filterClassrooms } from '../../Store/Actions/Classrooms';

class SearchBar extends Component {
  static propTypes = {
    filterClassrooms: PropTypes.func.isRequired,
  };

  // Upon changing the text in the searchBar, update the list.
  // The second line makes sure anything that's typed stays.
  onChange = (event) => {
    // eslint-disable-next-line react/destructuring-assignment
    this.props.filterClassrooms(event.target.value);
    this.setState({
      [event.target.name]: event.target.value,
    });
  }

  // Prevent page from reloading
  onSubmit = (event) => {
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.onSubmit}>
        <TextField
          id="outlined-building-input"
          label="Building Name"
          name="searchText"
          autoComplete="off"
          margin="normal"
          variant="outlined"
          onChange={this.onChange}
        />
      </form>
    );
  }
}

const mapStateToProps = state => ({
  searchText: state.classroomReducer.searchText,
});

export default connect(
  mapStateToProps,
  { filterClassrooms },
)(SearchBar);
