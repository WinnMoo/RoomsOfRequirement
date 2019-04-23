/**
 * The initial state of the store.
 *
 * `classrooms` is the raw data taken from the database
 *
 * `searchText` is the text that the users enters in the search bar
 *
 * `classroomList` is the data printed out to the browser
 *
 * `filteredClassrooms` is the combined list finally shown to the user using
 * `searchText` and `classroomList` as inputs
 */
const initialState = {
  classrooms: [],
  searchText: '',
  classroomList: [],
  filteredClassrooms: [],
};

const indexWeekday = (weekday) => {
  switch (weekday) {
    case 'Sa':
      return 0;
    case 'M':
      return 1;
    case 'Tu':
      return 2;
    case 'W':
      return 3;
    case 'Th':
      return 4;
    case 'F':
      return 5;
    default:
      return 6;
  }
};

const uniqueTimes = (value, index, self) => {
  return self.indexOf(value) === index;
};

/**
 * For every classroom in list, check if classroom already exists.
 *
 * If it does, add object to array, otherwise, add pair of times to existing classroom.
 * @param list Raw data taken from database
 * @returns Organized list of classrooms
 */
const getClassroomList = (list) => {
  const temp = [];
  for (let i = 0; i < list.length; i += 1) {
    const idx = temp.findIndex(room => room.classroom === list[i].classroom);
    if (idx === -1) {
      temp.push({
        class_id: list[i].class_id,
        classroom: list[i].classroom,
        times: [{
          weekday: list[i].weekday,
          start_time: list[i].start_time,
          end_time: list[i].end_time,
        }],
      });
    } else {
      temp[idx].times.push({
        weekday: list[i].weekday,
        start_time: list[i].start_time,
        end_time: list[i].end_time,
      });
    }
  }
  temp.sort((roomA, roomB) => roomA.classroom > roomB.classroom);
  temp.forEach((room) => {
    room.times.sort(((tA, tB) => tA.start_time > tB.start_time));
    room.times.sort(((tA, tB) => indexWeekday(tA.weekday) > indexWeekday(tB.weekday)));
  });
  return temp;
};

/**
 * Filter the classrooms that appear for the user based on search results
 * @param list Base classroom list, without any modifications
 * @param searchedText Text field data from SearchBar
 * @returns Final list of classrooms
 */
const filterClassrooms = (list, searchedText) => {
  let temp = list;
  if (searchedText !== '') {
    temp = temp.filter(room => room.classroom.includes(searchedText.toUpperCase()));
  }
  return temp;
};

export default function classroomReducer(state = initialState, action) {
  switch (action.type) {
    case 'GET_CLASSROOMS': {
      const groundTruth = action.payload.sort((roomA, roomB) => roomA.classroom > roomB.classroom);
      const list = getClassroomList(groundTruth);
      return {
        ...state,
        classrooms: groundTruth,
        classroomList: list,
        filteredClassrooms: list,
      };
    }
    case 'FILTER_CLASSROOMS':
      return {
        ...state,
        searchText: action.payload,
        filteredClassrooms: filterClassrooms(state.classroomList, action.payload),
      };
    default:
      return state;
  }
}
