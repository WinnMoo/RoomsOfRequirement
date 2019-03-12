import { FILTER_CLASSROOMS } from './Types';

export default function filterClassrooms(searchText) {
  return {
    type: FILTER_CLASSROOMS,
    payload: searchText,
  };
}
