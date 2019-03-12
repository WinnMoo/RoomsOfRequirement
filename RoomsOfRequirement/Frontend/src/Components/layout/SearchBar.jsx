import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import filterClassrooms from '../../Actions/Filter';

//  ///    ////      /////        ////////////        /////      ////    ///  //

// eslint-disable-next-line react/prefer-stateless-function
class SearchBar extends Component {
  static propTypes = {
    filterClassrooms: PropTypes.func.isRequired,
  };

  onChange = (event) => {
    // Maybe move updateClassrooms() here?
    // eslint-disable-next-line react/destructuring-assignment
    this.props.filterClassrooms(event.target.value);
    this.setState({
      [event.target.name]: event.target.value,
    });
  }

  onSubmit = (event) => {
    const { searchText } = this.state;
    event.preventDefault(); // Prevents the page from reloading
    filterClassrooms(searchText); // Calls the function in App.jsx
    this.setState({
      searchText: '',
    });
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
