import { GET_CLASSROOMS, FILTER_CLASSROOMS } from '../Actions/Types';

const initialState = {
  classrooms: [],
  searchText: '',
  filteredClassrooms: [],
};

const filterClassrooms = (state, searchedText) => {
  let temp = state.classrooms;
  if (searchedText !== '') {
    temp = temp.filter(room => room.classroom.includes(searchedText));
  }
  return temp;
};

export default (state = initialState, action) => {
  switch (action.type) {
    case GET_CLASSROOMS:
      return {
        ...state,
        classrooms: action.payload,
        filteredClassrooms: action.payload,
      };
    case FILTER_CLASSROOMS:
      return {
        ...state,
        searchText: action.payload,
        filteredClassrooms: filterClassrooms(state, action.payload),
      };
    default:
      return state;
  }
};
