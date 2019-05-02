import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';

import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import { CardActionArea } from '@material-ui/core';

import '../App.css';
import { selectClass } from '../../Store/Actions/Classrooms';

// eslint-disable-next-line react/prefer-stateless-function
class Classroom extends Component {
  static propTypes = {
    room: PropTypes.shape({
      classroom: PropTypes.string,
      times: PropTypes.arrayOf(
        PropTypes.shape({
          start_time: PropTypes.string,
          end_time: PropTypes.string,
        }),
      ),
    }).isRequired,
    selectClass: PropTypes.func.isRequired,
  };

  constructor(props) {
    super(props);
    this.onClick = this.onClick.bind(this);
  }

  onClick() {
    // eslint-disable-next-line react/destructuring-assignment
    this.props.selectClass(this.props.room);
  }

  days = (times) => {
    const display = [];
    for (let i = 0; i < times.length; i += 1) {
      const p = times[i].weekday;
      let idx = display.findIndex(room => room.day === p);
      if (idx === -1) {
        display.push({
          day: p,
          time: [],
        });
        idx = display.length - 1;
      }
      display[idx].time.push(`${times[i].start_time}-${times[i].end_time}`);
    }
    return display;
  }

  render() {
    const { room } = this.props;
    const { classroom, times } = room;
    return (
      <Link to={`/${classroom}`} style={{ textDecoration: 'none' }} onClick={this.onClick}>
        <Card className="Classroom-box" style={{ backgroundColor: '#ffa800' }}>
          <CardActionArea>
            <CardContent>
              <Typography component="h5" variant="h5" style={{ color: '#484236' }}>{classroom}</Typography>
              <Typography variant="subtitle1" color="textSecondary">
                {this.days(times).map(day => (
                  <div key={day.day}>
                    {`${day.day}: `}
                    {day.time.join(', ')}
                  </div>
                ))}
              </Typography>
            </CardContent>
          </CardActionArea>
        </Card>
      </Link>
    );
  }
}

const mapDispatchToProps = dispatch => ({
  selectClass: room => dispatch(selectClass(room)),
});

export default connect(null, mapDispatchToProps)(Classroom);
