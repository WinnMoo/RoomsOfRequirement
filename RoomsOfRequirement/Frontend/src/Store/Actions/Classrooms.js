import axios from 'axios';

// Use the REST API from Django to get the list of classrooms in the database
export function getClassrooms() {
  return (dispatch) => {
    axios
      .get('/api/Classrooms/')
      .then((res) => {
        dispatch({
          type: 'GET_CLASSROOMS',
          payload: res.data,
        });
      })
      .catch(err => console.log(err));
  };
}

// A simple function signature that passes the parameters into the Reducer
export function filterClassrooms(searchText) {
  return {
    type: 'FILTER_CLASSROOMS',
    payload: searchText,
  };
}

export function selectClass(classroom) {
  return {
    type: 'SELECT_CLASSROOM',
    payload: classroom,
  };
}
