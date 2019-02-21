import React, { Component } from 'react';
import PropTypes from 'prop-types';

// eslint-disable-next-line react/prefer-stateless-function
export default class SearchBar extends Component {
  state = {
    building: '',
  }

  onChange = (event) => {
    // Maybe move updateClassrooms() here?
    this.setState({
      [event.target.name]: event.target.value,
    });
  }

  onSubmit = (event) => {
    const { updateClassrooms } = this.props;
    const { building } = this.state;
    event.preventDefault();  // Prevents the page from reloading
    updateClassrooms(building);
    this.setState({
      building: '',
    });
  }

  render() {
    return (
      <form onSubmit={this.onSubmit}>
        <input
          type="text"
          name="building"
          placeholder="Building Name.."
          autoComplete="off"
          onChange={this.onChange}
        />
      </form>
    );
  }
}

SearchBar.propTypes = {
  updateClassrooms: PropTypes.func.isRequired,
};
