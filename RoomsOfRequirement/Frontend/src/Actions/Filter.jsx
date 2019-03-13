import { FILTER_CLASSROOMS } from './Types';

// A simple function signature that passes the parameters into the Reducer
export default function filterClassrooms(searchText) {
  return {
    type: FILTER_CLASSROOMS,
    payload: searchText,
  };
}
