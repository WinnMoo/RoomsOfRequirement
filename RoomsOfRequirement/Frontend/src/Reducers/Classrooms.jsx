import { GET_CLASSROOMS, FILTER_CLASSROOMS } from '../Actions/Types';

const initialState = {
  classrooms: [],
  searchText: '',
  classroomList: [],
  filteredClassrooms: [],
};

const getClassroomList = (list) => {
  const temp = [{
    classroom: '',
    times: [{
      start_time: '',
      end_time: '',
    }],
  }];
  // For every classroom in list, check if classroom already exists.
  // If it does, add object to array
  // Else add pair of times to existing classroom
  for (let i = 0; i < list.length; i += 1) {
    const idx = temp.findIndex(room => room.classroom === list[i].classroom);
    if (idx === -1) {
      temp.push({
        classroom: list[i].classroom,
        times: [{
          start_time: list[i].start_time,
          end_time: list[i].end_time,
        }],
      });
    } else {
      temp[idx].times.push({
        start_time: list[i].start_time,
        end_time: list[i].end_time,
      });
    }
  }
  return temp;
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
        classroomList: getClassroomList(action.payload),
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
