import axios from 'axios';

import { GET_CLASSROOMS } from './Types';

// Get the classrooms from the seperately running server on Django
const getClassrooms = () => (dispatch) => {
  axios
    .get('/api/Classrooms/')
    .then((res) => {
      dispatch({
        type: GET_CLASSROOMS,
        payload: res.data,
      });
    })
    .catch(err => console.log(err));
};

export default getClassrooms;
