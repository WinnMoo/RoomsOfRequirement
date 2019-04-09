import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import filterClassrooms from '../../Actions/Filter';

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
        <input
          type="text"
          name="searchText"
          placeholder="Building Name.."
          autoComplete="off"
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
