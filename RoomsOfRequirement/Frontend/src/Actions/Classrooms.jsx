import axios from 'axios';
import { GET_CLASSROOMS } from './Types';

// Use the REST API from Django to get the list of classrooms in the database
export default () => (dispatch) => {
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
