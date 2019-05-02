import axios from 'axios';

// TODO(Christopher): Test Django API for checkins
export const checkIn = (classID, userID) => (dispatch) => {
  axios.post('/api/checkins', { classID, userID }).then((res) => {
    dispatch({
      type: 'CHECK_IN',
      payload: res.data,
    });
  }).catch(err => console.log(err));
};

// TODO(Christopher): Test Django API for checkins
export const checkOut = id => (dispatch) => {
  axios.delete(`/api/checkins/${id}/`).then((res) => {
    dispatch({
      type: 'CHECK_OUT',
      payload: res.data,
    });
  }).catch(err => console.log(err));
};
