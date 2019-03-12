import { GET_CLASSROOMS, FILTER_CLASSROOMS } from '../Actions/Types';

const initialState = {
  classrooms: [
    {
      class_id: 1,
      classroom: 'VEC-202',
      start_time: '12:30',
      end_time: '13:45',
    },
    {
      class_id: 2,
      classroom: 'ECS-403',
      start_time: '14:00',
      end_time: '14:45',
    },
    {
      class_id: 3,
      classroom: 'EN1-109',
      start_time: '16:00',
      end_time: '17:45',
    },
  ],
  searchText: '',
  filteredClassrooms: [],
};

export function filterClassrooms(state, searchedText) {
  let temp = state.classrooms;
  if (searchedText !== '') {
    temp = temp.filter(room => room.classroom.includes(searchedText));
  }
  return temp;
}

export default function (state = initialState, action) {
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
}
